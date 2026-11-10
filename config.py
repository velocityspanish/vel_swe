"""VELOCITY SWEDISH - language pack, brand and motion design constants."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OUTPUT_DIR = BASE_DIR / "output"
LESSONS_DIR = OUTPUT_DIR / "lessons"
HISTORY_DIR = OUTPUT_DIR / "history"
SCENE_DIR = BASE_DIR / "scene"

VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
FPS = 30

# ---------------------------------------------------------------- brand

BRAND = "VELOCITY SWEDISH"
BRAND_LOCKUP_TOP = "VELOCITY"
BRAND_LOCKUP_BOTTOM = "SWEDISH"
HANDLE = "@velocityswedish"
MASCOT_NAME = "Velo"

# ==== LANGUAGE PACK START ====
LANGUAGE = {
    "code": "sv",
    "name": "Swedish",
    "native_name": "Svenska",
    "history_key": "swedish",
    "english_voice": "en-US-AvaNeural",
    "english_fallback_voice": "en-US-GuyNeural",
    "native_voice": "sv-SE-SofieNeural",
    "native_fallback_voice": "sv-SE-MattiasNeural",
    "native_engine": "edge",
    "native_lang_code": "sv",
    "english_rate": "-2%",
    "native_rate": "-6%",
    "english_pitch": "+0Hz",
    "native_pitch": "+0Hz",
    "native_label": "SVENSKA",
    "translit_label": "SAY IT LIKE",
    "greeting": "Hej!",
    "encouragement": "Fantastiskt!",
    "rtl": False,
    "char_tiles": False,
    "script_font": "",
}
# ==== LANGUAGE PACK END ====

AI_MODEL = os.getenv("AI_MODEL", "gemini-fast")
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "")

# ---------------------------------------------------------------- timing (seconds)

INTRO_DURATION = 4.0
OUTRO_DURATION = 5.2
EN_CARD_IN = 0.55
GAP_EN_NATIVE = 0.5
NATIVE_CARD_LEAD = 0.35
GAP_BEFORE_REPEAT = 0.8
TAIL_HOLD = 1.4
MAX_REEL_DURATION = 88.0

# ---------------------------------------------------------------- palette

INK = "#3C3C3C"
MUTED = "#8A8A8A"
CREAM = "#FFF8E7"
GREEN = "#58CC02"
GREEN_DARK = "#46A302"
GREEN_DEEP = "#3D8F00"
BLUE = "#1CB0F6"
PURPLE = "#A560E8"
ORANGE = "#FF7A00"
RED = "#FF4B4B"
YELLOW = "#F5A700"
TEAL = "#00A889"
PINK = "#E056A0"

PALETTE = [GREEN, BLUE, PURPLE, ORANGE, RED, YELLOW, TEAL, PINK]

# ---------------------------------------------------------------- categories
# (english, native, icon, accent)

# ==== CATEGORY TABLE START ====
CATEGORY_TABLE = [
    ("Motivation", "Motivation", "rocket", "#A560E8"),
    ("Love", "Kärlek", "heart", "#FF4B4B"),
    ("Success", "Framgång", "trophy", "#F5A700"),
    ("Wisdom", "Visdom", "book", "#A560E8"),
    ("Happiness", "Lycka", "smile", "#F5A700"),
    ("Self Improvement", "Självutveckling", "leaf", "#58CC02"),
    ("Gratitude", "Tacksamhet", "heart", "#FF7A00"),
    ("Friendship", "Vänskap", "users", "#00A889"),
    ("Hope", "Hopp", "sun", "#FF7A00"),
    ("Creativity", "Kreativitet", "palette", "#E056A0"),
    ("Inner Peace", "Inre Frus", "lotus", "#00A889"),
    ("Confidence", "Självförtroende", "shield", "#1CB0F6"),
    ("Perseverance", "Uthållighet", "mountain", "#FF7A00"),
    ("Inspiration", "Inspiration", "sparkles", "#A560E8"),
    ("Positive Life", "Positivt Liv", "sun", "#58CC02"),
    ("Courage", "Mod", "shield", "#FF4B4B"),
    ("Kindness", "Vänlighet", "heart", "#E056A0"),
    ("Patience", "Tålamod", "hourglass", "#00A889"),
    ("Forgiveness", "Förlåtelse", "hands", "#FF7A00"),
    ("Strength", "Styrka", "dumbbell", "#FF4B4B"),
    ("Joy", "Glädje", "smile", "#F5A700"),
    ("Balance", "Balans", "scale", "#00A889"),
    ("Growth", "Tillväxt", "sprout", "#58CC02"),
    ("Purpose", "Syfte", "target", "#A560E8"),
    ("Mindfulness", "Mindfulness", "lotus", "#00A889"),
]
# ==== CATEGORY TABLE END ====

CATEGORIES = [c[0] for c in CATEGORY_TABLE]
CATEGORIES_NATIVE = {c[0]: c[1] for c in CATEGORY_TABLE}
CATEGORY_META = {c[0]: {"native": c[1], "icon": c[2], "accent": c[3]} for c in CATEGORY_TABLE}
MAX_RECENT_CATEGORIES = 25

# ==== HASHTAGS START ====
HASHTAGS = [
    "#learnswedish",
    "#swedishlessons",
    "#swedishforbeginners",
    "#languagelearning",
    "#swedishvocabulary",
    "#velocityswedish",
    "#dailyswedish",
    "#swedish",
    "#learnlanguages",
    "#speakswedish",
    "#bilingual",
    "#languagetips",
]
# ==== HASHTAGS END ====
