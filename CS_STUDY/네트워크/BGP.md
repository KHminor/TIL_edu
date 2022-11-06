# BGP 

## BGP (Boarder Gateway Protocol)

* 각 경계 간으로 이루어지는 즉 AS와 AS 간 사용되는 라우팅 프로토콜 이다.

* 라우팅 방식이 Path Vector (or Advanced Distance Vector) 방식을 따른다.

* 수렴 속도가 느리다.

* IGP에 비해 설정이 복잡하고 경로 조정 시에 여러 가지를 고려해야 함으로 관리자가 적극 개입 한다.

  

## IGP(Interior Gateway Protocol)

* AS 내부 간에서 이루어지는 라우팅 프로토콜이다.
* 라우팅 방식이 Distance Vector 방식과 Link State 방식이 있다.
* 수렴 속도가 빠르다.
* 설정이 비교적 간단하고 경로 조정 시 단순히 Metric 값 조정으로 하여 간단하고 관리자 개입이 적다.



----

## BGP Routing

* BGP 라우팅 정보를 보내기 위해서는 eBGP와 iBGP가 사용되고 또한 IGP도 필요하다.

* 각 Protocol을 통해 라우팅 정보가 전송되어 라우팅이 이루어 진다.

* BGP에서 Protocol마다 사용하는 기능을 알아보면

  1. IGP

     * AS 내부의 라우팅 정책을 구현하기 위해 사용한다. (RIP, EIGRP, OSPF)

  2. eBGP

     * AS와 AS 간의 BGP 라우팅 정보를 교환하기 위해 사용한다.

  3. iBGP

     * AS 내에서 BGP 라우팅 정보를 교환하기 위해 사용한다.

     







---

## 용어 정리

자율 시스템(AS: Autonomous System) 

* AS 내의 라우터들은 서로 동일한 라우팅 프로토콜을 사용한다.
* AS 내의 네트워크와 라우터들은 한 조직에 의해 관리된다.
* 인터넷은 각 AS들이 복잡하게 연결 구성된다.

