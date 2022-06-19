# Read JSON as string

json_str = """
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


def tokenize(s: str) -> list:
    pass
