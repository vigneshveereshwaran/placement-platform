// ================================
// Placement Portal Main JS
// ================================

console.log("Placement Portal Loaded Successfully");

// ================================
// Sidebar Active Link
// ================================

const sidebarLinks = document.querySelectorAll(".sidebar a");

sidebarLinks.forEach(link => {

    link.addEventListener("click", function () {

        sidebarLinks.forEach(nav => {
            nav.classList.remove("active");
        });

        this.classList.add("active");

    });

});

// ================================
// Notification Auto Close
// ================================

const notifications = document.querySelectorAll(".notification-box");

notifications.forEach(notification => {

    notification.addEventListener("click", () => {

        notification.style.opacity = "0";

        setTimeout(() => {
            notification.style.display = "none";
        }, 300);

    });

});

// ================================
// Form Validation
// ================================

const forms = document.querySelectorAll("form");

forms.forEach(form => {

    form.addEventListener("submit", function (e) {

        const inputs = form.querySelectorAll("input");

        let isValid = true;

        inputs.forEach(input => {

            if (input.value.trim() === "") {

                isValid = false;

                input.style.border = "2px solid red";

            } else {

                input.style.border = "2px solid #00d4c7";

            }

        });

        if (!isValid) {

            e.preventDefault();

            alert("Please fill all fields!");

        }

    });

});

// ================================
// Dashboard Counter Animation
// ================================

const counters = document.querySelectorAll(".counter");

counters.forEach(counter => {

    counter.innerText = "0";

    const updateCounter = () => {

        const target = +counter.getAttribute("data-target");

        const current = +counter.innerText;

        const increment = target / 50;

        if (current < target) {

            counter.innerText = `${Math.ceil(current + increment)}`;

            setTimeout(updateCounter, 30);

        } else {

            counter.innerText = target;

        }

    };

    updateCounter();

});

// ================================
// Search Filter for Tables
// ================================

const searchInput = document.querySelector("#searchInput");

if (searchInput) {

    searchInput.addEventListener("keyup", function () {

        const filter = searchInput.value.toLowerCase();

        const rows = document.querySelectorAll(".company-table tr");

        rows.forEach((row, index) => {

            if (index === 0) return;

            const text = row.innerText.toLowerCase();

            row.style.display = text.includes(filter)
                ? ""
                : "none";

        });

    });

}

// ================================
// Dark Glow Hover Effect
// ================================

const cards = document.querySelectorAll(".page-card, .dashboard-card");

cards.forEach(card => {

    card.addEventListener("mouseenter", () => {

        card.style.boxShadow = "0 0 25px rgba(0,212,199,0.5)";

    });

    card.addEventListener("mouseleave", () => {

        card.style.boxShadow = "0 0 20px rgba(0,0,0,0.3)";

    });

});

// ================================
// Welcome Message
// ================================

window.addEventListener("load", () => {

    console.log("Welcome to Placement Portal");

});
