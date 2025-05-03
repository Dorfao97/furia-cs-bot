from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler, CallbackContext
import os
from dotenv import load_dotenv

load_dotenv()

# Carrega o token do Telegram
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Dicionário para armazenar preferências dos usuários
user_preferences = {}

# Função para o comando /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Olá! Eu sou o FURIA CS Bot! Digite /ajuda para ver o que posso fazer.")

# Função para o comando /ajuda
async def ajuda(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "/start - Iniciar o bot\n"
        "/ajuda - Ver comandos disponíveis\n"
        "/info - Saber mais sobre a FURIA CS\n"
        "/preferencia - Definir sua preferência de jogo"
    )

# Função para o comando /info
async def info(update: Update, context: CallbackContext):
    await update.message.reply_text("A FURIA é um dos maiores times de CS do Brasil! 🐆🔥")

# Função para o comando /preferencia
async def preferencia(update: Update, context: CallbackContext):
    # Pergunta ao usuário qual jogo ele prefere
    keyboard = [
        [InlineKeyboardButton("Counter-Strike", callback_data='CS')],
        [InlineKeyboardButton("Valorant", callback_data='Valorant')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Qual é o seu jogo preferido?", reply_markup=reply_markup)

# Função que lida com as respostas aos botões
async def button(update: Update, context: CallbackContext):
    query = update.callback_query
    choice = query.data

    # Armazenar a preferência do usuário
    user_preferences[query.from_user.id] = choice

    await query.answer()
    await query.edit_message_text(f"Sua preferência foi salva como: {choice}")

# Função para lidar com mensagens de texto
async def handle_message(update: Update, context: CallbackContext):
    if "FURIA" in update.message.text:
        await update.message.reply_text("FURIA é um time incrível!")
    else:
        await update.message.reply_text("Não entendi o que você disse. Digite /ajuda para ver os comandos.")

# Configurações do bot
if __name__ == '__main__':
    # Criação da aplicação do bot
    application = Application.builder().token(TOKEN).build()

    # Adicionando handlers para os comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("ajuda", ajuda))
    application.add_handler(CommandHandler("info", info))
    application.add_handler(CommandHandler("preferencia", preferencia))

    # Adicionando handler para responder aos botões inline
    application.add_handler(CallbackQueryHandler(button))

    # Adicionando handler para mensagens de texto
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Iniciando o bot
    print("Bot rodando... vá até o Telegram e digite /start")
    application.run_polling()

