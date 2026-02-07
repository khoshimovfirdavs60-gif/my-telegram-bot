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
