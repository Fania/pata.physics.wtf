"use strict";

// GOLDEN SPIRALS
function createSpiral(imglist) {
  // console.log('createSpiral', imglist);
  if (imglist.length === 10){
    // const fib = [10,10,20,30,50,80,130,210,340,550];
    const nums = ["one","two","three","four","five","six","seven","eight","nine","ten"];
    for (let i in imglist ) {
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


// TABS
const spiral_tab = document.querySelector("#spiral_tab");
const list_tab = document.querySelector("#list_tab");
const tabs = [spiral_tab, list_tab];
const spiral_trigger = document.querySelector("a[href='#spiral_tab']");
const list_trigger = document.querySelector("a[href='#list_tab']");
const triggers = [spiral_trigger, list_trigger];

// initial settings
hideAllSections();
spiral_trigger.classList.add("active");
spiral_tab.classList.remove("hide");

triggers.forEach( (tr,i) => 
  tr.addEventListener("click", () => showTab("main", tabs[i], tr) )
);