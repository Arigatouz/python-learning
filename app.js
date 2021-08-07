let name = "Ali";
let age = 15;

let message = `${name} has ${age} yeas old`;
console.log(message);

const cities = ["cairo", "gizzza", "behara"];

for (let city in cities) {
  console.log(cities[city].split(" ").join(",,"));
}
