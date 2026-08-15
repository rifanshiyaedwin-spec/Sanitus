# Netlify Deployment Guide for PlantaSanitus🌿

All required Netlify deployment files have been configured for **PlantaSanitus🌿**:
- `netlify.toml`: Route redirects & Netlify Functions config.
- `functions/app.py`: Serverless WSGI wrapper for Flask.
- `requirements.txt`: Python dependencies & `serverless-wsgi`.

---

## 🚀 Option 1: Deploy via GitHub (Recommended)

1. Push your project to a GitHub repository:
   ```bash
   git init
   git add .
   git commit -m "Configure Netlify Serverless Deployment"
   git branch -M main
   git remote add origin https://github.com/your-username/plantdisease.git
   git push -u origin main
   ```

2. Open [Netlify Dashboard](https://app.netlify.com/):
   - Click **Add new site** ➔ **Import an existing project**.
   - Select **GitHub** and pick your `plantdisease` repository.

3. Netlify will auto-detect settings from `netlify.toml`:
   - **Build Command**: `pip install -r requirements.txt`
   - **Functions directory**: `functions`
   - Click **Deploy Site**!

---

## 🌐 Setting Custom Domain (https://plantasanitus.com)

1. In your Netlify Site Dashboard, navigate to **Site Settings** ➔ **Domain Management**.
2. Click **Add custom domain** and enter `plantasanitus.com`.
3. Update your domain DNS records at your domain registrar:
   - **A Record**: Point `@` to Netlify IP `75.2.60.5`
   - **CNAME Record**: Point `www` to `your-site-name.netlify.app`
4. Netlify will automatically generate a free **HTTPS SSL Certificate**!
