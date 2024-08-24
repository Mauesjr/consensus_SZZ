import pandas as pd 
import glob 

files = glob.glob('out/*.json')
szz_unl = pd.read_csv('out/labels.csv')

szz_unl = szz_unl[szz_unl['label'] == 1].reset_index().drop(columns=['label','index'])  


# for file in files:
#     df = pd.read_json(file)
#     bics = list()
#     if file == 'out/maszz.json':
#         for index, row in df.iterrows():
#             for item in row['inducing_commit_hash']:
#                 bics.append(item)   
#     else:
#         continue
#     bics_b = pd.Series(bics).unique()
       

# files.remove('out/maszz.json')

similaridade = pd.DataFrame(columns = ['Variante', 'Similaridade'])

for file in files:
    df = pd.read_json(file)
    intersercao = 0

    bics = list()
    for index, row in df.iterrows():
        for item in row['inducing_commit_hash']:
            bics.append(item)
    bics = pd.Series(bics).unique()
    
    for bic in bics:
        if bic in szz_unl['commit'].astype(str).values:
            intersercao += 1
    uniao = len(bics) + len(szz_unl) - intersercao
    

    similaridade = similaridade._append({'Variante': file.split('/')[1].split('.')[0], 'Similaridade': (intersercao/uniao)*100}, ignore_index=True)
    # similaridade.to_csv('similaridade/maszz.csv', index=False)

# intersercao= 0
# for bic in szz_unl['commit'].astype(str).values:
#     if bic in bics_b:
#         intersercao += 1
#     uniao = len(szz_unl) + len(bics_b) - intersercao

# similaridade = similaridade._append({'Variante': 'unl_szz', 'Similaridade': (intersercao/uniao)*100}, ignore_index=True)
similaridade.to_csv('similaridade/unl_szz.csv', index=False)


    
            
    