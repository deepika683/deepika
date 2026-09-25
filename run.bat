@echo off
REM Starts the FastAPI backend and the Streamlit frontend in separate windows.
REM Usage: run.bat

start "LegalEase Backend" cmd /k "uvicorn legalEaseAPI.main:app --reload --port 8000"
timeout /t 2 /nobreak >nul
start "LegalEase Frontend" cmd /k "streamlit run frontend/app.py"
