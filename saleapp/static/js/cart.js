function addToCart(id, name, price) {
    fetch('/api/carts', {
        method: 'post',
        body: JSON.stringify({
            'id': id,
            "name": name,
            "price": price
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(res => res.json()).then(data => {
        let d = document.getElementsByClassName('class-counter');
        for (let c of d)
            c.innerText = data.total_quantity;
    });
}