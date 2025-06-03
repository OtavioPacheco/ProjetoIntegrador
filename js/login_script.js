//--------------------------------------------------------------------------------------------------\\
//Para funcionar é necessário que use em local server, o navegador nao suporta a estrutura de pastas
//--------------------------------------------------------------------------------------------------\\

//Comandos para subir em local server
//cd local_do_projeto
//python -m http.server
//é necessário que python esteja instalado

document.addEventListener("DOMContentLoaded", function () {
    const button = document.getElementById("button");
  
    button.addEventListener("click", function () {
      const email = document.getElementById("email").value.trim();
      const password = document.getElementById("password").value.trim();
  
      if (email && password) {
        localStorage.setItem("userEmail", email);
  
        window.location.href = "../pages/index.html"; 
      } else {
        alert("Por favor, preencha o e-mail e a senha.");
      }
    });
  });
  