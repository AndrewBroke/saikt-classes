let master_select = document.querySelector("#groups")
let last_select = null

function select_show(event){
    current_select_id = event.target.value

    current_select = document.getElementById(current_select_id)
    current_select.classList.toggle("group_select")
    
    if (last_select) {
        last_select.classList.toggle("group_select")
    }
    last_select = current_select
}


master_select.addEventListener("change", select_show)