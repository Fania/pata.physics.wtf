var microsoft_secret = keyconfig.microsoft_s;
var flickr_key = keyconfig.flickr_k;
var flick_secret = keyconfig.flick_s;
var bing_key = keyconfig.bing_k;
var bing_auth = keyconfig.bing_a;
var getty_key = keyconfig.getty_k;
var getty_key2 = keyconfig.getty_k2;
var youtube_key = keyconfig.youtube_k;


// FLICKR
function flickrsearch(queries){
  for(var x=0; x<10; x++){
    $.getJSON("http://api.flickr.com/services/feeds/photos_public.gne?jsoncallback=?",
      {
        tags: queries[x].query,
        tagmode: "all",
        format: "json"
      },
      function(data,status,ajax) {
        console.log("status " + status);
        console.log("ajax" + ajax);
        var title = "";
        var media = "";
        var link = "";
        var queryx = "TEST";
        if (data.items[0] != undefined) {
          title = data.items[0].title;
          media = data.items[0].media.m;
          link = data.items[0].link;
          console.log("test");
          // HOW DO I GET THE X NUMBER?????
          console.log(x);
          console.log(queries);
          // queryx = queries[x].query;
        }
        // call external function with current first result
        imgList([title, media, link, queryx]);
      } // end function data
    ); // end getJSON
    // imgList([title, media, link, queryx]);
  } // end of for loop
}; // end flickrsearch

var allImages = [];
// functio to accumulate images until 10 are reached and then
// calls the createSpiral function to display them all
function imgList(img){
  if (allImages[0] != "") {
    allImages.push(img);
  }
  if (allImages.length === 10) {
    createSpiral(allImages);
  }
} // end imgList

function createSpiral(imglist){
  // ' -*- '+imglist[3][3]
  if (imglist.length === 10){
    var spiral_code = ' \
    <div class="spouter"> \
      <div class="spleft"> \
        <div class="spltop"> \
          <div class="spltleft"> \
            <a id="a3" class="spimg" href="'+imglist[3][2]+'" ><img id="img3" src="'+imglist[3][1]+'" title="'+imglist[3][0]+' --- '+imglist[3][3]+'" height="210" width="210"/></a> \
          </div> \
          <div class="spltright"> \
            <div class="spltrtop"> \
              <a id="a8" class="spimg" href="'+imglist[8][2]+'" ><img id="img8" src="'+imglist[8][1]+'" title="'+imglist[8][0]+'" height="130" width="130"/></a> \
            </div> \
            <div class="spltrbottom"> \
              <div class="spltrbleft"> \
                <div class="spltrbltop"> \
                  <div class="spltrbltleft"> \
                    <a id="a0" class="spimg" href="'+imglist[0][2]+'" ><img id="img0" src="'+imglist[0][1]+'" title="'+imglist[0][0]+'" height="30" width="30"/></a> \
                  </div> \
                  <div class="spltrbltright"> \
                    <div class="spltrbltrtop"> \
                      <a id="a1" class="spimg" href="'+imglist[1][2]+'" ><img id="img1" src="'+imglist[1][1]+'" title="'+imglist[1][0]+'" height="20" width="20"/></a> \
                    </div> \
                    <div class="spltrbltrbottom"> \
                      <div class="spltrbltrbleft"> \
                        <a id="a5" class="spimg" href="'+imglist[5][2]+'" ><img id="img5" src="'+imglist[5][1]+'" title="'+imglist[5][0]+'" height="10" width="10"/></a> \
                      </div> \
                      <div class="spltrbltrbright"> \
                        <a id="a6" class="spimg" href="'+imglist[6][2]+'" ><img id="img6" src="'+imglist[6][1]+'" title="'+imglist[6][0]+'" height="10" width="10"/></a> \
                      </div> \
                    </div> \
                  </div> \
                </div> \
                <div class="spltrblbottom"> \
                  <a id="a7" class="spimg" href="'+imglist[7][2]+'" ><img id="img7" src="'+imglist[7][1]+'" title="'+imglist[7][0]+'" height="50" width="50"/></a> \
                </div> \
              </div> \
              <div class="spltrbright"> \
                <a id="a2" class="spimg" href="'+imglist[2][2]+'" ><img id="img2" src="'+imglist[2][1]+'" title="'+imglist[2][0]+'" height="80" width="80"/></a> \
              </div> \
            </div> \
          </div> \
        </div> \
        <div class="splbottom"> \
          <a id="a9" class="spimg" href="'+imglist[9][2]+'" ><img id="img9" src="'+imglist[9][1]+'" title="'+imglist[9][0]+'" height="340" width="340"/></a> \
        </div> \
      </div> \
      <div class="spright"> \
        <a id="a4" class="spimg" href="'+imglist[4][2]+'" ><img id="img4" src="'+imglist[4][1]+'" title="'+imglist[4][0]+'" height="550" width="550"/></a> \
      </div> \
    </div> \
    ';
    var list_code = [];
    for (i in imglist) {
      var img = ' \
        <div class="w3-col s12 m6 l3 w3-padding"> \
          <a href="'+imglist[i][2]+'"> \
            <img src="'+imglist[i][1]+'" \
            title="'+imglist[i][0]+'" style="width:100%"> \
          </a> \
        </div> \
      ';
      list_code.push(img);
    } // end for
    $('#img_spiral_div').html(spiral_code);
    $('#img_list_div').html(list_code);
  } // end if
  else{
    // console.log("inside else");
    $('.img_empty').wrap("<div>Not enough results found.</div>");
  } // end else
}



