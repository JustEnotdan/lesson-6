a = open("bakery.csv", "w+", encoding="utf-8")
a.write("5978,5\n8914,3\n7879,1\n1573,7")
num = input("Введите число(если их несколько, записывайте через пробел):   ")
a.seek(0)
if num == "":
    print(a.read())
elif len(num.split()) == 1:
    print(a.readlines()[int(num)-1:])
elif len(num.split()) == 2:
    print(a.readlines()[int(num.split()[0]) - 1: int(num.split()[1])])
