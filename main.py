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


def isString(char):
    # Implementar búsqueda de strings
    pass


def tokenize(s: str) -> list:
    tokens = []
    char = 0

    while char < len(json_str):
        # dict
        if char == "{":
            tokens.append = "OPEN_DICT"

        # str
        if isString(char):
            tokens.append = "STRING"

        # colon
        if isString():
            tokens.append = "STRING"

        # comma

        # int / float

        # arr
