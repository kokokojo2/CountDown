function post_reaction(url) {
    const Http = new XMLHttpRequest();

    Http.open("POST", url);
    Http.send();

    Http.onreadystatechange = (e) => {
        if(Http.readyState === 4 && Http.status === 200)
        {
            // TODO: do smth with html when request is done
            // probably buttons will have different classes that will help to distinguish current state of reaction
            // if button has class1 (reaction exist) - change it to class2 (reaction doesn't exist)
            // the initial state of reaction will be determined by server when constructing detail template
        }
    }
}