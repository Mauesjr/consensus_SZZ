import json
import glob

# with open('consensus_SZZ/out/bic_bszz_1720640354.json', 'r') as file:
#     data = json.load(file)

for file in glob.glob('consensus_SZZ/out/*'):
    with open(file,'r') as arquivo:
        data = json.load(arquivo)
    file_split = file.split('/')
    file_name = file_split[2]
    file_name = file_name.split('_')
    file_name = file_name[1]
    novo_data = data
    with open(file_split[0] + '/' + file_split[1] +'/'+ file_name +'.json','w' ) as novo_arquivo:
        json.dump(novo_data, novo_arquivo, indent = 4)

# with open('/home/marco/Documentos/decision_szz/pyszz_v2/out/example3l.json','w') as file:
    # json.dump(novo_data,file, indent=4)

