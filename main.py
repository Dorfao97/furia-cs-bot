from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler, CallbackContext
import os
from dotenv import load_dotenv

load_dotenv()

# Carrega o token do Telegram
TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    print("Erro: Token do Telegram não encontrado.")
    exit()

# Armazena preferências de jogo dos usuários
user_preferences = {}
# Armazena usuários que querem notificação antes dos jogos
notificacao_usuarios = set()


# /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Olá! Eu sou o FURIA CS Bot! Digite /ajuda para ver o que posso fazer."
    )


# /ajuda
async def ajuda(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "/start - Iniciar o bot\n"
        "/ajuda - Ver comandos disponíveis\n"
        "/info - Saber mais sobre a FURIA CS\n"
        "/preferencia - Definir sua preferência de jogo\n"
        "/proximosjogos - Ver os próximos jogos\n"
        "/notificar - Ser lembrado antes dos jogos\n"
        "/clipes - Ver os melhores clipes\n"
        "/torcer - Enviar mensagem de torcida"
    )


# /info
async def info(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "A FURIA é um dos maiores times de CS do Brasil! 🐆🔥"
    )


# /preferencia
async def preferencia(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Counter-Strike", callback_data='CS')],
        [InlineKeyboardButton("Valorant", callback_data='Valorant')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Qual é o seu jogo preferido?",
                                    reply_markup=reply_markup)


# Botões de resposta
async def button(update: Update, context: CallbackContext):
    query = update.callback_query
    choice = query.data
    user_preferences[query.from_user.id] = choice
    await query.answer()
    await query.edit_message_text(f"Sua preferência foi salva como: {choice}")


# /proximosjogos
async def proximos_jogos(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "📅 Próximos jogos da FURIA:\n\n"
        "🆚 FURIA x NAVI - 05/05 - 16h\n"
        "🆚 FURIA x Liquid - 08/05 - 19h\n"
        "⚠️ Use /notificar para receber alertas antes do jogo!"
    )


# /notificar
async def notificar(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    notificacao_usuarios.add(user_id)
    await update.message.reply_text("✅ Você será notificado antes dos jogos!")


# /clipes
async def clipes(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "🎥 Clipes recentes da FURIA:\n"
        "🔗 https://youtu.be/dqfURIA_clip1\n"
        "🔗 https://youtu.be/dqfURIA_clip2\n"
        "🔗 https://youtu.be/dqfURIA_clip3"
    )


# /torcer
async def torcer(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "🔥 VAI FURIAAA!! VAMO PRA CIMA!! 🐆💥"
    )


# Resposta a mensagens
async def handle_message(update: Update, context: CallbackContext):
    if "FURIA" in update.message.text.upper():
        await update.message.reply_text("FURIA é um time incrível!")
    else:
        await update.message.reply_text(
            "Não entendi o que você disse. Digite /ajuda para ver os comandos."
        )


# Main
if __name__ == '__main__':
    application = Application.builder().token(TOKEN).build()

    # Comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("ajuda", ajuda))
    application.add_handler(CommandHandler("info", info))
    application.add_handler(CommandHandler("preferencia", preferencia))
    application.add_handler(CommandHandler("proximosjogos", proximos_jogos))
    application.add_handler(CommandHandler("notificar", notificar))
    application.add_handler(CommandHandler("clipes", clipes))
    application.add_handler(CommandHandler("torcer", torcer))

    # Botões inline
    application.add_handler(CallbackQueryHandler(button))

    # Mensagens de texto
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot rodando... vá até o Telegram e digite /start")
    application.run_polling()
