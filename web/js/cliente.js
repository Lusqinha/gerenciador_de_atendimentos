async function cadastrarCliente() {
    const cli_nome = document.getElementById("cli_name").value;
    const cli_celular = document.getElementById("cli_celular").value;
    const cli_email = document.getElementById("cli_email").value;
    const cli_acesso = document.getElementById("cli_acesso").value;
    const cli_sistema = document.getElementById("cli_sistema").value;
    console.log(cli_nome, cli_celular, cli_email, cli_acesso, cli_sistema)
    const resultado = await eel.cli_create(cli_nome, cli_celular, cli_email, cli_acesso, cli_sistema)();
    alert(resultado)
    return resultado;
}

async function listarClientes() {
    const resultado = await eel.cli_read_all()();

    return resultado;
}

async function buscarCliente() {
    const cli_nome = document.getElementById("cli_nome").value;
    const resultado = await eel.cli_search(cli_id)();

    return resultado;
}

async function atualizarCliente() {
    const cli_id = document.getElementById("cli_id").value;
    const cli_nome = document.getElementById("cli_nome").value;
    const cli_celular = document.getElementById("cli_celular").value;
    const cli_email = document.getElementById("cli_email").value;
    const cli_acesso = document.getElementById("cli_acesso").value;
    const cli_sistema = document.getElementById("cli_sistema").value;
    const resultado = await eel.cli_update(cli_id, cli_nome, cli_celular, cli_email, cli_acesso, cli_sistema)();

    return resultado;
}

async function deletarCliente() {
    const cli_id = document.getElementById("cli_id").value;
    const resultado = await eel.cli_delete(cli_id)();

    return resultado;
}


function read_list_cliente() {
    var x = listarClientes().then(function (result) {
        alert(result)
    });
}

read_list_cliente()