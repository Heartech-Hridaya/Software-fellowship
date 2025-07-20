// // // const message = 'Hello world this is me '
// // // document.querySelector('#header').innerHTML = message
// // // console.log(message)

// // // let a;
// // // console.log(typeof(a));

// // // let b= null;
// // // console.log(typeof(b));
 
// // let myKey = ""
// // let name = 'Hridaya';
// // let age = 18;
// // let place = 'Pulchowk';

// // let person = {
// //   name: 'Sajal',
// //   age: '17',
// //   place: 'London',
// //   [myKey] : "from my api"
// // };

// // // let greeting = `Hello ${name}, you'r at ${place} and it seems you'r currently ${age} yrs old.`;
// // // console.log(greeting);
// // // document.querySelector('#header').innerHTML = greeting;


// // let greeting2 = `Hello ${person.name}, you'r at ${person["place"]} and it seems you'r currently ${person.age} yrs old.`;
// // console.log(greeting2);
// // document.querySelector('#header').innerHTML = greeting2;

// // console.log(person[myKey])
// // console.log(Object.keys(person))


// function greet(name="Hridaya"){
//     return (`Hello ${name}`)
//   }
  
//   const mf =()=>{console.log(greet()) }
//   mf()
  
//   function add(a,b){
//       return a+b
//   }
//   const a =()=>{console.log(add(3,5)) }
//   a()
  
  // for (let i=0;i<5;i++){
//     console.log("one")
// }

// let i = 0
// while(i<5){
//     console.log(1)
//     i = i+1
// }

// const arr = [1,2,3,4,5,6,7,8,9]

// for (let i=0;i<arr.length;i++){
//     console.log(arr[i])
// }

// arr.forEach((el)=>{
//     console.log("these are the numbers :",el)
// })

// const arr2 = arr.map((a)=>{
//     console.log("printing ",a)
//     return a+"2"
// })       
// console.log(arr2())


console.log("Linking successful");

const myButton = document.getElementById("myButton");
console.log(myButton);

const colorPalette = [
  "#2C3E50", // Midnight Blue
  "#34495E", // Wet Asphalt
  "#E74C3C", // Alizarin Red
  "#2ECC71", // Emerald Green
  "#F1C40F", // Sunflower Yellow
  "#E67E22", // Carrot Orange
  "#2980B9", // Belize Hole Blue
  "#9B59B6", // Amethyst Purple
  "#ECF0F1", // Clouds White
  "#95A5A6"  // Concrete Gray
];

const body = document.querySelector("body");

myButton.addEventListener("click", function () {
  console.log("Button Clicked!");
  let randomIndex = Math.floor(Math.random() * colorPalette.length);
  let ranColor = colorPalette[randomIndex];
  body.style.backgroundColor = ranColor;
});
