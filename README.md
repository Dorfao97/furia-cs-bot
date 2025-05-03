# 🤖 FURIA CS Bot - Telegram

Bot oficial para fãs do time de CS:GO da **FURIA**!  
Acompanhe partidas, veja clipes, receba notificações e interaja como um verdadeiro torcedor.  
Feito para o desafio de estágio da FURIA 2025.

---

## 📲 Como usar

1. Acesse o bot no Telegram (link em breve).
2. Digite `/start` para começar.
3. Use os comandos disponíveis para explorar os recursos.

---

## ⚙️ Funcionalidades

| Comando              | Descrição                                                                 |
|----------------------|--------------------------------------------------------------------------|
| `/start`             | Inicia o bot e envia uma mensagem de boas-vindas.                        |
| `/ajuda`             | Lista todos os comandos disponíveis.                                     |
| `/info`              | Informa sobre o time de CS da FURIA.                                     |
| `/preferencia`       | Escolha entre *CS* ou *Valorant* como jogo favorito.                     |
| `/proximosjogos`     | Mostra os próximos confrontos da FURIA.                                  |
| `/notificar`         | Cadastra o usuário para receber alertas antes dos jogos.                 |
| `/clipes`            | Envia links com os melhores momentos recentes da FURIA.                  |
| `/torcer`            | Envia uma mensagem de torcida animada.                                   |
| Texto com “FURIA”    | Responde com uma mensagem especial de admiração ao time.                 |

---

## 🧠 Tecnologias Utilizadas

- Python 3.10+
- [python-telegram-bot v20+](https://docs.python-telegram-bot.org/en/stable/)
- dotenv para variáveis de ambiente

---

## 📁 Estrutura Básica

```bash
.
├── bot.py              # Código principal do bot
├── .env                # Token do Telegram (não subir no GitHub)
├── requirements.txt    # Dependências do projeto
└── README.md           # Este documento
