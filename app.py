from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Load full dataset
with open("kmbr_full_dataset.json", "r", encoding="utf-8") as f:
    full_dataset = json.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/building/<building_type>")
def building_type_rules(building_type):
    rules = full_dataset.get("building_types", {}).get(building_type.lower(), [])
    return render_template("building_type_rules.html", building_type=building_type, rules=rules)

# ----------- CALCULATORS ----------------

@app.route("/calculator/fsi", methods=["GET", "POST"])
def fsi():
    result = None
    if request.method == "POST":
        plot_area = float(request.form["plot_area"])
        builtup_area = float(request.form["builtup_area"])
        result = builtup_area / plot_area if plot_area else 0
    return render_template("fsi_calculator.html", result=result)

@app.route("/calculator/parking", methods=["GET", "POST"])
def parking():
    result = None
    if request.method == "POST":
        area = float(request.form["area"])
        building_type = request.form["building_type"]
        rules = {
            "residential": area / 75,
            "hospital": area / 60,
            "mall": 1260 / 90 + max(0, area - 1260) / 60
        }
        result = round(rules.get(building_type, 0), 2)
    return render_template("parking_calculator.html", result=result)

@app.route("/calculator/setback", methods=["GET", "POST"])
def setback():
    result = None
    if request.method == "POST":
        building_type = request.form["building_type"]
        height = float(request.form["height"])

        base_setbacks = {
            "residential": 3,
            "lodging": 6,
            "hospital": 6,
            "industrial": 9
        }

        increment_rule = {
            "residential": 0.5,
            "lodging": 0.5,
            "hospital": 0.5,
            "industrial": 0.5
        }

        base = base_setbacks.get(building_type, 3)
        increment = increment_rule.get(building_type, 0.5)

        extra = ((height - 10) // 3) * increment if height > 10 else 0
        total = round(base + extra, 2)
        result = f"{total} meters (Base: {base}m + Extra: {extra}m)"

    return render_template("setback_calculator.html", result=result)

@app.route("/calculator/toilet", methods=["GET", "POST"])
def toilet():
    result = {}
    if request.method == "POST":
        occupants = int(request.form["occupants"])
        building_type = request.form.get("building_type", "general")

        if building_type == "hospital":
            result["inpatients"] = max(1, occupants // 8)
            result["outpatients_male"] = max(1, occupants // 100)
            result["outpatients_female"] = max(2, occupants // 100)
        elif building_type == "assembly":
            result["male"] = max(1, occupants // 50)
            result["female"] = max(1, occupants // 30)
        else:
            result["male"] = max(1, occupants // 50)
            result["female"] = max(1, occupants // 30)

    return render_template("toilet_calculator.html", result=result)

@app.route("/calculator/coverage", methods=["GET", "POST"])
def coverage():
    result = None
    allowed = None
    if request.method == "POST":
        plot_area = float(request.form["plot_area"])
        builtup_area = float(request.form["builtup_area"])
        building_type = request.form.get("building_type", "residential")

        max_coverage = {
            "residential": 65,
            "lodging": 60,
            "hospital": 50,
            "storage": 50
        }

        allowed = max_coverage.get(building_type, 100)
        result = round((builtup_area / plot_area) * 100, 2) if plot_area else 0

    return render_template("coverage_calculator.html", result=result, allowed=allowed)

@app.route("/calculator/occupancy", methods=["GET", "POST"])
def occupancy():
    result = None
    if request.method == "POST":
        floor_area = float(request.form["floor_area"])
        usage = request.form["usage"]
        factors = {
            "assembly": 1.2,
            "educational": 4,
            "residential": 9.3,
            "business": 10,
            "mercantile": 3,
            "industrial": 10
        }
        result = int(floor_area / factors.get(usage, 1))
    return render_template("occupancy_calculator.html", result=result)

# -----------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
