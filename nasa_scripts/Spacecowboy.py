# Astrophysical constants
sol_rad = 695700    # Radius of the sun in kilometers
radj = 69911        # Radius of jupiter in kilometers
G = 6.67408 * (10 ** -20) # Gravity constant in km^3 * kg^-1 * s^-2
massj = 1.898 * (10 ** 27) # Mass of jupiter in kilograms

# Common functions
def implode(i, delimeter) :
    imploded = "";
    for e in i :
        imploded += e + delimeter

    imploded = imploded[:-len(delimeter)]
    return imploded