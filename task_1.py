BASE_RATE = 30.0
FAT_VALUE = 0.40
SNF_VALUE = 0.30

farmer_id = input("Enter farmer ID: ")
total = 0

for i in range(1, 4):
    litres = float(input("Enter litres: "))
    fat = float(input("Enter fat: "))
    snf = float(input("Enter SNF: "))

    if litres < 0 or fat < 2 or fat > 7 or snf < 0:
        print("Invalid input")
        continue

    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)

    rate = BASE_RATE + fat_steps * FAT_VALUE + snf_steps * SNF_VALUE
    amount = round(litres * rate, 2)
    total = total + amount

    print("Rate:", round(rate, 2))
    print("Amount:", amount)

print("Farmer ID:", farmer_id)
print("Total payment:", round(total, 2))