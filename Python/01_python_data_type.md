# 01_Python _data_type

## 1-1. Numeric_Type
---
- 정수형(int)
  - 진수 표현 : 2진수(0b) / 8진수(0o) / 16진수(0x)
- 실수형(float)
  - 실수 연산시 주의할 점(부동 소수점) : 컴퓨터는 2진수, 사람은 10진수 사용 0.1이 2진수로 나타내면 0.001100110011...(무한반복)으로 표현되어 근사값만 표시된다
  - ```python
    print(3.2-3.1) != print(1.2-1.1)
    해결법
    # 1. 임의의 작은 수 활용
    print(abs(a - b)) <= 1e - 10) #True
    # 2. python 3.5 이상
    imort math
    print(math.isclose(a, b)) #True
    ```
- 연산자 : + , - , * , / , ** , % , //