"use strict";

// VIDEO SPIRAL
function createVideoSpiral(videolist) {
  // console.log("videos");
  const nums = ["one","two","three","four","five","six","seven","eight","nine","ten"];
  for ( i in videolist ) {
    if (i < 4) {
      vid_spiral_div.insertAdjacentHTML("beforeend", 
        `<iframe class="${nums[i]}" title="${videolist[i][0]}" alt="${videolist[i][2]}" src="https://www.youtube.com/embed/${videolist[i][2]}?controls=0&rel=0&showinfo=0&modestbranding=0&controls=0" frameborder="0"></iframe>`);
    } else {
      vid_spiral_div.insertAdjacentHTML("beforeend", 
        `<a class="${nums[i]}" href="https://www.youtube.com/embed/${videolist[i][2]}"><img src="${videolist[i][1]}" alt="${videolist[i][0]}" title="${videolist[i][0]}"></a>`);
    }
  }
}


// TABS
const spiral_tab = document.querySelector("#vid_spiral_tab");
const list_tab = document.querySelector("#vid_list_tab");
const tabs = [spiral_tab, list_tab];
const spiral_trigger = document.querySelector("a[href='#vid_spiral_tab']");
const list_trigger = document.querySelector("a[href='#vid_list_tab']");
const triggers = [spiral_trigger, list_trigger];

// initial settings
hideAllSections();
spiral_trigger.classList.add("active");
spiral_tab.classList.remove("hide");

triggers.forEach( (tr,i) => 
  tr.addEventListener("click", () => showTab("main", tabs[i], tr) )
);