document.addEventListener("DOMContentLoaded", function() {
    const checkboxes = document.querySelectorAll(".form-check-input");
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener("change", filterProducts);
    });

    document.querySelectorAll(".add-to-cart").forEach(button => {
        button.addEventListener("click", function() {
            const productId = this.getAttribute("data-id");
            addToCart(productId);
        });
    });
});

function filterProducts() {
    const selectedCategories = Array.from(document.querySelectorAll(".form-check-input:checked"))
        .map(input => input.id);
    
    document.querySelectorAll(".product-card").forEach(card => {
        const category = card.getAttribute("data-category");
        card.style.display = selectedCategories.includes(category) ? "block" : "none";
    });
}

function addToCart(productId) {
    let cart = JSON.parse(localStorage.getItem("cart")) || [];
    cart.push(productId);
    localStorage.setItem("cart", JSON.stringify(cart));
    alert("Product added to cart!");
}
