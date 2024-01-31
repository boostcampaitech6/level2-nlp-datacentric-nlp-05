from koeda import RD, RI, SR, RS 
from hanspell import spell_checker
from tqdm import tqdm
import re

def data_preprocess(data):
    """
    데이터 전처리를 수행합니다.

    Args:
        data (DataFrame): DataFrame 형태인 train data를 입력으로 받습니다.

    Returns:
        DataFrame: 데이터 전처리를 수행하고 나서 DataFrame을 반환합니다.
    """
    
    for idx, text in enumerate(tqdm(data["text"], desc="data preprocessing")):
        # spelled_data = spell_checker.check(text)                                        # 맞춤법 검사
        preprocessed_data = re.sub('[^A-Za-zㄱ-힣0-9\s]', ' ', text)                      # 특수문자 처리
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
    
    for idx, text in enumerate(tqdm(data["text"], desc="data augmentation")):
        augmented_data = random_delete(text, p=0.2)
        data.loc[len(data)] = [data.iloc[idx, 0], augmented_data, data.iloc[idx, 2], data.iloc[idx, 3], data.iloc[idx, 4], data.iloc[idx, 5]]

    
    return data