// JavaScript code to handle modal functionality

    // Get the modal element
    var modal = document.getElementById("addModal");
    // var editModal = document.getElementById("editModal");

    // Get the button that opens the modal
    var addButton = document.querySelector(".add-button");
    // var editButtons = document.querySelectorAll(".edit-button");

    // Get the <span> element that closes the modal
    var closeBtn = document.querySelector(".close");

    // When the user clicks the button, open the modal
    addButton.onclick = function() {
        modal.style.display = "block";
    }
    
    // editButtons.forEach(function(button) {
    //     button.onclick = function() {
    //         var row = button.parentNode.parentNode;
    //         var accountNumber = row.cells[0].textContent;
    //         var description = row.cells[1].textContent;
            
    //         // Populate the form fields with existing data
    //         var editForm = document.getElementById("editForm");
    //         console.log(editForm)
    //         editForm.elements["AccountNumber"].value = accountNumber;
    //         editForm.elements["Description"].value = description;
            
    //         editModal.style.display = "block";
    //     };
    // });

    // When the user clicks on <span> (x), close the modal
    // closeBtn.onclick = function() {
    //     modal.style.display = "none";
    //     editModal.style.display = "none";
    // }

    // When the user clicks anywhere outside of the modal, close it
    // window.onclick = function(event) {
    //     if (event.target == modal) {
    //         modal.style.display = "none";
    //     }
    //     if (event.target == editModal) {
    //         modal.style.display = "none";
    //     }
    // }

    // window.onclick = function(event) {
    //     if (event.target == editModal) {
    //         editModal.style.display = "none";
    //     }
    // }    