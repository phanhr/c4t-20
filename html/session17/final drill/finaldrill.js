var song_container = document.getElementById("song_container");
var songs = song_container.getElementsByClassName("song");
console.log(songs);

for (var i = 0; i < songs.length;i++) {
    var song = songs[i];
    var info = song.getElementsByClassName("title");
    for (var a=0;a<info.length;a++) {
        console.log(info[a].textContent);
    };
};

var deleteButtons = document.getElementsByClassName("deleteClick");
for (var i = 0; i < deleteButtons.length; i++) {
    var deleteButton = deleteButtons[i];
    deleteButton.addEventListener("click", function(e) {
        var div = e.target.parentNode;
        div.remove();
    })
};

var editButtons = document.getElementsByClassName("Edit");
for (var i=0;i<editButtons.length;i++) {
    var editButton = editButtons[i];
    editButton.addEventListener("click", function(e) {
        var divEdit = e.target.parentNode;
        console.log(divEdit.getAttribute("song_id"));
    })
};

var moreButtons = document.getElementsByClassName("more");
for (var i = 0;i<moreButtons.length;i++){
    var moreButton = moreButtons[i];
    moreButton.addEventListener("click", function(e) {
        var divMore = e.target.parentNode;
        console.log(divMore.getAttribute("song_id"));
        var titles = divMore.getElementsByClassName("title");
        for (var i=0;i<titles.length;i++) {
            console.log(titles[i].textContent);
        };
        var artists = divMore.getElementsByClassName("artist")
        for (var i=0;i<artists.length;i++) {
            console.log(artists[i].textContent);
        };
    });
};

var addButtons = document.getElementsByClassName("add")
for (var i=0; i<addButtons.length; i++) {
    var addButton = addButtons[i]
    addButton.addEventListener("click", function(e) {
        var divAdd = e.target.parentNode;
        var newDiv = document.createElement("div");
        var newAtt = document.createAttribute("class");
        newAtt.value="song";
        newDiv.setAttributeNode(newAtt);
        divAdd.appendChild(newDiv);
        console.log(divAdd)
    });
};