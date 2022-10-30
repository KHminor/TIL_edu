# Django shortcuts functions

get_objects_or_404() 

* 모델 managet objects에서 get()을 호출하지만, 

* 해당 객체가 없을 땐 기존 DoesNoeExist 예외 대신 Http404를 raise함

* 쉽게 말하자면 해당 객체가 있을 땐 get(), 

* 없을 땐 Http404 를 보여준다

  

get_list_or_404()

* 모델 manager objects에서 filter()의 결과를 반환하고
* 해당 객체 목록이 없을 땐 Http404를 raise함





---



Build RESTful API

* DRF(Django Rest Framework)에서 api_view decorators는 필수
  * from rest_framework.decorators import api_view
  * ex) @api_view(['GET','POST'])
* status 보이기
  * from rest_framework import status
* 유효성 검사시 유효하지 않을 때 에러처리
  * is_valid(raise_exception=True)
    * HTTP 400 응답을 반환
* read_only_fields
  * 외래 키 필드를 읽기 전용 필드로 설정
  * 읽기 전용 필드는 데이터를 전송하는 시점에 
    * 해당 필드를 유효성 검사에서 제외시키고 데이터 조회시 출력하도록 함.
* 역참조 데이터 조회시
  * 예를 들어 movie에 대한 comments 를 조회할 경우 
    * 다수일 수 있기 때문에
      *  many=True
    * 읽기만 하기에
      * read_only=True
  * comment model에서 movie를 FK 설정 할 때 
    * movie = FK(..., related_name='comments')
    * related_name을 통해 역참조 시 생성되는 commnet_set을 override 할 수 있다.
  * source
    * 필드를 채우는데 사용할 속성의 이름
    * Ex) movie serializers.py 에서 영화를 조회 시 해당 영화의 댓글 개수까지 함께 출력

` 읽기 전용 필드 지정 이슈 `

* 특정 필드를 overrid 혹은 추가한 경우 read_only_fiedls 가 동작하지 않으니 주의
  * 뭔말이야...

---



forms.py 에서 modelform을 불러오는 방법

* from django import form



ModelForm에서 속성 제외

* exclude = ' '



영화 장르 리스트 만들기

* forms.py
  * CHOICES[('--장르--'),('--장르--'), ]  <---- 형식으로 장르 만들기
  * forms.ChoiceField(choices=CHOICES) <---- 형식으로 넣어주기
  * widget=form.TextInput(attrs={'class':'{{클래스명}}, 'placeholder': {{placeholder}})





comment 작성

* create comment 

  * forms.py
    * exclude 로 movie를 넣어주지 않도록 하기

  * views.py
    * 우선 detail view에서 commentForm을 전송해주고
      * detail.html에서 해당 form이 보이도록 하기
      * create comment 를 작성시 
        * 영화에 대한 pk 값을 가져와서 어떤 영화의 댓글인지 지정하기위해
        *  commentForm에 request.POST 값을 담아서 
        * 유효성 검사 후 
        * 저장하기 전에 (commit=False)
        * 댓글의 영화가 어떤건지 movie를 담아주고 저장하기

* delete comment

  * urls.py 
    * 어떤 영화의 댓글인지 알 수 있도록
      * movie_pk, comment_pk 값 모두 담아서 보내기
  * views.py
    * 우선 detail 함수 수정
      * 현재 해당 영화의 댓글을 모두 찾기위해
        * comments = movie.comment_set.all()
    * delete_comment 생성
      * comment_pk 값으로 comment 를 찾아서 삭제하는 코드 작성 후
      * 댓글에는 영화에 대한 pk값이 없기에 movie_pk 값을 담아주기

---

헷갈리는 포인트

1. update(movie)
   * POST
     * movie = Movie.objects.get(pk=movie_pk)
     * form = MovieModelForm(request.POST, instance=movie)
   * GET
     * form = MovieModelForm(instance=movie)
2. comment(movie)
   * comment_create
     * url에서 movie_pk 보내기
     * view
       * 우선 detail 페이지 수정
         * comment_form = CommentForm() 담아서 보내주고
         * detail.html 에서 보여주기
       * comment_create view
         * movie = Movie.objects.get(pk=movie_pk)
         * comment_form = CommentForm(reqeust.POST)
         * comment_form 유효성 검사 후
         * comment = comment_form.save(commit=False)
         * comment.movie = movie
         * commnet.save 후 detail 페이지로 리다이렉트
   * comment_delete
     * url에서는 어떤 영화의 어떤 댓글인지 알 수 있도록
       * movie_pk, comment_pk를 함께 보내주기
     * view
       * 우선 detail 부터 수정
         * 모든 댓글을 찾기위해
           * movie = Movie.objects.get(pk=movie_pk)
           * comments = movie.comment_set.all() 
           * comment form은 위에서 작성했으니 위에 보고 참고하기
           * 이후 detail 페이지로 보내기
       * comment_delete 
         * 삭제할 댓글을 알 수 있도록
           * comment = Comment.objects.get(pk=comment_pk) 
           * comment.delete() 하여 detail 페이지로 보내기
         * detail 페이지
           * form 태그를 통해 삭제 요청을 보낼 수 있도록 
             * movie_pk와 comment_pk 값을 함께 보내주기



---



에러 코드 

WSGIRequest: render, redirect 실수