// GETTY
function gettysearch(query){
  var appendApiKeyHeader = function( xhr ) {
    xhr.setRequestHeader('Api-Key', getty_key2)
  }
  var searchRequest = {
    "phrase": query,
    "page_size": 10
  }
  // console.log('query ' + searchRequest.phrase)
  function GetSearchResults(callback) {
    $.ajax({
      type: "GET",
      beforeSend: appendApiKeyHeader,
      url: "https://api.gettyimages.com/v3/search/images/creative",
      data: searchRequest})
      .success(function (data, textStatus, jqXHR) {
        // console.log('data ' + data.images);
        var imgs = [];
        $.each(data.images, function(i,item){
          imgs.push([item.title, item.display_sizes[0].uri, ""]);
        });
        // console.log('imglist ' + imgs);
        createSpiral(imgs)
      }) // end of success
      .fail(function (data, err) {
        console.log('API error');
      }); // end of fail
  } // end GetSearchResults
  GetSearchResults();
}; // end of gettysearch



// BING
function bingsearch(query){
  var myurl1 = "https://api.datamarket.azure.com/Bing/Search/Image?";
  var myurl2 = "Query=" + "'" + query + "'" + "&$top=10&$format=json";
  var furl = myurl1 + myurl2;
  function GetSearchResults() {
    $.ajax({
      method: "post",
      url: furl,
      headers: {'Authorization': bing_auth},
      success: function (data) {
        var imglist = []
        $.each(data.d.results, function(i,item){
          imglist.push([item.Title, item.Thumbnail.MediaUrl, item.SourceUrl]);
        });
        createSpiral(imglist)
      }, // end of success
      failure: function (err) {
        console.log('API error');
      } // end of fail
    });
  } // end GetSearchResults
  GetSearchResults();
}; // end of bingsearch

/////////////////////////////////////////////////////////////////////

