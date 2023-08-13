(function() {
    const loginForm = document.getElementById("login-form");

    //Handles user authentication asynchronously. Also taken from ChatGPT
    loginForm.addEventListener("submit", async (event) => {
      event.preventDefault();
  
      const email = loginForm.email.value;
      const password = loginForm.password.value;
  
      try {
        const userCredential = await firebase.auth().signInWithEmailAndPassword(email, password);
        // User is logged in successfully, you can redirect to the chat page or perform other actions.
      } catch (error) {
        // Handle authentication errors, show error messages to the user, etc.
        console.error(error.message);
      }
    });
})();