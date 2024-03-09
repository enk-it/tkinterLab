def validate_float(string):
    validSymbols = "0123456789.-"
    validNumbers = "0123456789"
    validMasks = ['n', 'n.n', '-n.n', '-n']

    if len(string) == 0:
        return False

    for symbol in string:
        if symbol not in validSymbols:
            return False

    mask = string
    for symbol in validNumbers:
        mask = mask.replace(symbol, 'n')
    last_mask = -1
    while last_mask != mask:
        last_mask = mask
        mask = mask.replace('nn', "n")
    if mask not in validMasks:
        return False

    return True