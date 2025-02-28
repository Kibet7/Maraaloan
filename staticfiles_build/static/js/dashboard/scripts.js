document.addEventListener("DOMContentLoaded", function () {
    const homeIcon = document.getElementById("homeIcon");
    const toggleNavigation = document.getElementById("toggleNavigation");
    const navigation = document.getElementById("navigation");
    const navLinks = document.querySelectorAll(".custom-nav-link");

    // Toggle navigation visibility on Home Icon or button click
    const toggleNav = () => navigation.classList.toggle("active");
    homeIcon.addEventListener("click", toggleNav);
    toggleNavigation.addEventListener("click", toggleNav);

    // Collapse navigation on link click
    navLinks.forEach((link) => {
        link.addEventListener("click", function () {
            if (window.innerWidth <= 768) {
                navigation.classList.remove("active");
            }
            // Show the selected section
            document.querySelectorAll(".content-section").forEach((section) => section.classList.add("d-none"));
            const target = document.getElementById(this.getAttribute("data-target"));
            if (target) target.classList.remove("d-none");
        });
    });
});


const slides = document.querySelectorAll(".slide");
const prevBtn = document.querySelector(".prev-btn");
const nextBtn = document.querySelector(".next-btn");
let currentIndex = 0;

function updateSlides() {
    slides.forEach((slide, index) => {
        slide.style.transform = `translateX(${(index - currentIndex) * 100}%)`;
    });
}

prevBtn.addEventListener("click", () => {
    currentIndex = (currentIndex - 1 + slides.length) % slides.length;
    updateSlides();
});

nextBtn.addEventListener("click", () => {
    currentIndex = (currentIndex + 1) % slides.length;
    updateSlides();
});

updateSlides();



document.querySelector('.application-form').addEventListener('submit', function (e) {
    // Add custom validation logic if needed
    // For example, check if all fields are filled out
});





 document.getElementById('next-btn-1').addEventListener('click', function() {
        document.getElementById('borrower-section').style.display = 'none';
        document.getElementById('guarantor1-section').style.display = 'block';
    });

    document.getElementById('next-btn-2').addEventListener('click', function() {
        document.getElementById('guarantor1-section').style.display = 'none';
        document.getElementById('guarantor2-section').style.display = 'block';
        document.getElementById('submit-btn').disabled = false;
    });

    document.getElementById('loan-application-form').addEventListener('input', function() {
        let isFormValid = true;
        const inputs = document.querySelectorAll('input[required], select[required]');
        inputs.forEach(function(input) {
            if (!input.value) {
                isFormValid = false;
            }
        });
        document.getElementById('submit-btn').disabled = !isFormValid;
    });