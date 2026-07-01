// Wait until the page is fully loaded
document.addEventListener("DOMContentLoaded", () => {

    // Get the Generate button
    const button = document.getElementById("runBtn");

    // Check if the button exists
    if (!button) {
        console.error("Error: Button with id 'runBtn' was not found.");
        return;
    }

    // Add click event
    button.addEventListener("click", () => {

        // Disable button temporarily
        button.disabled = true;

        // Change button text
        button.textContent = "🎨 Generating...";

        // Simulate loading
        setTimeout(() => {

            // Change button appearance
            button.textContent = "✅ Artwork Generated!";
            button.style.backgroundColor = "#6BCB77";

            // Show information
            alert(
`🎨 Hirst Dot Portrait Generator

This project recreates Damien Hirst-inspired dot paintings using Python Turtle Graphics.

✨ Features:
• Randomly generated colorful dot artwork
• RGB colors extracted using Colorgram
• Built with Python Turtle
• Uses loops, functions, randomness, and coordinate positioning

⚠️ Note:
This website is a showcase of the project.
To generate the actual artwork, run the Python (.py) file in PyCharm or any Python IDE.`
            );

        }, 1000);

    });

});
