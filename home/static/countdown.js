function displayCountdownChanges(detail_view_mode, days, hours, minutes, seconds, totalSeconds, index)
{
    var hoursStr = null;
    var minutesStr = null;
    var secondsStr = null;
    var daysStr = null;

    if(totalSeconds > 0) {
         hoursStr = (hours > 9) ? hours.toString() : "0" + hours.toString();
         minutesStr = (minutes > 9) ? minutes.toString() : "0" + minutes.toString();
         secondsStr = (seconds > 9) ? seconds.toString() : "0" + seconds.toString();
         daysStr = days.toString();
    }

    else if(totalSeconds <= 0) {
         hoursStr = "00";
         minutesStr = "00";
         secondsStr = "00";
         daysStr = "0";
    }

    if(!detail_view_mode) {
        if(totalSeconds > 0) {
            console.log(index)
            document.getElementById("timer-" + index + "-days").innerText = daysStr;
            document.getElementById("timer-" + index + "-hours").innerText = hoursStr;
            document.getElementById("timer-" + index + "-minutes").innerText = minutesStr;
            document.getElementById("timer-" + index + "-seconds").innerText = secondsStr;
        }
        else {
            document.getElementById("timer-" + index + "-days").innerText = daysStr;
            document.getElementById("timer-" + index + "-hours").innerText = hoursStr;
            document.getElementById("timer-" + index + "-minutes").innerText = minutesStr;
            document.getElementById("timer-" + index + "-seconds").innerText = secondsStr;
        }
    }
    else {
        document.getElementById("days").innerText = daysStr;
        document.getElementById("hours").innerText = hoursStr;
        document.getElementById("minutes").innerText = minutesStr;
        document.getElementById("seconds").innerText = secondsStr;
    }


}
function updateCountdownList()
{
    for(var [index, countDownTimeSeconds] of countdownArray.entries()) {

        var days = Math.floor(countDownTimeSeconds / (60 * 60 * 24));
        var hours = Math.floor((countDownTimeSeconds / (60 * 60)) % 24);
        var minutes = Math.floor(countDownTimeSeconds / 60 % 60);
        var seconds = Math.floor((countDownTimeSeconds % 60));

        console.log(index)
        displayCountdownChanges(false, days, hours, minutes, seconds, countDownTimeSeconds, index + 1);

        if(countDownTimeSeconds >= 0) {
                countDownTimeSeconds--;
        }

        countdownArray[index] = countDownTimeSeconds;
    }
}
function updateCountdown() {

            var days = Math.floor(countDownTimeSeconds / (60 * 60 * 24));
            var hours = Math.floor((countDownTimeSeconds / (60 * 60)) % 24);
            var minutes = Math.floor(countDownTimeSeconds / 60 % 60);
            var seconds = Math.floor((countDownTimeSeconds % 60));


            if(days > 999) {
                document.getElementById("days").setAttribute("style", "width: 100px;")
            }

            displayCountdownChanges(true, days, hours, minutes, seconds, countDownTimeSeconds);

            if(countDownTimeSeconds >= 0) {
                countDownTimeSeconds--;
            }
            else {
                confetti({
                        particleCount: 100,
                        startVelocity: 30,
                        spread: 360,
                        origin: {
                            x: Math.random(),
                            y: Math.random() - 0.2
                        }
                        });

                confetti({
                        particleCount: 100,
                        startVelocity: 30,
                        spread: 360,
                        origin: {
                            x: Math.random(),
                            y: Math.random() - 0.2
                        }
                        });

                confetti({
                        particleCount: 100,
                        startVelocity: 30,
                        spread: 360,
                        origin: {
                            x: Math.random(),
                            y: Math.random() - 0.2
                        }
                        });

                const Http = new XMLHttpRequest();

                Http.open("GET", url);
                Http.send();

                Http.onreadystatechange = (e) => {
                    if(Http.readyState === 4 && Http.status === 200)
                    {
                        const finished_text = document.createElement("div");
                        finished_text.className = "col-7 main-text mt-5";
                        finished_text.innerHTML = "<p>" + Http.responseText + "</p>";

                        document.getElementById("wrapper").appendChild(finished_text);
                        clearInterval(intervalID);
                    }
                }
            }
        }