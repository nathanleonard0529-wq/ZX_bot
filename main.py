import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ChatJoinRequestHandler, ContextTypes

TOKEN = os.getenv("TOKEN")
SECOND_CHANNEL = "https://t.me/+OaXah8WFb3JmYjE0"

async def join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    join_request = update.chat_join_request
    user = join_request.from_user

    # Envoi du message privé
    await context.bot.send_message(
        chat_id=user.id,
        text=(
            "🚨 ALERTE CONFIANCE 🚨\n\n"
            "➡️ CONFIANCE 99% 🔥\n\n"
            "Rejoins le canal ici 👇\n"
            f"{SECOND_CHANNEL}"
        )
    )

    # Accepte automatiquement la demande
    await context.bot.approve_chat_join_request(
        chat_id=join_request.chat.id,
        user_id=user.id
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(ChatJoinRequestHandler(join_request))

print("Bot lancé ✅")
app.run_polling()
