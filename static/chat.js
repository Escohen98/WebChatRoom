//Probably temporary. Going to pass everything to the back-end.
(function() {
    window.addEventListener("load", initialize)

    function initialize() {
        document.getElementById("send-btn").addEventListener("click", addBubble);
        document.getElementById("add-btn").addEventListener("click", () =>
            document.getElementById("new-channel").hidden = false);
        document.getElementById("back-btn").addEventListener("click", hideChannelPopup);
        
        // Listen for form submission event
        document.getElementById("channel-form").addEventListener("submit", handleChannelSubmit);
    }

    //Adds chat bubble assuming the template doesn't get re-rendered (TBD)
    function addBubble() {
        console.log("Later.")
    }

    // Handle form submission
    function handleChannelSubmit(event) {
        
        console.log("here"); // This should be printed in the console
        // You can use AJAX or fetch to send the form data to the server if needed
        
        hideChannelPopup(); // Hide the popup after submission
    }

    //Hides the new channel popup
    //Will also add a new channel assuming the same as addBubble()
    function hideChannelPopup() {
        document.getElementById("new-channel").hidden = true;
        //More later.
    }
})();
