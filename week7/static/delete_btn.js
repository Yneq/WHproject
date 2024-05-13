document.addEventListener('DOMContentLoaded', function() {
    const deleteButtons = document.querySelectorAll('.delete_btn');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function() {
            const messageId = this.getAttribute('data-id');
            console.log('Delete button clicked, message ID:', messageId);  
            if (messageId) {
                deleteMessage(this, messageId);
            } else {
                console.error('No message ID found for this button');
            }
        });
    });
});

function deleteMessage(target, id) {
    console.log('Attempting to delete message with ID:', id);
    fetch('/deleteMessage', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message_id: id })
    })
    .then(response => {
        console.log('Response status:', response.status); 
        if (!response.ok) {
            throw response;
        }
        return response.json();
    })
    .then(data => {
        if (target) {
            target.closest('li').remove();
        }
    })
    .catch(error => {
        console.error('Error deleting message:', error);
    });
}


document.addEventListener('DOMContentLoaded', function() {
    const queryButton = document.querySelector('#username_input +button');
    if (queryButton) {
        queryButton.addEventListener('click', queryMember);
    } else {
        console.error('Query button not found');
    }
});


function queryMember() {
    const username = document.querySelector('#username_input').value;
    fetch(`/api/member?username=${username}`)
    .then(response => response.json())
    .then(data => {
        if (data.data === null) {
            document.querySelector('#member_info').textContent = 'No Data';
       } else {
            document.querySelector('#member_info').textContent = `${data.data.name}(${data.data.username})`;
       }
    });
}
