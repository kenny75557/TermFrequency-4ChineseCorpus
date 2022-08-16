import json
from tqdm import tqdm

with open('/user_data/TermFrequency-4ChineseCorpus/data/wiki_data/wiki_tokenize_2021_08_05_500000.json') as file:
    wiki_data=json.load(file)

flag_list=['n','ng','nr','nrfg','nrt','ns','nt','nz']
tf_table={}

print(wiki_data[0])
# for doc in tqdm(wiki_data):
#     for 