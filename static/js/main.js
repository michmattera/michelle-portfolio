// main js
document.addEventListener('DOMContentLoaded', function() {
    var options = {
        strings: ["I'm a Full-Stack Developer", 'I Build Websites', "I'm a Back-end Developer", 'I am a data analyst', "I'm a Front-end Developer"],
        typeSpeed: 120,
        backSpeed: 50,
        backDelay: 1500,
        loop: true
    };

    var typed = new Typed('#headline', options);
});




document.addEventListener("DOMContentLoaded", function() {
    const images = document.querySelectorAll('.enter-animation');

    function checkPosition() {
        images.forEach(image => {
            const windowHeight = window.innerHeight;
            const triggerBottom = image.getBoundingClientRect().top + (image.clientHeight / 2);

            if (triggerBottom < windowHeight) {
                image.classList.add('visible');
            }
        });
    }

    checkPosition();
    window.addEventListener('scroll', checkPosition);
});


