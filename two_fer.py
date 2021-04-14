def two_fer(name = None):
    str = "One for you, one for me."
    if name:
        str = f"One for {name}, one for me."
        return str
    else:
        return str
