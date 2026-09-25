#!/usr/bin/env bash
# Starts the FastAPI backend and the Streamlit frontend together.
# Usage: bash run.sh

set -e

echo "Starting FastAPI backend on http://localhost:8000 ..."
uvicorn legalEaseAPI.main:app --reload --port 8000 &
BACKEND_PID=$!

sleep 2

echo "Starting Streamlit frontend on http://localhost:8501 ..."
streamlit run frontend/app.py

# When Streamlit exits, also stop the backend
kill $BACKEND_PID
