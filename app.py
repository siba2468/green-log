
import json
from pathlib import Path
from flask import Flask, request, redirect

app = Flask(__name__)
DATA_FILE = Path(__file__).with_name("plant.json")

@app.route("/", methods=["GET", "POST"])
def home():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        plant = json.load(file)

    if request.method == "POST":
        new_height = float(request.form["height"])
        plant["heights"].append(new_height)

        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(plant, file, ensure_ascii=False, indent=4)

        return redirect("/")

    name = plant["name"]
    heights = plant["heights"]
    latest_height = heights[-1]
    growth = latest_height - heights[0]

    return f"""
    <html>
    <head>
        <meta charset="utf-8">
        <title>Green Log</title>
    </head>
    <body>
        <h1>Green Log 🌱</h1>
        <h2>植物名：{name}</h2>
        <p>現在の高さ：{latest_height} cm</p>
        <p>成長量：{growth} cm</p>
        <p>成長記録：{heights}</p>

        <hr>

        <h3>高さを記録する</h3>
        <form method="POST">
            <input type="number" name="height"
                   step="0.1" min="0" required
                   placeholder="今回の高さ(cm)">
            <button type="submit">記録する</button>
        </form>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
