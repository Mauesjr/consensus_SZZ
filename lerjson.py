import json

with open('/home/marco/Documentos/decision_szz/pyszz_v2/out/bic_lszz_1715780238.json', 'r') as file:
    data = json.load(file)
novo_data = data
with open('/home/marco/Documentos/decision_szz/pyszz_v2/out/example3l.json','w') as file:
    json.dump(novo_data,file, indent=4)

