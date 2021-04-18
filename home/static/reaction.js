function post_reaction(url, trigger_id) {
    const Http = new XMLHttpRequest();

    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange = (e) => {
        if(Http.readyState === 4 && Http.status === 200)
        {
            var reactions_number = JSON.parse(Http.responseText);

            var triggered_button = document.getElementById(trigger_id);
            if(triggered_button.className.includes("blue")) {
                console.log('like');
                triggered_button.className = "reaction-btn border round";
            }
            else {
                triggered_button.className += " blue";
            }

            document.getElementById("laugh-amount").innerText = reactions_number["laugh"];
            document.getElementById("cry-amount").innerText = reactions_number["cry"];
            document.getElementById("like-amount").innerText = reactions_number["like"];
            document.getElementById("dislike-amount").innerText = reactions_number["negative"];

            // probably buttons will have different classes that will help to distinguish current state of reaction
            // if button has class1 (reaction exist) - change it to class2 (reaction doesn't exist)
            // the initial state of reaction will be determined by server when constructing detail template
        }
    }
}