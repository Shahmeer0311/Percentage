

maths = int(input("Maths Score /40"))
english = int(input("English score /25"))
history= int(input("History score /35"))
chemistry = int(input("chemistry score /42"))
biology = int(input("Biology score /52"))
physics = int(input("Physics score /51"))

total = maths + english + history + chemistry + biology + physics
percentage = (total / 255) * 100
print(percentage)
