const [✓, ✗] = [true, false];
const ASCII_CHARS_STANDARD = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';

const ⵌ = l => l.length;
const ᒪ = A => [...A]
const 𝒮 = (d, k, v) => (!(k in d) || d[k] === null) ? (d[k] = v) : d[k];
const [𝒪, 𝒟, 𝒪k, 𝒪v] = [Object.entries, Object.fromEntries, Object.keys, Object.values];
const ᴍ = (l, 𝑓) => ᒪ(l).map(𝑓);
const ᴍv = (d, 𝑓) => 𝒟(𝒪(d).map(([k,v]) => [k,𝑓(v)]));
const ᴍk = (d, 𝑓) => 𝒟(𝒪(d).map(([k,v]) => [𝑓(k),v]));
const ζ = (𝑥, 𝑦) => ᒪ(𝑥).map((k, i) => [k, 𝑦[i]]);

const int = Math.floor;
const ends = l => l.map((𝑥,i)=>[i==0,𝑥,i==ⵌ(l)-1]);
const all = A => A.every(x=>x);
const sort = (A,f,r=𝔽) => A.sort((a,b) => (r ? 1 : -1)*(b > a ? 1 : -1)) // what?
const merge = (...o) => Object.assign({}, ...o)
const range = (a, b) => [...Array(b-a).keys()].map(i => i+a);
const print = (...x) => console.log(...x) || x[0]
const table = (...x) => console.table(...x) || x[0]
const sleep = s => new Promise(r => setTimeout(r, 1000 * s));
const strfmt = (str, args) => {
    for (const [k, v] of Object.entries(args))
        str = str.replace(new RegExp("\\{" + k + "\\}", "gi"), v);
    return str; };
const makeid = (length, chars=ASCII_CHARS_STANDARD) => 
    range(0, length)
        .map(_=>chars.charAt(int(Math.random()*chars.length)))
        .reduce((a,b)=>a+b, '');
const groups = (l, 𝑓) => {
    O = {};
    l.forEach(𝑥 => 𝒮(O, 𝑓(𝑥), []).push(𝑥))
    return O; }

var objIdMap=new WeakMap, objectCount = 0;
const id = object => { // https://stackoverflow.com/a/35306050
  !objIdMap.has(object) && objIdMap.set(object,++objectCount);
  return objIdMap.get(object); }
    
// Start of HTML stuff
const GID = id => document.getElementById(id);
const VAL = id => GID(id).value;
const QSA = (sel, e=document) => ᒪ(e.querySelectorAll(sel));
const SAT = (ε, a, v) => ε.setAttribute(a, v);

const setLocal = (k, v) => localStorage[k] = JSON.stringify(v);
const getLocal = (k   ) => JSON.parse(localStorage[k]);

const ε_clone = ε => {
    if(!(ε instanceof Node)) return ε;
    if(ε.tagName == 'F') return ε.𝑓();
    const ə = ε.cloneNode(false);
    ('𝕤' in ε) && (ə.𝕤 = ε.𝕤);
    if(ε instanceof HTMLElement)
        ə.append(...ᴍ(ε.childNodes, ε_clone));
    return ə; }

const 𝐶 = d => {
    const cache_specials = 𝕊 => {
        const psu = 𝕊.e.parentElement ?? <>{𝕊.e}</>;
        for(const c of psu.querySelectorAll("[T]")) {
            if('𝕤' in c) continue;
            𝕊[𝕊.𝐴[id(c)] = c.getAttribute('T')] = c;
            c.removeAttribute('T'); }
        for(let c of psu.querySelectorAll('*')) {
            if('𝕤' in c) {
                if(!('𝑃' in c.𝕤)) c.𝕤.𝑃 = 𝕊;
                continue; }
            c.𝕤 = 𝕊; } }
    const 𝑓 = (...par) => {
        const 𝕊 = merge(d, ...par);
        ᴍ(𝒪(𝕊), ([k,ε]) => (ε instanceof Node) && (𝕊[k] = ε_clone(ε)));
        𝕊.𝐴 = {};
        𝕊.𝐿 = (𝕊, 𝑥) => {
            let k = 𝕊;
            while(k && !(𝑥 in k)) k = k.𝑃;
            return k[𝑥]; };
        (𝕊.𝑅 = cache_specials.bind(null, 𝕊))();
        for(const [k, v] of 𝒪(𝕊))
            if(v instanceof Function)
                𝕊[k] = v.bind(null, v.is𝐶 ? {"𝑃": 𝕊} : 𝕊)
        𝕊.init();
        return 𝕊.e; }
    𝑓.is𝐶 = true;
    return 𝑓; };

const createElement = (tagName, attrs={}, ...children) => {
    const elm = document.createElement(tagName);
    attrs && 𝒪(attrs).forEach(([k,v]) => 
        k == 'HTML' ? elm.innerHTML=v : elm.setAttribute(k,v));
    children && children.forEach(𝑐 => {
        if(𝑐 instanceof Function) {
            const ε = document.createElement("f")
            ε.𝑓 = 𝑐;
            elm.append(ε);
        }else Array.isArray(𝑐) ? elm.append(...𝑐) : elm.append(𝑐); });
    return elm; };