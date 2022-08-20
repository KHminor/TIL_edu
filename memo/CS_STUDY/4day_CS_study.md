# Process Synchronizion



##### 프로세스간의 동기화 문제 발생 원인과 예시

우선 데이터의 접근에 대해서 한번 더 집고 넘어가자면

컴퓨터 안에서 어떤 연산을 할 경우 

항상 데이터를 읽어 와서 연산을 하고 결과를 다시 어딘가에 저장하도록 되어있다.

<img src="CPU and IO Bursts in Program Execution.assets/apahfl-16604647981193.PNG" style="zoom:33%;" />

예를 들어 

1. CPU와 메모리가 있을 경우 ( 3. 연산 = CPU, 1. Data = 메모리) 

   - 메모리에 있는 데이터를 읽어와서 CPU에서 연산을 하고 연산을 마친 해당 데이터를 다시 메모리에 넣을 것입니다.

   

2. 컴퓨터 내부와 I/O를 하는 하드디스크의 경우

   - 하드디스크에 있는 파일을 읽어와서 컴퓨터 내부에서 어떤 작업을 하고 해당 결과를 밖으로 내보낼 것입니다.



**다만 이런 상황에서 문제가 되는 것은**

이러한 데이터를 한 군데에서 읽은 후 연산을 하는 것이 아닌 여러 곳에서 읽은 후 연산을 하는 과정에서 문제가 발생하게 된다.

예를 들어 Storage- box 에 저장되어 있는 count 라는 변수 값이 있는데 해당 count를 다른 Execution-box에서 활용을 하려고 하는데 

연산을 마무리 하고 다른 곳에서 count를 사용할 경우 문제가 되지 않지만 

좌측 box에서 count를 읽은 후 연산을 하는 도중 우측 box에서 count를 읽은 후 연산을 한다면 

각각의 box들은 완료된 count의 값을 가지고 연산을 하는 것이 아닌 완료 이전의 count 값을 가지고 연산을 하기에 문제가 발생하게 된다.   

<img src="CPU and IO Bursts in Program Execution.assets/race.PNG" style="zoom:33%;" />

그래서 지금처럼 하나의 공유데이터를 다수가 동시에 접근하려 할때 생기는 문제를 Race Condition 즉 경쟁 상태라고 한다.



이제 본론으로 들어와 프로세스 동기화 문제에 알아보자면

공유 데이터의 동시 접근은 데이터의 불일지 문제를 발생시킬 수 있으며

race condition(경쟁 상태)을 막기 위해서는 concurrent process(병행 프로세스)는 동기화가 되어야 한다. 

그래서 병행 프로세스 사용으로 인한 일관성(Consistency) 문제를 해결하기 위해선 협력 프로세스 간의 실행 순서를 정해주는 메커니즘이 필요하다.



<img src="CPU and IO Bursts in Program Execution.assets/race2.PNG" style="zoom:33%;" />

위의 그림처럼 각각의 프로세스가 X라는 공유데이터를 가지고 1을 더하거나 빼는 처리를 하고 싶을 때 

고급언어에서의 X = X+1 or X = X-1가 기계어로 바뀌게 되면 원자적(Atomic)으로 전송이 되는 것이 아닌 

여러개의 기계어인 초록색, 파란색 말풍선 과정으로 나뉘어 실행 된다고 한다. 	

초록색 말풍선을 예시로 본다면 

1. 변수 X는 reg1에 읽혀져서 
2. reg1 값을 1 증가 시킨 후 
3. 해당 reg1을 다시 메모리에 저장하는 작업이 일어난다.

그런데 해당 작업이 일어나는 도중에 쪼개져서 CPU가 다른 프로세스한테 넘어가게 되는 경우에 문제가 발생하게 된다.

---



##### Critical-Section Problem

n 개의 프로세스가 공유 데이터를 동시에 사용하기를 원하는 경우 : critical section 

각 프로세스의 code segment에는 공유 데이터를 접근하는 코드인 critical section이 존재

이때 critical section이란 공유 데이터를 의미하는 것이 아닌 

공유 데이터를 각각의 프로세스가 접근하는 코드를 critical section 이라고 한다.

<img src="CPU and IO Bursts in Program Execution.assets/critical section.PNG" style="zoom:33%;" />

그래서 critical section에 들어갔을 경우 다른 모든 프로세스가 critical section에 들어갈 수 없도록 해야한다.

쉽게 생각한다면 p1에서 critical section에 들어갔을 경우 Lock을 걸어 다른 모든 프로세스가 critical section에 들어갈 수 없도록 한 후 

작업이 완료 된 후 Unlock을 하여 다른 프로세스도 처리할 수 있도록 하는 과정을 의미한다. 

<img src="CPU and IO Bursts in Program Execution.assets/inti.PNG" style="zoom:33%;" />\

위의 사진처럼 critical section을 수행하기 전에 

CPU를 빼앗기더라도 다른 프로세스가 동일 데이터에 접근하는 critical section을 수행하지 못하도록 코드를 추가하고 (Lock)

수행을 완료 후엔 unlock을 하여 다른 프로세스도 접근 할 수 있도록 한다. (unlock)

---



##### 해결 알고리즘 1 - turn

아래의 그림에서 Synchronization variable 이란 

프로세스 들은 수행의 동기화를 위해 몇몇 변수를 공유할 수 있다 라는 의미로 받아들이면 좋을 것 같다.

<img src="CPU and IO Bursts in Program Execution.assets/al1.PNG" style="zoom:33%;" />

우선 critical section에 들어가기 전에 turn을 체크하게 되는데 

여기서 turn은 누구의 차례인지를 의미하는데 

