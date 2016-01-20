function go() {
  alert('hi');
}

// can call function in list
var myList = ['apples', 12, go];
// can make list in list
var myList = ['apples', 12, ['Mark', 'Tom']];

myList[0] // apples

// adding 1 more to list
myList[3] = 'pineapples';

// change value
myList[0] = 'watermelon';

// remove value from list and add it to currentFruit
var currentFruit = myList.shift()

// forEach
var myList = ['apples', 'oranges', 'bananas'];

myList.forEach(function(value, index) {
  alert('I have ' + value + ' in my shopping bag');
  console.log(value, index);
});
