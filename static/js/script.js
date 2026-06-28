// ===============================
// DOM Elements
// ===============================

const form = document.getElementById("profileForm");

const nameInput = document.getElementById("name");
const ageInput = document.getElementById("age");
const occupationInput = document.getElementById("occupation");
const locationInput = document.getElementById("location");
const emailInput = document.getElementById("email");
const imageInput = document.getElementById("image_url");
const bioInput = document.getElementById("bio");

const previewName = document.getElementById("previewName");
const previewAge = document.getElementById("previewAge");
const previewOccupation = document.getElementById("previewOccupation");
const previewLocation = document.getElementById("previewLocation");
const previewEmail = document.getElementById("previewEmail");
const previewImage = document.getElementById("previewImage");
const previewBio = document.getElementById("previewBio");

const charCount = document.getElementById("charCount");

// Placeholder Image

const defaultImage =
    "https://placehold.co/150x150";

// ===============================
// Character Counter
// ===============================

bioInput.addEventListener("input", () => {

    charCount.textContent =
        `${bioInput.value.length} / 200`;

});

// ===============================
// Live Name Preview
// ===============================

nameInput.addEventListener("input", () => {

    previewName.textContent =
        nameInput.value.trim() || "Your Name";

});

// ===============================
// Live Age Preview
// ===============================

ageInput.addEventListener("input", () => {

    previewAge.textContent =
        ageInput.value
        ? `Age: ${ageInput.value}`
        : "Age: --";

});

// ===============================
// Live Occupation Preview
// ===============================

occupationInput.addEventListener("input", () => {

    previewOccupation.textContent =
        occupationInput.value.trim() || "Occupation";

});

// ===============================
// Live Location Preview
// ===============================

locationInput.addEventListener("input", () => {

    previewLocation.textContent =
        locationInput.value.trim() || "Location";

});

// ===============================
// Live Email Preview
// ===============================

emailInput.addEventListener("input", () => {

    previewEmail.textContent =
        emailInput.value.trim() || "example@email.com";

});

// ===============================
// Live Bio Preview
// ===============================

bioInput.addEventListener("input", () => {

    previewBio.textContent =
        bioInput.value.trim() ||
        "Your bio will appear here after entering the details.";

});

// ===============================
// Live Image Preview
// ===============================

imageInput.addEventListener("input", () => {

    const imageURL = imageInput.value.trim();

    if (imageURL === "") {
        previewImage.src = defaultImage;
        return;
    }

    previewImage.src = imageURL;

});

// ===============================
// Image Error Fallback
// ===============================

previewImage.onerror = function () {

    previewImage.src = defaultImage;

};


// ===============================
// Autofocus
// ===============================

window.addEventListener("load", () => {

    nameInput.focus();

});

