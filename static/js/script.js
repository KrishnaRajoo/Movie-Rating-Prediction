const form = document.querySelector("form");
const button = document.querySelector("button");

if (form) {

    form.addEventListener("submit", function () {

        button.disabled = true;

        button.innerHTML = `
            <span class="loader"></span>
            Predicting...
        `;

    });

}

// Fade animation when page loads
window.addEventListener("load", () => {

    document.body.style.opacity = "1";

});

// Input focus animation
const inputs = document.querySelectorAll("input");

inputs.forEach(input => {

    input.addEventListener("focus", () => {

        input.parentElement.style.transform = "translateY(-3px)";

    });

    input.addEventListener("blur", () => {

        input.parentElement.style.transform = "translateY(0px)";

    });

});
for(let i=0;i<25;i++){

    const star=document.createElement("div");

    star.className="particle";

    star.style.left=Math.random()*100+"vw";

    star.style.top=Math.random()*100+"vh";

    star.style.animationDelay=Math.random()*5+"s";

    document.body.appendChild(star);

}
