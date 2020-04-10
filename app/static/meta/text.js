"use strict";

// TEXT SEARCH

// randomise poem
const shuffleButton = document.getElementById("shuffle");
shuffleButton.addEventListener("click", shufflePoem);
let cnt = 0; // counter
function shufflePoem() {
  cnt += 1;
  // [[file, [s1,s2,s3], algo],...]
  let rlist = [];
  for (let i = 0; i < 14; i++) {
    let r = Math.floor(Math.random() * n);
    let t = sentences[r][0]; // title
    let al = sentences[r][2]; // algorithm
    let b = sentences[r][1][0]; // before
    let m = sentences[r][1][1]; // middle / keyword
    let a = sentences[r][1][2]; // after
    let fullsent = `<div id="subpoem${i}"><span title="${t}, ${al}">${b} <form class="inlineform" action="../textresults" method="post"><input type="radio" name="corpus" value="${corpus}" checked><input type="submit" name="query" value="${m}"></form> ${a}</span></div>`;
    rlist[i] = fullsent;
  }
  rlist[3] = rlist[3].concat('<br>');
  rlist[7] = rlist[7].concat('<br>');
  rlist[10] = rlist[10].concat('<br>');
  let output = rlist.join('');
  document.getElementById('clickcount').innerHTML = cnt;
  document.getElementById('random_poem').innerHTML = output;
}


// EMAILS
function sendEmail(link, query, corpus, poem) {
  const poemail = `Poem generated using https://pata.physics.wtf\r\n------------------------------------------------------------\r\nKeyword: ${query}\r\nCorpus: ${corpus}\r\n------------------------------------------------------------\r\n\n${poem}`;
  const subject = encodeURIComponent("Pataphysical Poetry");
  const bcc = "pata@physics.wtf";
  const text = encodeURIComponent(poemail);
  const mailtoString = `mailto:?subject=${subject}&body=${text}`;
  link.href = mailtoString;
}


// QUENEAU
let qlink = document.getElementById("emailQueneau");
qlink.addEventListener("click", getQueneau);
function getQueneau() {
  const query = document.getElementById('querydiv').innerHTML;
  const corpus = document.getElementById('corpusdiv').innerHTML;
  const lollength = document.getElementById('lollength').innerHTML;
  const lineitem1 = document.getElementById('clicks1').innerHTML;
  const lineitem2 = document.getElementById('clicks2').innerHTML;
  const lineitem3 = document.getElementById('clicks3').innerHTML;
  const lineitem4 = document.getElementById('clicks4').innerHTML;
  const lineitem5 = document.getElementById('clicks5').innerHTML;
  const lineitem6 = document.getElementById('clicks6').innerHTML;
  const lineitem7 = document.getElementById('clicks7').innerHTML;
  const lineitem8 = document.getElementById('clicks8').innerHTML;
  const lineitem9 = document.getElementById('clicks9').innerHTML;
  const lineitem10 = document.getElementById('clicks10').innerHTML;
  const lineitem11 = document.getElementById('clicks11').innerHTML;
  const lineitem12 = document.getElementById('clicks12').innerHTML;
  const lineitem13 = document.getElementById('clicks13').innerHTML;
  const lineitem14 = document.getElementById('clicks14').innerHTML;
  let linearray = [];
  let poemsarray = [];
  const re = /<form class="inlineform" action="\.\.\/textresults" method="post"><input type="radio" name="corpus" value="(?:faustroll|shakespeare)|" checked=""><input type="submit" name="query" value="|"><\/form>/g;
  const allLines = document.getElementsByClassName('lines');
  for (let i = 0; i < lollength; i++) {
    let lineitem = eval(`lineitem${i + 1}`);
    linearray[i] = allLines[i].children[lineitem - 1];
    poemsarray[i] = linearray[i].innerHTML;
    poemsarray[i] = poemsarray[i].replace(re, '');
  }
  if (poemsarray[3]) poemsarray[3] = poemsarray[3] + '\n';
  if (poemsarray[7]) poemsarray[7] = poemsarray[7] + '\n';
  if (poemsarray[10]) poemsarray[10] = poemsarray[10] + '\n';
  const poems = poemsarray.join('\n');
  sendEmail(qlink, query, corpus, poems);
}


