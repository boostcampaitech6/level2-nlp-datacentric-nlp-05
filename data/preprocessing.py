import pandas as pd

train = pd.read_csv("cbert_aug/aug_data_1_7_0_1.0/KLUE-TC/train_epoch_9.tsv", sep='\t')
train.columns = ['text', 'target']
train.to_csv('train_final.csv', index=False)