var updateBtns = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function() {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'Action: ', action)
        console.log('USER:', user)
        if (user == 'AnonymousUser') {
            console.log('Usuario no autenticado')


        } else {
            updateOrdenCliente(productId, action)
        }


    })

}

// function updateOrdenCliente(productId, action) {


//     var url = '/update_item/'
//     console.log('URL', url)

//     fetch(url, {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//                 'X-CSRFToken': csrftoken,
//             },
//             body: JSON.stringify({ 'productId': productId, 'action': action })


//         })
//         .then((response) => {
//             return response.json();
//         })
//         .then((data) => {
//             console.log('data:', data)
//             location.reload()
//         })
// }

function updateOrdenCliente(productId, action) {


    var url = '/update_item/'
    console.log('URL', url)

    fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({ 'productId': productId, 'action': action })


        })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            console.log('data:', data)
            location.reload()
            if (data.quantity === 0) {
                // esto hace que se envie al metodo de views llamado updateItem
                fetch('/update_item/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrftoken,
                    },
                    body: JSON.stringify({ 'productId': productId, 'action': 'remove' })
                })
                .then((response) => {
                    return response.json();
                })
                .then((data) => {
                    console.log('data:', data)
                })
            }
        })
}


