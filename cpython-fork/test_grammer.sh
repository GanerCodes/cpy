rm ./parse.py || :
set -e
python -m pip install pegen --break-system-packages
python -m pegen -vo ./parse.py ./Grammar/python.gram
cpy_tool ; cpy_binary ./parse.py TESTING1.py
# cpy_binary ./parse.py TESTING.py