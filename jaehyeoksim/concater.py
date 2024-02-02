import pandas as pd

def editer(path):
    """해당 파일의 'text'열에 있는 문자중 삭제하고 싶은 문자를 삭제해주는 함수

    Args:
        path (str): 대상 CSV파일 경로
    """
    df = pd.read_csv(path)
    df['text'] = df['text'].str.replace('\[포토S\] ', '', regex=True)
    print(df['text'])
    df.to_csv(path, index=False)
    
def set_rows(path, size):
    """해당 파일의 사이즈를 랜덤으로 size의 크기에 맞춰주는 함수

    Args:
        path (str): 대상 CSV파일 경로
        size (int): 목표 size
    """
    df = pd.read_csv(path)
    sampled_df = df.sample(n=size, replace=False).reset_index(drop=True)
    sampled_df.to_csv(path, index=False)  
    
# 각 레이블 별 크롤링한 데이터
crawled_files = ['../data/005_2_train.csv',
                 '../data/023_4_train.csv',
                 '../data/023_6_train.csv',
                 '../data/477_5_train.csv',
                 '../data/092_0_train.csv',
                 '../data/215_1_train.csv',
                 '../data/346_3_train.csv']

# 빈 DataFrame생성
df = pd.DataFrame()

# 각 레이블 별 크롤링한 데이터를 2,000개로 모두 맞줘서 합함(다 합하면 14,000개)
for file in crawled_files:
    set_rows(file, 2000)
    df1 = pd.read_csv(file)
    df = pd.concat([df, df1])
    
# 혹시 있을 수 있는 Nan값 제거, target label값 float로 있을수 있으니 int로 맞춰줌
df.dropna(inplace=True)
df['target'] = df['target'].astype(int)  

# baseline train을 크롤링한 데이터들과 합침(다 합하면 21,000개)
df1 = pd.read_csv('../data/train.csv')
df = pd.concat([df, df1])

# 학습 시 편향을 막기 위해 각 행들을 랜덤으로 섞음
df = df.sample(frac=1).reset_index(drop=True)

# CSV파일로 만듦
df.to_csv('../data/file_name_train.csv', index=False)

# 제거하고 싶은 문자 제거
editer('../data/file_name_train.csv')