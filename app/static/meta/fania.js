// APIs

// FLICKR
function flickrsearch(queries){
  console.log("flickr");
  let results = [];
  const tags = queries.join(",");
  const baseURL = `https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=${keyconfig.flickr_k}&format=json&per_page=10&nojsoncallback=1&sort=date-taken-desc&safe_search=1&tags=`;
  const url = baseURL + tags;
  const request = new Request(url);
  fetch(request)
    .then(response => response.json())
    .then(data => {
      (data.photos.photo).forEach(d => {
        if (d != undefined) {
          const img_url = `https://farm${d.farm}.staticflickr.com/${d.server}/${d.id}_${d.secret}_q.jpg`;
          const page_url = `https://www.flickr.com/photos/${d.owner}/${d.id}`;
          results.push([d.title, img_url, page_url]);
        }
      });
      createSpiral(results);
    });
}; // end flickrsearch






// BING
function bingsearch(queries){
  console.log("bing");
  let results = [];
  const options = { 
    method: 'GET',
    headers: new Headers({'Ocp-Apim-Subscription-Key':keyconfig.bing_k}),
    mode: 'cors',
    cache: 'default' 
  };
  const queryString = `${queries.join(" | ")}`;
  const base_url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search";
  const params = `?q=${queryString}&count=10`;
  const fullUrl = base_url + params;
  const request = new Request(fullUrl, options);
  fetch(request)
    .then(response => response.json())
    .then(data => {
      (data.value).forEach(d => {
        results.push([d.name, d.thumbnailUrl, d.hostPageUrl]);
      });
      createSpiral(results);
    });
}; // end of bingsearch






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






function createSpiral(imglist) {
  console.log(imglist);
  if (imglist.length === 10){
    // const fib = [10,10,20,30,50,80,130,210,340,550];
    const nums = ["one","two","three","four","five","six","seven","eight","nine","ten"];
    for ( i in imglist ) {
      let link = document.createElement("a");
      let img = document.createElement("img");
      link.href = imglist[i][2];
      link.classList.add(nums[i]);
      img.src = imglist[i][1];
      img.alt = imglist[i][0];
      img.title = imglist[i][0];
      link.appendChild(img);
      img_spiral_div.appendChild(link);
      let listimg = `
        <a href="${imglist[i][2]}">
          <img src="${imglist[i][1]}" alt="${imglist[i][0]}" title="${imglist[i][0]}">
        </a>`;
      img_list_div.insertAdjacentHTML("beforeend", listimg);
    };
  } else {
    const placeholders = document.querySelectorAll(".img_empty");
    placeholders.forEach( p => 
      p.innerHTML = "<div>Not enough results found.</div>");
  }
}




// function createVideoSpiral(videolist) {
//   // console.log(videolist);
//   if (videolist.length === 10){
//     const sizes = [10,10,20,30,50,80,130,210,340,550];
//     const nums = ["one","two","three","four","five","six","seven","eight","nine","ten"];
//     for ( i in videolist ) {
//       let link = document.createElement("a");
//       let img = document.createElement("img");
//       link.href = videolist[i][2];
//       link.classList.add(nums[i]);
//       img.src = videolist[i][1];
//       img.alt = videolist[i][0];
//       img.title = videolist[i][0];
//       link.appendChild(img);
//       img_spiral_div.insertAdjacentHTML("beforeend", 
//         `<iframe width="${sizes[i]}" height="${sizes[i]}" src="https://www.youtube.com/embed/{{ videos_vids.3.2 }}?controls=0&rel=0&showinfo=0&modestbranding=1&controls=0" frameborder="0" ></iframe>`);

//       let listimg = `
//         <a href="${videolist[i][2]}">
//           <img src="${videolist[i][1]}" alt="${videolist[i][0]}" title="${videolist[i][0]}">
//         </a>`;
//       img_list_div.insertAdjacentHTML("beforeend", listimg);
//     };
//   } else {
//     const placeholders = document.querySelectorAll(".img_empty");
//     placeholders.forEach( p => 
//       p.innerHTML = "<div>Not enough results found.</div>");
//   }
// }





/////////////////////////////////////////////////////////////////////

