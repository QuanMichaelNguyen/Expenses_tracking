document.addEventListener("DOMContentLoaded", function() {
    // Get references to the buttons
    var addExpenseBtn = document.getElementById("addExpenseBtn");
    var modifyExpenseBtn = document.getElementById("modifyExpenseBtn");
    var deleteExpenseBtn = document.getElementById("deleteExpenseBtn");

    // Add click event listeners to the buttons
    addExpenseBtn.addEventListener("click", function() {
        // Code to execute when "Add Expense" button is clicked
        alert("Add Expense button clicked!");
    });

    modifyExpenseBtn.addEventListener("click", function() {
        // Code to execute when "Modify Expense" button is clicked
        alert("Modify Expense button clicked!");
    });

    deleteExpenseBtn.addEventListener("click", function() {
        // Code to execute when "Delete Expense" button is clicked
        alert("Delete Expense button clicked!");
    });
});