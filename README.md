# LegalEase — AI-Powered Legal Document Generator

Generates employment contracts, NDAs, lease agreements, and other legal
documents from simple form inputs, using Google's Gemini model. Export as
`.txt`, `.docx`, or `.pdf`.

**Stack:** FastAPI (backend) + Streamlit (frontend) + Google Gemini (AI core)

---

## 1. Project Structure

```
LegalEase/
├── ai_core/
│   ├── __init__.py
│   └── gemini_generator.py      # Gemini API wrapper
├── legalEaseAPI/
│   ├── __init__.py
│   ├── main.py                  # FastAPI app entrypoint
│   └── routes.py                # /generate endpoint
├── frontend/
│   ├── __init__.py
│   └── app.py                   # Streamlit UI
├── utils/
│   ├── __init__.py
│   └── formatters.py            # sanitize_text, format_docx, format_pdf, format_html_preview
├── assets/
│   └── logo.png                 # optional — add your own logo here
├── config.py                    # shared config / env loading
├── requirements.txt
├── .env.example                 # copy to .env and fill in your API key
├── run.sh                       # start both servers (Mac/Linux)
├── run.bat                      # start both servers (Windows)
└── README.md
```

---

## 2. Prerequisites

- Python 3.10+ installed
- A free Gemini API key: https://aistudio.google.com/app/apikey
- VS Code (with the Python extension installed)

---

## 3. VS Code Setup

1. Unzip/copy the `LegalEase` folder anywhere on your machine.
2. Open VS Code → **File → Open Folder** → select the `LegalEase` folder.
3. Open a new terminal in VS Code: **Terminal → New Terminal**.
4. Create and activate a virtual environment:

   **Windows (PowerShell):**
   ```powershell
   python -m venv venv
   venv\Scripts\activate
   ```

   **Mac/Linux:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   In the VS Code bottom-right, make sure the selected Python interpreter is
   the one inside `venv` (click it if prompted and choose the `venv` option).

5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

6. Set up your API key:
   - Copy `.env.example` to a new file named `.env` in the project root.
   - Open `.env` and replace `your_gemini_api_key_here` with your real Gemini
     API key.

7. (Optional) Add your own logo:
   - Drop a PNG at `assets/logo.png`. If it's missing, the app still works
     and just shows a text title instead.

---

## 4. Running the App

You need **two processes running at the same time**: the FastAPI backend and
the Streamlit frontend. Use two VS Code terminals (Terminal → Split Terminal),
or the provided run scripts.

### Option A — Two terminals (recommended, easiest to debug)

**Terminal 1 — Backend:**
```bash
uvicorn legalEaseAPI.main:app --reload --port 8000
```
You should see `Application startup complete.` and the API live at
`http://127.0.0.1:8000`.

**Terminal 2 — Frontend:**
```bash
streamlit run frontend/app.py
```
This opens the UI in your browser at `http://localhost:8501`.

### Option B — One command

**Mac/Linux:**
```bash
bash run.sh
```

**Windows:**
```bat
run.bat
```

---

## 5. Testing the App

1. With both servers running, go to `http://localhost:8501`.
2. Fill in the form, e.g.:
   - **Document Type:** Freelance Work Contract
   - **Parties Involved:** Jane Doe (Service Provider), TechNova Inc. (Client)
   - **Terms & Conditions:** Work must be delivered by May 15, 2025; Payment
     due within 7 days of invoice; Confidentiality must be maintained at all
     times
   - **Effective Date:** April 15, 2025
3. Click **Generate Document** — you should see a success message and a
   styled preview.
4. Click **✏️ Click to Edit Document** to tweak the text inline.
5. Use the three download buttons to confirm `.txt`, `.docx`, and `.pdf`
   files all download correctly and open without errors.

### Quick API-only test (optional)

With the backend running, open `http://127.0.0.1:8000/docs` in a browser —
this is FastAPI's interactive Swagger UI. Expand `POST /generate`, click
**Try it out**, fill in the sample JSON, and click **Execute** to confirm the
Gemini integration works independently of the Streamlit UI.

You can also test from the terminal:
```bash
curl -X POST http://127.0.0.1:8000/generate ^
  -H "Content-Type: application/json" ^
  -d "{\"document_type\":\"NDA\",\"parties\":\"Alice, Bob\",\"terms\":\"Confidential for 2 years\",\"dates\":\"Jan 1, 2026\"}"
```
(On Mac/Linux, replace `^` line continuations with `\`.)

---

## 6. Troubleshooting

| Problem | Fix |
|---|---|
| `GEMINI_API_KEY is not set` | Make sure you created `.env` (not just `.env.example`) and it contains a real key, then restart the backend. |
| Streamlit shows "Could not reach the backend API" | Make sure the FastAPI server (Terminal 1) is running on port 8000 before generating a document. |
| `ModuleNotFoundError` | Make sure your virtual environment is activated and `pip install -r requirements.txt` completed without errors. |
| PDF/DOCX missing logo | This is expected if `assets/logo.png` doesn't exist — it's optional. |
| Gemini errors like model not found | Your API key may not have access to `gemini-1.5-pro`. Try setting `GEMINI_MODEL=gemini-1.5-flash` in `.env`. |

---

## 7. Deployment Notes (optional, for later)

- **Backend:** deployable to Render, Railway, Fly.io, or any VPS running
  `uvicorn legalEaseAPI.main:app --host 0.0.0.0 --port $PORT`.
- **Frontend:** deployable to Streamlit Community Cloud — just point it at
  `frontend/app.py` and set `BACKEND_URL` to your deployed backend's public
  URL as an environment variable/secret.
- Remember to set `GEMINI_API_KEY` as a secret/environment variable on
  whichever platform you deploy to — never commit `.env` to source control.
