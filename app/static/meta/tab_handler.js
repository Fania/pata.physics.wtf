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

// eventListeners
triggers.forEach( (tr,i) => 
  tr.addEventListener("click", () => showTab("main", tabs[i], tr) )
);
sub_triggers.forEach( (str,i) => 
  str.addEventListener("click", () => showTab("sub", sub_tabs[i], str) )
);

function showTab(type, tab, trigger) {
  // console.log(tab, trigger);
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
