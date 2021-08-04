
// script to change display for hamburger menu when viewing page on mobile

// grab elements 
let hamburgerMenu = document.getElementById("menu");
let mobilMenu = document.getElementById("mobileMenu");
let sumbitButton = document.getElementById("sumbit");

// onclick function for menu icon
hamburgerMenu.addEventListener('click', () => {
    if (mobilMenu.style.display === "block") {
        mobilMenu.style.display = "none";
    } else {
        mobilMenu.style.display = "block";
    }
}); 
// mouse leave function for mobile menu
mobilMenu.addEventListener('mouseleave', () => {
    mobilMenu.style.display="none";
});
// sumbit button messafe
sumbitButton.addEventListener('click', () => {
    alert("Your message has been sent!");
});