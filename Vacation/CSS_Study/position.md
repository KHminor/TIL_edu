# Position

## static

- 기본(defaulte)값
- left,right,top,bottom 다 안먹힌다.

## relative

* 상대적인이라는 뜻으로
* position:relative 로 한 뒤 
* left,right,top,bottom에 수치를 적용시키면 아래의 사진과 같이 된다.

<img src="position.assets/image-20221207111810448.png" alt="image-20221207111810448" style="zoom:33%;" />



- 또한 relative는 부모의 위치를 기준으로해서 자신의 위치가 결정된다. (상단의 Hello와 border의 거리 비교) 

<img src="position.assets/image-20221207112003715.png" alt="image-20221207112003715" style="zoom:33%;" /><img src="position.assets/image-20221207112133919.png" alt="image-20221207112133919" style="zoom:33%;" />



## absolute

* 자신의 영역이 붕뜬 상태가 되며

* 아래에 있던 태그가 올라오게 된다.

* 부모로부터 자유로워지게 된다.

  <img src="position.assets/image-20221207112426565.png" alt="image-20221207112426565" style="zoom: 33%;" /><img src="position.assets/image-20221207112442915.png" alt="image-20221207112442915" style="zoom: 33%;" />



부모의 태그가 static이 아닌 relative로 되어 있다면

* 또한 left를 0으로 주게 되면 아래와 같이 부모의 태그의 가장 왼쪽에 붙게 되며

<img src="position.assets/image-20221207112637102.png" alt="image-20221207112637102" style="zoom:50%;" />

* top을 0으로 주게 되면 아래와 같이 부모의 태그 가장 위쪽에 붙게 된다.

<img src="position.assets/image-20221207112757624.png" alt="image-20221207112757624" style="zoom:50%;" />

## fixed