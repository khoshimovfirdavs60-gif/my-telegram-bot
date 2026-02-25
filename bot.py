from keep_alive import keep_alive
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Diqqat! Token qo'shtirnoq ichida bo'lishi shart
API_TOKEN = '8234203352:AAEms-xXd1ZvYqn1gpsU5oEaukYZNFHRIbc'

# PDF-dagi barcha mashqlar javoblari (1 dan 11 gacha)
PART1_DATA = {
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
PART2_DATA = {
    "1": ["rainforest", "insects", "(the) monkey", "characters", "six/6", "L-O-M-B-A-R-D-I-O"],
    "2": ["(the) environment", "wildlife", "writer", "course", "February", "M-I-T-C-H-E-L-L"],
    "3": ["farmer", "comedy", "voice", "university", "(the) passenger", "july"],
    "4": ["energy", "health", "rocket", "chemistry", "80/eighty", "L-O-C-K-H-A-R-T"],
    "5": ["gate", "drink", "Lambs", "climbing", "4.15", "C-A-F-F-E-R-T-Y-S"],
    "6": ["flute", "drama", "7.75", "24th June/June 24th", "orchestra", "D-R-I-S-C-O-L-L"],
    "7": ["shopping", "bags", "charity", "environmental", "rivers", "neighbour"],
    "8": ["changes", "flowers", "published", "cancelled", "10.00/10 am", "library"],
    "9": ["building", "September", "exercises", "training", "restaurant", "134"],
    "10": ["interview", "entertainment", "7.00/7pm/7 o'clock", "competitions", "free", "£170"],
    "11": ["days", "height", "plain", "accurate", "reading", "photos"],
    "12": ["1576", "climbing", "path", "13/13th", "celebrity", "poetry"],
    "13": ["pet", "cleaners", "magazine", "10.30 pm", "Theatre", "ticket"],
    "14": ["accommodation", "damaged", "kitchen", "subjects", "five/5", "doctor"],
    "15": ["15/fifteen", "9.30", "art", "Starting", "October", "food"],
    "16": ["walking", "600/six hundred", "diving", "June", "tour", "flights"],
    "17": ["introduction", "questions", "next", "200/two hundred", "manager", "Juice"],
    "18": ["13th/thirteenth", "park", "3.6/six", "cycling", "map", "team"],
    "19": ["History", "sweets", "January", "8/eight", "10/ten", "bag"],
    "20": ["front", "2.7/seven", "music", "local", "Thursday", "5/five minutes"],
    "21": ["jobs", "primary", "80 (eighty)", "weather", "control", "coffee"],
    "22": ["8.40", "notebook", "painting", "boat", "Tuesday", "A-R-U-N-D-E-L"],
    "23": ["train", "10.15", "3.30/thirty", "bridges", "fish", "boats"],
    "24": ["5/five", "make-up", "officer", "director", "clothes", "dinner"],
    "25": ["history", "tea", "interviews", "name", "reporter", "house"],
    "26": ["June", "map", "kilometres", "Walsh", "boots", "7/seven"],
    "27": ["(west) London", "furniture", "18/eighteen", "plants", "5.50/fifty", "7th June"],
    "28": ["views", "15th April", "markets", "balls", "chocolate", "exodus"],
    "29": ["19th century", "1975", "attic", "dining", "lawyer", "riding"],
    "30": ["Hall", "streets", "Cafe", "8.95", "studios", "tea"],
    "31": ["cash", "street", "Sunday", "holidays", "(full) medical", "booked"],
    "32": ["16th century", "family", "places", "(traditional) lunch", "five", "13.50"],
    "33": ["sign", "costume", "(individual) needs", "trainer", "strategies", "105"],
    "34": ["office", "lunch", "twelve/12", "11.30", "4.50", "aerobics"],
    "35": ["self-service", "9.30", "landscape", "materials", "reception", "group"],
    "36": ["width", "handler", "pick", "nine", "attitude", "ears"],
    "37": ["hairdryer", "glass", "plugs", "ball", "machine", "flying"],
    "38": ["management", "corporate", "presenter", "area", "keeper", "voluntary"],
    "39": ["engineer", "minute", "socially", "multiple", "script", "passion"],
    "40": ["chest", "northern", "forests", "winter", "mice", "diary"],
    "41": ["history", "caravan", "party", "shoulders", "plants", "january"],
    "42": ["october", "voice", "confident", "singing", "shoes", "glasses"],
    "43": ["west", "dolphins", "bike", "foot", "mask", "walking"],
    "44": ["lighting", "age", "leaf", "eyes", "monster", "detailed"],
    "45": ["alcohol", "tobacco", "physically", "unlikely", "trained", "embarrassment"],
    "46": ["campaigns", "2.4%", "images", "fiction", "apology", "tabloids"],
    "47": ["matchgirl.com", "may", "bones", "hairpins", "chewing", "perfectionist"],
    "48": ["poster", "changes", "farmers", "motorbike", "traffic", "gardening"],
    "49": ["final", "industrial", "gun", "waiter", "company", "metal"],
    "50": ["detective", "photos", "electric", "windows", "paper", "pollution"]
}
PART3_DATA = {
    "1": ["C", "E", "B", "D", "A"], "2": ["D", "B", "F", "C", "A"],
    "3": ["F", "E", "B", "D", "C"], "4": ["A", "E", "F", "C", "D"],
    "5": ["B", "F", "A", "C", "E"], "6": ["F", "B", "H", "C", "A"],
    "7": ["E", "C", "A", "G", "D"], "8": ["G", "B", "A", "H", "F"],
    "9": ["D", "H", "A", "G", "C"], "10": ["F", "G", "B", "E", "D"],
    "11": ["B", "H", "A", "C", "F"], "12": ["E", "D", "F", "A", "C"],
    "13": ["H", "E", "D", "F", "C"], "14": ["G", "B", "F", "C", "E"],
    "15": ["B", "H", "F", "D", "C"], "16": ["E", "A", "D", "B", "F"],
    "17": ["B", "A", "C", "D", "E"], "18": ["D", "B", "E", "C", "A"],
    "19": ["C", "E", "A", "F", "D"], "20": ["D", "A", "B", "C", "F"],
    "21": ["D", "F", "E", "B", "C"], "22": ["D", "A", "B", "E", "F"],
    "23": ["E", "F", "C", "D", "B"], "24": ["C", "B", "D", "F", "E"],
    "25": ["E", "D", "F", "C", "A"], "26": ["D", "F", "A", "B", "C"],
    "27": ["C", "A", "E", "B", "F"], "28": ["C", "E", "D", "A", "F"],
    "29": ["D", "E", "A", "F", "C"], "30": ["D", "A", "F", "B", "E"],
    "31": ["B", "E", "A", "D", "F"], "32": ["C", "F", "A", "E", "D"],
    "33": ["F", "C", "A", "D", "B"], "34": ["D", "B", "C", "A", "F"],
    "35": ["B", "D", "F", "A", "E"], "36": ["E", "B", "F", "C", "A"],
    "37": ["E", "F", "A", "B", "D"], "38": ["D", "G", "A", "B", "E"],
    "39": ["B", "D", "G", "F", "A"], "40": ["A", "C", "E", "F", "G"],
    "41": ["B", "D", "A", "E"], "42": ["C", "D", "A", "F", "E"],
    "43": ["G", "H", "E", "C", "B"], "44": ["F", "C", "H", "E", "D"],
    "45": ["F", "A", "C", "E"], "46": ["G", "E", "F", "A", "C"],
    "47": ["C", "F", "E", "B", "D"], "48": ["E", "C", "D", "F", "A"],
    "49": ["C", "E", "F", "D", "A"], "50": ["C", "E", "D", "A", "F"]
}
PART4_DATA = {
    "1": ["E", "C", "D", "A", "B"], "2": ["B", "F", "C", "A", "D"],
    "3": ["G", "B", "F", "A", "C"], "4": ["I", "H", "F", "B", "D"],
    "5": ["C", "E", "B", "D", "A"], "6": ["C", "D", "F", "B", "A"],
    "7": ["C", "G", "F", "A", "E"], "8": ["A", "I", "F", "E"],
    "9": ["F", "G", "B", "D", "C"], "10": ["G", "D", "B", "F"],
    "11": ["F", "H", "C", "B", "G"], "12": ["H", "C", "F", "G", "B"],
    "13": ["E", "D", "B", "C", "H"], "14": ["H", "D", "F", "A", "E"],
    "15": ["E", "C", "B", "G", "D"], "16": ["D", "C", "G", "H", "E"],
    "17": ["H", "C", "G", "B", "A"], "18": ["C", "F", "A", "E", "H"],
    "19": ["E", "G", "A", "B", "F"], "20": ["D", "F", "G", "B", "A"],
    "21": ["B", "A", "E", "C", "D"], "22": ["B", "A", "C", "E", "D"],
    "23": ["B", "E", "G", "F", "H"], "24": ["C", "F", "B", "G", "E"],
    "25": ["F", "B", "C", "E", "A"], "26": ["F", "E", "D", "C", "A"],
    "27": ["C", "D", "B", "F", "A"], "28": ["B", "G", "E", "C", "H"],
    "29": ["D", "E", "K", "C", "B"], "30": ["D", "A", "C", "B", "E"],
    "31": ["B", "C", "D", "F", "E"], "32": ["D", "C", "E", "A", "F"],
    "33": ["B", "D", "C", "G", "F"], "34": ["E", "I", "J", "F", "C"],
    "35": ["G", "F", "B", "E", "A"], "36": ["C", "B", "F", "G"],
    "37": ["F", "G", "D", "B", "H"], "38": ["E", "F", "A", "D"],
    "39": ["C", "A", "E", "F", "D"], "40": ["I", "B", "E"],
    "41": ["C", "G", "A", "E", "F"], "42": ["H", "F", "E", "A", "D"],
    "43": ["C", "B", "H", "D", "G"], "44": ["D", "F", "B", "A", "G"],
    "45": ["C", "F", "A", "H", "E"], "46": ["H", "E", "F", "D", "B"],
    "47": ["E", "G", "A", "C", "B"], "48": ["D", "H", "C", "A", "B"],
    "49": ["D", "F", "B", "A", "G"], "50": ["B", "E", "H", "G"]
}
PART5_DATA = {
    "1": ["B", "A", "C", "C", "C", "B"], "2": ["A", "B", "A", "A", "B", "C"],
    "3": ["A", "C", "A", "B", "A", "C"], "4": ["A", "B", "B", "C", "C", "B"],
    "5": ["A", "B", "C", "A", "B", "A"], "6": ["C", "B", "A", "B", "C", "B"],
    "7": ["C", "B", "A", "C", "B", "A"], "8": ["A", "C", "C", "B", "C", "B"],
    "9": ["A", "C", "A", "C", "C", "B"], "10": ["A", "A", "B", "C", "C", "A"],
    "11": ["B", "A", "B", "B", "B", "A"], "12": ["C", "C", "A", "C", "A", "C"],
    "13": ["B", "B", "B", "A", "A", "B"], "14": ["A", "C", "B", "A", "C", "A"],
    "15": ["B", "C", "A", "B", "A", "A"], "16": ["C", "B", "B", "C", "C", "B"],
    "17": ["B", "A", "C", "B", "C", "A"], "18": ["B", "A", "B", "A", "A", "C"],
    "19": ["C", "C", "B", "C", "B", "A"], "20": ["B", "B", "A", "C", "B", "A"],
    "21": ["A", "C", "A", "B", "B", "A"], "22": ["B", "C", "A", "C", "A", "C"],
    "23": ["C", "B", "B", "B", "B", "C"], "24": ["C", "B", "C", "A", "B", "C"],
    "25": ["B", "C", "B", "A", "A", "C"], "26": ["C", "A", "B", "C", "C", "A"],
    "27": ["C", "C", "A", "C", "C", "A"], "28": ["A", "B", "A", "B", "A", "C"],
    "29": ["B", "C", "B", "C", "A", "C"], "30": ["B", "B", "C", "A", "B", "C"],
    "31": ["B", "A", "C", "B", "A", "A"], "32": ["B", "C", "C", "A", "B", "C"],
    "33": ["C", "B", "B", "C", "C", "A"], "34": ["B", "B", "A", "C", "C", "C"],
    "35": ["C", "B", "C", "A", "C", "A"], "36": ["C", "C", "B", "C", "B", "B"],
    "37": ["A", "C", "C", "B", "A", "B"], "38": ["B", "C", "B", "C", "A", "C"],
    "39": ["B", "B", "C", "A", "B", "C"], "40": ["B", "A", "C", "B", "A", "A"],
    "41": ["B", "A", "B", "A", "A", "C"], "42": ["C", "B", "A", "C", "A", "B"],
    "43": ["A", "C", "B", "A", "C", "B"], "44": ["C", "A", "B", "B", "C", "A"],
    "45": ["B", "A", "C", "C", "B", "A"], "46": ["C", "A", "A", "B", "B", "A"],
    "47": ["B", "C", "B", "C", "A", "B"], "48": ["C", "B", "A", "B", "C", "B"],
    "49": ["A", "A", "B", "C", "B", "C"], "50": ["A", "B", "C", "A", "C", "A"]
}
"1": ["puzzle", "confusion", "meditation", "stone", "coins", "tree"],
    "2": ["business", "western", "sahara", "alps", "level", "degree"],
    "3": ["newspaper", "readers", "fishing", "market", "children", "channels"],
    "4": ["pool", "address", "3. 4", "water", "accidents", "door"],
    "5": ["business", "character", "career", "obvious", "winter", "disappointing"],
    "6": ["homes", "ingredients", "magazine", "loan", "food", "moment"],
    "7": ["1970", "famous", "children", "breathe", "float", "confident"],
    "8": ["brain", "stress", "feelings", "read", "reward", "nets"],
    "9": ["copying", "ideas", "grammar", "consonants", "awareness", "contact"],
    "10": ["fresher", "presentation", "transport", "waste", "freezer", "environment"],
    "11": ["400", "27", "rabbits", "caves", "hunt", "road"],
    "12": ["composer", "contacts", "mending", "wood", "museum", "dry"],
    "13": ["water", "minerals", "gold", "stone", "cooling", "windows"],
    "14": ["gene", "power/powers", "strangers", "erosion", "islands", "roads"],
    "15": ["violin", "commissions", "energy", "complex", "opera", "disturbing"],
    "16": ["road", "path", "meat & vegetables", "energy", "worried", "30 dollars/thirty dollars"],
    "17": ["natural", "interact", "artists", "heating", "intimidating", "tail"],
    "18": ["fort", "legal", "vision", "wax", "laser", "ink"],
    "19": ["tunnel", "wax", "balloon", "green", "sweetheart", "stone"],
    "20": ["adventure", "preparation", "ice", "perfume", "toothbrush", "satisfaction"],
    "21": ["wolf", "oasis", "roots", "seeds", "tunnels", "batteries"],
    "22": ["student", "heights", "websites", "helmet", "airport", "months"],
    "23": ["design", "libraries", "workshop", "puzzles", "dishes", "drawers"],
    "24": ["21", "wind", "shoulders", "smell", "mice", "feathers"],
    "25": ["period", "tight", "arms", "gloves", "plastic", "knees"],
    "26": ["bubbles", "problematic", "drying", "marketing", "vegetarians", "initiative"],
    "27": ["bulbs", "sponge", "reproductive", "land", "juice", "leaks/leaking"],
    "28": ["colony", "wood", "feedback", "staircase", "intelligence", "(mathematical) model"],
    "29": ["insect", "gold", "storms", "holes", "boiled", "blankets"],
    "30": ["mass-producing", "popcorn", "exploded", "restaurant", "competition", "counter"],
    "31": ["competing", "continuous", "habitats", "reservoirs", "licenses", "considerate"],
    "32": ["qualifications", "volunteer", "deadline", "barriers", "violence", "sentence"],
    "33": ["assistant", "intimidated", "trainee", "interviews", "news", "flexibility"],
    "34": ["animation", "interfaces", "star", "narrative", "difficulty", "dedication"],
    "35": ["mining", "curious", "threatened", "hum", "grease", "rugs"],
    "36": ["moon", "cliff/cliffs", "paper", "thunderstorm", "silent", "(youngest/younger) sons"],
    "37": ["gossip", "sophistication", "anecdotes", "accounts", "careers", "procedures"],
    "38": ["(road) map", "management", "marketing", "distractions", "past", "problem-solvers"],
    "39": ["accent", "attitudes", "lawyer", "art", "piano", "bookshelves"],
    "40": ["unusual", "self-funded", "church", "romantic", "shadows", "childhood"],
    "41": ["flu", "skiing", "sunrise", "ordinary", "panic", "gratitude"],
    "42": ["kites", "architects", "kayaking", "geologist", "mind", "networking"],
    "43": ["hammer", "pumpkin", "marble", "scope", "jacket", "incredible"],
    "44": ["uncle", "tester", "jungle", "research", "adventure", "satisfying"],
    "45": ["tours", "light", "cheetahs", "crocodile", "april", "farm"],
    "46": ["mountain", "windows", "sun", "folk", "models", "spectators"],
    "47": ["barriers", "segregated", "maids", "editing", "(night) clubs", "resonant"],
    "48": ["guide", "helmet", "landing", "wrist", "device", "parachute"],
    "49": ["nuts", "tea", "rabbit", "employer", "salty", "ate"],
    "50": ["silence", "rabbits", "internet", "calls", "car", "university"]
}
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "🎧 **Listening Checker Bot**\n\n"
        "Tekshirish uchun mashq va savol raqamini javob bilan yuboring.\n"
        "Namuna: `1 1 A` (1-mashq, 1-savol, javob A)")

