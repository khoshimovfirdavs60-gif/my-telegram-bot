from keep_alive import keep_alive
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Diqqat! Token qo'shtirnoq ichida bo'lishi shart
API_TOKEN = '8234203352:AAEms-xXd1ZvYqn1gpsU5oEaukYZNFHRIbc'

# PDF-dagi barcha mashqlar javoblari (1 dan 11 gacha)
ANSWERS_DATA = {
    "1": ["A", "B", "B", "C", "B", "C", "A", "A"],
    "2": ["C", "C", "A", "C", "B", "C", "B", "C"],
    "3": ["A", "B", "C", "B", "C", "B", "B", "C"],
    "4": ["C", "B", "A", "A", "B", "A", "B", "B"],
    "5": ["A", "A", "A", "C", "B", "C", "B", "C"],
    "6": ["B", "A", "B", "C", "A", "A", "A", "B"],
    "7": ["C", "C", "C", "B", "A", "B", "A", "A"],
    "8": ["C", "B", "C", "B", "B", "C", "A", "A"],
    "9": ["B", "C", "A", "A", "A", "C", "B", "A"],
    "10": ["B", "A", "B", "A", "C", "C", "C", "A"],
    "11": ["C", "B", "C", "C", "C", "B", "A", "A"]
    "12": ["C", "B", "C", "B", "C", "B", "C", "C"],
    "13": ["A", "A", "A", "B", "B", "C", "B", "A"],
    "14": ["B", "A", "C", "A", "B", "B", "C", "B"],
    "15": ["A", "B", "B", "A", "C", "C", "B", "B"],
    "16": ["A", "C", "B", "A", "B", "B", "C", "B"],
    "17": ["A", "A", "A", "C", "B", "B", "A", "B"],
    "18": ["C", "B", "A", "D", "C", "C", "D", "A"],
    "19": ["A", "A", "C", "B", "A", "C", "B", "A"],
    "20": ["A", "A", "A", "C", "C", "A", "B", "A"],
    "21": ["C", "A", "B", "B", "A", "B", "C", "A"],
    "22": ["B", "A", "B", "B", "A", "C", "C", "B"],
    "23": ["C", "A", "B", "B", "B", "C", "A", "C"],
    "24": ["C", "A", "B", "B", "A", "A", "B", "B"],
    "25": ["C", "A", "C", "B", "C", "A", "C", "B"],
    "26": ["B", "C", "A", "A", "C", "A", "B", "C"],
    "27": ["B", "B", "A", "C", "A", "C", "B", "A"],
    "28": ["C", "C", "A", "A", "C", "A", "B", "A"],
    "29": ["A", "C", "C", "B", "B", "C", "B", "A"],
    "30": ["A", "B", "A", "C", "B", "A", "B", "A"],
    "31": ["C", "B", "A", "C", "A", "C", "A", "B"],
    "32": ["B", "B", "B", "A", "C", "C", "C", "A"],
    "33": ["B", "A", "B", "C", "A", "C", "C", "C"],
    "34": ["B", "C", "C", "C", "C", "C", "C", "C"],
    "35": ["B", "B", "B", "B", "A", "C", "A", "B"],
    "36": ["A", "C", "C", "C", "C", "B", "B", "A"],
    "37": ["A", "C", "B", "C", "B", "C", "A"],
    "38": ["C", "B", "B", "A", "C", "C", "B"],
    "39": ["A", "B", "B", "A", "B", "A", "C"],
    "40": ["A", "C", "B", "A", "C", "B", "C"],
    "41": ["A", "C", "B", "C", "B", "A", "A"],
    "42": ["B", "C", "B", "A", "A", "B", "C"],
    "43": ["A", "B", "C", "C", "C", "A"],
    "44": ["C", "A", "A", "B", "A"],
    "45": ["A", "C", "B", "C", "B", "B", "C", "B", "B", "A"],
    "46": ["A", "B", "C", "A", "A", "C", "A"],
    "47": ["A", "C", "B", "C", "B", "A", "B"],
    "48": ["B", "A", "A", "A", "C", "B"],
    "49": ["B", "A", "A", "C", "B"],
    "50": ["C", "B", "C", "A", "C", "A", "C", "B"]
}

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "🎧 **Listening Checker Bot**\n\n"
        "Tekshirish uchun mashq va savol raqamini javob bilan yuboring.\n"
        "Namuna: `1 1 A` (1-mashq, 1-savol, javob A)")


@dp.message()
async def check_answer(message: types.Message):
    try:
        # Xabarni qismlarga ajratamiz (Namuna: "1 1 A")
        parts = message.text.upper().split()
        if len(parts) < 3:
            return await message.answer(
                "⚠️ Namuna: `1 1 A` (Mashq Savol Javob)")

        ex_num = parts[0]  # Mashq raqami
        q_idx = int(parts[1]) - 1  # Savol indeksi (0 dan boshlanadi)
        user_choice = parts[2]  # Foydalanuvchi javobi

        if ex_num in ANSWERS_DATA:
            correct_list = ANSWERS_DATA[ex_num]

            if 0 <= q_idx < len(correct_list):
                if user_choice == correct_list[q_idx]:
                    await message.answer(
                        f"Mashq {ex_num}, Savol {q_idx+1}: ✅ To'g'ri!")
                else:
                    # BU YERDA TO'G'RI JAVOBNI KO'RSATMAYMIZ!
                    await message.answer(
                        f"Mashq {ex_num}, Savol {q_idx+1}: ❌ Noto'g'ri!")
            else:
                await message.answer(
                    f"❌ {ex_num}-mashqda {len(correct_list)} ta savol bor.")
        else:
            await message.answer(f"❌ {ex_num}-mashq bazada yo'q.")
    except:
        await message.answer(
            "⚠️ Faqat raqam va harf yuboring. Namuna: `1 1 A` ")
async def main():
    # Faqat bitta joyda, main ichida chaqiramiz
    keep_alive() 
    print("Bot muvaffaqiyatli ishga tushdi!")
    await dp.start_polling(bot)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
