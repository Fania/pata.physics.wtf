"use strict";

// LOADING ICON
const loadDiv = document.getElementById("loading");
window.addEventListener('load', () => loadDiv.classList.remove("show") );
const loadTriggers = document.querySelectorAll("[type='submit']");
loadTriggers.forEach(lt => 
  lt.addEventListener("click", () => loadDiv.classList.add("show")));




// TABS
function showTab(type, tab, trigger) {
  type === "sub" ? hideAllSubSections() : hideAllSections();
  tab.classList.remove("hide");
  trigger.classList.add("active");
  event.preventDefault();
}
function hideAllSections() {
  tabs.forEach( tab => tab.classList.add("hide") );
  triggers.forEach( tr => tr.classList.remove("active") );
}
function hideAllSubSections() {
  sub_tabs.forEach( stab => stab.classList.add("hide") );
  sub_triggers.forEach( str => str.classList.remove("active") );
}








// APIs

// FLICKR
// works but not used
// function flickrsearch(queries){
//   console.log("flickrsearch, flickr");
//   let results = [];
//   const tags = queries.join(",");
//   const baseURL = `https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=${keyconfig.flickr_k}&format=json&per_page=10&nojsoncallback=1&sort=date-taken-desc&safe_search=1&tags=`;
//   const url = baseURL + tags;
//   const request = new Request(url);
//   fetch(request)
//     .then(response => response.json())
//     .then(data => {
//       (data.photos.photo).forEach(d => {
//         if (d != undefined) {
//           const img_url = `https://farm${d.farm}.staticflickr.com/${d.server}/${d.id}_${d.secret}_q.jpg`;
//           const page_url = `https://www.flickr.com/photos/${d.owner}/${d.id}`;
//           results.push([d.title, img_url, page_url]);
//         }
//       });
//       createSpiral(results);
//     });
// }; // end flickrsearch






// BING
// works but not used
// function bingsearch(queries){
//   console.log("bingsearch, bing");
//   let results = [];
//   const options = { 
//     method: 'GET',
//     headers: new Headers({'Ocp-Apim-Subscription-Key':keyconfig.bing_k}),
//     mode: 'cors',
//     cache: 'default' 
//   };
//   const queryString = `${queries.join(" | ")}`;
//   const base_url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search";
//   const params = `?q=${queryString}&count=10`;
//   const fullUrl = base_url + params;
//   const request = new Request(fullUrl, options);
//   fetch(request)
//     .then(response => response.json())
//     .then(data => {
//       (data.value).forEach(d => {
//         results.push([d.name, d.thumbnailUrl, d.hostPageUrl]);
//       });
//       createSpiral(results);
//     });
// }; // end of bingsearch






// GETTY
// Getty is dead. Long live Flickr/Bing.
// function gettysearch(query){
//   let appendApiKeyHeader = function( xhr ) {
//     xhr.setRequestHeader('Api-Key', getty_key2)
//   }
//   let searchRequest = {
//     "phrase": query,
//     "page_size": 10
//   }
//   // console.log('query ' + searchRequest.phrase)
//   function GetSearchResults(callback) {
//     $.ajax({
//       type: "GET",
//       beforeSend: appendApiKeyHeader,
//       url: "https://api.gettyimages.com/v3/search/images/creative",
//       data: searchRequest})
//       .success(function (data, textStatus, jqXHR) {
//         // console.log('data ' + data.images);
//         let imgs = [];
//         $.each(data.images, function(i,item){
//           imgs.push([item.title, item.display_sizes[0].uri, ""]);
//         });
//         // console.log('imglist ' + imgs);
//         createSpiral(imgs)
//       }) // end of success
//       .fail(function (data, err) {
//         console.log('API error');
//       }); // end of fail
//   } // end GetSearchResults
//   GetSearchResults();
// }; // end of gettysearch



