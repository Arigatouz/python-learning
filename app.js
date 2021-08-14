let name = "Ali";
let age = 15;

let message = `${name} has ${age} yeas old`;
console.log(message);

const cities = ["cairo", "gizzza", "behara"];

for (let city in cities) {
  console.log(cities[city].split(" ").join(",,"));
}

let names = ["ahmed", "karima", "hamza", "soad"];
let modifiedNames = names.forEach((name) => console.log(name));
console.log(modifiedNames);
