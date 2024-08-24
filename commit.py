import pandas as pd
import glob

files = glob.glob('out/*.json')
files = sorted(files)
print('-----------------')

for file in files:
    print('File:', file)
    df = pd.read_json(file)
 
    for index, series in df.iterrows():
        if series['fix_commit_hash'] == '511a533d15c070ac4c0f9a510dd78f0619581b77':
            for intem in series['inducing_commit_hash']:
                print(intem)
            break
        else:
            continue
    print('-----------------')