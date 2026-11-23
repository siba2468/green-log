
import json
from pathlib import Path
from datetime import date
from flask import Flask, request, redirect

app = Flask(__name__)
DATA_FILE = Path(__file__).with_name("plant.json")


@app.route("/", methods=["GET", "POST"])
def home():
    # JSONファイルから全植物のデータを読み込む
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

        plant_id = request.args.get("id", default=0, type=int)
        plant = data["plants"][plant_id]

    # 水やり記録がなければ追加
    if "watering" not in plant:
        plant["watering"] = []

    if request.method == "POST":

        # 高さを記録する
        if request.form["action"] == "height":
            new_height = float(request.form["height"])
            plant["heights"].append(new_height)

        # 水やりを記録する
        elif request.form["action"] == "water":
            today = date.today().isoformat()
            plant["watering"].append(today)

        # 全植物のデータをJSONに保存する
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        return redirect("/")

    name = plant["name"]

    name = plant["name"]
    heights = plant["heights"]
    latest_height = heights[-1]
    growth = latest_height - heights[0]

    temperature = 24.5
    humidity = 55.0
    pressure = 1013.2

    # 最後の水やり日
    if plant["watering"]:
        last_water = plant["watering"][-1]
    else:
        last_water = "まだ記録がありません"

    return f"""
    <html>
    <head>
        <meta charset="utf-8">
        <title>Green Log</title>
    </head>
    <body>
        <h1>Green Log 🌱</h1>
        <h3>表示する植物を選択 🌿</h3>
        
        <form method="GET">
            <select name="id">
                <option value="0">パキラ</option>
                <option value="1">テーブルヤシ</option>
            </select>
            <button type="submit">表示する</button>
        </form>
        <h2>植物名：{name}</h2>

        <p>現在の高さ：{latest_height} cm</p>
        <p>成長量：{growth} cm</p>
        <p>成長記録：{heights}</p>

        <h3>お部屋の環境 🌡️</h3>
        <p>温度：{temperature} ℃</p>
        <p>湿度：{humidity} %</p>
        <p>気圧：{pressure} hPa</p>
        <hr>

        <hr>

        <h3>高さを記録する 📏</h3>
        <form method="POST">
            <input type="hidden" name="action" value="height">
            <input type="number" name="height"
                   step="0.1" min="0" required
                   placeholder="今回の高さ(cm)">
            <button type="submit">記録する</button>
        </form>

        <hr>

        <h3>水やり記録 💧</h3>
        <p>最後の水やり：{last_water}</p>

        <form method="POST">
            <input type="hidden" name="action" value="water">
            <button type="submit">水やりした！</button>
        </form>

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
