var addcart=document.getElementsByClassName("insert-cart")

for(var i=0;i<addcart.length;i++){
    addcart[i].addEventListener('click',function(){
        var id=this.dataset.product
        var act=this.dataset.action
        console.log("id:",id,"action:",act)

        console.log("username:",user)
        if(user=="AnonymousUser"){
            alert("you are not logined");
            window.location.href="http://127.0.0.1:8000/login";
        }
        else{
            addtocart(id,act)
        }
    })
}
function addtocart(id,act)
{
    console.log("we have yor data")
    var url='/addtocart'
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productid':id,'action':act})
    })
    .then((response)=>{
        return response.json()
    })

    .then((data)=>{
        location.reload(true);
        console.log("value:",data)
        
    })
}
//cart viewing
