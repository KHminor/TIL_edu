// type 함수타입 = (a: string) => number

// let 함수: 함수타입 = (a) => {
//   return 1
// }

// type 회원정보타입 =  {
//   name: string,
//   plusOne: (a: number) => number,
//   changeName: (x: string) => string
// }

// let 회원정보: 회원정보타입 = {
//   name: 'kim',
//   plusOne(a){
//     return a + 1
//   },
//   changeName: (x)=> {
//     return x+'안녕' 
//   }
// }

// 회원정보.plusOne(1)
// 회원정보.changeName('ㅋㅋㅋ')

type 컷제로 = (문자: string)=> string

let cutZero: 컷제로 = (문자) => {
  if (문자[0] === '0') {
    return 문자.substring(1)
  } else {
    return 문자
  }
}

console.log(cutZero('안녕하세요'))
console.log(cutZero('0안녕하세요'))


type 대시제거 = (문자: string) => number

let removeDash: 대시제거 = (문자) => {
  if (문자.indexOf('') !== -1) {
    return Number(문자.replace('-',''))
  } else {
    return Number(문자)
  }
}

console.log(removeDash('1234'))
console.log(removeDash('12-345'))
console.log(removeDash('1-2-345'))