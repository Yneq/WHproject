document.querySelector('#login_form').addEventListener('submit', function(event) {
    let termsCheckbox = document.querySelector('#terms_checkbox');
    if(!termsCheckbox.checked) {
        alert('Please check the checkbox first');
        event.preventDefault();
    }
});