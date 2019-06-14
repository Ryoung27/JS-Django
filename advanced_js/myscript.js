function hello(){
    console.log("Hello World")
}

hello()

function hello_you(name="Ronnie", title='Sir '){
    // console.log("Hello " + title + name)
    return title+ " "+name;
}

hello_you("richie", "Guy ")
console.log(hello_you())

function addNumb(x, y){
    console.log(x + y)
}

addNumb(1, 2)

function timesFive(x){
    var results = x * 5
    return results
}

// function sleepIn(weekday, weekend){
//     if(weekend = "Saturday" or weekend = "Sunday"){
//         return "Sleep in."
//     } else {
//         return "Work"
//     }
// }

//Arrays
var countries = ["USA", "Germany", "China", "Russia"]
console.log(countries[0])

countries[2] = "France"
console.log(countries[2])

console.log(countries)

// var mixed = [True, "True", 1]

var myArr = ['one', 'two', 'three']

var lastItem = myArr.pop()

console.log(myArr)

myArr.push("four")
console.log(myArr)

for(var i = 0; i<Array.length; i++){

}

function addAwesome(name){
    console.log(name+" is awesome!")
}

let carInfo = {
    make: "Toyota",
    year: 1995,
    model: "Camery"
};

console.log(carInfo)
console.log(carInfo["make"])

let myNewO = {
    a: "hello",
    b: [1,2,3],
    c: {
        inside: [
            'a', 'b', 'c'
        ]
    }
}

console.log(myNewO["a"])
console.log(myNewO["b"][1])
console.log(myNewO["c"].inside[1])

for(key in carInfo){
    console.log(key)
}