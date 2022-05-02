function product_page(){
    // This URL path is going to be the route defined in app.py
    let theURL='/productInfo';

    // This logger is just to keep track of the function call.
    // You can use such log messages to debug your code if you need.
    console.log("Making a RESTful request to the server!")

    // fetch is a Javascript function that sends a request to a server
    let response = fetch(theURL);
};