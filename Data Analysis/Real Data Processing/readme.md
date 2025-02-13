# 학습 목표
실전 파이썬 데이터 전처리로 코로나 현황 이해하기

# 학습 내용
- [pandas 라이브러리로 실제 데이터 전처리하기](https://github.com/kimayeon-hub/Python_for_AI/blob/master/Data%20Analysis/Real%20Data%20Processing/Real%20Data%20Processing%20with%20pandas.ipynb)
- [최종 전처리 데이터로 그래프 만들기](https://github.com/kimayeon-hub/Python_for_AI/blob/master/Data%20Analysis/Real%20Data%20Processing/graph%20with%20real%20data%20processing%20file.ipynb)
- 만든 결과물: https://public.flourish.studio/visualisation/21606865/

# 이 학습을 위한 기초 정보
### 데이터 시각화란?
- 데이터 분석 결과를 쉽게 이해할 수 있도록 시각적으로 표현하고 전달되는 과정
- 탐색적 데이터 분석, 데이터 처리, 데이터 예측 모든 경우, 결과를 알아보기 쉽게 하기 위해 데이터 시각화는 필수적임
- 다양한 시작화 기법 중, 흥미로운 데이터 시각화 과정을 진행해보기로 함
  - https://app.flourish.studio
  - https://public.flourish.studio/visualisation/2897018/
 <br>
 
  <img src="https://www.fun-coding.org/00_Images/covid_graph_ex2.jpg" />

  > 지금까지 익힌 데이터 처리 기술을 기반으로 데이터 시각화를 위해, raw data를 포맷에 맞추어 변환하여 그래프를 만들어 보기로 함

### 데이터 시각화를 위한 데이터 포맷 이해
- 데이터 시각화를 위해, raw data를 변환해야 함
- 지금까지 익힌 데이터 처리 기술을 사용해서, 데이터를 변환하기로 함

> 필요한 데이터
>  - 국가명
>  - 국기
>  - 날짜별 확진자 수
<img src="https://www.fun-coding.org/00_Images/covid_ex_data_format.jpg" />

  > 이 형식으로 데이터를 변환시킬 것!
