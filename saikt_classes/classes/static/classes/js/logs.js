submit_btn = document.querySelector(".submit_btn")
clear_btn = document.querySelector(".clear_btn")
filter_input = document.querySelector(".filter_input")


function filter(e){
    if(e.currentTarget == submit_btn){
        filter_input.setAttribute("value", "submit")
    }
    else{
        filter_input.setAttribute("value", "clear")
    }
}

clear_btn.addEventListener("click", filter)
submit_btn.addEventListener("click", filter)
