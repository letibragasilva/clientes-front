console.log("JavaScript carregado!");

function validarFormulario() {
    const nome = document.getElementById("nome").value;
    const email = document.getElementById("email").value;
    const telefone = document.getElementById("telefone").value;
    const nome = document.getElementById("nome").value;

    if (nome.length < 3) {
        alert("Nome precisa ter pelo menos 3 caracteres");
        return false;
    }

    return true;
}