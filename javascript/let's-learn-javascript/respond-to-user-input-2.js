var simon = document.getElementById("simon");
var simonPic = document.getElementById("simon-pic");
var bruce = document.getElementById("simon");
var brucePic = document.getElementById("simon-pic");
var ben = document.getElementById("simon");
var benPic = document.getElementById("simon-pic");


simon.addEventListener("click", function() {
  if (simonPic.className === "hide") {
    simonPic.className = "";
  } else {
    simonPic.className = "hide";
  }
});

bruce.addEventListener("click", function() {
  if (brucePic.className === "hide") {
    brucePic.className = "";
  } else {
    brucePic.className = "hide";
  }
});

ben.addEventListener("click", function() {
  if (benPic.className === "hide") {
    benPic.className = "";
  } else {
    benPic.className = "hide";
  }
});


simon.addEventListener("click", picLink);
bruce.addEventListener("click", picLink);
ben.addEventListener("click", picLink);

// Shorter and better way!!
// this everything you click in this example
function picLink() {
  var allImages = document.querySelectorAll("img");

  for (var i = 0; i < allImages.length; i ++) {
    allImages[i].className = "hide";
  }
  
  var picId = this.attributes["data-img"].value;
  var pic = document.getElementById(picId);

  if (pic.className === "hide") {
    pic.className = "";
  } else {
    pic.className = "hide";
  }
}
