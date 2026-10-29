import json
import os

if os.path.exists("plant.json"):
    with open("plant.json","r",encoding="utf-8")as file:
        plant=json.load(file)

    print("前回の記録を読み込みました！")

else:
    plant_name = input ("植物の名前:")
    first_height = float(input("最初の高さ(cm):"))

    plant={
        "name":plant_name,
        "height":[first_height]
    }

    print("新しい植物を登録しました！")


new_height = float(input("今回の高さ(cm):"))

plant["heights"].append(new_height)

growth = plant["heights"][-1] - plant["heights"][0]

print("成長記録:",plant["heights"])
print("成長量:",growth,"cm")

with open("plant.json","w",encoding="utf-8")as file:
    json.dump(plant,file,ensure_ascii=False,indent=4)