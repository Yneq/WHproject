document.addEventListener('DOMContentLoaded', function() {
    const deleteButtons = document.querySelectorAll('.delete_btn');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function() {
            const messageId = this.getAttribute('data-id');
            console.log('Delete button clicked, message ID:', messageId);  // 确认ID是否正确获取
            if (messageId) {
                deleteMessage(this, messageId);
            } else {
                console.error('No message ID found for this button');
            }
        });
    });
});

function deleteMessage(target, id) {
    console.log('Attempting to delete message with ID:', id); // 确认函数被调用和ID传递
    fetch('/deleteMessage', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message_id: id })
    })
    .then(response => {
        console.log('Response status:', response.status); // 输出响应状态
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