- 현재 turn == 0 의 경우 나의 turn 이 되는 것이고
- 현재 turn == 1 의 경우 나의 turn 이 아니고 다른 프로세스의 차례를 의미한다.

그래서 위의 노란색 구역을 해석해 보자면 

우선 while (turn != 0): 을 들어가면

- 현재 turn 이 1인 상태로 나의 차례가 아닌 경우 해당 위치에서 머무르고 
- turn이 0의 경우 critical section에 들어간다고 한다.



현재 turn 이 0이 아닌 경우 ( 즉 나의 차례가 아닌 경우) 

-  계속 while 문만 돌다가 할당된 CPU 시간만 소비하고 반납을 하게 된다. 



그런데 여기서 turn이 어떻게 나의 차례인 0으로 변경이 되는가 하면 상대방에 의해서 바뀌게 된다. 

위의 그림을 다시 보자면 critical section을 사용하고 나갈 때 turn = 1 즉 상대방으로 변경되기에 나의 차례가 0으로 변경 될 수 있게 된다.



Turn Algorithm을 정리하자면 

- critical section에 들어가기 전에 이번이 나의 차례인지를 체크해서 
- 나의 차례가 아닌 경우 (turn = 1) 이면 계속 기다리고
- 나의 차례인 경우 (turn = 0) 이면 critical section에 들어가서 공유 코드를 수행하고 
- 처리가 끝나게 되면 나의 차례를 상대방 차례로 변경 (turn = 0 -> 1) 



**<문제점>**

물론 동시에 들어가는 경우는 turn 으로 인해 생기지 않는데

다만 엄격하게 turn을 상대방 1번 , 나 1번 식이다 보니 반드시 한번씩 교대로 들어가야 하기에 

critical section의 빈도수가 많은 프로세스가 있을 경우는 불합리 하게 계속 기다리게 되는 상황이 발생하게 된다.



**<프로그램적 해결법의 충족 조건>** 

<img src="CPU and IO Bursts in Program Execution.assets/goruf-166047125781910.PNG" style="zoom:33%;" />

Bounded Waiting = No starvation (기아현상 방지) 으로 Progress 와는 달리

여러 프로세스가 있을 경우 예를 들어 프로세스 A,B,C 가 있을 경우

A와 B만 서로 turn을 주고받고 할 경우 C는 Starvation이 발생하게 되는데 이를 방지하는 조건.

---



##### 해결 알고리즘 2 - flag

<img src="CPU and IO Bursts in Program Execution.assets/algo2.PNG" style="zoom:33%;" />

Flag Algorithm은 

프로세스마다 각자의 flag가 있는데 critical section에 들어가고 싶다라고 하면

- 자신의 flag를 들어서(flag = true) critical section에 들어가고 싶다라는 의중을 두게 된다.

- 들어가기전에 다른 프로세스들 중에서도 flag를 들어서 flag = true 상태가 되어있는지 체크하여 동시 접근이 안되도록 방지.

  (현재는 프로세스 i, j 가 있기에 flag[j] == True 인지를 확인)  

  - 만약 flag가 들려있다면 while 문을 계속 돌면서 critical section에 들어가지 않는다.
  - 만약 flag가 내려저 있다면(flag == False) critical section에 들어가게 된다.

- 이때 flag가 내려지게 되는 경우는 

  - 누구나 critical section에 들어갔다 나오게 되는 경우를 만들어 
  - flag를 내리게 하는 flag [i] = false를 수행하게 한다 ( 현재는 프로세스 i이기에 flag[i])



**<문제점>**

우선 동시에 들어가게 되는 경우는 방지하게 된다 flag를 들어서 바로 들어가는 것이 아닌 

다른 프로세스들도 들었는지 확인을 하는 while 문을 돌기 때문에 Mutual Exclusion(상호 배제)은 방지하게 된다.

다만 flag algorithm 도 turn algorithm 처럼 critical section을 수행하는 프로세스가 없는 경우에도 진행이 안되는 문제가 발생하게 된다.

우선 flag를 든다고 해서 critical section에 들어가는 것을 잘 기억하고 

상대방이 flag를 들었다고 해서 못들어가는 상황을 예로 들어보자면

- flag를 들기만하고 아직 critical section 들어가지 못한 상황이라면 
- 나는 상대방이 flag를 들었으니까 계속 기다려야지 하는 상황이 계속 되는 것이기에
- 진행이 되지 않는 문제가 발생하게 된다. (Not progress requirement)

---



##### Peterson's Algorithm

perterson's algorithm의 경우 앞서 소개한 turn, flag algorithm의 변수를 모두 사용하게 된다.

<img src="CPU and IO Bursts in Program Execution.assets/peter.PNG" style="zoom:33%;" />

**<순서>**

- flag를 이용해서 critical section에 들어가겠다는 의중을 표하고
- turn을 우선 상대방의 turn으로 만들어 놓고 (이유가 있기에 turn을 상대방으로 바꾼다고 한다.)
- 체크를 한다.
  - 상대방이 flag를 들고 있는지와 
  - 이번 차례가 상대방 차례인지.
  - 위의 두가지를 만족할 경우 while문을 돌며 기다리고 
  - 둘중 하나라도 아닌 경우 critical section에 들어가게 된다.
- 그리고 critical section를 다 사용하고 나올때는 flag를 False로 변경 후 나오게 된다.

**<문제점>**

비효율적인 문제점이 있다.

만약에 해당 프로세스가 critical section에 들어가지 못하는 상황일 경우 

즉 while 문에서 빠져나가지 못하는 경우

CPU를 가지고 while문만 돌고 있게 되기에 이런 상황을 

Busy Waiting or Spin Lock 이라고 해서 계속 CPU와 Memory를 쓰면서 기다리며 자원을 낭비하는 상황을 의미한다.

