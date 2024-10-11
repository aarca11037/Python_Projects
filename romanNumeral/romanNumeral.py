
def roman_to_int(numeral):
    final_answer = 0

    if "IV" in numeral:
        final_answer += 4
        numeral = numeral.replace("IV", "")
    if "IX" in numeral:
        final_answer += 9
        numeral = numeral.replace("IX", "")
    if "XL" in numeral:
        final_answer += 40
        numeral = numeral.replace("XL", "")
    if "XC" in numeral:
        final_answer += 90
        numeral = numeral.replace("XC", "")
    if "CD" in numeral:
        final_answer += 400
        numeral = numeral.replace("CD", "")
    if "CM" in numeral:
        final_answer += 900
        numeral = numeral.replace("CM", "")

    for i in numeral:
        if i == "M":
            final_answer += 1000
        elif i == "D":
            final_answer += 500
        elif i == "C":
            final_answer += 100 
        elif i == "L":
            final_answer += 50
        elif i == "X":
            final_answer += 10
        elif i == "V":
            final_answer += 5
        elif i == "I":
            final_answer += 1
    
    return final_answer

numeral_input = (input("Please enter the Roman Numerals you want to convert: ")).upper()
print("The Roman Numeral translates to: " + str(roman_to_int(numeral_input)))