// SCROLL BUTTONS
if(window.location.pathname === '/textresults') {
  if (DYN_WEB.Scroll_Div.isSupported() ) {
      DYN_WEB.Event.add( window, 'load', function() {
  		// wndo args(id of scroll area div, id of content div)
      // addGlideControls args(id, axis('v'|'h'), distance, duration)
      let wndo1 = new DYN_WEB.Scroll_Div('wn1', 'lyr1');
  		wndo1.addGlideControls('scrollLinks1', 'h', 635, 300);
      let wndo2 = new DYN_WEB.Scroll_Div('wn2', 'lyr2');
      wndo2.addGlideControls('scrollLinks2', 'h', 635, 300);
      let wndo3 = new DYN_WEB.Scroll_Div('wn3', 'lyr3');
      wndo3.addGlideControls('scrollLinks3', 'h', 635, 300);
      let wndo4 = new DYN_WEB.Scroll_Div('wn4', 'lyr4');
      wndo4.addGlideControls('scrollLinks4', 'h', 635, 300);
      let wndo5 = new DYN_WEB.Scroll_Div('wn5', 'lyr5');
      wndo5.addGlideControls('scrollLinks5', 'h', 635, 300);
      let wndo6 = new DYN_WEB.Scroll_Div('wn6', 'lyr6');
      wndo6.addGlideControls('scrollLinks6', 'h', 635, 300);
      let wndo7 = new DYN_WEB.Scroll_Div('wn7', 'lyr7');
      wndo7.addGlideControls('scrollLinks7', 'h', 635, 300);
      let wndo8 = new DYN_WEB.Scroll_Div('wn8', 'lyr8');
      wndo8.addGlideControls('scrollLinks8', 'h', 635, 300);
      let wndo9 = new DYN_WEB.Scroll_Div('wn9', 'lyr9');
      wndo9.addGlideControls('scrollLinks9', 'h', 635, 300);
      let wndo10 = new DYN_WEB.Scroll_Div('wn10', 'lyr10');
      wndo10.addGlideControls('scrollLinks10', 'h', 635, 300);
      let wndo11 = new DYN_WEB.Scroll_Div('wn11', 'lyr11');
      wndo11.addGlideControls('scrollLinks11', 'h', 635, 300);
      let wndo12 = new DYN_WEB.Scroll_Div('wn12', 'lyr12');
      wndo12.addGlideControls('scrollLinks12', 'h', 635, 300);
      let wndo13 = new DYN_WEB.Scroll_Div('wn13', 'lyr13');
      wndo13.addGlideControls('scrollLinks13', 'h', 635, 300);
      let wndo14 = new DYN_WEB.Scroll_Div('wn14', 'lyr14');
      wndo14.addGlideControls('scrollLinks14', 'h', 635, 300);
  	});
  } else {
    console.log("no DYN_WEB");
  }
} // end scrolldiv poems







// LOADING ICON
function loading() {
  $('.loading').show();
}







// POEM EMAILS
function Mailto_url(){
	let encode_mailto_component = function(str){
		try{ return encodeURIComponent(str); }
		catch(e){ return escape(str); }
	};
	let AddressList = function(){
		let list = [];
		this.length = 0;
		this.add = function(address){
			if(address) {
				list.push(address);
				this.length = list.length;
			}
		};
		this.get = function(){
			return list.join(';');
		};
	};
	let subject = '',
		body = '',
		mainList = new AddressList(),
		ccList = new AddressList(),
		bccList = new AddressList();
	this.setSubject = function(str){ subject = encode_mailto_component(str); };
	this.setBody = function(str){ body = encode_mailto_component(str); };
	this.addMain = function(x) { mainList.add(x); };
	this.addCC = function(x) { ccList.add(x); };
	this.addBCC = function(x) { bccList.add(x); };
	this.getURL = function(allow_empty_mainList){
		let out = ['mailto:'];
		let extras = [];
		if(mainList.length === 0 && !allow_empty_mainList){
			throw('Mailto_url: no main addressees');
		}
		else{
			out.push(mainList.get());
		}
		if(subject) { extras.push('subject=' + subject); }
		if(ccList.length) { extras.push('cc=' + ccList.get()); }
		if(bccList.length) { extras.push('bcc=' + bccList.get()); }
		if(body) { extras.push('body=' + body); }
		if(extras.length) { out.push('?' + extras.join('&')); }
		return out.join('');
	};
}

// Queneau Email
function getContent(link) {
  // console.log(link);
  const query = document.getElementById('querydiv').innerHTML;
  const corpus = document.getElementById('corpusdiv').innerHTML;
  const lollength = document.getElementById('lollength').innerHTML;
  let lineitem1 = document.getElementById('clicks1').innerHTML;
  let lineitem2 = document.getElementById('clicks2').innerHTML;
  let lineitem3 = document.getElementById('clicks3').innerHTML;
  let lineitem4 = document.getElementById('clicks4').innerHTML;
  let lineitem5 = document.getElementById('clicks5').innerHTML;
  let lineitem6 = document.getElementById('clicks6').innerHTML;
  let lineitem7 = document.getElementById('clicks7').innerHTML;
  let lineitem8 = document.getElementById('clicks8').innerHTML;
  let lineitem9 = document.getElementById('clicks9').innerHTML;
  let lineitem10 = document.getElementById('clicks10').innerHTML;
  let lineitem11 = document.getElementById('clicks11').innerHTML;
  let lineitem12 = document.getElementById('clicks12').innerHTML;
  let lineitem13 = document.getElementById('clicks13').innerHTML;
  let lineitem14 = document.getElementById('clicks14').innerHTML;
  let linearray = [];
  let poemsarray = [];
  const re = /<form class="inlineform" action="\.\.\/textresults" method="post"><input type="radio" name="corpus" value="(?:faustroll|shakespeare)|" checked=""><input type="submit" name="query" value="|" onclick="loading\(\)|"><\/form>/g;
  for (let i = 0; i < lollength; i++) {
    let lid = 'lyr' + (i + 1);
    let lineitem = eval('lineitem' + (i + 1));
    linearray[i] = document.getElementById(lid).children[lineitem - 1];
    poemsarray[i] = linearray[i].innerHTML;
    poemsarray[i] = poemsarray[i].replace(re, '');
  }
  if (poemsarray[3]) poemsarray[3] = poemsarray[3] + '\n';
  if (poemsarray[7]) poemsarray[7] = poemsarray[7] + '\n';
  if (poemsarray[10]) poemsarray[10] = poemsarray[10] + '\n';
  let poems = poemsarray.join('\n');
  let poemail = `Poem generated using http://pata.physics.wtf\r\n------------------------------------------------------------\r\nKeyword: ${query}\r\nCorpus: ${corpus}\r\n------------------------------------------------------------\r\n\n${poems}`;
  let mailTo = new Mailto_url();
	mailTo.setSubject("Pataphysical Poetry");
	mailTo.setBody(poemail);
	link.href = mailTo.getURL(true);
}

