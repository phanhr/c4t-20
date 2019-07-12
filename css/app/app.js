var rightIndex;
var score = 0;
var timeId;
function generateColors() {
    var r = Math.floor(Math.random() * 255);
    var g = Math.floor(Math.random() *255);
    var b = Math.floor(Math.random() *255);
    var rightColor = `rgb(${r}, ${g}, ${b})`;
    var rgb = document.getElementById("rgb");
    rgb.textContent = rightColor;
    var ballContainer = document.getElementById("ball_container");
    var balls = ballContainer.getElementsByClassName("ball");
    rightIndex = Math.floor(Math.random() *3);
    balls[rightIndex].style.backgroundColor = rightColor;
    for (var i=0;i<balls.length;i++) {
        if (i != rightIndex) {
            var error1 = Math.floor(Math.random() * 100 + 25);
            var x = Math.random();
            if (x>0.5) {
                error1=-error1;
            }

            var error2 = Math.floor(Math.random() * 100 + 25);
            var x = Math.random();
            if (x>0.5) {
                error2=-error2;
            }

            var error3 = Math.floor(Math.random() * 100 + 25);
            var x = Math.random();
            if (x>0.5) {
                error3=-error3;
            }
            balls[i].style.backgroundColor = `rgb(${r+error1}, ${g+error2}, ${b+error3})`
        }
    }
}

function eventListen() {
    var ballContainer = document.getElementById("ball_container");
    var balls = ballContainer.getElementsByClassName("ball");
    timeId = setTimeout(timeOut,3000);
    for (var i = 0; i<balls.length; i++) {
        var ball = balls[i];
        ballListened = ball.addEventListener("click", function(e) {
            clearInter();
            var ballClicked = e.target;
            if (ballClicked.getAttribute("index")==rightIndex) {
                score ++;
                trueClicked();
            } else {
                score = score + 0;
                falseClicked();
            }
            var scoreLine = document.getElementById("score");
            scoreLine.textContent = `Score: ${score}`;
            generateColors;
        });
    };
    
};


function pause() {
    var audio = document.getElementById("player");
    audio.pause();
}

function trueClicked() {
    var trueClicked = document.getElementById("true");
    trueClicked.play();
}

function falseClicked() {
    var falseClicked = document.getElementById("false");
    falseClicked.play();
}

function bellRing() {
    var bellRing = document.getElementById("bell");
    bellRing.play();
};

function timeOut() {
    bellRing();
    alert("time out");
};

function clearInter() {
    clearInterval(timeId);
}
generateColors();
eventListen();
