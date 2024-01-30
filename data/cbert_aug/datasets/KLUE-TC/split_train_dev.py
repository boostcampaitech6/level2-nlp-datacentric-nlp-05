import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("../../../train.csv")
df.drop(columns=['ID', 'url', 'date'], inplace=True)
df.columns = ['sentence', 'label']
df.to_csv("train_dev.tsv", index=False, sep='\t')
train, dev = train_test_split(df, test_size=0.1, stratify=df['label'], random_state=456)
train.to_csv("train.tsv", index=False, sep='\t')
dev.to_csv("dev.tsv", index=False, sep='\t')
