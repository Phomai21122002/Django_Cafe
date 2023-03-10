
const addcarts = document.querySelectorAll('.js-btn-cart')
const formcurtain = document.querySelector('.js-form')
const formorder = document.querySelector('.js-form-order')
const btnclose = document.querySelector('.js-form-close')

function ShowBoardBuyCart() {
    formcurtain.classList.add('open')
}

function RemoveBoardBuyCart() {
    formcurtain.classList.remove('open')
}

for (const addcart of addcarts) {
    addcart.addEventListener('click', ShowBoardBuyCart)
}

btnclose.addEventListener('click', RemoveBoardBuyCart)
formcurtain.addEventListener('click', RemoveBoardBuyCart)
formorder.addEventListener('click', function(event) {
    event.stopPropagation()
})