
(function() {

   closeSlideMenu();
   document.getElementById("open-slide").classList.add('closed');
   document.getElementById("open-slide").classList.remove('opened');
        
})();

function openSlideMenu() {
    document.getElementById('side-menu').style.width = '250px';
    document.getElementById('main').style.marginLeft = '250px';
    document.getElementById('side-menu-link').style.display='inline-block';
    document.getElementById('side-menu-link2').style.display='inline-block';
    document.getElementById('side-menu-link3').style.display='inline-block';
    document.getElementById('side-menu-link4').style.display='inline-block';
    document.getElementById('side-menu-link5').style.display='inline-block';

}
function closeSlideMenu() {
    document.getElementById('side-menu').style.width = '60px';
    document.getElementById('main').style.marginLeft = '60px';
    document.getElementById('side-menu-link').style.display='none';
    document.getElementById('side-menu-link2').style.display='none';
    document.getElementById('side-menu-link3').style.display='none';
    document.getElementById('side-menu-link4').style.display='none';
    document.getElementById('side-menu-link5').style.display='none';

}

function menuToggle(){
    var x = document.getElementById('side-menu');
    if (x.style.width >= '250px'){
        x.style.width = '60px';
    }else if(x.style.display <= '250px'){
        x.style.width = '250px';

    }
}

//this the function that i added to handle the onclick event
window.onclick = function(event) {
  if (event.target.matches('.navbartoggle')) {
    if(event.target.matches('.opened')){
    
        closeSlideMenu();

        document.getElementById("open-slide").classList.add('closed');
        document.getElementById("open-slide").classList.remove('opened');
        
    } else if(event.target.matches('.closed')){
    
        openSlideMenu();

        document.getElementById("open-slide").classList.add('opened');
        document.getElementById("open-slide").classList.remove('closed');
    }
    
  }
}