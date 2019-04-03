let btn = document.getElementsByClassName("remove_button")
let item = document.getElementsByClassName("item")

btn[0].addEventListener('click', () => {
    item[0].innerHTML = ''
})
btn[1].addEventListener('click', () => {
    item[1].innerHTML = ''
})
