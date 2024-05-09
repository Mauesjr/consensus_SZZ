import json

with open('consensus_SZZ/out/bic_agszz_issues_filter_1715256613.json', 'r') as file:
    data = json.load(file)
novo_data = data
with open('consensus_SZZ/out/jenkins_agssz_issue_filter.json','w') as file:
    json.dump(novo_data,file, indent=4)