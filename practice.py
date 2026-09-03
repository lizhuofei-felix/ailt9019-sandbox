def final_price(price, discount):
    return price * (1 - discount)

for price, discount in ((100, 0.2), (50, 0)):
    print(f"final_price({price}, {discount}) = {final_price(price, discount)}")