user_sessions = {}

@dp.message()
async def check_answer(message: types.Message):
    user_id = message.from_user.id
    text = message.text.strip().lower()
    qismlar = text.split()

    # 1. SAVOL TANLASH (Namuna: pt 6 1 1)
    if len(qismlar) == 4 and qismlar[0] == "pt":
        try:
            part_num = qismlar[1]
            mashq_num = qismlar[2]
            savol_idx = int(qismlar[3]) - 1

            # Qaysi partligini aniqlash va javobni olish
            correct_answer = None
            if part_num == "1": correct_answer = PART1_DATA.get(mashq_num, [])[savol_idx]
            elif part_num == "2": correct_answer = PART2_DATA.get(mashq_num, [])[savol_idx]
            elif part_num == "3": correct_answer = PART3_DATA.get(mashq_num, [])[savol_idx]
            elif part_num == "4": correct_answer = PART4_DATA.get(mashq_num, [])[savol_idx]
            elif part_num == "5": correct_answer = PART5_DATA.get(mashq_num, [])[savol_idx]
            elif part_num == "6": correct_answer = PART6_DATA.get(mashq_num, [])[savol_idx]

            if correct_answer:
                # Javobni xotiraga saqlaymiz
                user_sessions[user_id] = correct_answer.lower()
                await message.answer(f"❓ Part {part_num}, {mashq_num}-mashq, {savol_idx+1}-savol tanlandi.\n\nEndi javobni yozing:")
            else:
                await message.answer("❌ Bunday mashq yoki savol topilmadi.")
        except (IndexError, KeyError, ValueError):
            await message.answer("❌ Xato! Namuna: pt 6 1 1")
        return

    # 2. JAVOBNI TEKSHIRISH (Foydalanuvchi so'zni o'zini yozganda)
    if user_id in user_sessions:
        togri_javob = user_sessions[user_id]
        
        if text == togri_javob:
            await message.answer("✅ To'g'ri!")
            # Javobni topgandan keyin sessiyani tozalaymiz
            del user_sessions[user_id]
        else:
            await message.answer("❌ Xato! Qayta urinib ko'ring yoki boshqa savol tanlang.")
    else:
        # Agar savol tanlamasdan pt deb yozsa
        if text.startswith("pt"):
            await message.answer("⚠️ Savolni tanlash uchun masalan: `pt 6 1 1` deb yozing.")
        elif not text.startswith("/"):
            await message.answer("⚠️ Avval savolni tanlang. Namuna: `pt 6 1 1` (Part 6, 1-mashq, 1-savol)")
