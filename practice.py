"""Small function example from the AILT9019 Getting Started Guide."""


def final_price(price: float, discount: float) -> float:
    """Return the price after applying a decimal discount."""
    return price * (1 - discount)


if __name__ == "__main__":
    examples = ((100, 0.20), (50, 0))
    for price, discount in examples:
        print(f"final_price({price}, {discount}) = {final_price(price, discount)}")
