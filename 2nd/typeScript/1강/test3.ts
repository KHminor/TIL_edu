// type CodeType = string | number[]

// let 변수 :CodeType = []

// type AnimalType = {name: string , age?: number}

// let 동물: AnimalType = {
//   name: '사자'
// }

// const 출생지역 =  {region: '서울'}
// 출생지역.region = '부산'

// const 지역: string[] = ['부산','울산']
// 지역[0] = '서울'

// type GirlFriend = {
//   readonly name: string 
// }

// const 여친: GirlFriend = {
//   name: '엠버'
// }

// type 이름 = {name: number}
// type 이름1 = {name: number}

// const 변수1: 이름&이름1 = {name: 1}
// console.log(변수1);

// 2.
type 해당 = {key:number}
type 타입1 = {color?: string}
type 타입2 = {size: number}
type 타입3 =  {readonly position: number[]}