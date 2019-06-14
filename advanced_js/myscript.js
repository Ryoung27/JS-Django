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

