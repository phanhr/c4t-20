 function startClick() { //call back
    console.log("start clicked")
}

var btn = document.getElementById("btn");
btn.addEventListener("click", function(e) {
    console.log(e);
});

var searchBar = document.getElementById("searchBar");
searchBar.value = "";

var menu = document.getElementById("menu");
// var newItem = document.createElement("li")
// newItem.innerText = "Fries"
// menu.appendChild(newItem)
var liList = menu.getElementsByTagName("li");
// console.log(liList);
// var firstli = liList[0];
// firstli.remove();
menu.textContent = "";

function myFunction() {
    var x = document.getElementById("myDiv");
    if (x.style.display == "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none"
    };
    console.log(x.style.display);
};

var deleteButtons = document.getElementsByClassName("btn_delete")
for (var i = 0; i < deleteButtons.length; i++) {
    var deleteButton = deleteButtons[i];
    deleteButton.addEventListener("click", function(e) {
        var eTarget = e.target;
        var div = eTarget.parentNode;
        div.remove();
    })
}