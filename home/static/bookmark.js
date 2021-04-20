function bookmark(url) {
    const Http = new XMLHttpRequest();

    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange = (e) => {
        if(Http.readyState === 4 && Http.status === 200)
        {
            console.log(Http.responseText);
            if(Http.responseText == 'added')
            {
                document.getElementById("bookmark-btn").className = "fa fa-star fa-lg";
            }
            else if(Http.responseText == 'removed')
            {
                document.getElementById("bookmark-btn").className = "fa fa-star-o fa-lg";
            }
        }
    }
}