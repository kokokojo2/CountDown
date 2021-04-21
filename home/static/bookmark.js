function bookmark(url, detail_mode, id) {
    const Http = new XMLHttpRequest();

    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange = (e) => {
        if(Http.readyState === 4 && Http.status === 200)
        {
            if(detail_mode)
            {
                if(Http.responseText == 'added')
                {
                    document.getElementById(id).className = "fa fa-star fa-lg";
                }
                else if(Http.responseText == 'removed')
                {
                    document.getElementById(id).className = "fa fa-star-o fa-lg";
                }
            }
            else if(!detail_mode && Http.responseText == 'removed')
            {
                var sideBar = document.getElementById("sidebar-wrapper");
                sideBar.removeChild(document.getElementById(id))
            }

        }
    }
}