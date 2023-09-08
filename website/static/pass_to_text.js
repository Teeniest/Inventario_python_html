// Change the type of input to password or text
function pass_to_text() {
    let temp = document.getElementById("password");
     
    if (temp.type === "password") {
        temp.type = "text";
    }
    else {
        temp.type = "password";
    }
}