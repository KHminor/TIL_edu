class Car {
    model: string
    price: number
    constructor(a: string, b: number) {
        this.model = a,
        this.price = b
    }

    tax(): number {
        return this.price/10
    }
}

let car1 = new Car('소나타', 3000)
console.log(car1) //콘솔창 출력결과는 { model : '소나타', price : 3000 }
console.log(car1.tax()) //콘솔창 출력결과는 300


class Word {
    num: number[] = []
    str: string[] = []
    constructor(...parameters: (string|number)[]) {
        parameters.forEach((e)=> {
            if (typeof(e) === 'number') {
                this.num.push(e)
            } else {
                this.str.push(e)
            }
            
        })
    }
}

let obj = new Word('kim', 3, 5, 'park');
console.log(obj.num) //[3,5]
console.log(obj.str) //['kim', 'park']