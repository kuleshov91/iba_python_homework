# Торговая фирма в первый день работы реализовала товаров на P тыс. руб.,
# а затем ежедневно увеличивала выручку на 3%. Какой будет выручка фирмы в тот день,
# когда она впервые превысит заданное значение Q?
# Сколько дней придется торговать фирме для достижения этого результата?


totalRevenue = int(input("Enter total revenue: \n"))
revenue = 30000
daysCount = 1

while totalRevenue - revenue > 0:
    totalRevenue -= revenue
    revenue *= 1.03
    revenue = round(revenue, 2)
    daysCount += 1


print("company will reach a goal at", daysCount, "day")
print("revenue at", daysCount, "day is", revenue)
