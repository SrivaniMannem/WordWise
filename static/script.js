// WordWise starter script: small interaction confirmation.
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".save-btn").forEach((button) => {
    button.addEventListener("click", () => {
      button.textContent = "Updating...";
    });
  });
});
