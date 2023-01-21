type Square = {color: string, width: number}
interface Square1 {color: string, width: number}

let 네모 = {color: 'red', width: 100}

interface Student {
    name: string
}


interface Teacher extends Student {
    age: number
}


let 학생: Student = {name: 'kim'}
let 선생: Teacher = {name: 'kim', age: 20}

type Animal = { name: string}
type Cat = { age: number } & Animal