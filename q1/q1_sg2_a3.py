year = int(input("Enter your birth year: "))
print(year)
if year < 1900:
    print("Year should not be before 1900.")
    exit()
cycle = (year-1900) % 12
if cycle == 0:
    sign = "Rat (鼠 / Shǔ)"
elif cycle == 1:
    sign = "Ox (牛 / Niú)"
elif cycle == 2:
    sign = "Tiger (虎 / Hǔ)"
elif cycle == 3:
    sign = "Rabbit (兔 / Tù)"
elif cycle == 4:
    sign = "Dragon (龙 / Lóng)"
elif cycle == 5:
    sign = "Snake (蛇 / Shé)"
elif cycle == 6:
    sign = "Horse (马 / Mǎ)"
elif cycle == 7:
    sign = "Goat (羊 / Yáng)"
elif cycle == 8:
    sign = "Monkey (猴 / Hóu)"
elif cycle == 9:
    sign = "Rooster (鸡 / Jī)"
elif cycle == 10:
    sign = "Dog (狗 / Gǒu)"
else:
    sign = "Pig (猪 / Zhū)"

print(f"Your Chinese Zodiac Sign is: {sign}")
    
