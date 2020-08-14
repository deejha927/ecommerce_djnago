var viewcart=document.getElementsByClassName("view-cart")
for(var i=0;i<viewcart.length;i++){
    addcart[i].addEventListener('click',function(){
        var id=this.dataset.info
        var act=this.dataset.act
        console.log("id:",id,"action:",act)

        console.log("username:",user)
        if(user=="AnonymousUser"){
            console.log("not logged in")
        }
        else{
            console.log("Valid user")
        }
    })
}