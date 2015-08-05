// SCROLL BUTTONS
if ( DYN_WEB.Scroll_Div.isSupported() ) {
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
}

// LOADING ICON
function loading(){
  $(".loading").show();
}

// FACEBOOK
(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = "//connect.facebook.net/en_GB/sdk.js#xfbml=1&version=v2.4";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));

// TWITTER
!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');

// POEM EMAIL
function Mailto_url(){
	var encode_mailto_component = function(str){
		try{ return encodeURIComponent(str); }
		catch(e){ return escape(str); }
	}
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
	this.setSubject = function(str){ subject = encode_mailto_component(str); }
	this.setBody = function(str){ body = encode_mailto_component(str); }
	this.addMain = function(x) { mainList.add(x); }
	this.addCC = function(x) { ccList.add(x); }
	this.addBCC = function(x) { bccList.add(x); }
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
	}
}
function getContent(link) {

  var query = document.getElementById('querydiv').innerHTML;
  
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

	var line1 = document.getElementById('lyr1').children[lineitem1 - 1];
  var line2 = document.getElementById('lyr2').children[lineitem2 - 1];
  var line3 = document.getElementById('lyr3').children[lineitem3 - 1];
  var line4 = document.getElementById('lyr4').children[lineitem4 - 1];
  var line5 = document.getElementById('lyr5').children[lineitem5 - 1];
  var line6 = document.getElementById('lyr6').children[lineitem6 - 1];
  var line7 = document.getElementById('lyr7').children[lineitem7 - 1];
  var line8 = document.getElementById('lyr8').children[lineitem8 - 1];
  var line9 = document.getElementById('lyr9').children[lineitem9 - 1];
  var line10 = document.getElementById('lyr10').children[lineitem10 - 1];
  var line11 = document.getElementById('lyr11').children[lineitem11 - 1];
  var line12 = document.getElementById('lyr12').children[lineitem12 - 1];
  var line13 = document.getElementById('lyr13').children[lineitem13 - 1];
  var line14 = document.getElementById('lyr14').children[lineitem14 - 1];

	if(line1 && line1.innerHTML &&
    line2 && line2.innerHTML &&
    line3 && line3.innerHTML &&
    line4 && line4.innerHTML &&
    line5 && line5.innerHTML &&
    line6 && line6.innerHTML &&
    line7 && line7.innerHTML &&
    line8 && line8.innerHTML &&
    line9 && line9.innerHTML &&
    line10 && line10.innerHTML &&
    line11 && line11.innerHTML &&
    line12 && line12.innerHTML &&
    line13 && line13.innerHTML &&
    line14 && line14.innerHTML){

    poems = line1.innerHTML +'\r\n'+ line2.innerHTML +'\r\n'+ line3.innerHTML +'\r\n'+ line4.innerHTML +'\r\n\n'+ line5.innerHTML +'\r\n'+ line6.innerHTML +'\r\n'+ line7.innerHTML +'\r\n'+ line8.innerHTML +'\r\n\n'+ line9.innerHTML +'\r\n'+ line10.innerHTML +'\r\n'+ line11.innerHTML +'\r\n\n'+ line12.innerHTML +'\r\n'+ line13.innerHTML +'\r\n'+ line14.innerHTML;

    var re1 = new RegExp("<form class=\"inform\" action=\"..\/textresults\" method=\"post\"><input class=\"inlink\" type=\"submit\" name=\"query\" value=\"", "g");
    var re2 = new RegExp('\" onclick=\"loading', "g");
    var re3 = new RegExp(';"></form>', "g");
    var re4 = /\(\)/g;
    var poems1 = poems.replace(re1, '');
    var poems2 = poems1.replace(re2, '');
    var poems3 = poems2.replace(re3, '');
    var poems4 = poems3.replace(re4, '');

    var pre = "Poem generated using http://pata.physics.wtf\r\n------------------------------------------------------------\r\n\nKeyword: ";
    var post = "\r\n------------------------------------------------------------\r\n\n"
    var poemail = pre + query + post + poems4;


    var mailTo = new Mailto_url();
		mailTo.setSubject("Patahpysical Poetry");
		mailTo.setBody(poemail);
		link.href = mailTo.getURL(true);
		return true;
	}
	return false;
}
function getRandContent(link) {

  var query = document.getElementById('querydiv').innerHTML;

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

    var re1 = new RegExp("<form class=\"inform\" action=\"..\/textresults\" method=\"post\"><input class=\"inlink\" type=\"submit\" name=\"query\" value=\"", "g");
    var re2 = new RegExp('\" onclick=\"loading', "g");
    var re3 = new RegExp(';"></form>', "g");
    var re4 = /\(\)/g;
    var poems1 = poems.replace(re1, '');
    var poems2 = poems1.replace(re2, '');
    var poems3 = poems2.replace(re3, '');
    var poems4 = poems3.replace(re4, '');

    var pre = "Poem generated using http://pata.physics.wtf\r\n------------------------------------------------------------\r\n\nKeyword: ";
    var post = "\r\n------------------------------------------------------------\r\n\n"
    var poemail = pre + query + post + poems4;

    var mailTo = new Mailto_url();
		mailTo.setSubject("Patahpysical Poetry");
		mailTo.setBody(poemail);
		link.href = mailTo.getURL(true);
		return true;
	}
	return false;
}
