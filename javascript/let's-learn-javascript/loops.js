// while do for loops

// while loop - check and then doing
var times = 0;
while (times < 10) {
  console.log('tried it', times);
  times ++ // times = times + 1;
}


// do loop - first made it then check
var times = 0;

do {
  console.log('tried it', times);
  times ++;
} while(times < 10);


// for loop - doing for every element
for (setup, comparison, change) {

}

for (var i = 0; i < 10; i ++) {
  console.log('i is', i);
}

// doing while i < length of myList

var myList = ['Apples', 'Oranges', 'Bananas'];

for (var i = 0; i < myList.length; i ++) {
  console.log(myList[i])
}
