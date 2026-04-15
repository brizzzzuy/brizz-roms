# BrizZ Firmware Site

A Django-based platform for distributing custom Android ROM builds (HyperOS/AOSP), Magisk modules, and team news.

## Features

- **Devices** — Browse supported devices, filter by brand, download ROM builds per Android version
- **Tweaks** — Magisk modules and system tweaks with download links
- **Blog** — Team news and release announcements
- **About** — Meet the team

## Tech Stack

- Python 3.13 / Django 4.2
- SQLite (dev) / PostgreSQL-ready (prod)
- WhiteNoise for static file serving
- Gunicorn WSGI server

## Local Setup

```bash
# 1. Clone & enter
git clone <repo-url>
cd brizzz

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
cp .env.example .env
# Edit .env and set SECRET_KEY

# 5. Run migrations
python manage.py migrate

# 6. Create admin user
python manage.py createsuperuser

# 7. Start dev server
python manage.py runserver
```

Visit `http://127.0.0.1:8000` — admin panel at `/admin/`.

## Deployment (Railway / Heroku)

1. Set environment variables in your platform dashboard:
   - `SECRET_KEY` — a long random string
   - `DEBUG` — `False`
   - `ALLOWED_HOSTS` — your domain (e.g. `brizzz.up.railway.app`)

2. Collect static files (run once or add to build command):
   ```bash
   python manage.py collectstatic --noinput
   ```

3. The `Procfile` starts gunicorn automatically.

## Project Structure

```
brizzz/
├── core/         # Homepage & About page
├── devices/      # Device list & ROM build downloads
├── blog/         # Blog posts
├── tweaks/       # Magisk modules / tweaks
├── templates/    # Global base template
├── static/       # CSS and images
├── media/        # User-uploaded content (not committed)
├── firmwaresite/ # Django project settings & URL config
├── Procfile
├── requirements.txt
└── runtime.txt
```

## Admin

All content is managed via Django's built-in admin at `/admin/`. Add devices, builds, blog posts, team members, and tweaks there.
