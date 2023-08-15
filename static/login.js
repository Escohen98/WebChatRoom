//Handler for login.html
(function() {

    window.addEventListener("load", initialize);

    //Initialize to add visibility toggle.
    function initialize() {
        let checkbox = document.getElementById("toggle-visibility")
        checkbox.addEventListener("click", toggleVisibility);
        checkbox.checked = false;
    }

    //Changes the visibility for the password input
    function toggleVisibility() {
        input = document.getElementById("pass-input");
        if (input.type === "password") {
            input.type = "text";
        } else {
            input.type = "password";
        }
    } 
})();