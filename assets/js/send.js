document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('service-request');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const formData = new FormData(form);

        // Преобразуем FormData в обычный объект
        const data = {};
        formData.forEach((value, key) => {
            data[key] = value;
        });

        axios.post('https://khnz.tech/api/service-request', data)
            .then(response => {
                console.log('Success:', response.data);
                alert('Ваше сообщение было успешно отправлено');
                form.reset();
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Произошла ошибка при отправке сообщения. Попробуйте еще раз.');
            });
    });
});
