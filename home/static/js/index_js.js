
// const addcarts = document.querySelectorAll('.js-btn-cart')
// const formcurtain = document.querySelector('.js-form')
// const formorder = document.querySelector('.js-form-order')
// const btnclose = document.querySelector('.js-form-close')

// function ShowBoardBuyCart() {
//     formcurtain.classList.add('open')
// }

// function RemoveBoardBuyCart() {
//     formcurtain.classList.remove('open')
// }

// for (const addcart of addcarts) {
//     addcart.addEventListener('click', ShowBoardBuyCart)
// }

// btnclose.addEventListener('click', RemoveBoardBuyCart)
// formcurtain.addEventListener('click', RemoveBoardBuyCart)
// formorder.addEventListener('click', function(event) {
//     event.stopPropagation()
// })

// tang so luong product
let amountElement = document.getElementById('amount')
let amount = amountElement.value

let render = (amount) => {
    amountElement.value = amount
}

let handle_plus = () => {
    amount++
    render(amount);
}

let handle_minus = () => {
    if (amount > 1)
        amount--;
    render(amount);
}

amountElement.addEventListener('input', () => {
    amount = amountElement.value;
    amount = parseInt(amount);
    amount = (isNaN(amount) || amount == 0)?1:amount;
    render(amount)
})


// chon dia diem giao hang

let order_shop = document.getElementById('order_shop')
let order_address = document.getElementById('order_address')
let fill_out = document.getElementById('form_fillout')
order_shop.addEventListener('change', () => {
    fill_out.classList.add('open')
})

order_address.addEventListener('change', () => {
    if(fill_out.classList.contains('open') == true) {
        fill_out.classList.remove('open')
    }
})