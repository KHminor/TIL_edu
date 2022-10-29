1. project 생성

2. app 생성

   1. 생성 후 settings.py 에서 등록
   2. 프로젝트의 urls.py 에서 앱으로 url을 보낼 수 있도록 include 하기
   3. JSON 데이터를 가져오는거만 하는게 아니면 해당 앱에서 urls.py 에서 앱 등록

3. CRUD+comment

   1. model 작성

      1. 예를 들어 movie를 작성한다고 하면 title,description,audience,Release_date,score, genre 등등 작성

   2. form 작성

      1. 해당 앱에 forms.py 를 생성하여 forms.modelform를 통해 클래스를 생성

   3. index 작성

      1. 기본 페이지 작성

   4. create 작성

      1. get 요청의 경우와 post 요청의 경우에 맞게 데이터 보내주기 

   5. detail 작성

      1. movie_pk에 맞는 영화를 html로 보내주기

   6. delete 작성

   7. update 작성

      1. create 와 마찬가지로 get 요청과 post 요청에 맞게 데이터 보내기
      2. 여기서 주의 할 것은 기존 데이터에 수정을 하는것이기에 
      3. modelform(request.POST, instance=request.data) 하기

   8. comment

      1. comment 작성을 위한 model 수정

         1. comment model 요소
            1. movie(FK), content, created_at, updated_at
         2. 여기서 FK 작성 유의
            1. comment에서 movie를 참조하기에 
            2. ForeignKey를 사용하고
            3. 첫번째 요소로 Movie 클래스를 넣어주고
            4. 다음으로는 제약조건으로 models.CASCADE 를 넣어준다.

      2. comment 생성

         1. urls.py 에 movie_pk 값과 함께 comment_create 를 만든다.

         2. 그리고 views.py에 코멘트 생성을 위해 POST 요청에 맞게 작성

         3. POST

            1. movie를 찾기 위해 pk 값에 맞는 movie를 찾아준다
            2.  movie_form 에는 request.POST 값을 담은 ModelForm을 보내준다.
            3. comment_form의 유효성 검사 후
            4. comment_form.save() 하기 전에 (commit=False) 하여 comment에 담아주고
            5. comment.movie= movie를 하여 어떤 영화의 댓글인지 넣어주고
            6. comment.save() 해주기

         4. def detail 에서 comment 를 보여줄 수 있도록 하기

            1. movie를 먼저 movie_pk 에 맞는걸 담아주고

            2. comment_form에 ModelForm을 담아서 보내주고 

            3. comments = movie.comment_set.all() 하여 담아준다

               - 여기서 _set을 하는 이유는 영화 입장에서 댓글은 

                 ​	역참조하는 것이기 때문.

            4. context에 담아주기

            5. 이후 detail.html 에서 if 문을 통해 comment 가 있다면 보여주고

            6. for 문을 통해 comments 안에서 comment 를 하나씩 꺼내 보이기

            7. comment.content 로 댓글 내용 보이도록 하기  

      3. comment 삭제

         1. url에서 movie_pk와 comment_pk 를 함께 담은 url 만들기
         2. view에서는 movie를 찾을 필요 없이
         3. comment = Comment.objects.get(pk=comment_pk)를 하여 찾고
         4. comment.delete()를 해주고
         5. redirect를 통해 detail.html 에 movie_pk를 보내준다.
         6. 이후 datail.html 에서 comment를 삭제할때는 comment 보이는 하단에
         7. form 태그를 통해 movie.pk와 comment.pk 를 함께 보내 POST 요청 보내기

4. 

