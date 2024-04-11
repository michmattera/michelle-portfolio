import emailjs from '@emailjs/browser';

// main js
document.addEventListener('DOMContentLoaded', function () {
    var options = {
        strings: ["I'm a Full-Stack Developer", 'I Build Websites', "I'm a Back-end Developer", 'I am a data analyst', "I'm a Front-end Developer"],
        typeSpeed: 120,
        backSpeed: 50,
        backDelay: 1500,
        loop: true
    };

    var typed = new Typed('#headline', options);
});




document.addEventListener("DOMContentLoaded", function () {
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


//test
(function () {
    emailjs.init("service_mb7svba");
})();
// document.getElementById('contact-form').addEventListener('submit', function (event) {
//     event.preventDefault();
//     emailjs.sendForm('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', this)
//         .then(function (response) {
//             console.log('Email sent!', response.status, response.text);
//             alert('Email sent successfully!');
//         }, function (error) {
//             console.error('Error sending email:', error);
//             alert('Oops! Something went wrong.');
//         });
// });

// document.getElementById('contact-form').addEventListener('submit', function (event) {
//     event.preventDefault(); // Prevent the form from submitting by default

//     // Get the user's inputs
//     const name = document.getElementById('name').value;
//     const email = document.getElementById('email').value;
//     const subject = document.getElementById('subject').value;
//     const message = document.getElementById('message').value;

//     // Send the email using EmailJS
//     emailjs.send("service_mb7svba", "template_lhd31t3", {
//         from_name: name,
//         reply_to: email,
//         subject: subject,
//         message_html: message
//     }).then(function (response) {
//         console.log("Email sent successfully:", response);
//         // Optionally, display a success message to the user
//     }, function (error) {
//         console.error("Email sending failed:", error);
//         // Optionally, display an error message to the user
//     });
// });

function sendEmail() {
    // Get input values
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var subject = document.getElementById('subject').value;
    var message = document.getElementById('message').value;

    // Send email using EmailJS
    emailjs.send("service_mb7svba", "template_lhd31t3", {
        from_name: name,
        email: email,
        subject: subject,
        message: message
    }).then(function(response) {
        console.log("Email sent successfully:", response);
        // Optionally, display a success message to the user
    }, function(error) {
        console.error("Email sending failed:", error);
        // Optionally, display an error message to the user
    });
}