// RANDOM
let rlink = document.getElementById("emailRandom");
rlink.addEventListener("click", getRandom);
function getRandom() {
  const query = document.getElementById('querydiv').innerHTML;
  const corpus = document.getElementById('corpusdiv').innerHTML;
  const line0 = document.getElementById('subpoem0').children[0].innerHTML;
  const line1 = document.getElementById('subpoem1').children[0].innerHTML;
  const line2 = document.getElementById('subpoem2').children[0].innerHTML;
  const line3 = document.getElementById('subpoem3').children[0].innerHTML;
  const line4 = document.getElementById('subpoem4').children[0].innerHTML;
  const line5 = document.getElementById('subpoem5').children[0].innerHTML;
  const line6 = document.getElementById('subpoem6').children[0].innerHTML;
  const line7 = document.getElementById('subpoem7').children[0].innerHTML;
  const line8 = document.getElementById('subpoem8').children[0].innerHTML;
  const line9 = document.getElementById('subpoem9').children[0].innerHTML;
  const line10 = document.getElementById('subpoem10').children[0].innerHTML;
  const line11 = document.getElementById('subpoem11').children[0].innerHTML;
  const line12 = document.getElementById('subpoem12').children[0].innerHTML;
  const line13 = document.getElementById('subpoem13').children[0].innerHTML;
  if(line0 && line1 && line2 && line3 && line4 && line5 && line6 && line7 && line8 && line9 && line10 && line11 && line12 && line13) {
    let poems = line0 +'\r\n'+ line1 +'\r\n'+ line2 +'\r\n'+ line3 +'\r\n\n'+ line4 +'\r\n'+ line5 +'\r\n'+ line6 +'\r\n'+ line7 +'\r\n\n'+ line8 +'\r\n'+ line9 +'\r\n'+ line10 +'\r\n\n'+ line11 +'\r\n'+ line12 +'\r\n'+ line13;
    const re = /<form class="inlineform" action="\.\.\/textresults" method="post"><input type="radio" name="corpus" value="(?:faustroll|shakespeare)|" checked=""><input type="submit" name="query" value="|"><\/form>/g;
    poems = poems.replace(re, '');
    sendEmail(rlink, query, corpus, poems);
  }
}


// TABS
const poetry_tab = document.querySelector("#poetry_tab");
const sources_tab = document.querySelector("#sources_tab");
const algo_tab = document.querySelector("#algo_tab");
const tabs = [poetry_tab, sources_tab, algo_tab];

const poetry_trigger = document.querySelector("a[href='#poetry_tab']");
const sources_trigger = document.querySelector("a[href='#sources_tab']");
const algo_trigger = document.querySelector("a[href='#algo_tab']");
const triggers = [poetry_trigger, sources_trigger, algo_trigger];

const queneau_tab = document.querySelector("#q_tab");
const random_tab = document.querySelector("#r_tab");
const sub_tabs = [queneau_tab, random_tab];

const queneau_trigger = document.querySelector("a[href='#q_tab']");
const random_trigger = document.querySelector("a[href='#r_tab']");
const sub_triggers = [queneau_trigger, random_trigger];

// initial settings
hideAllSections();
poetry_trigger.classList.add("active");
poetry_tab.classList.remove("hide");
hideAllSubSections();
queneau_trigger.classList.add("active");
queneau_tab.classList.remove("hide");

triggers.forEach( (tr,i) => 
  tr.addEventListener("click", () => showTab("main", tabs[i], tr) )
);
sub_triggers.forEach( (str,i) => 
  str.addEventListener("click", () => showTab("sub", sub_tabs[i], str) )
);