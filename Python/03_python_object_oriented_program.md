##  3-1. OOP(객체지향 프로그래밍)
---
- 객체지향 프로그래밍이란?
  - 컴퓨터 프로그래밍의 패러다임(방법론) 중 하나.
  - 컴퓨터 프로그램을 명렁어 목록에서 보는 시각에서 벗어나 여러개의 독린된 단위, 즉"객체"들의 모임으로 파악하고자 하나는 것. 각 객체는 메시지를 주고받고, 데이터를 처리한다.

- 객체
  - 객체란? 클래스에서 정의한 것을 토대로 메모리(저장공간)에 할단된 것. 프로그램에서 사용되는 데이터 또는 식별자에 의해 참조되는 공간을 의미하며, 변수, 자료 구조, 함수 또는 메서드가 될 수 있다.
  - 객체의 구성요소
    - 변수(속성) : 클래스 변수 / 인스턴스 변수
    - 메서드(기능) : 클래스 메서드 / 인스턴스 메서드 / 스태틱(정적) 메서드
  - 클래스로 만든 객체를 인스턴스 라고도 함. ("~~은 인스턴스다." 라는 말보다는 "어떤 클래스(타입)의 인스턴스다." 라고 표현하는게 맞다.)
  - 파이썬은 모든 것이 객체(object).

- 객체와 클래스 문법
  ```python
  class Person: # 클래스 정의
      blood_color = 'red' # 클래스 변수 정의
      count = 0
      def __init__(self, name): # 생성자
          self.name = name # 인스턴스 변수 정의
          Person.count += 1 # 생성시 클래스 변수 접근

      def talk(self): 
          print(f'안녕, 나는{self.name}이야') 
      
      @classmethod # 클래스 메서드. 데코레이터를 사용하여 정의, 첫번째 인자로 클래스(cls)가 전달됨.
      def number_of_population(cls):
          print(f'인구수는 {cls.count}입니다.')
      
      @staticmethod # 스태틱 메서드
      def check_rich(money): # 스태틱 메서드는 cls, self 사용 x
          return money > 10000

 
  person1 = Person('지민') # 인스턴스 생성, 인스턴스 변수 할당
  print(person1.name) # 지민, 인스턴스 변수 접근
  print(Person.blood_color) # 클래스 변수 접근
  print(person1.blood_color) # 인스턴스 내부에서 변수를 찾고 없으면 클래스 변수로 넘어간다. 인스턴스에서 클래스변수 접근 가능.
  Person.blood_color = 'blue' # 클래스 변수 변경.
  person1.blood_color = 'black' #해당 인스턴스만 새로운 인스턴스 변수가 생성됨.
  
  print(isinstance(person1, Person)) # True
  print(type(Person)) # <class 'type'>
  print(type(person1)) # <class '__main__.Person'>
  ```
  - 인스턴스 변수란? 인스턴스가 개인적으로 가지고 있는 속성(attribute), 각 인스턴스 고유 변수
  - 메서드 : 특정 데이터 타입/클래스의 객체에 공통적으로 적용 가능한 행위(함수).
    - 클래스 메서드 / 인스턴스 메서드 / 스태틱 메서드
    - 클래스는 인스턴스 변수 사용이 불가. 인스턴스 메서드는 클래스 변수, 인스턴스 변수 둘 다 사용이 가능.
    - 스태틱 메서드는 클래스, 인스턴스 변수 아무것도 사용하지 않을 경우 사용. 즉, 객체 상태나 클래스 상태 수정할 수 없음
  - 매직 메서드 : Double underscore(__)가 있는 메서드는 특수한 동작을 위해 만들어진 메서드로 특정 상황에서 자동으로 불리는 메서드. 인스턴스 메서드에 포함되어 있다.
  - 데코레이터 : 함수를 어떤 함수로 꾸며서 새로운 기능 부여. @데코레이터(함수명) 형태로 함수 위에 작성. 순서대로 적용 되기 때문에 작성 순서가 중요

- 객체 비교 == vs is
  - == (동등한) : 변수가 참조하는 객체가 동등한(내용이 같은) 경우 True, 두 객체가 같아 보이지만 실제로 동일한 대상을 가리키고 있다고 확인해 준 것은 아님. equal
  - is (동일한) : 두 변수가 동일한 객체를 가리키는 경우(주소까지 같아야 한다.) True. identical

- 인스턴스와 클래스 간의 이름 공간(namespace)
  ```python
  Class Person:
      name = 'nuknown'

      def talk(slef):
          print(self.name)
  
  person1 = Person()
  person1.talk() # unknown

  person2 = Person()
  person2.name = 'Heo'
  person2.talk() # Heo

  print(Person.name) # unknown 
  print(person1.name) # unknown 클래스 변수
  print(person2.name) # Heo 인스턴스 변수
  ```
## 3-2. 객체지향의 핵심 개념
---
- 객체지향의 핵심 4가지 : 추상화 / 상속 / 다형성 / 캡슐화
- 추상화 : 복잡한 것 숨기고, 필요한 것을 들어낸다. (ex, 변수, 함수, 클래스)
- 상속 : 부모클래스와 자식클래스의 관계 -> 물려받기 하위클래스는 상위 클래스에 정의된 모든 요소(속성, 메서드)를 상속받아 사용할 수 있다.(재사용이 가능해진다.)
- 다형성 : 이름은 같은데 동작은 다른 것. 동일한 메서드가 클래스에 따라 다르게 행동할 수 있음을 의미.(메서드 오버라이딩)
- 캡슐화 : 민감한 정보를 숨김. 객체의 일부 구현 내용에 대해 외부로부터의 직접적인 액세스를 차단.(getter/setter) 파이썬에서는 암묵적으로 존재하지만, 언어적으로는 존재하지 않음.