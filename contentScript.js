// chrome.tabs.query({active: true, currentWindow: true}, tabs => {
//     let url = tabs[0].url;
//     console.log(url);
//     // use `url` here inside the callback because it's asynchronous!
// });


// chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {

//     // since only one tab should be active and in the current window at once
//     // the return variable should only have one entry
//     var activeTab = tabs[0];
//     var activeTabId = activeTab.id; // or do whatever you need
//     document.addEventListener('click', () => alert(activeTabId));

//  });

