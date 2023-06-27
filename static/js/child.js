// JavaScript code to handle modal functionality

    // Get the modal element
    var modal = document.getElementById("addModal");

    // Get the button that opens the modal
    var addButton = document.querySelector(".add-button");

    // Get the <span> element that closes the modal
    var closeBtn = document.querySelector(".close");

    // When the user clicks the button, open the modal
    addButton.onclick = function() {
        modal.style.display = "block";
    }

    // When the user clicks on <span> (x), close the modal
    closeBtn.onclick = function() {
        modal.style.display = "none";
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }