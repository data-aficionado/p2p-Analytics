document.addEventListener('DOMContentLoaded', (event) => {
    const exploreButton = document.querySelector('.explore-button');
    if (exploreButton) {
        exploreButton.addEventListener('mouseover', () => {
            exploreButton.style.color = 'white';
            exploreButton.style.backgroundColor = '#34495e';
        });
        exploreButton.addEventListener('mouseout', () => {
            exploreButton.style.color = '#2c3e50';
            exploreButton.style.backgroundColor = '#f4f4f4';
        });
    }
});
