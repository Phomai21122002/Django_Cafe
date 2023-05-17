const addBtn = document.getElementById('add_product_btn');
const buyBtn = document.getElementById('buy_product_btn');
const payBill = document.getElementById('pay_bill');

const setCookie = (name, json) => {
    let cookieValue = '';
    let expire = '';
    let period = '';

    //Specify the cookie name and value
    cookieValue = name + '=' + JSON.stringify(json) + ';';

    //Specify the path to set the cookie
    cookieValue += 'path=/ ;';

    //Specify how long you want to keep cookie
    period = 30; //days to store
    expire = new Date();
    expire.setTime(expire.getTime() + 1000 * 3600 * 24 * period);
    expire.toUTCString();
    cookieValue += 'expires=' + expire + ';';

    document.cookie = cookieValue;
};

const addProductIntoCookie = ({ product }) => {
    var cart = JSON.parse(document.cookie.split('cart=')[1]);
    var isValidID = false;
    var count = 0;
    var idProduct;
    // nếu trùng sản phẩm đang có trong giỏ hàng
    for (let i = 0; i < cart.length; i++) {
        if (cart[i].idProduct == product.idProduct) {
            var countBefore = Number(cart[i].count);
            countBefore += Number(product.count);
            count = countBefore;
            idProduct = cart[i].id;
            cart[i].count = countBefore;
            isValidID = true;
            break;
        }
    }

    if (isValidID) {
        setCookie('cart', cart);

        return { result: false, count: count, idProduct: idProduct }; // chỉ thêm số lượng
    } else {
        cart.push(product);
        setCookie('cart', cart);
        return { result: true, product: product };
    }
};

buyBtn.addEventListener('click', () => {
    const count = Number(document.getElementById('amount').value);
    console.log(count);
    const path = window.location.pathname;
    const id = path.split('/')[2];
    const nameProduct = document.querySelector('.form-navbar-contact_title').textContent.trim();
    const price = Number(document.getElementById('price_product').textContent);

    const product = {
        idProduct: id,
        count: count,
        nameProduct: nameProduct,
        price: price,
    };

    const resultHandle = addProductIntoCookie({ product: product });

    if (resultHandle.result == true) {
        addProductViewCart({ product: resultHandle.product });
    }
});

const addProductViewCart = ({ product }) => {
    const formshipment = document.querySelector('.header-top-shipment_list');
    formshipment.innerHTML += `<li class="header-top-shipment_item">
                                    <div class="header-top-shipment_box">
                                        <div class="header-top-shipment_box-flex">
                                            <div class="header-top-shipment_name">
                                                ${product.nameProduct}
                                            </div>
                                            <div class="header-top-shipment_size">
                                                (Size L)
                                            </div>
                                        </div>
                                        
                                        <div class="header-top-shipment_price">
                                            ₫${product.price}
                                        </div>
                                    </div>
                                    <ul class="header-top-shipment_sublist style">
                                        <li class="header-top-shipment_subitem">
                                            1 x 50% đường
                                        </li>
                                        <li class="header-top-shipment_subitem">
                                            1 x 50% đá
                                        </li>
                                        <li class="header-top-shipment_subitem">
                                            1 x Thêm sữa
                                        </li>
                                        <li class="header-top-shipment_subitem">
                                            1 x Thêm thạch
                                        </li>
                                    </ul>
                                    <div class="header-top-shipment_boxbottom">
                                        <button value="${product.idProduct}" class="header-top-shipment_btndelete btn-delete">
                                            Xóa
                                        </button>
                                        <div class="form-order_boxnumber ">
                                            <div class="form-order_minus pd">
                                                <i class="form-order_changenumber-icon fa-solid fa-minus"></i>
                                            </div>
                                            <span class="form-order_number">${product.count}</span>
                                            <div class="form-order_plus pd">
                                                <i class="form-order_changenumber-icon fa-solid fa-plus"></i>
                                            </div>
                                        </div>
                                    </div>
                                </li>`;
};

if (document.cookie.split('cart=').length < 2) {
    setCookie('cart', []);
}

// Lấy dữ liệu cart từ cookie và gán vào view
var cart = JSON.parse(document.cookie.split('cart=')[1]);

for (let i = 0; i < cart.length; i++) {
    const product = cart[i];
    addProductViewCart({ product });
}

