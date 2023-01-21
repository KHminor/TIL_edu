// function 클리닝함수(arr: (number | string)[]) {
//   let newArr: number[] = arr.map((e)=> {
//     if (typeof(e) === 'string') {
//       return parseInt(e)
//     } else {
//       return e
//     }
//   })
//   return newArr
// }
// console.log(클리닝함수(['1',2,'3']))
function 만들함수(선생님) {
    if (typeof (선생님.subject) === 'string') {
        return 선생님.subject;
    }
    else {
        return 선생님.subject[선생님.subject.length - 1];
    }
}
console.log(만들함수({ subject: 'math' }));
console.log(만들함수({ subject: ['science', 'art', 'korean'] }));
// 만들함수({ hello : 'hi' })
