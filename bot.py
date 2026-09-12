
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)
import os 

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

LINK_CORRETORA = "https://trade.polariumbroker.com/register?aff=823552&aff_model=revenue&afftrack=telegram"

LINK_CANAL = os.getenv("TELEGRAM_CHANNEL_LINK")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    mensagem = """
🔥 BEM-VINDO AO FORJADO NO CAOS 🔥

Você entrou para a tropa que acompanha operações ao vivo e leitura real de mercado.

📈 Aqui você terá acesso a:

✅ Lives operacionais
✅ Estratégias ao vivo
✅ Gestão de banca
✅ Entradas em tempo real

👇 Escolha uma opção abaixo:
"""

    keyboard = [

        [InlineKeyboardButton(
            "🚀 QUERO CRIAR MINHA CONTA",
            callback_data="criar_conta"
        )],

        [InlineKeyboardButton(
            "✅ JÁ SOU CADASTRADO",
            callback_data="ja_cadastrado"
        )]

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        mensagem,
        reply_markup=reply_markup
    )


async def liberar_canal(query, context):
    keyboard = [
        [InlineKeyboardButton(
            "🔥 ENTRAR NO CANAL VIP",
            url="https://t.me/+PACHFGmDH_UxZjVh"
        )]
    ]

    await query.message.reply_text(
        """
✅ Acesso liberado!

Clique abaixo para entrar no canal VIP:
""",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    if query.data == "criar_conta":

        keyboard = [
            [InlineKeyboardButton(
                "🚀 FAZER CADASTRO",
                url=LINK_CORRETORA
            )],
            [InlineKeyboardButton(
                "✅ JÁ FIZ O CADASTRO",
                callback_data="liberar_canal"
            )]
        ]

        await query.message.reply_text(
            """
🔥 Perfeito.

Faça sua configuração inicial na corretora abaixo.

Depois clique em **JÁ FIZ O CADASTRO** para liberar sua entrada no canal VIP.
""",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "ja_cadastrado":

        await liberar_canal(query, context)

    elif query.data == "liberar_canal":

        await liberar_canal(query, context)
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

print("BOT ONLINE 🔥")

app.run_polling()


