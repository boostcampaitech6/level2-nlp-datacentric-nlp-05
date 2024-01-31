import os
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('../train_sampled.csv')

os.makedirs('./datasets/KLUE-TC', exist_ok=True)
os.makedirs('./aug_data/KLUE-TC', exist_ok=True)

df.drop(columns=['ID', 'url', 'date'], inplace=True)
df.columns = ['sentence', 'label']

df.to_csv('./datasets/KLUE-TC/train_dev.tsv', index=False, sep='\t')
df.to_csv('./aug_data/KLUE-TC/train_origin.tsv', index=False, sep='\t')

train, dev = train_test_split(df, test_size=0.1, stratify=df['label'], random_state=456)
train.to_csv('./datasets/KLUE-TC/train.tsv', index=False, sep='\t')
dev.to_csv('./datasets/KLUE-TC/dev.tsv', index=False, sep='\t')