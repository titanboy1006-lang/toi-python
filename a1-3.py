money = int(input("money value(money:)"))
ten_baht = money // 10
money = money % 10
five_baht = money // 5
money = money % 5
two_baht = money // 2
money = money % 2
one_baht = money
print("10 baht", ten_baht,"\n","5 baht", five_baht,"\n","2 baht", two_baht,"\n","1 baht", one_baht,"\n")