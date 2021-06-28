var addcart = document.getElementsByClassName("insert-cart")
$("#btn1").click(function() {
    alert("You Need To Login Before Buying Product.")
    window.location.href = "/login";
})
for (var i = 0; i < addcart.length; i++) {
    addcart[i].addEventListener('click', function() {
        var id = this.dataset.product
        var act = this.dataset.action
        console.log("id:", id, "action:", act)
        addtocart(id, act)
    })
}

function addtocart(id, act) {
    console.log("we have yor data")
    var url = '/addtocart'
    fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({ 'productid': id, 'action': act })
        })
        .then((response) => {
            return response.json()
        })

    .then((data) => {
        location.reload(true);
        console.log("value:", data)

    })
}
//cart viewing