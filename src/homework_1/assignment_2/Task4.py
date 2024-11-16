#Фирма ежегодно на протяжении n лет закупала оборудование стоимостью соответственно
# s1, s2, ..., sn pублей в год (эти числа вводятся и обрабатываются последовательно).
# Ежегодно в результате износа и морального старения (амортизации) все имеющееся оборудование уценивается на р%.
# Какова общая стоимость накопленного оборудования за n лет?

years = int(input("Enter years: "))
depreciation = int(input("Enter depreciation in percents: "))
totalEquipmentCost = 0
equipmentCost = []

for i in range(years):
    equipmentCost.append(int(input(f"Enter equipment cost in {i + 1} year: ")))

for i in range(len(equipmentCost)):
    for j in range(len(equipmentCost) - i):
        equipmentCost[i] *= 1 - depreciation / 100
    totalEquipmentCost += round(equipmentCost[i], 2)

print("total equipment cost:", totalEquipmentCost)
