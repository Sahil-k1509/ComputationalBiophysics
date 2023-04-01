# import os

# files = os.listdir('aligned_hla')

# for file in files:
#     outstring = ''
#     with open(f'aligned_hla/{file}', 'r') as f:
#         line = f.readline()
#         if line[0] == '>': continue
#         else:
#             while line and line != '\n':
#                 idx, _, sequence, length = line.split()
#                 outstring += f'>{idx}\n{sequence.upper()}\n'
#                 line = f.readline()
                
#     with open(f'aligned_hla/{file}', 'w') as f: 
#         f.write(outstring)

out = ''
with open('hla_paratope_msa.fa', 'r') as f:
    line = f.readline()
    while line and line != '\n':
        if line[0] == '>': 
            _, hla = line.split()
            seq = f.readline().strip()
            out += f'{hla}\t{seq}\n'
            line = f.readline()
            
with open('hla_msa.txt', 'w') as f:
    f.write(out)