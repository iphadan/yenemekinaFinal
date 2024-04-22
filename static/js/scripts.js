function copyToClipboard(text) {

    console.log(text);
    document.execCommand('copy',text);
    
}