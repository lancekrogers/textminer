import re


def phone_numbers(text):
    return re.findall(r"\(\d{3}\).\d{3}.\d{4}", text)




# hard mode

def emails(text):
    pass

