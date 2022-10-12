### 기본적으로  settings.py에서 STATICFILES_DIR을 따로 선언하지 않으면

기본 설정 경로인 app(전체앱)/static/이 기본 경로로 되어있어 모든앱의 static파일을 탐색한다. 이때 서로다른 앱에 static파일안에 동일한 이름의 사진파일이 있을 수 있기에 

articles/static/articles  와 같은 폴더 구조를 만들어서 이름공간을 분리한다.

해당 사진 호출은 다음과 같다.

```html
<img src="{% static 'articles/sample_img_1.jpeg' %}" alt="sample_img">
```

위 코드는 articles / static / articles / sample_img_1.jpeg 와 같은 경로의 사진을 불러온다. 만약 sample_img_1이 articles 앱에 없고 accounts앱의 static / accounts폴더에 있다면
accounts / static / accounts / sample_img_1.jpeg 즉, 다음과 같이 호출\

```html
<img src="{% static 'accounts/sample_img_1.jpeg' %}" alt="sample_img"> 
```

결론은 app(전체 앱 이름) / static 까지는 장고가 자동으로 붙여준다. 이후 경로만 입력하면 된다!



### 이제 기본 app / static 경로가 아닌 내가 원하는 경로에 추가하고싶은경우.

STATICFILES_DIR 을 선언하여 리스트내부에 경로를 추가해준다.

```python
#settings.py
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```

여기서 BASE_DIR은 프로젝트파일이있는 경로를 표시한다. 우리 수업 파일을 기준으로하면 07_DJANGO 안까지만 들어온 경로 즉, BASE_DIR / 'static'  ==  07_DJango / static 

이미지를 호출할 때,

```html
<img src="{% static 'sample_img_2.jpeg' %}" alt="sample_img">
```

07_DJango / static / sample_img_2.jpeg 경로의 파일을 불러온다.

### 그럼 만약 static 파일이 crud(프로젝트) 파일 안에 있으면 ?

전체 경로는 07_Django / crud / assets / sample_img_3.jpeg 이다,
(워크샵 온실 문제에 맞게 statics 파일 이름을 assets로 바꾼 것.)

두가지 방법으로 나눌 수 있다.

1. 애초에 STATICFILES_DIRS 에 crud / assets 경로도 같이 입력해주기.
   
   ```python
   # settings.py
   STATICFILES_DIRS = [
       BASE_DIR / 'crud/assets', # ==  BASE_DIR / 'crud' / 'assets',
   ]
   ```
   
   ```html
   <img src="{% static 'sample_img_3.jpg' %}" alt="sample_img">
   ```

2. crud경로 까지만 추가하기.
   
   ```python
   # settings.py
   STATICFILES_DIRS = [
       BASE_DIR / 'crud',
   ]
   ```
   
   ```html
   <img src="{% static 'assets/sample_img_3.jpg' %}" alt="sample_img">
   ```

3. 주의 할 점은 BASE_DIR이 프로젝트 내부 경로까지 포함하는 것이 아니다.
   
   다음 코드는 이미지 파일을 불러오지 못한다.
   
   ```python
   # settings.py
   STATICFILES_DIRS = [
       BASE_DIR / 'assets',
   ]
   ```
   
   ```html
   <img src="{% static 'sample_img_3.jpg' %}" alt="sample_img">
   ```

    위 코드의 경로는 

    07_Django /  assets / sample_img_3.jpeg  (crud, 프로젝트 파일 경로가 빠져있음.)