// SCROLL BUTTONS
if(window.location.pathname === '/textresults') {
  if (DYN_WEB.Scroll_Div.isSupported() ) {
      DYN_WEB.Event.add( window, 'load', function() {
  		// wndo args(id of scroll area div, id of content div)
      // addGlideControls args(id, axis('v'|'h'), distance, duration)
      var wndo1 = new DYN_WEB.Scroll_Div('wn1', 'lyr1');
  		wndo1.addGlideControls('scrollLinks1', 'h', 635, 300);
      var wndo2 = new DYN_WEB.Scroll_Div('wn2', 'lyr2');
      wndo2.addGlideControls('scrollLinks2', 'h', 635, 300);
      var wndo3 = new DYN_WEB.Scroll_Div('wn3', 'lyr3');
      wndo3.addGlideControls('scrollLinks3', 'h', 635, 300);
      var wndo4 = new DYN_WEB.Scroll_Div('wn4', 'lyr4');
      wndo4.addGlideControls('scrollLinks4', 'h', 635, 300);
      var wndo5 = new DYN_WEB.Scroll_Div('wn5', 'lyr5');
      wndo5.addGlideControls('scrollLinks5', 'h', 635, 300);
      var wndo6 = new DYN_WEB.Scroll_Div('wn6', 'lyr6');
      wndo6.addGlideControls('scrollLinks6', 'h', 635, 300);
      var wndo7 = new DYN_WEB.Scroll_Div('wn7', 'lyr7');
      wndo7.addGlideControls('scrollLinks7', 'h', 635, 300);
      var wndo8 = new DYN_WEB.Scroll_Div('wn8', 'lyr8');
      wndo8.addGlideControls('scrollLinks8', 'h', 635, 300);
      var wndo9 = new DYN_WEB.Scroll_Div('wn9', 'lyr9');
      wndo9.addGlideControls('scrollLinks9', 'h', 635, 300);
      var wndo10 = new DYN_WEB.Scroll_Div('wn10', 'lyr10');
      wndo10.addGlideControls('scrollLinks10', 'h', 635, 300);
      var wndo11 = new DYN_WEB.Scroll_Div('wn11', 'lyr11');
      wndo11.addGlideControls('scrollLinks11', 'h', 635, 300);
      var wndo12 = new DYN_WEB.Scroll_Div('wn12', 'lyr12');
      wndo12.addGlideControls('scrollLinks12', 'h', 635, 300);
      var wndo13 = new DYN_WEB.Scroll_Div('wn13', 'lyr13');
      wndo13.addGlideControls('scrollLinks13', 'h', 635, 300);
      var wndo14 = new DYN_WEB.Scroll_Div('wn14', 'lyr14');
      wndo14.addGlideControls('scrollLinks14', 'h', 635, 300);
  	});
  }else{
    alert("no DYN_WEB");
  }
} // end scrolldiv poems

// LOADING ICON
function loading() {
  $('.loading').show();
}

// FACEBOOK
// (function(d, s, id) {
//   var js, fjs = d.getElementsByTagName(s)[0];
//   if (d.getElementById(id)) return;
//   js = d.createElement(s); js.id = id;
//   js.src = '//connect.facebook.net/en_GB/sdk.js#xfbml=1&version=v2.4';
//   fjs.parentNode.insertBefore(js, fjs);
// }(document, 'script', 'facebook-jssdk'));
//
// // TWITTER
// !function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');

