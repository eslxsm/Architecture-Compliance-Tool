import json

def get_rules_for_building(region, district, building_type):
    # This is for the original /rules route (optional now)
    with open("rules_db.json", "r", encoding="utf-8") as f:
        all_rules = json.load(f)

    rules = []

    for r in all_rules:
        if r["building_type"] == building_type:
            # Match by exact region + district
            if r.get("region") == region and r.get("district") == district:
                rules.append(r)
            # Match region-only
            elif r.get("region") == region and r.get("district") is None:
                rules.append(r)
            # Fallback to national
            elif r.get("region") == "India":
                rules.append(r)

    return rules
