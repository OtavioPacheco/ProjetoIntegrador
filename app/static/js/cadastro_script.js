document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("form-cadastro");

  form.addEventListener("submit", async (event) => {
    event.preventDefault(); // impede o refresh da página

    const nome = document.getElementById("nome").value.trim();
    const email = document.getElementById("email").value.trim();
    const senha = document.getElementById("senha").value.trim();

    if (!nome || !email || !senha) {
      alert("Preencha todos os campos.");
      return;
    }

    try {
      const resposta = await fetch("/usuario/cadastrar", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ nome, email, senha })
      });

      const data = await resposta.json();

      if (resposta.status === 201) {
        alert("Cadastro realizado com sucesso!");
        window.location.href = "/login"; // redireciona para login
      } else {
        alert(data.erro || "Erro ao cadastrar.");
      }

    } catch (erro) {
      console.error("Erro ao chamar o controller:", erro);
      alert("Erro de comunicação com o servidor.");
    }
  })})