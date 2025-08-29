from flask import Flask, render_template, jsonify, request, abort
import json
from pathlib import Path

app = Flask(__name__)

DATA_PATH = Path(__file__).parent / "data" / "poi_goa.json"

def load_poi():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/explore")
def explore():
    # optional query params: q (search), category
    q = request.args.get("q", "", type=str).lower().strip()
    category = request.args.get("category", "", type=str).lower().strip()
    pois = load_poi()
    filtered = []
    for p in pois:
        if q and (q not in p["name"].lower() and q not in p.get("area","").lower()):
            continue
        if category and category != p["category"].lower():
            continue
        filtered.append(p)
    return render_template("explore.html", pois=filtered, q=q, category=category)

@app.route("/poi/<poi_id>")
def poi_detail(poi_id):
    pois = load_poi()
    for p in pois:
        if p["id"] == poi_id:
            return render_template("poi_detail.html", poi=p)
    abort(404)

@app.route("/ar")
def ar_view():
    # This page uses AR.js (location-based) to place POIs around the user.
    # The browser will ask for geolocation and camera permissions.
    return render_template("ar.html")

@app.route("/api/poi")
def api_poi():
    pois = load_poi()
    q = request.args.get("q", "", type=str).lower().strip()
    category = request.args.get("category", "", type=str).lower().strip()
    if q or category:
        pois = [p for p in pois if
                (not q or (q in p["name"].lower() or q in p.get("area","").lower()))
                and (not category or category == p["category"].lower())]
    return jsonify(pois)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)