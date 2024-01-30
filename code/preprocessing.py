import pandas as pd
import re

from koeda import RD, RI, SR, RS 

def data_preprocess(data):
    """
    데이터 전처리를 수행합니다.

    Args:
        data (DataFrame): DataFrame 형태인 train data를 입력으로 받습니다.

    Returns:
        DataFrame: 데이터 전처리를 수행하고 나서 DataFrame을 반환합니다.
    """
    
    for idx, text in enumerate(data["text"]):
        preprocessed_data = re.sub('[^A-Za-zㄱ-힣0-9\s]', ' ', str(text))    # 특수문자 제거
        data.iloc[idx, 1] = preprocessed_data
        
        
    return data


def data_augmentation(data):
    """
    데이터 증강을 수행합니다.

    Args:
        data (DataFrame): DataFrame 형태인 train data를 입력으로 받습니다.

    Returns:
        DataFrame: 데이터 증강을 수행하고 나서 DataFrame을 반환합니다.
    """
    
    random_delete = RD()    # 문장 내의 각 단어들을 무작위로 제거
    random_insert = RI()    # 하나의 단어를 선택하고 그 단어의 유의어를 문장내의 임의의 위치에 삽입
    random_swap = RS()      # 랜덤으로 2개의 단어를 선택해 위치를 바꿈
    synonym_replace = SR()  # stop words가 아닌 단어들 중에서 랜덤으로 선택해 유의어로 교체
    
    for idx, text in enumerate(data["text"]):
        length = len(data)
        
        augmented_data1 = random_delete(text, p=0.1)
        augmented_data2 = random_insert(text, p=0.1)
        augmented_data3 = random_swap(text, p=0.1)
        augmented_data4 = synonym_replace(text, p=0.1)
        
        data.loc[length] = [data.iloc[idx, 0], augmented_data1, data.iloc[idx, 2], data.iloc[idx, 3], data.iloc[idx, 4]]
        data.loc[length+1] = [data.iloc[idx, 0], augmented_data2, data.iloc[idx, 2], data.iloc[idx, 3], data.iloc[idx, 4]]
        data.loc[length+2] = [data.iloc[idx, 0], augmented_data3, data.iloc[idx, 2], data.iloc[idx, 3], data.iloc[idx, 4]]
        data.loc[length+3] = [data.iloc[idx, 0], augmented_data4, data.iloc[idx, 2], data.iloc[idx, 3], data.iloc[idx, 4]]
    
    
    return data