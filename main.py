# Read JSON as string

s = """
{
    "k1": "value \"hey\" you",
    "k2": -10.57,
    "k3": {},
    "k4": {"k1": null},
    "k5": [1, "hello"]
}
"""


def isString(prev_char, char):
    inStr = True
    isQuotation = char == '"'
    escapeChar = prev_char == "\\"

    if isQuotation and not escapeChar:
        return inStr
    else:
        return not inStr


def tokenize(json_str: str) -> list:
    i = 0
    tokenized = []

    while i < len(json_str):
        char = json_str[i]
        if char == "{":
            tokenized.append("OPEN_DICT"+str(i))

        elif char == "}":
            tokenized.append("CLOSE_DICT"+str(i))

        elif char == ":":
            tokenized.append("COLON")

        elif char == ",":
            tokenized.append("COMMA")

        elif char == "[":
            tokenized.append("OPEN_ARR")

        elif char == "]":
            tokenized.append("CLOSE_ARR")

        i += 1

    return tokenized


print(tokenize(s))
