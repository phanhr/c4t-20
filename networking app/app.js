var url = "https://gateway.marvel.com:443/v1/public/characters";
var publicKey = "6112836c4293741e27ba26813815f357";
var privateKey = "186bf6b8e879ee24788303e7bddefd8588d3f633";
var key = marvelKey(privateKey, publicKey);
var fullUrl = `${url}?${key}`;
console.log(fullUrl);


function renderCharacterDetails(characterDetail) {
    var detailsBox = document.getElementById("details-box");
    var content = document.getElementById("content");
    content.remove();
    var searchArea = document.getElementById("search-area");
    searchArea.remove();
    content.textContent = "";
    detailsBox.textContent = "";
    var character=characterDetail[0];
    var characterName = character.name;
    var imgSrc = character.thumbnail.path +'.'+ character.thumbnail.extension;
    var description = character.description;
    if (description=="") {
        description = "No description"
    };
    var characterDetailsHTML = `
    <div id="box">
        <img src="${imgSrc}" id="image">
        <div id="details-container">
            <h2 id="name" class="bold">${characterName}</h2>
            <h5 class="white" id="description">${description}</h5>
            <h3 class="bold">Related comics</h3>
            <h4 class="white" id="related-comics"></h4>
            <h3 class="bold">Related events</h3>
            <h4 class="white" id="related-events"></h4>
        </div>
    </div>
    `
    
    detailsBox.insertAdjacentHTML("beforeend",characterDetailsHTML)
    var relatedEvents = character.events.items;
    for (var b=0;b<relatedEvents.length;b++) {
        var relatedEvent = relatedEvents[b].name;
        var event = document.createElement("span");
        if (relatedEvent==[]) {
            event.innerHTML = "Not Found";
        } else {
            event.innerHTML = relatedEvent;
        }
        console.log(relatedEvent)
        document.getElementById("related-events").appendChild(event);
    };
    
    var relatedComics = character.comics.items;
    
    for (var a=0;a<relatedComics.length;a++) {
        var relatedComic = relatedComics[a].name;
        var comic = document.createElement("span");
        if (comic=="") {
            comic.innerHTML = "Not Found"
        } else {
            comic.innerHTML = relatedComic;
        }
        document.getElementById("related-comics").appendChild(comic);
        };
}

function detailsClicked() {

    var detailsClicked = document.getElementsByClassName("detailsClicked");
        for (var a=0;a<detailsClicked.length;a++) {
            var detail = detailsClicked[a];
            detail.addEventListener("click", function(e) {
                var characterClicked = e.target.parentNode.childNodes[3].textContent;
                
                var key = marvelKey(privateKey, publicKey);
                var fullUrl = `${url}?${key}&name=${characterClicked}`
                sendGetRequest(fullUrl, function(responseData) {
                    var characterDetail = responseData.data.results;
                    renderCharacterDetails(characterDetail);
                })
            })
        }
    
}

function renderCharacters(characters) {
    var content = document.getElementById("content");
    content.textContent = "";
    for (var i=0;i<characters.length;i++) {
        var character = characters[i];
        var characterName= character.name;
        var imgSrc = character.thumbnail.path + '.' + character.thumbnail.extension;
        var comicsAvailable = character.comics.available;
        
        var characterHTML = `
        <div class="detailsClicked">
        <img src="${imgSrc}">
        <h2 id="name">${characterName}</h2>
        <h3>Comics: ${comicsAvailable}</h3>
        </div>
        `
        content.insertAdjacentHTML("beforeend", characterHTML);
        
    };
    detailsClicked();
    
    };

function fetchCharacters() {
    sendGetRequest(fullUrl, function (responseData) {
        var characters = responseData.data.results;
        renderCharacters(characters);
    });
}

function setUpEvents() {
    var btnSearch = document.getElementById("btn_search");
    btnSearch.addEventListener("click", function(e) {
        var searchBar = document.getElementById("search_bar");
        var searchValue = searchBar.value;
        var key = marvelKey(privateKey, publicKey);
        var fullUrl = `${url}?${key}`;
        if (searchValue != "") {
            fullUrl+=`&nameStartsWith=${searchValue}`;
        }
        sendGetRequest(fullUrl, function(responseData) {
            var characters = responseData.data.results;
            renderCharacters(characters);
        })
    })
}

fetchCharacters();
setUpEvents();