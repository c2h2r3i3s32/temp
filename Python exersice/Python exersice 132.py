def get_province_and_address_type(postal_code):
    province_map = {
        'A': 'Newfoundland',
        'B': 'Nova Scotia',
        'C': 'Prince Edward Island',
        'E': 'New Brunswick',
        'G': 'Quebec',
        'H': 'Quebec',
        'J': 'Quebec',
        'K': 'Ontario',
        'L': 'Ontario',
        'M': 'Ontario',
        'N': 'Ontario',
        'P': 'Ontario',
        'R': 'Manitoba',
        'S': 'Saskatchewan',
        'T': 'Alberta',
        'V': 'British Columbia',
        'X': 'Nunavut or Northwest Territories',
        'Y': 'Yukon'
    }
    
    first_char = postal_code[0].upper()
    if first_char not in province_map:
        return "Error: Invalid first character in postal code."
    
    province = province_map[first_char]
    
    if postal_code[1] == '0':
        address_type = "rural"
    else:
        address_type = "urban"
    
    return f"The postal code is for an {address_type} address in {province}."

postal_code = input("Enter a Canadian postal code").upper()
    
if len(postal_code) < 6 or not postal_code[1].isdigit() or not postal_code[4].isdigit():
    print("Error: Invalid postal code format.")
else:
    result = get_province_and_address_type(postal_code)
    print(result)


