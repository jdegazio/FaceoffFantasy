// Declare passwordOneInput and passwordTwoInput as global variables
var passwordOneInput;
var passwordTwoInput;

function validateUsername() {
    const usernameInput = document.getElementById('newUsername').value;
    if (!usernameInput) {
        return false; // Prevent form submission
    }

    // Check for special characters other than underscores
    if (/[^a-zA-Z0-9_]/.test(usernameInput)) {
        return false; // Prevent form submission
    }

    return true; // Validation passed
}

function validateEmail() {
    const emailInput = document.getElementById('newEmail').value;
    if (!emailInput) {
        return false; // Prevent form submission
    }

    // Basic email format validation using a regular expression
    if (!/^\S+@\S+\.\S+$/.test(emailInput)) {
        return false; // Prevent form submission
    }

    return true; // Validation passed
}

function validatePassword() {
    passwordOneInput = document.getElementById('newPassword').value;
    passwordTwoInput = document.getElementById('confirmPassword').value;

    if (passwordOneInput !== passwordTwoInput) {
        return false; // Prevent form submission
    }

    if (passwordOneInput.length < 8) {
        return false; // Prevent form submission
    }

    return true; // Validation passed
}

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('createAccountForm');
    const errorMessage = document.getElementById('error-message');
    const verificationMessage = document.getElementById('verification-message');
    const messageGraphic = document.getElementById('message-graphic');
	passwordOneInput = document.getElementById('newPassword').value;
    passwordTwoInput = document.getElementById('confirmPassword').value;

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent form submission by default

        const usernameValid = validateUsername();
        const emailValid = validateEmail();
        const passwordValid = validatePassword();

        if (usernameValid !== false && emailValid !== false && passwordValid !== false) {
		verificationMessage.style.display = 'block'; // Show the verification message
		errorMessage.style.display = 'none'; // Hide the error message
		messageGraphic.style.display = 'none';
		} else {
			if (!usernameValid) {
				errorMessage.innerHTML = "This username is invalid or taken.";
			} else if (!emailValid) {
				errorMessage.innerHTML = "This email is invalid.";
			} else if (!passwordValid) {
				if (passwordOneInput !== passwordTwoInput) {
					errorMessage.innerHTML = "These passwords do not match.";
				} else {
					errorMessage.innerHTML = "This password is invalid or too short.";
				}
			}

			errorMessage.style.display = 'block'; // Show the error message
			verificationMessage.style.display = 'none'; // Hide the verification message
			messageGraphic.style.display = 'none';
		}
    });
});