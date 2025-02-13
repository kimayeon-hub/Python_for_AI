# 학습 목표
데이터 분석을 위한 시각화 라이브러리 사용법 익히기

# 학습 내용
- 가장 빠른 시각화 라이브러리 사용법 이해 (iplot)
- 디테일하고 가장 이쁜 시각화 라이브러리 사용법 이해 ([plotly.graph_objects](https://github.com/kimayeon-hub/Python_for_AI/blob/master/Data%20Analysis/Using%20the%20Visualization%20Library/plotly.graph_objects.ipynb))
- [수치형 데이터와 범주형 데이터](https://github.com/kimayeon-hub/Python_for_AI/blob/master/Data%20Analysis/Using%20the%20Visualization%20Library/numerical%20type%20data%20and%20categorical%20data.ipynb)
- [테이블 데이터와 시계열 데이터](https://github.com/kimayeon-hub/Python_for_AI/blob/master/Data%20Analysis/Using%20the%20Visualization%20Library/Table%20data%20and%20time%20series%20data.ipynb)
- EDA와 데이터 타입에 따른 시각화 기법5

# 학습 내용 정리
### 탐색적 데이터 분석 (EDA)
1. 데이터의 출처와 주제에 대해 이해 <br>
2. 데이터의 크기 확인 <br>
3. <b>데이터 구성 요소(feature)의 속성(특징) 확인</b>
    - `수치형 데이터일 경우`에는 다음과 같이 EDA 5 수치 + 평균(mean) 확인
      - 최소값(minimum), 제1사분위수, 중간값(mediam)=제2사분위수, 제3사분위수, 최대값(maximum) + 평균(mean) 확인
      - 특잇값(outlier) 확인
      - 필요하면 boxplot 과 histogram 그려보기
    - `범주형 데이터일 경우`에는 각 수준별 갯수 세기
      - 필요하면 절대 빈도(bar 그래프), 상대 빈도(원 그래프) 그려보기
    - `시계열 데이터일 경우`에는 필요하면 line 또는 bar 그래프 그리기
    - `feature 간 상관관계 분석이 필요할 경우`에는 heatmap 또는 scatter 그래프 그리기

# EDA를 위한 주요 데이터 시각화 라이브러리
- matplotlib
- seaborn
- plotly

# 가장 최신 기술로, 손쉽게 시각화 익히기
- matplotlib 은 오래된 전통적인 라이브러리
  - 이 한계를 보완하기 위해 seaborn 라이브러리가 출현
  - 오래된 라이브러리로 인터페이스가 복잡함

- 최신 시각화 라이브러리: `plotly`
  - pandas 기능과 plotly 를 조합해서 최신/가장 빠르게 시각화 가능
  - pandas 데이터프레임.iplot() 같은 형태로 데이터프레임을 바로 그래프로 그릴 수 있음
  - https://plotly.com/python/

> 정말 다양한 시각화 기법 중, 가장 쉽게 사용할 수 있는 기법에 익숙해지는 것이 목표
  
  