// Random Email
function getRandContent(link) {
  // console.log(link);
  let query = document.getElementById('querydiv').innerHTML;
  let corpus = document.getElementById('corpusdiv').innerHTML;
  let count = document.getElementById('clickcount').innerHTML;
  if (count == 0) {
    // console.log("random count == 0");
    let line0 = document.getElementById('subpoem0').children[0].innerHTML;
    let line1 = document.getElementById('subpoem1').children[0].innerHTML;
    let line2 = document.getElementById('subpoem2').children[0].innerHTML;
    let line3 = document.getElementById('subpoem3').children[0].innerHTML;
    let line4 = document.getElementById('subpoem4').children[0].innerHTML;
    let line5 = document.getElementById('subpoem5').children[0].innerHTML;
    let line6 = document.getElementById('subpoem6').children[0].innerHTML;
    let line7 = document.getElementById('subpoem7').children[0].innerHTML;
    let line8 = document.getElementById('subpoem8').children[0].innerHTML;
    let line9 = document.getElementById('subpoem9').children[0].innerHTML;
    let line10 = document.getElementById('subpoem10').children[0].innerHTML;
    let line11 = document.getElementById('subpoem11').children[0].innerHTML;
    let line12 = document.getElementById('subpoem12').children[0].innerHTML;
    let line13 = document.getElementById('subpoem13').children[0].innerHTML;
    if(line0 && line1 && line2 && line3 && line4 && line5 && line6 && line7 && line8 && line9 && line10 && line11 && line12 && line13) {
      poems = line0 +'\r\n'+ line1 +'\r\n'+ line2 +'\r\n'+ line3 +'\r\n\n'+ line4 +'\r\n'+ line5 +'\r\n'+ line6 +'\r\n'+ line7 +'\r\n\n'+ line8 +'\r\n'+ line9 +'\r\n'+ line10 +'\r\n\n'+ line11 +'\r\n'+ line12 +'\r\n'+ line13;
      const re = /<form class="inlineform" action="\.\.\/textresults" method="post"><input type="radio" name="corpus" value="(?:faustroll|shakespeare)|" checked=""><input type="submit" name="query" value="|" onclick="loading\(\)|"><\/form>/g;
      poems = poems.replace(re, '');
      let poemail = `Poem generated using http://pata.physics.wtf\r\n------------------------------------------------------------\r\nKeyword: ${query}\r\nCorpus: ${corpus}\r\n------------------------------------------------------------\r\n\n${poems}`;
      let mailTo = new Mailto_url();
  		mailTo.setSubject("Pataphysical Poetry");
  		mailTo.setBody(poemail);
  		link.href = mailTo.getURL(true);
  	}
  // count == 0
  } else {
    // console.log("random count > 0");
      let inner = document.getElementById('random_poem').innerHTML;
      const re = /<form class="inlineform" action="\.\.\/textresults" method="post"><input type="radio" name="corpus" value="(?:faustroll|shakespeare)|" checked=""><input type="submit" name="query" value="|" onclick="loading\(\)|"><\/form>/g;
      let re1 = new RegExp("<br>", "g");
      let re2 = /<span title=\"((\w)+(\,)?(\-)?(\')?(\.)?(\s)*)+(\:\s)?((\w)+(\,)?(\-)?(\')?(\.)?(\s)*)+\">/g;
      let re3 = new RegExp("</span>", "g");
      poems = inner.replace(re, '');
      poems = poems.replace(re1, '');
      poems = poems.replace(re2, '');
      poems = poems.replace(re3, '\n');
      let sp = poems.split(/\n/);
      sp[3] = sp[3] + '\n';
      sp[7] = sp[7] + '\n';
      sp[10] = sp[10] + '\n';
      let comp = sp.join('\n');
      let poemail = `Poem generated using http://pata.physics.wtf\r\n------------------------------------------------------------\r\nKeyword: ${query}\r\nCorpus: ${corpus}\r\n------------------------------------------------------------\r\n\n${comp}`;
      let mailTo1 = new Mailto_url();
  		mailTo1.setSubject("Pataphysical Poetry");
  		mailTo1.setBody(poemail);
  		link.href = mailTo1.getURL(true);
  } // count > 0
}

