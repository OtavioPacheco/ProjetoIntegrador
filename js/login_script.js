document.addEventListener("DOMContentLoaded", function () {
    const button = document.getElementById("button");
  
    button.addEventListener("click", function () {
      const email = document.getElementById("email").value.trim();
      const password = document.getElementById("password").value.trim();
  
      if (email && password) {
        // 1. Salva o e-mail no localStorage
        localStorage.setItem("userEmail", email);
  
        // 2. Redireciona para a página principal
        window.location.href = "../pages/index.html"; // ajuste o caminho se necessário
      } else {
        alert("Por favor, preencha o e-mail e a senha.");
      }
    });
  });
  