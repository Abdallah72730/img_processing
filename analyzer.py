import statistics

def calculate_median(prices: list) -> float:


    sortedPrices = sorted(prices)

    median = 0
    if len(sortedPrices) % 2 == 0:
        median = ((sortedPrices[(len(sortedPrices)//2)-1]) + (sortedPrices[(len(sortedPrices)//2)])) / 2

        return median
    elif len(sortedPrices) % 2 != 0:
        median = sortedPrices[(len(sortedPrices)//2)]
        return median

def generate_report(prices: list) -> dict:
    
    if not prices:
        return {"error": "no price data provided"}

    median_price = calculate_median(prices)

    report = {
        "data_points": len(prices),
        "price_list": prices,
        "median": median_price,
        "minimum": min(prices),
        "maximum": max(prices),
        "range": round((max(prices) - min(prices)), 2)
    }

    return report



if __name__ == "__main__":
    test_prices = [299.99, 310.25, 225.62, 330.25, 285.99, 100.25]

    report = generate_report(test_prices)

    print("Testing analyzer with", test_prices)

    for key, value in report.items():
        if key != "price_list":
            print(f"{key} : {value}")
        else:
            continue
    
    import statistics
    print(" statistics.median check: ", statistics.median(test_prices))
