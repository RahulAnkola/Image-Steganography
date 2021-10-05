function myFunction() {
    var btnReadmore = document.getElementById("dots");
    var moreText = document.getElementById("readmore");
    
    if(moreText.style.display=="none"){
        moreText.style.display="inline";
        btnReadmore.innerHTML ="Read Less";
    }
    else{
        moreText.style.display="none";
        btnReadmore.innerHTML = "Read More...";
    }
    
  }