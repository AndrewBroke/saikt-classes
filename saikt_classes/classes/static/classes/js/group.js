var lessonInput = document.getElementById("lesson-input")
var bonusInput = document.getElementById("bonus-input")

function lesson_limit(e) {
    var value = lessonInput.value.toString() + e.key
    console.log(value)
    if (value < 0 || value > 10) {
        e.preventDefault();
        alert(
            "За занятие можно добавить только до 10 баллов"
        )
    }
}

function bonus_limit(e) {
    var value = bonusInput.value.toString() + e.key
    console.log(value)
    if (value < 0 || value > 10) {
        e.preventDefault();
        alert(
            "За занятие можно добавить только до 10 баллов"
        )
    }
}

lessonInput.addEventListener("keypress", lesson_limit)
bonusInput.addEventListener("keypress", bonus_limit)


function open_btn(event) {
    let inputs = document.querySelectorAll(".controls-course")
    for (let i = 0; i < inputs.length; i++) {
        console.log(inputs[i])
        inputs[i].classList.remove("input-show")
    }
}

function close_btn(event) {
    let inputs = document.querySelectorAll(".controls-course")
    for (let i = 0; i < inputs.length; i++) {
        console.log(inputs[i])
        inputs[i].classList.add("input-show")
    }
}

let closeBtn = document.querySelector("#closeBtn")
let openBtn = document.querySelector("#openBtn")
openBtn.addEventListener("click", open_btn)
closeBtn.addEventListener("click", close_btn)