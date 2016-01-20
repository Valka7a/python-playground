// piece of code that does one or more actions
// do not repeat yourself DRY


// reusable
function go(name, age) {
  alert(name);
  alert(age);
}

go('Valyo', 24);
go('Valyo2', 19);


// sum function
function add(first, second) {
  return first + second;
}

var sum = add(1, 2);
alert(sum)


// function with two returns
function goo(name, age) {
  if (age < 20) {
    return name + '!';
  } else {
    return name;
  }
}

alert( goo('Valyo', 25) );
