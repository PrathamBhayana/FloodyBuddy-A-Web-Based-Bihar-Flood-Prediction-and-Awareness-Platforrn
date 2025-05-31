let icon = document.querySelector(".sml-dev");
let ul = document.querySelector(".navbar");

icon.addEventListener("click", ()=> {
    ul.classList.toggle("show");
    
    if( ul.classList.contains('show')){
        document.querySelector('.ham').style.display='none';
        document.querySelector('.cross').style.display='inline';
    }

    else{
        document.querySelector('.ham').style.display='inline';
            document.querySelector('.cross').style.display='none';
    }

})