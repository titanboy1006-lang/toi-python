amount = int(input())
price = int(input())
membership = input()
sum = price * amount
def result(sum, percent):
    print(sum)
    discount = sum * percent / 100
    print(discount)
    print(sum - discount)
if membership == "y":
    if sum <= 500:
        result(sum, 10)
    elif sum > 500 and sum < 1000:
        result(sum, 15)
    elif sum > 1000:
        result(sum, 20)
elif membership == "n":
    if sum <= 500:
        result(sum, 5)
    elif sum > 500 and sum < 1000:
        result(sum, 10)
    elif sum > 1000:
        result(sum, 15)
