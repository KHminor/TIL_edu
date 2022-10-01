## Problem_a.py

1. 문제 해결 방법

   교수님께서 설계해주신 구조를 기반으로 작성했습니다.

   ```bash 
   result = {
   'id' : movie.get('id'), 
   'title' : movie.get('title'), 
   "poster_path" : movie.get("poster_path"), 
   "vote_average" : movie.get("vote_average"), 
   "overview" : movie.get("overview"), 
   "genre_ids" : movie.get("genre_ids")
   }
   return result
   ```

   

2. 어려운 점과 문제가 생겼던 원인

   1. 하나의 딕셔너리 구조에 딕셔너리를 넣어주는 것이 익숙하지 않아서 어려웠습니다.

   2. 딕셔너리에 값을 추가하는 방법이 헷갈렸습니다.

      ```bash
      # python dict의 값 얻어오기
      # a.get('key값') 
      # a['key값']
      ```





---



## Problem_b.py

1. 문제 해결 방법

   1. 기존의 problem_a 의 구조에서 genres_ids 를 추가로 받았습니다.

      ```bash 
      a = movie.get("genre_ids")
      ```

      

   2. 첫번째 for문을 이용해 genres 파일의 모든 장르의 수 만큼 비교할 수 있게 하였고

      두번째 for문을 이용해 영화의 개수대로 반복할 수 있게 하여

      첫번째 for문의 genres의 값과 두번째 for문의 해당 영화의 genres와 같은지 비교할 수 있게 하였습니다.

      

      ```bash
          a = movie.get("genre_ids")
          li = []
          le = len(a)
          for i in range(len(genres)):
              for j in range(le):    
                  if genres[i].get("id") == a[j]:
                      li.append(genres[i].get("name"))
      ```

   3. 그리고 비교하여 같은 값이 나왔다면 해당 값을 기존에 정의했던 리스트 타입 li에 append 하여 

      모두 반복하여 추가한 li값을 Dict 타입 변수 result 의 genre_ids에 지정하였습니다.

      ```bash
          result = {
              'id' : movie.get('id'), 
              'title' : movie.get('title'), 
              "poster_path" : movie.get("poster_path"), 
              "vote_average" : movie.get("vote_average"), 
              "overview" : movie.get("overview"), 
              "genre_ids" : li        
          }
          return result
      
      ```

   

2. 어려운 점과 문제가 생겼던 원인

   1. JSON형태의 구조의 여러 값이 있는 상태에서 어떻게해야 값을 얻을 수 있는지에 대한 어려움
   2. 받아온 값이 리스트형태로 2개가 있는 경우 해당 값을 또 다른 JSON 파일의 값과의 연동하여 얻기
   3. 단순히 Key와 Valus로만 보게 되어 자료구조에 대한 혼동이 있었습니다. (ex. 모두 dict, 모두 list) )



---



## Problem_c.py

1. 문제 해결 방법

   기존의 problem_b 의 구조에서 하나의 영화에 대한 자료가 아닌 다양한 영화들의 자료들을 

   통해 원하는 것을 리턴해야 하기에 problem_b 의 구조에서 전체를 반복문을 통해 

   기존에 정의했던 new_list에 축적을 하여 retrun 하여 해결 했습니다.

   ```bash
       new_list = []
       for m in range(len(movies)):
           
           a = movies[m].get("genre_ids")
           li = []
           le = len(a)
           for i in range(len(genres)):
               for j in range(le):    
                   if genres[i].get("id") == a[j]:
                       li.append(genres[i].get("name"))
           # print()
           # genre_names = dict(zip(a,li))
           
   
           # [18, 80]
           result = {
               'id' : movies[m].get('id'), 
               'title' : movies[m].get('title'), 
               "poster_path" : movies[m].get("poster_path"), 
               "vote_average" : movies[m].get("vote_average"), 
               "overview" : movies[m].get("overview"), 
               "genre_ids" : li     
           }
           new_list.append(result)
       return new_list
   ```

   

2. 어려운 점과 문제가 생겼던 원인

   1. 하나의 영화의 데이터에서 다양한 영화의 데이터를 받는다는게 단순한 듯하면서 복잡하게 생각하게 

      되어져서 어려웠습니다.



---

## Problem_d.py

1. 문제 해결 방법

   영화 데이터들을 반복문을 통해 돌아가며 들어가 원하는 데이터를 얻고 난 뒤 기존의 값과 비교하여 

   해당  revenue 값이 기존 값보다 클 경우 기존에 정의했던 get_revenue에 추가하는 동시에 

   revenue 값의 영화 이름을 best_title에 넣어주어 마지막으로 가장 큰 revenue 값을 가진 영화 이름을 

   리턴 하여 해결했습니다.

   ```bash
   get_revenue = 0
   best_title = ""
   for i in range(len(movies)):
   
   id = movies[i].get("id")
   
   open_f = open(f'data/movies/{id}.json', encoding='utf-8')
   open_f_list = json.load(open_f)
   open_revenue = open_f_list.get('revenue')
   open_title = open_f_list.get("title")
   if get_revenue < open_revenue:
   get_revenue = open_revenue
   best_title = open_title
   
   return best_title
   ```



2. 새롭게 시도한 것

   다른 파일