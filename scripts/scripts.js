document.addEventListener('DOMContentLoaded', function () {
    const typewriter = document.getElementById('typewriter');
    let text = "Explore!!";
    let index = 0;
    function type() {
        typewriter.textContent = text.slice(0, index);
        index++;
        if (index > text.length) {
            index = 0;
        }
    }
    setInterval(type, 300);
});
