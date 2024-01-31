import pandas as pd


def sampling(df):
    samples_0, samples_1, samples_2  = df[df['target'] == 0], df[df['target'] == 1], df[df['target'] == 2]
    samples_3, samples_4, samples_5, samples_6 = (df[df['target'] == 3].sample(n=int(len(df[df['target'] == 3]) * 0.5), replace=True, random_state=42), 
                                                  df[df['target'] == 4].sample(n=int(len(df[df['target'] == 4]) * 0.5), replace=True, random_state=42), 
                                                  df[df['target'] == 5].sample(n=int(len(df[df['target'] == 5]) * 0.5), replace=True, random_state=42), 
                                                  df[df['target'] == 6].sample(n=int(len(df[df['target'] == 6]) * 0.5), replace=True, random_state=42))
    df_sampled = pd.concat([samples_0, samples_1, samples_2, samples_3, samples_4, samples_5, samples_6], ignore_index=True)
    
    return df_sampled

train = pd.read_csv('train.csv')
train_sampled = sampling(train)
train_sampled.to_csv('train_sampled.csv', index=False)
