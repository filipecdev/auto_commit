# Auto Commit Script

Script em Python para verificar automaticamente se houve alterações em
um repositório Git e realizar o commit de forma automática.

Ideal para: - Backups locais - Anotações automáticas - Repositórios de
estudo ou logs - Ambientes onde mudanças frequentes não devem ser
esquecidas


## 📌 Funcionalidades

-   Verifica se há alterações no repositório
-   Executa `git add .`
-   Cria commit automático com timestamp
-   Permite definir o repositório via parâmetro
-   Pode ser executado manualmente ou via `cron`



## 🛠️ Requisitos

-   Python 3.8+
-   Git instalado
-   Repositório Git já inicializado
-   Autenticação Git configurada (SSH recomendado, caso use push)



## 📂 Estrutura

    .
    ├── auto_commit.py
    └── README.md



## Uso

### Execução manual

    python3 auto_commit.py /caminho/para/o/repositorio

Exemplo:

    python3 auto_commit.py /home/user/projetos/meu-repo



## ⏱️ Execução automática (cron)

Editar o crontab:

    crontab -e

Executar a cada 30 minutos:

    */30 * * * * /usr/bin/python3 /home/github/auto_commit/auto_commit.py /home/github/anotacoes


## 📝 Mensagem de commit

O commit é gerado automaticamente no formato:

    Auto-commit - YYYY-MM-DD HH:MM:SS

⚠️ Importante:\
Para uso com `cron`, configure autenticação via SSH.

