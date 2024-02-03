import pandas as pd
import googletrans

def back_translate(input_str):
    """역번역 process를 진행하는 함수

    Args:
        input_str (str): 역번역을 수행할 '한국어'문장

    Returns:
        str: 역번역 된 '한국어'문장
    """
    translator = googletrans.Translator()
    try:
        result = translator.translate(input_str, dest='en').text
        result = translator.translate(result, dest='ko').text
        return result
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def back_translated_df(df):
    """데이터 프레임 내 모든 'text'열에 대하여 역번역을 수행하는 함수

    Args:
        df (DataFrame): 역번역을 수행할 'text'가 있는 DataFrame

    Returns:
        DataFrame: 역번역 된 'text'가 있는 DataFrame
    """
    i = 0
    j = 0
    new_df = {'ID': [], 'text': [], 'target': [], 'url': [], 'date': []}
    
    for idx, row in df.iterrows():
        origin_data = row['text']
        translated_data = back_translate(origin_data)
        
        if origin_data != translated_data:
            new_df['ID'].append(row['ID'])
            new_df['text'].append(translated_data)
            new_df['target'].append(row['target'])
            new_df['url'].append(row['url'])
            new_df['date'].append(row['date'])
            j += 1
        else:
            i += 1
        
        if idx % 100 == 0:    
            print(f'{idx+1}/{len(df)}  translated : {j} / not translated : {i}')
                
            
    new_df = pd.DataFrame(new_df)  
    df = pd.concat([df, new_df]) 
    print(f'{i} sentences were not translated')   
    return df

# 역번역을 수행할 CSV파일을 DataFrame형태로 불러옴
df = pd.read_csv('../data/final_5_train.csv')

# 역번역 수행(21000문장 기준 약 12시간 소요)
df = back_translated_df(df)

# 역번역 된 문장들과 원래 문장들이 합해진 상태로 CSV파일로 만들기
df.to_csv('../data/final_5_train.csv', index=False)

# 원본문장 + 증강된 문장의 size확인
print(f'translation finished! size:{len(df)}')