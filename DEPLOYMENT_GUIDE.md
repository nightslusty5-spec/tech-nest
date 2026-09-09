# 🚀 Render Deployment Guide: PULSE AUDIO E-Commerce

This guide walks you through deploying the **PULSE AUDIO** store live to **[Render.com](https://render.com/)** on the free tier.

---

## 📁 1. Files Prepared for Deployment
The project is already pre-configured with:
- `requirements.txt`: Python package dependencies (FastAPI, Uvicorn, SQLAlchemy, Pydantic, etc.).
- `render.yaml`: Blueprint configuration for 1-click deployment.
- `Procfile`: Process command for standard Render Web Services.
- `.gitignore`: Prevents committing temporary files, databases, and logs.

---

## 🐙 2. Push Code to GitHub

Open PowerShell or terminal in the project directory (`C:\Users\mihir\.gemini\antigravity\scratch\pulse_gear_ecommerce`) and run:

```bash
# 1. Initialize Git repository
git init

# 2. Stage all project files
git add .

# 3. Commit
git commit -m "Initial commit of Pulse Audio dynamic e-commerce store"

# 4. Set main branch
git branch -M main

# 5. Link to your GitHub repository (replace with your repo URL)
git remote add origin https://github.com/YOUR_USERNAME/pulse-audio-ecommerce.git

# 6. Push to GitHub
git push -u origin main
```

---

## 🌐 3. Deploy on Render.com

### Method 1: Standard Web Service (Recommended & Easy)

1. Sign up / Log in to **[Render Dashboard](https://dashboard.render.com/)**.
2. Click **"New +"** in the top right and select **"Web Service"**.
3. Choose **"Build and deploy from a Git repository"** and select your GitHub repository.
4. Fill in the deployment settings:
   - **Name**: `pulse-audio-ecommerce` (or your preferred name)
   - **Region**: Choose closest to India (e.g. `Singapore` or `Oregon`)
   - **Branch**: `main`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT`
   - **Instance Type**: `Free`
5. Click **"Create Web Service"**.

---

## ⚙️ 4. Environment Variables (Optional for Live Payments & Meta Ads)

In your Render service dashboard, go to **"Environment"** tab and add the following keys when ready:

| Key | Example Value | Description |
| :--- | :--- | :--- |
| `STORE_BRAND` | `PULSE AUDIO` | Store brand name |
| `RAZORPAY_KEY_ID` | `rzp_live_xxxxxxxx` | Your Live Razorpay Key ID |
| `RAZORPAY_KEY_SECRET` | `your_razorpay_secret` | Your Live Razorpay Secret |
| `META_PIXEL_ID` | `102938475610293` | Meta Pixel ID for tracking |
| `META_CAPI_ACCESS_TOKEN` | `EAAB...` | Meta Conversions API Access Token |

*(Note: If you do not provide Razorpay keys, the built-in Sandbox Simulator automatically handles test orders).*

---

## 🎉 5. Your Live Webpage

Once Render finishes building (~1-2 minutes), you will receive a free, secure HTTPS URL:

- **Store Homepage**: `https://pulse-audio-ecommerce.onrender.com/`
- **Product Page**: `https://pulse-audio-ecommerce.onrender.com/product/pulse-sonic-pro`
- **Checkout**: `https://pulse-audio-ecommerce.onrender.com/checkout.html`
- **Interactive Swagger Docs**: `https://pulse-audio-ecommerce.onrender.com/docs`
