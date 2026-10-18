# plant_name="パキラ"
# plant_heights=[2,4,6]

# new_height=input("植物の高さを入力してください:")

# new_height=float(new_height)

# plant_heights.append(new_height)

# print(plant_name)
# print(plant_heights)

plant={
    "name":"パキラ",
    "heights":[2,4,6,8]
}

# print(plant["name"])
# print(plant["heights"])

# new_height=input("新しい高さを入力してください：")
# new_height=float(new_height)

# plant["heights"].append(new_height)

# first_height=plant["heights"][0]
# latest_height=plant["heights"][-1]

# growth = latest_height-first_height

# print("植物名",plant["name"])
# print("成長記録：",plant["heights"])
# print("成長した高さ",growth,"cm")

plant_name="パキラ"

first_height=float(input("最初の高さを入力してください(cm)："))

plant={
    "name":plant_name,
    "heights":[first_height]
}

new_height=float(input("今回の高さ："))

plant["heights"].append(new_height)

print(plant["heights"])