# CLI Intro

## 각종 명령어

- 파일 생성

  - touch

    ```bash
    $ touch {파일명}  --- {}는 가변형
    ```

- 현재 폴더의 목록 확인

  - ls

    ```bash
    $ ls
    ```

    - 세부 목록 확인

      - ls -a

        ```bash
        $ ls -a
        ```

    - 세부 정보

      - ls -l

        ```bash
        $ ls -l
        ```

        

- 화면 클리어
  - cntl + l

- 현재 폴더 위치

  - pwd

    ```bash
    $ pwd
    ```

- 폴더 만들기

  - mkdir

    ```bash
    $ mkdir {폴더 이름}
    ```

- 현재 작업중인 디렉토리 변경

  - cd (change dir)

    ```bash
    $ cd {폴더 이름}
    ```

- 상위 폴더로 이동

  - cd ..	

    ``` bash
    $ cd ..
    ```

- 한번에 해당 폴더로 이동

  - cd {}/{}/

    ```bash
    Ex) $ cd desktop/lectures/startCamp
    ```

- 해당 위치에서 돌아가서 다른 폴더로 갈때

  - cd ../../{}

    ```bash
    Ex) $ cd ../../name
    ```

- 파일 지우기

  - rm {}

    ```bash
    $ rm {}
    ```

- 폴더 지우기

  - rm -r {}

    ```bash
    $ rm -r {}
    ```



- 절대 경로

  - 루트 디렉토리부터 목적 지점까지 거치는 모든 경로를 전부 작성한 것
  - 윈도우 바탕 화명의 절대 경로 - C:/Users/ssafy/Desktop

- 상대 경로

  - 현재 작업하고 있는 디렉토리를 기준으로 계산된 상대적 위치를 작성한 것

  - 현재 작업하고 있는 디렉토리가 C:/User 일 때

    윈도우 바탕 화면으로의 상대 경로는 ssafy/Desktop

  - ./ : 현재 작업하고 있는 폴더

  - ../ : 현재 작업하고 있는 폴더의 부모 폴더



- git log --oneline 
  밑에서 위로 로그가 남음