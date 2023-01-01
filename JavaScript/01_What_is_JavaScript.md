# 01_What_is_JavaScript?

### 0. Index
1. [자바스크립트로 할 수 있는 것.](#1-자바스크립트로-할-수-있는-것)
2. [웹브라우저와 자바스크립트.](#2-웹브라우저와-자바스크립트)

---

### 1. 자바스크립트로 할 수 있는 것.

- 웹 요소를 제어.
  - 웹 문서의 각 요소를 가져와 스타일을 변경하거나 움직이게 한다.
  - 해당하는 콘텐추만 바뀌어 새로운 콘텐츠를 보여 준다.
  - 서버로 정보를 전송하는 폼에서 입력된 정보가 형식에 맞는지 체크.  

- 웹 애플리케이션을 만든다.
  - 최근 웹은 사용자와 실시간으로 정보를 주고 받으며 마치 애플리케이션처럼 동작.
  - 문서 작성, 그림, 게임, 온라인 길찾기 모두 자바스크립트를 사용.

- 다양한 라이브러리를 사용 가능.
  - 웹플랫폼 중심 서비스가 늘어나면서 웹 브라우저를 통한 상호 작용의 중요해짐.
  - **리액트, 앵귤러, 뷰**와 같은 프레임워크.
  - 그래픽 활용을 위한 D3.js나 DOM을 쉽게 조작할 수 있게 해주는 **제이쿼리** 라이브러리 존재.

- 서버 개발 가능
  - node.js

---

### 2. 웹브라우저와 자바스크립트.
| 웹 브라우저에는 자바스크립트 코드를 읽고 처리하는 해석기(JavaScript interpreter)가 존재. 웹문서에서 `<script>`태그를 이용해 작성 가능. 또는 자바스크립트 소스만 별도 스크립트 파이로 작성 후 웹문서 연결 가능.

- 웹 문서 내부에 `<script>`태그로 자바스크립트 작성.
  - 웹 문서 내부 `<script> </script>`태그 사이에 소스 작성.
  - `<script>`태그는 하나의 문서에 여러개 작성도 가능.
  - 어디에나 위치할 수 있지만 `</body>`태그 직전에 작성 권장.
  - HTML, CSS와 달리 자바스크립트는 대소문자를 구별. (변수명 등 작성시 주의)
  ```html
    <!DOCTYPE html>
    <html lang="ko">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>글자색 바꾸기</title>
      <style>
        body { text-align:center; }
        #heading { color:blue; }
        #text { 
          color:gray;
          font-size:15px;
        }
      </style>	
    </head>
    <body>
      <h1 id="heading">자바스크립트</h1>
      <p id="text">위 텍스트를 클릭해 보세요</p>
      <!-- 자바스크립트 소스 -->
      <script>
        var heading = document.querySelector('#heading');
        heading.onclick = function() {
        heading.style.color = "red";
        }
      </script>
    </body>
    </html>
  ```

- 외부 스크립트 파일로 연결해서 자바스크립트 작성.
  - 