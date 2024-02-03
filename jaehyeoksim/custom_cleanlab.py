import pandas as pd
import numpy as np

def search_wrong_label_idx_1(target_label, output_path):
    """train dataset에서 원본 레이블들과 추론후 레이블들을 비교해서 다른경우의 행을 반환하는 함수
       단, 이 함수를 사용하는 경우에 train dataset의 원본 레이블은 모두 같은경우에만 사용 
        
    Args:
        target_label (int): 원본 레이블
        output_path (str): train dataset을 inference돌려서 나온 CSV파일의 경로

    Returns:
        ndarray: 원본 레이블과 추론 레이블이 일치하지 않는 행들의 모음
    """
    output_df = pd.read_csv(output_path)
    
    wrong_indices = []
    
    for idx, row in output_df.iterrows():
        if row['target'] != target_label:
            wrong_indices.append(idx)
            
    return np.array(wrong_indices)

def search_wrong_label_idx_2(train_path, output_path):
    """train dataset에서 원본 레이블들과 추론후 레이블들을 비교해서 다른경우의 행을 반환하는 함수
       단, 이 함수를 사용하는 경우에 train dataset의 원본 레이블은 모두 같지 않은 경우에만 사용 

    Args:
        train_path (str): 원본 train dataset의 CSV파일 경로
        output_path (str): train dataset을 inference돌려서 나온 CSV파일의 경로

    Returns:
        ndarray: 원본 레이블과 추론 레이블이 일치하지 않는 행들의 모음
    """
    train_df = pd.read_csv(train_path)
    output_df = pd.read_csv(output_path)
    
    train_target = train_df['target']
    output_target = output_df['target']
    
    diff_indices = train_target != output_target
    diff_indices = diff_indices.tolist()
    
    wrong_indices = []
    
    for i in range( len(diff_indices) ):
        if diff_indices[i]:
            wrong_indices.append(i)
    
    return np.array(wrong_indices)

def clean_potential_error_rows(path, wrong_labels):
    """위에서 받은 wrong_indices의 모든 행들을 삭제하는 함수

    Args:
        path (str): 원본 train dataset의 CSV파일 경로
        wrong_labels (ndarray): 원본 레이블과 추론 레이블이 일치하지 않는 행들의 모음
    """
    df = pd.read_csv(path)
    print('prev length ->', len(df))
    df = df.drop(wrong_labels).reset_index(drop=True)
    df.to_csv(path, index=False)
    print('output length ->', len(df))

# wrong_labels = search_wrong_label_idx_1(6, 'output_label_6.csv') # 크롤링한거 cleaning
wrong_labels = search_wrong_label_idx_2('../data/final_5_train.csv', 'output_7.csv') # 합쳐진거 cleaning

print('length of wrong_indices ->', len(wrong_labels))
print("wrong_indices ->", wrong_labels)

# 불일치 행 제거
clean_potential_error_rows('../data/final_5_train.csv', wrong_labels)