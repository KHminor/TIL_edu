// // 1번
// let 이름 = '홍민'
// let 나이 = 30
// let 출생지역 = '울산'

// // 2번
// let like = {name :'sabrina claudio', songName : 'Come Here'}

// // 3번
// let project :{
//   member : string[],
//   days : number,
//   started : boolean,
// } = {
//   member : ['kim', 'park'],
//   days : 30,
//   started : true,
// }
// let 리스트 :(string | number)[] = [1,'2',3]
// let 오브젝트 :{[key:string]: (string | number) } = {a:'123', b:123}

// let 아무거나 :any

// let 나이 : number | string
// 나이 + 1




// 숙제 1
let user :string = 'kim';
let age :undefined | number = undefined;
let married :boolean = false; 
let 철수 :(string | undefined | number | boolean)[] = [user, age, married];

// 숙제 2
let 학교 :{
  score : (number|boolean)[],
  teacher? : string,
  friend : string |(string)[]
} = {
  score : [100, 97, 84],
  teacher : 'Phil',
  friend : 'John'
}
학교.score[4] = false;
학교.friend = ['Lee' , 학교.teacher]