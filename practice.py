def final_price(price, discount):
    result = price * (1 - discount)
    return result


price1 = 100
discount1 = 0.2

price2 = 50
discount2 = 0

result1 = final_price(price1, discount1)
result2 = final_price(price2, discount2)

print("final_price(100, 0.2) =", result1)
print("final_price(50, 0) =", result2)
