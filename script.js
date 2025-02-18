document.addEventListener("DOMContentLoaded", function () {
    if (document.getElementById("productDisplay")) {
        loadFeaturedProducts();
    }
    if (document.getElementById("shopItems")) {
        loadShopItems();
    }
    if (document.getElementById("cartItems")) {
        loadCartItems();
    }
    if (document.getElementById("wishlistItems")) {
        loadWishlistItems();
    }
});

let cart = JSON.parse(localStorage.getItem("cart")) || [];
let products = [
    { id: 1, name: "Stylish Jacket", price: 1200, category: "Men" },
    { id: 2, name: "Elegant Dress", price: 1500, category: "Women" },
    { id: 3, name: "Casual Sneakers", price: 2000, category: "Shoes" },
    { id: 4, name: "Denim Jeans", price: 1800, category: "Men" },
    { id: 5, name: "Silk Saree", price: 2500, category: "Women" },
    { id: 6, name: "Running Shoes", price: 3000, category: "Shoes" }
];

function loadFooter() {
    document.body.insertAdjacentHTML("beforeend", `
        <footer style="position: fixed; bottom: 0; width: 100%; background: #333; color: white; text-align: center; padding: 10px;">
            <p>&copy; 2025 Fashion E-commerce. All rights reserved.</p>
            <nav>
                <ul style="list-style: none; padding: 0; display: flex; justify-content: center; gap: 15px;">
                    <li><a href="#home" onclick="navigateTo('home')" style="color: white; text-decoration: none;">Home</a></li>
                    <li><a href="#shop" onclick="navigateTo('shop')" style="color: white; text-decoration: none;">Shop</a></li>
                    <li><a href="#cart" onclick="navigateTo('cart')" style="color: white; text-decoration: none;">Cart</a></li>
                    <li><a href="#wishlist" onclick="navigateTo('wishlist')" style="color: white; text-decoration: none;">Wishlist</a></li>
                </ul>
            </nav>
        </footer>
    `);
}

document.addEventListener("DOMContentLoaded", loadFooter);

function loadFeaturedProducts() {
    displayProducts("productDisplay", products.slice(0, 3));
}

function loadShopItems() {
    displayProducts("shopItems", products);
}

function loadCartItems() {
    const cartContainer = document.getElementById("cartItems");
    cartContainer.innerHTML = "";
    if (cart.length === 0) {
        cartContainer.innerHTML = "Your cart is empty.";
    } else {
        cart.forEach((item, index) => {
            const itemDiv = document.createElement("div");
            itemDiv.classList.add("cart-item");
            itemDiv.innerHTML = `<h3>${item.name}</h3><p>Price: ₹${item.price}</p>
                                 <button onclick="removeFromCart(${index})">Remove</button>`;
            cartContainer.appendChild(itemDiv);
        });
    }
}

function loadWishlistItems() {
    document.getElementById("wishlistItems").innerHTML = "Your wishlist is empty.";
}

function displayProducts(containerId, productList) {
    const container = document.getElementById(containerId);
    container.innerHTML = "";
    productList.forEach(product => {
        const productDiv = document.createElement("div");
        productDiv.classList.add("product");
        productDiv.innerHTML = `<h3>${product.name}</h3><p>Price: ₹${product.price}</p><p>Category: ${product.category}</p>
                                <button onclick="addToCart(${product.id}, '${product.name}', ${product.price})">Add to Cart</button>`;
        container.appendChild(productDiv);
    });
}

function addToCart(id, name, price) {
    const item = cart.find(product => product.id === id);
    if (!item) {
        cart.push({ id, name, price });
    }
    localStorage.setItem("cart", JSON.stringify(cart));
    alert(`${name} added to cart!`);
    updateCartCount();
    loadCartItems();
}

function removeFromCart(index) {
    cart.splice(index, 1);
    localStorage.setItem("cart", JSON.stringify(cart));
    loadCartItems();
    updateCartCount();
}

function updateCartCount() {
    document.getElementById("cartCount").textContent = cart.length;
}

function searchProducts() {
    const query = document.getElementById("searchInput").value.toLowerCase();
    const searchResults = document.getElementById("shopItems");
    const filteredProducts = products.filter(product => product.name.toLowerCase().includes(query));
    
    if (filteredProducts.length > 0) {
        displayProducts("shopItems", filteredProducts);
    } else {
        searchResults.innerHTML = "<p>Product not found.</p>";
    }
}

function navigateTo(pageId) {
    document.querySelectorAll(".page").forEach(page => page.style.display = "none");
    document.getElementById(pageId).style.display = "block";
}
