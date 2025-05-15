  const email = localStorage.getItem("userEmail");
  const userSpan = document.getElementById("user-name");

  if (email) {
    userSpan.textContent = email;
  } else {
    userSpan.textContent = "Visitante";
  }

  document.addEventListener("DOMContentLoaded", function () {
    const authButton = document.getElementById("auth-button");
    const email = localStorage.getItem("userEmail");
  
    console.log("Email do localStorage:", email); 
  
    if (email && email !== "") {
      authButton.textContent = "Sair";
      authButton.classList.add("logout");
      authButton.classList.remove("login");
      authButton.onclick = function () {
        localStorage.removeItem("userEmail");
        window.location.href = "../pages/index.html"; 
      };
    } else {
      authButton.textContent = "Entrar";
      authButton.classList.add("login");
      authButton.classList.remove("logout");
      authButton.onclick = function () {
        window.location.href = "../pages/login.html"; 
      };
    }
  });
  