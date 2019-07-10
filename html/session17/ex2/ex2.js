var deleteClicks = document.getElementsByClassName("deleteClick");
for (var i =0; i<deleteClicks.length;i++) {
    var deleteClick = deleteClicks[i];
    deleteClick.addEventListener("click", function(e) {
        var div = e.target.parentNode;
        div.remove();
    });
};