function copyToClipboard(text) {

    console.log(text);
    document.execCommand('copy',text);
    
}

function loadCircle(){
    console.log('loading')
    document.getElementById("postLoading").removeAttribute="hidden";
    
    
    
    }