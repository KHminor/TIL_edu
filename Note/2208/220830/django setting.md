vs code 터미널에 작성

$ python -m venv venv
$ source venv/Scripts/activate
$ pip install django==3.2.13

$pip freeze > requirements.txt

프로젝트 생성

$ django-admin startproject firstpjt .

서버 실행

$ python manage.py runserver

앱 생성

$ python manage.py startapp articles

집으로 가서는 
vs code 에 
pip install -r requirements.txt 
읽어 들여서 설치하기

어플리케이션 생성 

$ python manage.py startapp pages