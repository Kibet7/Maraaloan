document.addEventListener('DOMContentLoaded', () => {
    const toggleNavigation = document.getElementById('toggleNavigation');
    const navigation = document.getElementById('navigation');
    const navButtons = document.querySelectorAll('.nav-link');
    const contentSections = document.querySelectorAll('.content-section');

    // Toggle navigation visibility
    toggleNavigation.addEventListener('click', () => {
        navigation.classList.toggle('active');
    });

    // Show single section and hide others
    navButtons.forEach((button) => {
        button.addEventListener('click', () => {
            const targetId = button.getAttribute('data-target');
            contentSections.forEach((section) => {
                if (section.id === targetId) {
                    section.classList.remove('d-none');
                } else {
                    section.classList.add('d-none');
                }
            });
            // Hide navigation after selection (for mobile)
            if (window.innerWidth < 768) {
                navigation.classList.remove('active');
            }
        });
    });
});
