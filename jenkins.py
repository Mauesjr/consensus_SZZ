import json

with open('marco_szz/issue_list.json', 'r') as file:
    data = json.load(file)

# for chave in data:
#     del data[chave]['creationdate']
#     del data[chave]['commitdate']
#     data[chave]['fix_commit_hash'] = data[chave].pop('hash')
#     data[chave]['earliest_issue_date'] = data[chave].pop('resolutiondate')
#     data[chave]['repo_name'] = 'jenkinsci/jenkins'

print(len(data))
'''
Importante resaltar que o jenkins é feito de forma
'''

# novo_data = list(data.values())

# with open('/home/marco/Documentos/decision_szz/consensus_SZZ/issue_list_rosa.json','w') as file:
    # json.dump(novo_data,file, indent=4)

