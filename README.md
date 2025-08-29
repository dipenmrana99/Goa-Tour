# Personalized Smart Tourism Concierge (Goa) — Flask + AR.js

A mini web app that helps travelers explore Goa with:
- **Explore**: searchable list + Leaflet map of attractions
- **AR Tours**: location-based AR labels for nearby POIs (AR.js + A-Frame)
- **Details**: rich pages with visiting info

## Quick start

```bash
# 1) Create and activate a virtual environment (optional but recommended)
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Run
python app.py
# The app will run at http://127.0.0.1:5000
```

> **AR Page Tips**
> - Use a **mobile device** for best results.
> - Allow **camera** and **location** permissions.
> - Go outside with good GPS visibility.
> - AR labels appear near the real-world positions of the POIs.

## Project structure

```
goa_ar_concierge/
├─ app.py
├─ requirements.txt
├─ data/
│  └─ poi_goa.json
├─ static/
│  ├─ css/styles.css
│  └─ js/main.js
└─ templates/
   ├─ base.html
   ├─ index.html
   ├─ explore.html
   ├─ ar.html
   └─ poi_detail.html
```

## Personalization ideas (next steps)
- User profile & preferences (e.g., loves beaches, budget, veg-friendly) to re-rank POIs.
- Itinerary builder with time windows and travel times.
- Live weather + best-hour suggestions.
- Offline tile caching for maps.
- Add more POIs and categories (cafés, waterfalls, treks, museums, night markets).