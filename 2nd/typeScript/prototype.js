var Car = /** @class */ (function () {
    function Car(a, b) {
        this.model = a,
            this.price = b;
    }
    Car.prototype.tax = function () {
        return this.price / 10;
    };
    return Car;
}());
var car1 = new Car('소나타', 3000);
console.log(car1); //콘솔창 출력결과는 { model : '소나타', price : 3000 }
console.log(car1.tax()); //콘솔창 출력결과는 300
var Word = /** @class */ (function () {
    function Word() {
        var parameters = [];
        for (var _i = 0; _i < arguments.length; _i++) {
            parameters[_i] = arguments[_i];
        }
        var _this = this;
        this.num = [];
        this.str = [];
        parameters.forEach(function (e) {
            if (typeof (e) === 'number') {
                _this.num.push(e);
            }
            else {
                _this.str.push(e);
            }
        });
    }
    return Word;
}());
var obj = new Word('kim', 3, 5, 'park');
console.log(obj.num); //[3,5]
console.log(obj.str); //['kim', 'park']
