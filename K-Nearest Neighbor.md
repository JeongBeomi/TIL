# K-NearNest Neighbor(K 근접 이웃)
### 0. 목차

### 1. 분류 및 예측을 위한 모델
- Model-based Learning
  - 선형 / 비선형 모델(e.q, liner regression, logistic regression)
  - Neural network
  - 의사 결정 나무
  - Support vector machine
  - 데이터로부터 모델을 생성하여 분류 / 예측 진행
  ![image](https://user-images.githubusercontent.com/109258397/220525121-55e720f1-f627-4f8f-a9f7-5a1de2c68285.png)

- Instance-based Learning
  - K-nearest neighbor
  - Locally weighted regression
  - 별도의 모델 생성 없이 인접 데이트를 분류 / 예측에 사용
  ![image](https://user-images.githubusercontent.com/109258397/220525549-70a94b31-38f9-436c-b8ed-57da7b45f491.png)

### 2. K-Nearest Neighbors
- 새로운 데이터와 가장 가까운 k개의 데이터를 정의하는 것
- KNN알고리즘
  ![image](https://user-images.githubusercontent.com/109258397/220525974-62280178-ce76-4943-b786-1de2dc086491.png)
  - 새로운 데이터가 발생한 이후에 예측 수행
- KNN 알고리즘의 구분 및 특징
  - Instance-based Learning : 각각의 관측치(instance)만을 이용하여 새로운 데이터에 대한 예측을 진행
  - Memory-based Learning : 모든 학습 데이터를 메모리에 저장 후, 이를 바탕으로 예측 시도
  - Lazy Learning : 모델을 별도로 학습하지 않는 테스팅 데이터가 들어와야 비로서 작동하는 게으른 알고리즘
- KNN 분류모델
  ![image](https://user-images.githubusercontent.com/109258397/220531578-37eeb1b3-9573-4dc3-b201-19b5c210e547.png)
  - 인접한 k개의 데이터로부터 majority voting 시행
- 분류 알고리즘
  1. 분류할 관측치 x 선택
  2. x로부터 인접한 k개의 학습 데이터를 탐색
  3. 탐색된 k개 학습 데이터의 majority class c를 정의
  4. c를 x 의 분류 결과로 반환

- KNN 예측 모델
  - k=3이상일 때 나오는 여러 값의 평균값으로 측정하는것이 정확도가 높다
  ![image](https://user-images.githubusercontent.com/109258397/220535824-71777cdd-3312-48a3-a831-0f29a6b871aa.png)
    - k = 1 : 9.0
    - k = 3 : (9.0 + 10.0 + 8.5)/3 = 9.17
  - 예측 알고리즘
    1. 예측할 관측치 x를 선택
    2. x로부터 인접한 k개의 학습 데이터를 탐색
    3. 탐색된 k개 학습 데이터의 평균을 x 의 예측 값으로 반환

### 3. KNN 하이퍼파라미터
- 우리가 결정해야 할것들 = 하이퍼파라미터
  1. k : 인접한 학습 데이터를 몇개까지 탐색할 것인가?
  2. Distance Measures : 데이터 간 거리는 어떻게 측정할 것인가?
- K에 따른 결과
  - k가 매우 작을 경우 : 데이터의 지역적 특성을 지나치게 반영(overfitting)
  - k가 매우 클 경우 : 다른 범주의 개체를 너무 많이 포함하여 오분류할 위험(underfitting)
  ![image](https://user-images.githubusercontent.com/109258397/220537627-9a431e87-7387-4bb5-b705-9883944ca88d.png)
- 거리측도(1-유사도)
  - 다양한 거리측도(Distance measure) 존재
  - 데이터 내 변수들이 각기 다른 데이터 범위, 분산 등을 가질 수 있음, 데이터 정규화를 통해 이를 맞추는 것이 중요

### 4. Weighted KNN
- 새 데이터와 기존 학습 관측치 간의 거리를 가중치로 하여 예측 결과를 도출함