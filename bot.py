
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

TOKEN = "8795619658:AAGKXKGv_IND95NiUa5vCbuUV9TB_oDil1o"

LINK_CORRETORA = "https://trade.polariumbroker.com/register?aff=823552&aff_model=revenue&afftrack=telegram"

LINK_CANAL = "https://t.me/+PACHFGmDH_UxZjVh"


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


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    # BOTÃO CADASTRO
    if query.data == "criar_conta":

        keyboard = [

            [InlineKeyboardButton(
                "🚀 FAZER CADASTRO",
                url=LINK_CORRETORA
            )],

            [InlineKeyboardButton(
                "🔥 ENTRAR NO CANAL VIP",
                url=LINK_CANAL
            )]

        ]

        await query.message.reply_text(
            """
🔥 Perfeito.

Faça sua configuração inicial na corretora abaixo e em seguida entre na sala operacional VIP.
""",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # BOTÃO JÁ CADASTRADO
    elif query.data == "ja_cadastrado":

        keyboard = [

            [InlineKeyboardButton(
                "🔥 ENTRAR NO CANAL VIP",
                url=LINK_CANAL
            )]

        ]

        await query.message.reply_text(
            """
✅ Acesso liberado.

Clique abaixo para entrar no canal VIP:
""",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(CallbackQueryHandler(button))

print("BOT ONLINE 🔥")
 
app.run_polling()

