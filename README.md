# BankNova AI — Wealth OS (Streamlit)

A Streamlit recreation of the BankNova AI landing page / wealth dashboard demo.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy to Streamlit Community Cloud

1. Create a new GitHub repository (e.g. `banknova-ai-streamlit`) and push this folder's contents to it:

   ```bash
   git init
   git add .
   git commit -m "Initial commit: BankNova AI Streamlit app"
   git branch -M main
   git remote add origin https://github.com/<your-username>/<your-repo>.git
   git push -u origin main
   ```

2. Go to [share.streamlit.io](https://share.streamlit.io), sign in with GitHub, and click **"New app"**.
3. Select your repository, branch `main`, and set the main file path to `app.py`.
4. Click **Deploy**. Streamlit Cloud will install `requirements.txt` automatically and your app will be live at `https://<your-app-name>.streamlit.app`.

## Files

- `app.py` — the full app (hero, portfolio card, feature grid, goal planning & portfolio X-ray demo tabs)
- `requirements.txt` — Python dependencies
- `.streamlit/config.toml` — theme and server configuration
