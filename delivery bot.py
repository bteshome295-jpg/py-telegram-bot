import telebot
from telebot import types

TOKEN = "8914682909:AAEubOSzVSy7OZVtcTWqEULz9Su7VLEE_nc"
bot = telebot.TeleBot(TOKEN)

# የራስሽን Telegram ID ከ @userinfobot አግኝተሽ እዚህ ጠቅላላ ቁጥሩን አስገቢ (ለምሳሌ: "123456789")
ADMIN_CHAT_ID = "6997377079"

GROUP_LINK = "https://t.me/kbgforstudents"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton('🍕 የምግብ ዝርዝር / Tarree nyaataa', callback_data='menu')
    btn2 = types.InlineKeyboardButton('🥤 የመጠጥ ዝርዝር / Dhugaatii', callback_data='drinks')
    btn3 = types.InlineKeyboardButton('📚 የቁሳቁስ ካታሎግ / Meshaalee', callback_data='supplies')
    btn4 = types.InlineKeyboardButton('🛒 ማዘዝ እፈልጋለሁ / Ajajuuf', callback_data='order')
    btn5 = types.InlineKeyboardButton('👥 ወደ ግሩፓችን ለመቀላቀል / Garee Keenya', url=GROUP_LINK)

    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    markup.add(btn5)

    welcome_text = (
        "🌸 **እንኳን ወደ ማሶቤ ምሳ በደህና መጡ!** 🌸\n"
        "🌸 **Baga gara Masobe Lunch Express nagaaan dhuftan!** 🌸\n\n"
        "📍 **የማሶቤ ምሳ አድራሻ / Teessoo Keenya:**\n"
        "👉 ከአዲሱ ክላስ በስተኋላ በኩል ወይም የኔትወርክ ሽቦ የቆመበት፣ መኪናዎች ከሚገኙበት ቦታ።\n"
        "👉 *Kutaa Barumsaa haaraa duuba, iddoo ukaa intarnetaa fi konkolaataan dhaabbatu bira.*\n\n"
        "🕒 **የማድረሻ ሰዓታት / Sa'aatii Tajaajilaa:**\n"
        "• ምሳ (Lunch): ከሰዓት **5:30 - 7:30** (Guyyaa 5:30 - 7:30)\n"
        "• እራት (Dinner): ከሌሊቱ **10:00 - 1:00** (Halkan 10:00 - 1:00)\n\n"
        "📞 ለተጨማሪ መረጃ ወይም ማዘዝ ሲፈልጉ / Odeeffannoo dabalataaf፦ **0905863723**\n\n"
        "ምን እንታዘዝ? / Maal isiniif ajajju?"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def callback_listener(call):
    if call.data == 'menu':
        menu_text = (
            "🍕 **የምግብ ዝርዝር እና ዋጋ / Tarree Nyaataa fi Gatii:**\n\n"
            "• ሽሮ (Shiro) - 110 ብር / ETB\n"
            "• ፍርፍር (Firfir) - 110 ብር / ETB\n"
            "• ፉል (Ful) - 110 ብር / ETB\n"
            "• እንቁላል ፍርፍር (Enqulal Firfir) - 140 ብር / ETB\n"
            "• ቲማቲም ለብለብ (Timatim Lebleb) - 110 ብር / ETB\n"
            "• ቲማቲም ሥልስ (Timatim Selse) - 110 ብር / ETB\n"
            "• ፓስታ በአትክልት (Pasta Be-Atkilt) - 110 ብር / ETB\n"
            "• ፓስታ በስጎ (Pasta Be-Sgo) - 110 ብር / ETB\n"
            "• እንቁላል ሳንድዊች (Enqulal Sandwich) - 70 ብር / ETB"
        )
        bot.send_message(call.message.chat.id, menu_text, parse_mode="Markdown")

    elif call.data == 'drinks':
        drinks_text = (
            "🥤 **የመጠጥ ዝርዝር እና ዋጋ / Dhugaatii fi Gatii:**\n\n"
            "• እርጎ (Ergoo) - 70 ብር / ETB\n"
            "• ሻይ (Shaahii) - 20 ብር / ETB\n"
            "• ቡና (Buna) - 30 ብር / ETB"
        )
        bot.send_message(call.message.chat.id, drinks_text, parse_mode="Markdown")

    elif call.data == 'supplies':
        supplies_text = (
            "📚 **የቁሳቁስ ካታሎግ / Meeshaalee:**\n\n"
            "• ፓድ (Pad)\n"
            "• ለውዝ (Oobi/Lewz)"
        )
        bot.send_message(call.message.chat.id, supplies_text, parse_mode="Markdown")

    elif call.data == 'order':
        msg = bot.send_message(
            call.message.chat.id,
            "📍 **የማሶቤ ምሳ አድራሻ / Teessoo፦** ከአዲሱ ክላስ በስተኋላ (Kutaa Barumsaa haaraa duuba)\n\n"
            "🕒 **የማድረሻ ሰዓታት / Sa'aatii Tajaajilaa፦**\n"
            "• ምሳ / Lunch: 5:30 - 7:30\n"
            "• እራት / Dinner: 10:00 - 1:00\n\n"
            "📞 Bilbila / ስልክ፦ **0905863723**\n\n"
            "📝 **እባክዎን የሚከተሉትን መረጃዎች አሟልተው ይላኩልን / Maaloo odeeffannoo kana ergaa፦**\n"
            "1. የሚፈልጉትን ምግብ/መጠጥ/ዕቃ (Nyaata/Dhugaatii barbaaddan)\n"
            "2. የስልክ ቁጥርዎን (Lakk. Bilbilaa)\n"
            "3. **ምግቡ እንዲደርስልዎ የሚፈልጉበትን አድራሻ - ብሎክ እና ዶርም ቁጥር (Teessoo - Lakk. Blokii fi Doormii)**",
            parse_mode="Markdown"
        )
        bot.register_next_step_handler(msg, process_order)

def process_order(message):
    user_info = f"👤 **ከ / Irraa:** @{message.from_user.username or message.from_user.first_name}\n"
    order_details = f"🛒 **የትዕዛዝ ዝርዝር እና አድራሻ / Ajaja fi Teessoo:**\n{message.text}"

    try:
        bot.send_message(ADMIN_CHAT_ID, f"🚨 **አዲስ ትዕዛዝ ደርሷል! / Ajaja Haaraa!** 🚨\n\n{user_info}\n{order_details}", parse_mode="Markdown")
        bot.reply_to(message, "✅ ትዕዛዝዎ በትክክል ደርሶናል! በቅርብ ጊዜ እናደርሳለን። እናመሰግናለን!\n✅ Ajajni keessan nu qaqqabeera! Galatoomaa!")
    except Exception as e:
        bot.reply_to(message, "✅ ትዕዛዝዎ ተመዝግቧል! እናመሰግናለን!\n✅ Ajajni keessan galmeeffameera!")

print("ቦቱ ሥራ ጀምሯል...")
bot.infinity_polling()