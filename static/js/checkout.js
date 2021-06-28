function payit(total) {
    var userdata = {
        'n1': null,
        'mail': null,
        'total': total,
    }
    var shippingdetails = {
        "address": null,
        'city': null,
        'state': null,
        'code': null,

    }
    userdata.n1 = form.n1.value;
    userdata.mail = form.mail.value;
    shippingdetails.address = form.address.value;
    shippingdetails.city = form.city.value;
    shippingdetails.state = form.state.value;
    shippingdetails.code = form.code.value;
    //alert(userdata.n1+" "+userdata.mail+" "+shippingdetails.address+" "+shippingdetails.city+" "+shippingdetails.state+" "+shippingdetails.code+" ");
    var url = '/placeorder'
    fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({
                'userdetails': userdata,
                'shippingdetails': shippingdetails
            })
        })
        .then((response) => {
            return response.json()
        })

    .then((data) => {
        alert("Your Order Has Been Placed");
        console.log("success:", data);
        window.location.href = "/";

    })
}
$("#form").submit(function(event) {
    var total = $("#total1").html();
    var res = total.split("₹");
    payit(res[1]);
    event.preventDefault();
});