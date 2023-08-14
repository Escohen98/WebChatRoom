//Probably temporary. Going to pass everything to the back-end.
(function() {
    window.getEventListener(load, "initialize");

    function initialize() {
        document.getElementById("send-btn").addEventListener(click, "addBubbble");
    }

    function addBubble() {
        console.log("Later.")
    }
})();
