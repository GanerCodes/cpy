#!/usr/bin/python 
import stat, os
from os import environ, fork
from os.path import expanduser, isfile, realpath, join as path_join, split as path_split
from subprocess import PIPE, Popen
from kthread import KThread as Thread
from random import randint
from time import time, sleep

def isfifo(path):
    try:
        return stat.S_ISFIFO(os.stat(path).st_mode)
    except Exception:
        pass
def try_run(f, *a, **k):
    try: f(*a, **k)
    except Exception as e: print(f"try_run failed: {e}")

script_directory = path_split(realpath(__file__))[0]
run_simple = lambda *a: Popen(a, stdout=PIPE).stdout.read().decode().strip()

XRESOURCES_LOCATION = expanduser("~/.Xresources")
fifo_path = path_join("/tmp", f"{hash(time())}_xnotipy.fifo")

class Notification:
    XNOTIFY_LOCATION = run_simple("which", "xnotify")
    RESOURCE_FILE_NAME = path_join(script_directory, "resources")
    __para_inline__ = { "IMG": "image",
                        "TAG": "tag",
                        "CMD": "cmd",
                        "BAR": "bar",
                        "SEC": ("time", 5) }
    __para_resource__ = {
        "background": ("background_color", "#000000"),
        "foreground": ("foreground_color", "#FFFFFF"),
        "border": ("border_color", "#FFFFFF"),
        "borderWidth": ("border_width", "1px"),
        "shrink": ("shrink", True),
        "title.font": "title_font",
        "body.font": "body_font",
        "wrap": ("text_wrap", True),
        "leading": "line_spacing",
        "alignment": ("text_alignment", "center"),
        "alignTop": "text_top_align",
        "padding": "padding",
        "maxHeight": "max_height",
        "gap": "gap",
        "imageWidth": "image_width",
        "geometry": "geometry",
        "gravity": ("base_location", "NE") }
    all_options = __para_inline__ | __para_resource__
    
    proc = fifo_write = fifo_read_thread = None
    cache, cache_idx = {}, hash(time())
    
    def get_fifo(𝕊):
        if isfifo(fifo_path):
            return fifo_path
        
        os.mkfifo(fifo_path, mode=0o777)
        stdin = os.open(fifo_path, os.O_RDONLY | os.O_NONBLOCK)
        Notification.proc = proc = Popen(
            [𝕊.XNOTIFY_LOCATION, "-b", str(𝕊.mouse_button), "-m", str(𝕊.monitor)],
            stdin=stdin, stdout=PIPE,
            universal_newlines=True, env=environ)
        os.close(stdin)
        Notification.fifo_write = open(fifo_path, 'w', buffering=1)
        Notification.fifo_read_thread = Thread(target=Notification.fifo_reader, args=(proc, ), daemon=True)
        Notification.fifo_read_thread.start()
        return fifo_path
    
    @classmethod
    def fifo_reader(ℂ, proc):
        while True:
            line = proc.stdout.readline()
            print(f"{line=}")
            if not line:
                break
            
            ID = line.strip()
            
            if ID in ℂ.cache:
                n = ℂ.cache.pop(ID)
                if isinstance(n.cmd, ℂ):
                    n.cmd.run()
                elif isinstance(n.cmd, str|list|tuple):
                    Popen(n.cmd)
                elif callable(n.cmd):
                    n.cmd()
    
    def get_name (𝕊, x): return x[0] if isinstance(x, tuple) else x
    def get_value(𝕊, x): return x[1] if isinstance(x, tuple) else None
    
    def __init__(𝕊, text="", cmd=None, mouse_button=1, monitor=0, **para):
        𝕊.mapping = {k: 𝕊.get_name(v) for k, v in 𝕊.all_options.items()}
        𝕊.inverse_mapping = {v: k for k, v in 𝕊.mapping.items()}
        
        𝕊.para = {
            v: 𝕊.get_value(𝕊.all_options[k]) for k, v in 𝕊.mapping.items()
        } | para
        
        if 𝕊.para["tag"] is None:
            𝕊.para["tag"] = str(randint(10 ** 8, 10 ** 10))
    
        if isinstance(t := 𝕊.para["geometry"], tuple|list):
            d = (t[2] if len(t) > 2 else 0, t[3] if len(t) > 3 else 0)
            𝕊.para["geometry"] = f"{t[0]}x{t[1]}{d[0]:+}{d[1]:+}"
        
        if cmd:
            ID = str(Notification.cache_idx)
            𝕊.para["cmd"] = ID
            Notification.cache[ID] = 𝕊
            Notification.cache_idx += 1
        
        𝕊.mouse_button = mouse_button
        𝕊.has_set_resources = False
        𝕊.monitor = monitor
        𝕊.text = text
        𝕊.cmd = cmd
        
        𝕊.get_fifo()
    
    def update_resources(𝕊):
        with open(𝕊.RESOURCE_FILE_NAME, "w") as f:
            for k, v in 𝕊.para.items():
                m = 𝕊.inverse_mapping[k]
                if v is None or not m in 𝕊.__para_resource__:
                    continue
                if isinstance(v, bool):
                    v = str(v).lower()
                f.write(f"xnotify.{m}: {v}\n")
        
        run_simple("xrdb", XRESOURCES_LOCATION, "-merge", 𝕊.RESOURCE_FILE_NAME)
    
    def run(𝕊, force_refresh_resources=False):
        if not 𝕊.has_set_resources or force_refresh_resources:
            𝕊.update_resources()
            𝕊.has_set_resources = True
        
        content = ''.join(f"{k}:{m}\t" for k in 𝕊.__para_inline__
             if (m := 𝕊.para[𝕊.mapping[k]]) is not None) + f"{𝕊.text}\n"
        
        Notification.fifo_write.write(content)
    
    def thread_run(𝕊, *args, **kwargs):
        Thread(target=𝕊.run, args=args, kwargs=kwargs).start()
    
    __call__ = thread_run
    
    def background_run(𝕊, *args, **kwargs):
        if fork() == 0:
            𝕊.run(*args, **kwargs)
            exit(0)
    
    @classmethod
    def exit(ℂ, t=0):
        def f():
            sleep(t)
            try_run(ℂ.fifo_read_thread.terminate)
            try_run(ℂ.proc.terminate)
            try_run(os.remove, fifo_path)
        Thread(target=f).start()

if __name__ == "__main__":
    n = Notification(
        "THE",
        geometry=(52, 5, -25, 25),
        shrink=False,
        border_width=1,
        image="./really_cool_image.png",
        cmd=Notification(
            "hey",
            cmd=["brave", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"]))
    n.thread_run()
    Notification.exit(5)