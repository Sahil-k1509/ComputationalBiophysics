import json
import os

HLA_LIST_FILE = 'hla_list.txt'
HLA_IMGT_FILE = 'MHC_paratope.txt'
HLA_OUTPUT = 'hla_data.json'

hla_list = []
with open(HLA_LIST_FILE, 'r') as f:
    line = f.readline()
    while line:
        hla_list.append(line.strip())
        line = f.readline()
        
hla_data = {}
with open(HLA_IMGT_FILE, 'r') as f:
    line = f.readline()
    while line:
        try:
            mhc, _, paratope = line.split(',')
            for hla in hla_list:
                if hla in mhc:
                    hla_data[hla] = hla_data.get(hla, []) 
                    hla_data[hla].append(paratope.strip())
        except ValueError: pass
        line = f.readline()
            
json_obj = json.dumps(hla_data, indent=4)
with open(HLA_OUTPUT, 'w') as out:
    out.write(json_obj)
    

try: os.mkdir('fasta_files')
except Exception: pass

for hla, seq_array in hla_data.items():
    fasta_str = ''
    for i in range(len(seq_array)):
        fasta_str += f'>{i}\n'
        fasta_str += seq_array[i] + '\n'
    
    fname = hla.replace('*', '_')
    with open(f'fasta_files/{fname}.faa', 'w') as f:
        f.write(fasta_str)