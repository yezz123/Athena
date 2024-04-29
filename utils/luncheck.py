def luhnCheck(card_number):
    """checks to make sure that the card passes a luhn mod-10 checksum"""

    sum = 0
    num_digits = len(card_number)
    oddeven = num_digits & 1

    for count in range(num_digits):
        digit = int(card_number[count])

        if not ((count & 1) ^ oddeven):
            digit *= 2
        if digit > 9:
            digit -= 9

        sum += digit

    return (sum % 10) == 0
