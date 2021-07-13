def to_roman(dinput):
    dinput = int(dinput)
    romanlist = [(1000,"M"),(900,"CM"), (500,"D"), (400,"CD"), (100,"C"), (90,"XC"), (50,"L"), (40, "XL"), (10,"X"), (9,"IX"), (5,"V"), (4,"IV"), (1, "I")]
    for roman_threshold, roman_numeral in romanlist:
       if dinput > roman_threshold:
           print(roman_numeral)
           dinput -= roman_threshold
    return dinput


def to_decimal(rinput):
    doutput = 0
    decimal_list = [(1000,"M"), (900,"CM"), (500,"D"), (400,"CD"), (100,"C"), (90,"XC"), (50,"L"), (40, "XL"), (10,"X"), (9,"IX"), (5,"V"), (4,"IV"), (1, "I")]
    rinput_digits = [char for char in rinput]
    for char in rinput_digits:
        for decimal_number, roman_digits in decimal_list:
            if char == roman_digits:
                doutput += decimal_number
    return doutput


x = input("Enter 1 to convert a decimal number to roman form, 2 to convert a roman number to decimal form.")
if x == "1":
    decimal_input = input("Enter decimal number.")
    to_roman(decimal_input)
elif x == "2":
    roman_input = input("Enter roman number.")
    print(to_decimal(roman_input))