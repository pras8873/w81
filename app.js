document.addEventListener("DOMContentLoaded", () => {

    // --- 1. Navigation Logic (Single Page App approach) ---
    const navLinks = document.querySelectorAll('.nav-links a');
    const sections = document.querySelectorAll('.section');

    // Make navigateTo available globally for inline onclick buttons
    window.navigateTo = function(targetId) {
        // Remove active class from all sections & links
        sections.forEach(sec => sec.classList.remove('active'));
        navLinks.forEach(link => link.classList.remove('active'));

        // Add active class to target section
        const targetSection = document.getElementById(targetId);
        if(targetSection) targetSection.classList.add('active');

        // Update Nav visual state
        const activeLink = document.querySelector(`.nav-links a[data-target="${targetId}"]`);
        if(activeLink) activeLink.classList.add('active');

        // Scroll to top
        window.scrollTo({ top: 0, behavior: 'smooth' });
    };

    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const target = link.getAttribute('data-target');
            navigateTo(target);
        });
    });

    // --- 2. Creative Section (Poems / Blogs Toggle) ---
    const toggleBtns = document.querySelectorAll('.toggle-btn');
    const iframe = document.getElementById('content-frame');
    const externalLink = document.getElementById('external-link');

    // Define the URLs for your subdomains
    const creativeUrls = {
        poems: "https://poems.prashu.dev",
        blogs: "https://blogs.prashu.dev" // Update this if your blog URL is different
    };

    toggleBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Update active button styling
            toggleBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            // Switch iframe source
            const frameType = btn.getAttribute('data-frame');
            const newUrl = creativeUrls[frameType];

            iframe.src = newUrl;
            externalLink.href = newUrl;
        });
    });

    // --- 3. Contact Form Submission Simulation ---
    const contactForm = document.getElementById('contact-form');
    const formStatus = document.getElementById('form-status');

    contactForm.addEventListener('submit', (e) => {
        e.preventDefault();

        // Change button text temporarily
        const submitBtn = contactForm.querySelector('button');
        const originalText = submitBtn.innerText;
        submitBtn.innerText = "Sending...";

        // Simulate network request
        setTimeout(() => {
            submitBtn.innerText = originalText;
            formStatus.style.color = "var(--accent-color)";
            formStatus.innerText = "Message sent successfully! I'll get back to you soon.";
            contactForm.reset();

            // Clear message after 4 seconds
            setTimeout(() => formStatus.innerText = "", 4000);
        }, 1500);
    });

    // --- 4. Privacy Policy Modal ---
    const privacyLink = document.getElementById('privacy-link');
    const privacyModal = document.getElementById('privacy-modal');
    const closeModal = document.querySelector('.close-modal');

    privacyLink.addEventListener('click', (e) => {
        e.preventDefault();
        privacyModal.classList.add('show');
    });

    closeModal.addEventListener('click', () => {
        privacyModal.classList.remove('show');
    });

    // Close modal if user clicks outside the content box
    window.addEventListener('click', (e) => {
        if (e.target === privacyModal) {
            privacyModal.classList.remove('show');
        }
    });
});