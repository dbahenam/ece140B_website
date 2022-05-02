function product_page(){
    fetch('/productInfo').then(function (response) {
        // The API call was successful!
        return response.text();
    })
};