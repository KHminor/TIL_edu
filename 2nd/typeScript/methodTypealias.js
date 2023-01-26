// type 함수타입 = (a: string) => number
var cutZero = function (문자) {
    if (문자[0] === '0') {
        return 문자.substring(1);
    }
    else {
        return 문자;
    }
};
console.log(cutZero('안녕하세요'));
console.log(cutZero('0안녕하세요'));
var removeDash = function (문자) {
    if (문자.indexOf('') !== -1) {
        return Number(문자.replace('-', ''));
    }
    else {
        return Number(문자);
    }
};
console.log(removeDash('1234'));
console.log(removeDash('12-345'));
console.log(removeDash('1-2-345'));
