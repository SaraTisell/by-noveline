
// Function to set copyright information
function setCopyrightInfo() {
    let currentYear = new Date().getFullYear();
    let copyrightInfo = document.getElementById("copyright");
    
    copyrightInfo.innerHTML= "© " + currentYear + " All Rights Reserved | By Noveline";
    // Add class for CSS purpose
    copyrightInfo.classList.add("copyright-text");
}

// Call function to set copyright information
setCopyrightInfo();
