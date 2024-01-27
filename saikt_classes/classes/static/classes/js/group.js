var lessonInput = document.querySelectorAll(".lesson-input")
var bonusInput = document.querySelectorAll(".bonus-input")

function lesson_limit(e) {
    var value = e.currentTarget.value.toString() + e.key
    console.log(value)
    if (e.key == "-") {
        e.preventDefault();
    }
    if (value < 0 || value > 10) {
        e.preventDefault();
    }
}

function bonus_limit(e) {
    var value = e.currentTarget.value.toString() + e.key
    console.log(value)
    if (value < -10 || value > 10) {
        e.preventDefault();
    }
}

for (let i = 0; i < lessonInput.length; i++) {
    lessonInput[i].addEventListener("keypress", lesson_limit)
    
}
for (let i = 0; i < bonusInput.length; i++) {
    bonusInput[i].addEventListener("keypress", bonus_limit)
    
}

try {
    let specialBtns = document.querySelector("#specialBtns")

    function open_btn(event) {
        let inputs = document.querySelectorAll(".controls-course")
        for (let i = 0; i < inputs.length; i++) {
            inputs[i].classList.remove("input-show")
        }
        specialBtns.classList.remove("target")
        specialBtns.classList.add("target_flex")
    }

    function close_btn(event) {
        let inputs = document.querySelectorAll(".controls-course")
        for (let i = 0; i < inputs.length; i++) {
            inputs[i].classList.add("input-show")
        }
        specialBtns.classList.add("target")
        specialBtns.classList.remove("target_flex")
    }

    let closeBtn = document.querySelector("#closeBtn")
    let openBtn = document.querySelector("#openBtn")
    openBtn.addEventListener("click", open_btn)
    closeBtn.addEventListener("click", close_btn)

    let lessonBtn = document.querySelector("#lessonBtn")
    let bonusBtn = document.querySelector("#bonusBtn")

    function post_type_change(event) {
        target = event.currentTarget
        if (target.id == "lessonBtn" ) {
            input_value = document.querySelectorAll(".lesson-input")
            xp_values = document.querySelectorAll(".xp_value")
            for (let i = 0; i < input_value.length; i++) {
                xp_values[i].setAttribute("value", input_value[i].value)
            }

        }
        else {
            input_value = document.querySelectorAll(".bonus-input")
            xp_values = document.querySelectorAll(".xp_value")
            for (let i = 0; i < input_value.length; i++) {
                xp_values[i].setAttribute("value", input_value[i].value)
            }
        }
    }

    lessonBtn.addEventListener("click", post_type_change)
    bonusBtn.addEventListener("click", post_type_change)
} catch(err) {
    
}