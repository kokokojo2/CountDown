function post_reaction(url) {
    const Http = new XMLHttpRequest();

    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange = (e) => {
        if(Http.readyState === 4 && Http.status === 200)
        {
            var reaction_data = JSON.parse(Http.responseText);

            document.getElementById("like").className = reaction_data["like_state"] ? "reaction-btn border round blue" : "reaction-btn border round";
            document.getElementById("dislike").className = reaction_data["dislike_state"] ? "reaction-btn border round blue" : "reaction-btn border round";
            document.getElementById("laugh").className = reaction_data["laugh_state"] ? "reaction-btn border round blue" : "reaction-btn border round";
            document.getElementById("cry").className = reaction_data["cry_state"] ? "reaction-btn border round blue" : "reaction-btn border round";

            document.getElementById("laugh-amount").innerText = reaction_data["laugh"];
            document.getElementById("cry-amount").innerText = reaction_data["cry"];
            document.getElementById("like-amount").innerText = reaction_data["like"];
            document.getElementById("dislike-amount").innerText = reaction_data["negative"];

            // probably buttons will have different classes that will help to distinguish current state of reaction
            // if button has class1 (reaction exist) - change it to class2 (reaction doesn't exist)
            // the initial state of reaction will be determined by server when constructing detail template
        }
    }
}