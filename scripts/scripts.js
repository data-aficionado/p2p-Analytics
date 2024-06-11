document.addEventListener('DOMContentLoaded', function () {
    const typewriter = document.getElementById('typewriter');
    let i = 0;
    const text = 'Explore!!';

    function typeEffect() {
        if (i < text.length) {
            typewriter.innerHTML += text.charAt(i);
            i++;
            setTimeout(typeEffect, 200);
        } else {
            setTimeout(() => {
                typewriter.innerHTML = '';
                i = 0;
                typeEffect();
            }, 1000);
        }
    }

    typeEffect();
});
