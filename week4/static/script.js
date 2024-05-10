document.querySelector('#login_form').addEventListener('submit', function(event) {
    let termsCheckbox = document.querySelector('#terms_checkbox');
    if(!termsCheckbox.checked) {
        alert('Please check the checkbox first');
        event.preventDefault();
    }
});

function calculateSquare() {
    let input = document.querySelector("#numberInput").value;
    let number = parseInt(input);

    if (!Number.isInteger(number) || number <= 0) {
        alert("Please enter a positive number");
    } else {
        window.location.href = `/square/${number}`;
    }
}