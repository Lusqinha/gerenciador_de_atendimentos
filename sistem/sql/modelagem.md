# Banco de dados - Organização de Tabelas


## Categoria
| cat_id | cat_nome |
| :--- | :--- |
| int | string |

## Status
| sta_id | sta_nome |
| :--- | :--- |
| int | string |

## Sistema
| sis_id | sis_nome |
| :--- | :--- |
| int | string |

### Cliente

| cli_nome | cli_celular | cli_email | cli_acesso | cli_sistema | cli_ultimo_acesso |
| :--- | :--- | :--- | :--- | :--- | :--- |
| string | string | string | string | categoria_FK | datetime |

### Atendimento

| ate_id | ate_cliente | ate_categoria | ate_descricao | ate_data_criacao | ate_status | 
| :--- | :--- | :--- | :--- | :--- | :--- |
| int | cliente_FK | categoria_FK | string | datetime | status_FK |


