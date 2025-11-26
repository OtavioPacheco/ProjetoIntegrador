document.addEventListener("DOMContentLoaded", () => {

    const form = document.getElementById("form-login");
    const button = document.getElementById("button");

    form.addEventListener("submit", async (event) => {
        event.preventDefault();

        const email = document.getElementById("email").value.trim();
        const senha = document.getElementById("password").value.trim();
        const urlHome = button.dataset.urlHome;  // pega rota da home

        if (!email || !senha) {
            alert("Preencha todos os campos.");
            return;
        }

        try {
            const resposta = await fetch("/usuario/login", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ email, senha })
            });

            const data = await resposta.json();

            if (resposta.status === 200) {
                alert("Login realizado com sucesso!");
                window.location.href = urlHome;
            } else {
                alert(data.erro || "Email ou senha incorretos.");
            }

        } catch (error) {
            console.error("Erro no login:", error);
            alert("Erro ao conectar com o servidor.");
        }
    });
});
