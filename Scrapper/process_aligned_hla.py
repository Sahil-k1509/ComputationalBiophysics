import os
import json

files = os.listdir('aligned_hla')

sequences = {}
for file in files:
    path = f'aligned_hla/{file}'
    seq_list = []
    with open(path, 'r') as f:
        line = f.readline()
        while line and line != '\n':
            if line[0] == '>': pass
            else: seq_list.append(line.strip().upper())
            line = f.readline()
    
    sequences[file.split('.')[0].replace('_', '*')] = seq_list
    

consensus_paratope = {}    
outputstr = ''    
for hla, alinged_seq in sequences.items():
    n, m = len(alinged_seq), len(alinged_seq[0])
    avg_paratope = ''
    for j in range(m):
        pos_counter = {}
        cmax = 0
        maxchr = ''
        for i in range(n): 
            if alinged_seq[i][j] == '-': continue
            pos_counter[alinged_seq[i][j]] = pos_counter.get(alinged_seq[i][j], 0)+1
            if pos_counter[alinged_seq[i][j]] > cmax:
                cmax = pos_counter[alinged_seq[i][j]]
                maxchr = alinged_seq[i][j]
        avg_paratope += maxchr
        
    consensus_paratope[hla] = avg_paratope
    outputstr += f'>{hla}\n{avg_paratope}\n'

with open('consensus_par.faa', 'w') as f: f.write(outputstr)

data = json.dumps(consensus_paratope, indent=4)
with open('consensus_paratope.json', 'w') as f:
    f.write(data)