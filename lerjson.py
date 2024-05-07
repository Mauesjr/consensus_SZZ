import json

with open('consensus_SZZ/out/bic_bszz_1715084601.json', 'r') as file:
    data = json.load(file)
novo_data = data
with open('consensus_SZZ/out/jenkins_bssz.json','w') as file:
    json.dump(novo_data,file, indent=4)