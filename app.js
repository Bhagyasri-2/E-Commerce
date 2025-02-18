// // Smooth scroll function
// function smoothScroll(target) {
//     const element = document.querySelector(target);
//     if (element) {
//         element.scrollIntoView({
//             behavior: 'smooth',
//             block: 'start'
//         });
//     }
// }

// // Add click event to shop button
// document.addEventListener('DOMContentLoaded', function() {
//     const shopButton = document.querySelector('.shop-btn');
    
//     if (shopButton) {
//         shopButton.addEventListener('click', function(e) {
//             e.preventDefault();
//             smoothScroll('#category-section');
//         });
//     }
// });

// // Smooth scroll to category section
// document.addEventListener('DOMContentLoaded', function() {
//     const shopButton = document.querySelector('.shop-btn');
//     const categorySection = document.getElementById('category-section');

//     if (shopButton && categorySection) {
//         shopButton.addEventListener('click', function(e) {
//             e.preventDefault();
            
//             // Calculate the position to scroll to
//             const offset = categorySection.offsetTop - 80; // Adjust 80px for header height
//             window.scrollTo({
//                 top: offset,
//                 behavior: 'smooth'
//             });
//         });
//     }
// });