document.addEventListener('DOMContentLoaded', function() {
    const notifications = document.querySelectorAll('.notification');

    notifications.forEach(notification => {
        // Изначально скрываем уведомление
        notification.style.transform = `translateY(-${notification.offsetHeight + 20}px)`;

        // Показываем уведомление
        setTimeout(() => {
            notification.classList.add('show');
        }, 100); // Небольшая задержка для анимации

        // Скрываем уведомление через 5 секунд (или другое время)
        setTimeout(() => {
            notification.classList.remove('show');
        }, 5000);

        // Добавляем обработчик клика для скрытия уведомления
        notification.addEventListener('click', () => {
            notification.classList.remove('show');
        });
    });
});