// POEM EMAIL
function Mailto_url(){
	var encode_mailto_component = function(str){
		try{ return encodeURIComponent(str); }
		catch(e){ return escape(str); }
	};
	var AddressList = function(){
		var list = [];
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
	var subject = '',
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
		var out = ['mailto:'];
		var extras = [];
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
  var query = document.getElementById('querydiv').innerHTML;
  var corpus = document.getElementById('corpusdiv').innerHTML;
  var lollength = document.getElementById('lollength').innerHTML;

  var lineitem1 = document.getElementById('clicks1').innerHTML;
  var lineitem2 = document.getElementById('clicks2').innerHTML;
  var lineitem3 = document.getElementById('clicks3').innerHTML;
  var lineitem4 = document.getElementById('clicks4').innerHTML;
  var lineitem5 = document.getElementById('clicks5').innerHTML;
  var lineitem6 = document.getElementById('clicks6').innerHTML;
  var lineitem7 = document.getElementById('clicks7').innerHTML;
  var lineitem8 = document.getElementById('clicks8').innerHTML;
  var lineitem9 = document.getElementById('clicks9').innerHTML;
  var lineitem10 = document.getElementById('clicks10').innerHTML;
  var lineitem11 = document.getElementById('clicks11').innerHTML;
  var lineitem12 = document.getElementById('clicks12').innerHTML;
  var lineitem13 = document.getElementById('clicks13').innerHTML;
  var lineitem14 = document.getElementById('clicks14').innerHTML;

  var linearray = [];
  var poemsarray = [];

  var re1 = new RegExp("<form class=\"inform\" action=\"..\/textresults\" method=\"post\"><input class=\"w3-hide\" type=\"radio\" name=\"corpus\" value=\"", "g");
  var re1A = new RegExp("\" checked=\"\"><input class=\"inlink\" type=\"submit\" name=\"query\" value=\"", "g");
  var re2 = new RegExp('\" onclick=\"loading()', "g");
  var re3 = new RegExp(';"></form>', "g");
  var re4 = /\(\)/g;

  for (var i = 0; i < lollength; i++) {
    var lid = 'lyr' + (i + 1);
    var lineitem = eval('lineitem' + (i + 1));
    linearray[i] = document.getElementById(lid).children[lineitem - 1];
    poemsarray[i] = linearray[i].innerHTML;
    var tmp = poemsarray[i];
    var tmp1 = tmp.replace(re1, '');
    var tmp1A = tmp1.replace(re1A, '');
    var tmp1B = tmp1A.replace(corpus, '');
    var tmp2 = tmp1B.replace(re2, '');
    var tmp3 = tmp2.replace(re3, '');
    var tmp4 = tmp3.replace(re4, '');
    poemsarray[i] = tmp4;
  }

  if (poemsarray[3]) {
      poemsarray[3] = poemsarray[3] + '\n';
  }
  if (poemsarray[7]) {
      poemsarray[7] = poemsarray[7] + '\n';
  }
  if (poemsarray[10]) {
      poemsarray[10] = poemsarray[10] + '\n';
  }

  var poems = poemsarray.join('\n');

  var pre = "Poem generated using http://pata.physics.wtf\r\n------------------------------------------------------------\r\nKeyword: ";
  var mid = "\r\nCorpus: ";
  var post = "\r\n------------------------------------------------------------\r\n\n";
  var poemail = pre + query + mid + corpus + post + poems;

  var mailTo = new Mailto_url();
	mailTo.setSubject("Pataphysical Poetry");
	mailTo.setBody(poemail);
	link.href = mailTo.getURL(true);

	return true;
}

// Random Email
function getRandContent(link) {

  var query = document.getElementById('querydiv').innerHTML;
  var corpus = document.getElementById('corpusdiv').innerHTML;
  var count = document.getElementById('clickcount').innerHTML;

  if (count == 0) {
    var line0 = document.getElementById('subpoem0').children[0].innerHTML;
    var line1 = document.getElementById('subpoem1').children[0].innerHTML;
    var line2 = document.getElementById('subpoem2').children[0].innerHTML;
    var line3 = document.getElementById('subpoem3').children[0].innerHTML;
    var line4 = document.getElementById('subpoem4').children[0].innerHTML;
    var line5 = document.getElementById('subpoem5').children[0].innerHTML;
    var line6 = document.getElementById('subpoem6').children[0].innerHTML;
    var line7 = document.getElementById('subpoem7').children[0].innerHTML;
    var line8 = document.getElementById('subpoem8').children[0].innerHTML;
    var line9 = document.getElementById('subpoem9').children[0].innerHTML;
    var line10 = document.getElementById('subpoem10').children[0].innerHTML;
    var line11 = document.getElementById('subpoem11').children[0].innerHTML;
    var line12 = document.getElementById('subpoem12').children[0].innerHTML;
    var line13 = document.getElementById('subpoem13').children[0].innerHTML;

    if(line0 && line1 && line2 && line3 && line4 && line5 && line6 && line7 && line8 && line9 && line10 && line11 && line12 && line13){

      poems = line0 +'\r\n'+ line1 +'\r\n'+ line2 +'\r\n'+ line3 +'\r\n\n'+ line4 +'\r\n'+ line5 +'\r\n'+ line6 +'\r\n'+ line7 +'\r\n\n'+ line8 +'\r\n'+ line9 +'\r\n'+ line10 +'\r\n\n'+ line11 +'\r\n'+ line12 +'\r\n'+ line13;

      var re1 = new RegExp("<form class=\"inform\" action=\"..\/textresults\" method=\"post\"><input class=\"w3-hide\" type=\"radio\" name=\"corpus\" value=\"", "g");
      var re1A = new RegExp("\" checked=\"\"><input class=\"inlink\" type=\"submit\" name=\"query\" value=\"", "g");
      var re1B = new RegExp(corpus, "g");
      var re2 = new RegExp('\" onclick=\"loading', "g");
      var re3 = new RegExp(';"></form>', "g");
      var re4 = /\(\)/g;
      var poems1 = poems.replace(re1, '');
      var poems1A = poems1.replace(re1A, '');
      var poems1B = poems1A.replace(re1B, '');
      var poems2 = poems1B.replace(re2, '');
      var poems3 = poems2.replace(re3, '');
      var poems4 = poems3.replace(re4, '');

      var pre = "Poem generated using http://pata.physics.wtf\r\n------------------------------------------------------------\r\nKeyword: ";
      var mid = "\r\nCorpus: ";
      var post = "\r\n------------------------------------------------------------\r\n\n";
      var poemail = pre + query + mid + corpus + post + poems4;

      var mailTo = new Mailto_url();
  		mailTo.setSubject("Pataphysical Poetry");
  		mailTo.setBody(poemail);
  		link.href = mailTo.getURL(true);
  		return true;
  	}
    return true;
  // count == 0
  } else {
      var inner = document.getElementById('random_poem').innerHTML;

      // CONTINUE FIXING HERE

      var re1 = new RegExp("<form class=\"inform\" action=\"..\/textresults\" method=\"post\"><input class=\"w3-hide\" type=\"radio\" name=\"corpus\" value=\"", "g");
      var re1A = new RegExp("\" checked=\"\"><input class=\"inlink\" type=\"submit\" name=\"query\" value=\"", "g");
      var re1B = new RegExp(corpus, "g");
      var re2 = new RegExp('\" onclick=\"loading', "g");
      var re3 = new RegExp(';"></form>', "g");
      var re4 = /\(\)/g;
      var re5 = new RegExp("<br>", "g");
      var re6 = /<span title=\"((\w)+(\,)?(\-)?(\')?(\.)?(\s)*)+(\:\s)?((\w)+(\,)?(\-)?(\')?(\.)?(\s)*)+\">/g;
      var re7 = new RegExp("</span>", "g");
      var poems1 = inner.replace(re1, '');
      var poems1A = poems1.replace(re1A, '');
      var poems1B = poems1A.replace(re1B, '');
      var poems2 = poems1B.replace(re2, '');
      var poems3 = poems2.replace(re3, '');
      var poems4 = poems3.replace(re4, '');
      var poems5 = poems4.replace(re5, '');
      var poems6 = poems5.replace(re6, '');
      var poems7 = poems6.replace(re7, '\n');

      var sp = poems7.split(/\n/);
      sp[3] = sp[3] + '\n';
      sp[7] = sp[7] + '\n';
      sp[10] = sp[10] + '\n';
      var comp = sp.join('\n');

      var pre = "Poem generated using http://pata.physics.wtf\r\n------------------------------------------------------------\r\nKeyword: ";
      var mid = "\r\nCorpus: ";
      var post = "\r\n------------------------------------------------------------\r\n\n";
      var poemail = pre + query + mid + corpus + post + comp;

      var mailTo1 = new Mailto_url();
  		mailTo1.setSubject("Pataphysical Poetry");
  		mailTo1.setBody(poemail);
  		link.href = mailTo1.getURL(true);
  		return true;
  } // count > 0

	return false;
}

// GETTY

var appendApiKeyHeader = function( xhr ) {
  xhr.setRequestHeader('Api-Key', getty_key)
}

function GetSearchResults(words) {
  var searchRequest = { "phrase": words }
  $.ajax({
    type: "GET",
    beforeSend: appendApiKeyHeader,
    url: "https://api.gettyimages.com/v3/search/creative",
    data: searchRequest})
    .success(function (data, textStatus, jqXHR) { /* use search results */ })
    .fail(function (data, err) { /* handle errors */ });
}
