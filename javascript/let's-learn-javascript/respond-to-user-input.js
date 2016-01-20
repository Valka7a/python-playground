// Javascript Evenets:
// - click
// - mouseenter
// - mouseleave
// - mousedown
// - mouseup
// - mousemove
// - keydown
// - keyup
// - blur
// - focus

var numOne = document.getElementById("num-one");
var numOne = document.getElementById("num-two");
var numOne = document.getElementById("add-sum");

numOne.addEventListener("input", add);
numTwo.addEventListener("input", add);

function add() {
            // number               if none put 0
  var one = parseFloat(numOne.value) || 0;
  var two = parseFloat(numTwo.value) || 0;
  var sum = one + two;
  addSum.innerHTML = "your sum is:" + sum;
  addSum.innerHTML = "your sum is:" + (one + two); // other way
  console.log(one, two);
}
