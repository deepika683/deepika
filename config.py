"""
config.py
Centralized configuration for the LegalEase project.
Loads environment variables from .env and exposes shared constants/paths.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env file from project root
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

# --- API Keys / Model config ---
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-pro")

# --- Backend URL (used by Streamlit frontend) ---
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

# --- Paths ---
ASSETS_DIR = BASE_DIR / "assets"
LOGO_PATH = ASSETS_DIR / "logo.png"

# --- App metadata ---
APP_NAME = "LegalEase"
APP_TAGLINE = "AI Legal Document Generator"
