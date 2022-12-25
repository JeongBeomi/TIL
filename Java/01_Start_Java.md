# 01_Start_Java

### 0. Index
1. [Programming & Java](#1-programming--java)
2. [변수와 자료형](#2-변수와-자료형)  


---


## 1. Programming & Java
- Java의 장점
  1. 플랫폼 종속되지 않는 프로그램을 개발하여 여러 플랫폼에서 실행 가능하다.
  ![image](https://user-images.githubusercontent.com/109258397/206990602-7959bd14-1739-4cbc-9273-33b96b1c4d3f.png)
     - 바이트 코드는 완벽한 실행 파일이 아님, 다시 말해 운영체제에 맞는 완벽한 기계어가 아닌 중간 기계어.
     - 이 바이트코드를 실행하기 위해서는 운영체제 맞는 자바 가상머신(Java Virtual Machine; JVM)이 필요.
     - 운영체제에서 직접 실행하는게 아니라 가상 머신에서 먼저 실행 후, 가상머신에서 운영체제에 맞는 실행 파일러 바꿔준다.

  2. 객체 지향 언어이기 때문에 유자보수가 쉽고, 확장성이 좋다.

  3. 프로그램이 안정적이다.
     - C나 C++에서 제공하는 문법인 포인터를 사용하지 않아 메모리를 직접 제어할 수 없다. 하지만 프로그램에서 메모리를 직접제어하면 오류가 발생할 수 있어 이러한 위험성을 사전에 방지
     - 동적 메모리 수거를 프로그래머가 하지 않고 가비지 컬렉터(Garbage Collector; GC)를 이용 메모리 효율적 관리 가능.
      - GC?
    더 이상 사용하지 않는 메모리를 수집하는 기능. C나 C++에서는 필요없는 메모리 사용 해제를 프로그래머가 직접 해야 했지만, 자바는 가비지컬렉터가 사용하지 않는 동적메모리를 주기적으로 수거한다.

<br>

- 구조 : project / package(패키지명 - 소문자 시작) / class(클래스명 - 소문자 시작) 

- 실행파일의 저장 위치
  - 프로젝트 폴더 내부 src 폴더와 bin폴더가 존재.
  - src폴더 : 사용자 작성한 소스 코드(filename.java)가 있는 폴더. 
  - bin폴더 : 컴파일된 실행 파일(filename.class)이 있는 폴더. 해당 파일이 앞서 배운 바이트 코드로 이루어진 자바 클래스 파일입니다.

<br>

---

<br>

## 2. 변수와 자료형

- 컴퓨터에서 수 표현
  - 2진수
  - n개의 비트가 있다면 나타낼 수 있는 숫자의 개수는 2^n개
  - 프로그램에서 표현 : 2진수-0B / 8진수-0 / 16진수-0XA
  - 부호 있는 수를 표현 방법 : 2의 보수
    - -5를 만드는 방법
    1. 10진수 5를 2진수 8비트로 나타낸 00000101의 1의 보수 구하기 -> 11111010
    2. 제일 낮은 자리 1더하기 -> 11111011 = -5
    3. 00000101 + 11111010 = 100000000 최상위 비트는 버려짐 -> 0

<br>

- 변수
  - 처음에 사용한 값과 다르게 변하는 값
  - 해당 데이터를 저정하는 공간
  - 어떤 데이터 형태(문자열, 정수 등)를 저장할 것인지 지정해야 한다. -> 변수의 '자료형'
  ```java
  int variable; // 정수형(int-자료형) 변수 variable을 선언
  variable = 10; // 값 10을 variable변수에 대입
  ```
  - 변수 이름 제약 사항
    - 변수 이름은 영문자(대문자, 소문자)나 숫자를 사용 가능, 특수 문자는 $, _ 만 사용 가능
    - 변수이름은 숫자 시작 불가능
    - 예약어(프로그래밍 언어에서 이미 약속되어 있는 단어) 사용 불가
    - 카멜 케이스 (ex, numberOfStudent)

<br>

- 자료형
  - 기본 자료형 종류
  ![image](https://user-images.githubusercontent.com/109258397/208289425-750cda3a-079a-40c7-ac73-c1c15b5ec5b3.png)  

  - 정수 자료형 (맨 앞 비트는 부호 비트)
  ![image](https://user-images.githubusercontent.com/109258397/208289480-83db139a-bfcb-447b-80b6-f1142c8661df.png)  

  - 자료형이 다른 정수의 덧셈
    ```java
      public static void main(String[] args) {
        short sVal = 10;
        byte bVal = 20;
        System.out.println(sVal + bVal);
      }
      
    ```
    - 정수값 연산시 4바이트를 기본 단위로 사용하기 때문에, 연산전에 모두 int형으로 변환 또한 더한 결과 값도 int형으로 저장.
    - 다른 자료형이 필요없는 것은 아니다. 1바이트 단위 조작하는경우, 다른언어와 호환을 위해서 필요하다.  
 
 <br/> 

- 문자 자료형
  - 컴퓨터 내부에서 표현할 때는 0과 1의 조합
  - 어떤 문자를 표현하기 위해 특정 정수값으로 정하고 약속
  - 이런 코드 값을 모아 둔 것을 '문자 세트'라고 한다
  - 문자 -> 정해진 코드 값 : 인코딩 / 코드 값 -> 문자 : 다코딩
  ![image](https://user-images.githubusercontent.com/109258397/208290498-e22a1900-ce21-420b-8f6e-e2da15aee27f.png)  

  ```java
  	char ch1 = 'A';					// 문자형 자료형 char(2byte)
		System.out.println(ch1);		// A : 문자 출력
		System.out.println((int)ch1);	// 65 : 문자에 해당하는 정수 값(아스키 코드 값)

		char ch2 = 66;					// 정수값 대입
		System.out.println(ch2);		// B : 정수 값에 해당하는 문자 출력
		
		int ch3 = 67; 
		System.out.println(ch3);		// 67 : 정수값 출력
		System.out.println((char)ch1);	// C : 정수 값에 해당하는 문자 출력
  ```
  - 문자 -> ' ' / 문자열 -> " "
  - 문자열 끝에는 항상 널(\0)로 끝난다. ("A" -> "A\0")
  - 자바에서 문자열은 String클래스(추후 학습)

- 실수 자료형
  - 부동 소수점 방식을 사용.
  - float(4byte) / double(8byte)
  ![image](https://user-images.githubusercontent.com/109258397/208619182-37d26650-3f80-4a43-bd28-70674f43f951.png)
  ```java
    public static void main(String[] args) {
      double dnum = 3.14;
      float fnum = 3.14F;		// F-식별자
      
      System.out.println(dnum);
      System.out.println(fnum);
	  7;}
  ```
  - 부동 소수점 방식의 오류 : 지수로 표현되는 값이 0을 나타낼 수 없다 -> 오차 발생
  ```java
  	public static void main(String[] args) {
      double dnum = 1;
      
      for(int i = 0; i < 10000; i++) {
        dnum = dnum + 0.1;
        }

      System.out.println(dnum);
	  }
  ```
  ```
    실행 결과 : 1001.000000000159
  ```

- 논리 자료형
  - boolean형 변수
  - 1바이트로 값을 저정, true(참) / false(거짓) 두가지 값만 가진다.
  ```java
    public static void main(String[] args) {
      boolean isMarried = true;
      System.out.println(isMarried);
	  }
  ```

- 자료형 없이 변수 선언(자바 10부터 생긴 문법)
  - 지역 변수 자료형 추론, 컴파일러가 변수에 대입되는 자료를 보고 추측.
  - 유의 사항
    1. 한번 선언한 자료형 변수를 다른 자료형으로 사용 불가
    2. 지역 변수만 가능({}내에서 사용하는 변수, 자세한 내용은 추후 학습)
  ```java
    public static void main(String[] args) {
      var i = 10;			// int
      var j = 10.0;		// double
      var str = "Hello";	// String
      
      System.out.println(i);		// 10
      System.out.println(j);		// 10.0
      System.out.println(str);	// "Hello"
      
      str = "test";	// 다른 문자열은 대입 가능
      // str = 3;  srt변수는 String형으로 먼저 사용, 정수 값을 넣을 수 없다.
	  }
  ```

- 상수와 리터럴
  - 변하지 않는 수
  - 상수 이름은 대문자를 주로 사용, 여러단어 연결시 _ 기호 권장
  - 상수 선언(final예약어)
  ```java
    public static void main(String[] args) {
      final int MAX_NUM = 100;
      final int MIN_NUM;
      
      MIN_NUM = 0;	// 사용하기전에 초기화. 초기화하지 않으면 오류 발생.
      
      System.out.println(MAX_NUM);
      System.out.println(MIN_NUM);
      
      //MAX_NUM = 10000; 오류 발생 상수는 값을 변경할 수 없다.
	  }
  ```
  - 리터럴
  - 상수