document.addEventListener("DOMContentLoaded", function () {
    let typewriterText = document.getElementById("typewriter");
    let text = "Explore!!";
    let index = 0;

    function type() {
        if (index < text.length) {
            typewriterText.innerHTML += text.charAt(index);
            index++;
            setTimeout(type, 200); // Adjust the typing speed here
        } else {
            setTimeout(erase, 2000); // Wait before starting to erase
        }
    }

    function erase() {
        if (index > 0) {
            typewriterText.innerHTML = text.substring(0, index - 1);
            index--;
            setTimeout(erase, 100); // Adjust the erasing speed here
        } else {
            setTimeout(type, 200); // Wait before starting to type again
        }
    }

    type();
});
