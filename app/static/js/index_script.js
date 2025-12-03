document.addEventListener("DOMContentLoaded", function () {
  const email = localStorage.getItem("userEmail");
  const userSpan = document.getElementById("user-name");
  const authButton = document.getElementById("auth-button");

  const URL_HOME = authButton.dataset.urlHome;
  const URL_LOGIN = authButton.dataset.urlLogin;

  // Mostra nome do usuário ou "Visitante"
  userSpan.textContent = email ? email : "Visitante";

  console.log("Email do localStorage:", email);

  if (email && email !== "") {
    authButton.textContent = "Sair";
    authButton.classList.add("logout");
    authButton.classList.remove("login");

    authButton.onclick = function () {
      localStorage.removeItem("userEmail");
      window.location.href = URL_HOME;
    };
  } else {
    authButton.textContent = "Entrar";
    authButton.classList.add("login");
    authButton.classList.remove("logout");

    authButton.onclick = function () {
      window.location.href = URL_LOGIN;
    };
  }
});
