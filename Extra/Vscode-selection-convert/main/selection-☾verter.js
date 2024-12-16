const CPY_PATH = `/home/ganer/Projects/cpy`

const fs = require('fs');
const ζ = (...𝔸)=>[...𝔸[0]].map((_,i)=>𝔸.map(x=>x[i]));
const CHARLISTS = fs.readFileSync(`${CPY_PATH}/FontCompose/.SCRIPT_MAP`,
        {encoding: 'utf8', flag: 'r'}).split('\n').map(x=>[...x]);
const [SUP, SUB, NRM] = [{}, {}, {}];
for(const [n,p,b] of ζ(...CHARLISTS)) {
    SUP[n] = p; SUB[n] = b;
    NRM[b] = NRM[p] = n; }
module.exports = {
    sup(s) { return [...s].map(c=>SUP[c]??c).join(''); },
    sub(s) { return [...s].map(c=>SUB[c]??c).join(''); },
    nrm(s) { return [...s].map(c=>NRM[c]??c).join(''); } }