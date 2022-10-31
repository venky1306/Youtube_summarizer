var button1 = document.getElementById('generate');
var button2 = document.getElementById('clipboard');

var tab_url = 'http://127.0.0.1:5000/api/summarize?youtube_url=';
// https://www.youtube.com/watch?v=tTlmacNPYCE&ab_channel=jabykoay
chrome.tabs.query({
    active: true,
    lastFocusedWindow: true
    }, 
    function(tabs) {
        // and use that tab to fill in out title and url
        var tab = tabs[0];
        console.log(tab.url);
        // alert(tab.url);
        tab_url += tab.url;
});

button1.onclick = function() {
    var text;
    var Http = new XMLHttpRequest();
    Http.open("GET", tab_url);
    Http.send()
    Http.onreadystatechange = function() { 
            text =  Http.responseText;
            // console.log(text);
            document.getElementById('summary').innerHTML = text;
    }
    // document.getElementById("content").innerHTML = text;

}

button2.onclick = function() {
    var text = document.getElementById('summary').innerText;
    var elem = document.createElement("textarea");
    document.body.appendChild(elem);
    elem.value = text;
    elem.select();
    document.execCommand("copy");
    document.body.removeChild(elem);

    var tooltip = document.getElementById("myTooltip");
    tooltip.innerHTML = "Copied";

}

button2.onmouseout = function() {
    var tooltip = document.getElementById("myTooltip");
    tooltip.innerHTML = "Copy to clipboard";
}






