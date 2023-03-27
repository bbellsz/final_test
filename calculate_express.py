#central,northern,northeastern,eastern,western,southern
def calculate_express(weight,zone):
    if weight <= 0:
        price = 0
    elif weight > 20:
        price = 500
    elif weight>= 10:
        if zone == "central" or zone == "eastern" or zone == "western":
            price = 420
        else: price = 460
    else: 
        if zone == "central" or zone == "eastern" or zone == "western":
            price = 200
        else: price = 240
    return price
