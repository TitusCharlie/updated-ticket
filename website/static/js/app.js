const navList = document.getElementById("navBar");
window.onscroll = function(){
  if(document.body.scrollTop < 0 || document.documentElement.scrollTop > 5){
    navBar.classList.add("headTransparent");
    navBar.classList.remove("head");
  }else{
    navBar.classList.add("head");
    navBar.classList.remove("headTransparent");
  }
}