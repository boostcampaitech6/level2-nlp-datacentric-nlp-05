import pandas as pd
import re

def data_preprocess(data):
    """데이터 전처리를 수행합니다.

    Args:
        data (DataFrame): DataFrame 형태인 train data를 입력으로 받습니다.

    Returns:
        DataFrame: 데이터 전처리를 수행하고 나서 DataFrame을 반환합니다.
    """
    
    for idx, text in enumerate(data["text"]):
        preprocessed_data = re.sub('[^A-Za-zㄱ-힣0-9\s]', ' ', text)    # 특수문자 제거
        preprocessed_data = re.sub('[一-龥]', '', preprocessed_data)    # 한자 제거
        data.iloc[idx, 1] = preprocessed_data
        
        
    return data