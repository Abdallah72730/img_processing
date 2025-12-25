import re 
9

def extract_prices_from_html(html : str) -> list:

    if not html:
        return []

    price_pattern = r"\$?\s*(\d{1,3}(?:,\d{3})*\.?\d{0,2})"


    #findall is basically just camparing everything in the html and extracts things that matches the pattern! 
    matches = re.findall(price_pattern, html)

    prices = []
    for match in matches:

        #rmoves commas
        clean_match = match.replace(",", "")

        try:
            price = float(clean_match)

            # check just to make sure prices make sense
            if 0 < price < 100000:
                prices.append(price)
        except ValueError:
            continue

    print(f"Found {len(prices)} in the raw HTML")

    return prices 


if __name__ == "__main__":

    html = """
    <div class = "s-item__price">299.99</div>
    <span>Price : USD 450.50 </span>
    <div>1,299.99</div>
    <div>Invalid: 12.345.36</div>
    """

    parsed_prices = extract_prices_from_html(html)

    print("Parsed prices from provided html is: ", parsed_prices)
