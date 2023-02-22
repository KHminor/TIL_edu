// 숙제 1
interface 타입지정 {
    brand: string,
    serialNumber: number,
    model: string[]
}

let 상품: 타입지정 = { brand : 'Samsung', serialNumber : 1360, model : ['TV', 'phone'] }

// 숙제 3

interface AddCard {
    card?: boolean
}


// 숙제 2

interface 오브젝트 extends AddCard{
    product: string,
    price: number
}

let 장바구니: 오브젝트[] = [ { product : '청소기', price : 7000 }, { product : '삼다수', price : 800 }, { product : '청소기', price : 7000, card : false } ] 


console.log(장바구니);


// 숙제 4

interface ObjType {
    plus: (a: number, b: number) => number,
    minus: (a: number, b: number) => number
}


let 옵젝 = {
    plus(a,b){
        return a+b
    },
    minus(a,b){
        return a-b
    }
}