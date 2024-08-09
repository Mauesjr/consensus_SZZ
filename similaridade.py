import pandas as pd 
import glob 

files = glob.glob('out/*.json')

for file in files:
    df = pd.read_json(file)
    bics = list()
    if file == 'out/rszz.json':
        for index, row in df.iterrows():
            for item in row['inducing_commit_hash']:
                bics.append(item)   
    else:
        continue
    bics_b = pd.Series(bics).unique()
       

files.remove('out/rszz.json')

similaridade = pd.DataFrame(columns = ['Variante', 'Similaridade'])

for file in files:
    df = pd.read_json(file)
    count = 0
    bics = list()
    for index, row in df.iterrows():
        for item in row['inducing_commit_hash']:
            bics.append(item)
    bics = pd.Series(bics).unique()
    for bic in bics:
        if bic in bics_b:
            count += 1
    similaridade = similaridade._append({'Variante': file.split('/')[1].split('.')[0], 'Similaridade': count/len(bics_b)*100}, ignore_index=True)

similaridade.to_csv('similaridade/rszz.csv', index=False)



    
            
    