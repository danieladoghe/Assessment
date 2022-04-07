ENGLISH = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}
SCALES = {1000 ** 1: "thousand", 1000 ** 2: "million", 1000 ** 3: "billion"}
def say(number):
    """Given a number from 0 to 999,999,999,999, returns that number spelled
     out in English.
 
    :param number: int - the number
    :return: str - the number in English
    """
    if not 0 <= number <= 999999999999:
        raise ValueError("input out of range")
    word = []
    chunks = []
    while number:
        number, chunk = divmod(number, 1000)
        chunks.append(chunk)
    for scale, chunk in enumerate(chunks):
        # Do nothing for zeroes.
        if chunk == 0:
            continue
        sections = []
        tens = chunk % 100
        hundreds = chunk // 100
        # One through 19, or multiple of 10, ignore zeros.
        if tens == 0:
            pass
        elif 1 <= tens < 20 or tens % 10 == 0:
            sections.append(ENGLISH[tens])
        else:
            ones = tens % 10
            tens = tens // 10 * 10
            sections.append(f"{ENGLISH[tens]}-{ENGLISH[ones]}")
        # Hundreds
        if hundreds:
            sections.insert(0, f"{ENGLISH[hundreds]} hundred")
        # Scaling: thousands, millions, billions
        if scale > 0:
            sections.append(SCALES[1000 ** scale])
        word.insert(0, " ".join(sections))
    return " ".join(word) or "zero"