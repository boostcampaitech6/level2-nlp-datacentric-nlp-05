# 주제 분류 프로젝트
주제 분류 프로젝트인 KLUE-Topic Classification benchmark는 뉴스의 헤드라인을 통해 그 뉴스가 어떤 topic을 갖는지를 분류해내는 task입니다. 각 문장 데이터에는 IT과학, 경제, 사회, 생활문화, 세계, 스포츠, 정치 중 하나가 라벨링되어 있습니다. 이번 task는 모델의 변경이 아닌 Data-Centric으로 오로지 데이터의 수정으로만 성능 향상을 이끌어냅니다. 

# 평가 지표
### Macro F1
KLUE Topic classification의 공식 리더보드와 동일한 평가 방법인 Macro F1을 사용합니다. 각 라벨별로 F1 score를 계산하고, 모든 label의 각 F1 score에 대한 평균을 계산합니다.

# Data
아래와 같은 구조를 가지고 있습니다.

- ID : 각 데이터 샘플의 고유번호
- text : 분류의 대상이 되는 자연어 텍스트
- target : 정수로 인코딩된 라벨
- url : 해당 데이터 샘플의 뉴스 url
- date : 해당 데이터 샘플의 뉴스가 작성된 날짜와 시간

# 팀 역할 및 실험 내용
| 이름 | 역할 및 실험 내용|
| :--- | :--- |
| 김기호 | • EDA <br/> • Data Augmentation &emsp; |
| 박상기 | • Spell check <br/> • Cleanlab <br/> • Back Translation <br/> • AEDA &emsp; |
| 방신근 | • Paper research &emsp; |
| 심재혁 | • Crawling <br/> • Back Translation <br/> • Customized Cleanlab &emsp; |
| 황순열 | • EDA <br/> • post-analysis <br/> • Data Augmentation(Mixup) &emsp; |
| 김건우 | • Data Augmentation(RS,SR,RD,RI) <br/> • Data Filtering(부산대 맞춤법검사기) <br/> • Data Cleaning &emsp; |