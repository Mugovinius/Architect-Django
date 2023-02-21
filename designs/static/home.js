const serviceCont = document.querySelector(".service-container");
const prevBtn = document.querySelector(".service-left");
const nextBtn = document.querySelector(".service-right");
let currentItems = 0;
let djangoData = "{{data|safe}}";
let mydata =JSON.parse(djangoData);
console.log(mydata);
function displayNext(menuItems){
    let displayMenu = menuItems.map(function(item){
        return `<div class="indiv-service">
        <img src=${item.service_image}>
        <h2>${item.service_name}</h2>
        <p>${item.description}</p>
    </div>`;
    });
    displayMenu = displayMenu.join("");
    serviceCont.innerHTML = displayMenu;
}
const displayNextThree = () => {
    displayNext(data.slice(currentItems, currentItems + 3));
}
const miniWidth = () => {
    displayNext(data.slice(currentItems, currentItems + 1));
}            
 
window.addEventListener("DOMContentLoaded", function(){
    if (this.window.innerWidth <=555){
        miniWidth();
    }else{
        //console.log(window.innerWidth);
        displayNextThree();
    }
});
