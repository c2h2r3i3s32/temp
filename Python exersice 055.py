radiation = int(input("Electromagnetic radiation"))

if radiation <= 3 * 10 ** 9:
    print("Radio waves")
if radiation >= 3 * 10 ** 9 and radiation <= 3 * 10 ** 12:
    print("Microwaves")
if radiation >= 3 * 10 ** 12 and radiation <= 4.3 * 10 ** 14:
    print("Infrared light")
if radiation >= 4.3 * 10 ** 14 and radiation <= 7.5 * 10 ** 14:
    print("Visible light")
if radiation >= 7.5 * 10 ** 14 and radiation <= 3 * 10 ** 17:
    print("Ultraviolet light")
if radiation >= 3 * 10 ** 17 and radiation <= 3 * 10 ** 19:
    print("X-rays")
if radiation >= 3 * 10 ** 19:
    print("Gamma rays")