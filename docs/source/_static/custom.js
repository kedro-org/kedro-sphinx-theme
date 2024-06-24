document.addEventListener('DOMContentLoaded', function() {
    // Select all navigation links within the .wy-main-nav container
    var navLinks = document.querySelectorAll('.wy-main-nav .wy-main-nav-link');

    // Function to remove 'active' class from all links
    function removeActiveClass() {
        navLinks.forEach(function(link) {
            link.classList.remove('active');
        });
    }

    // Add click event listener to each link
    navLinks.forEach(function(link) {
        link.addEventListener('click', function(event) {
            // Prevent the default link action
            event.preventDefault();

            // Remove 'active' class from all links
            removeActiveClass();

            // Add 'active' class to the clicked link
            event.target.classList.add('active');
        });
    });
});