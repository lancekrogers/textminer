import re

def binary(bin):
    return re.match("0|1", bin)


def binary_even(even_bin):
    answer = bool
    try:
        if even_bin[0] == 0 and len(even_bin) > 1:
            new = even_bin[1:]
            bine = int(new, base=2)
            answer = (bine % 2) == 0
        else:
            new = even_bin
            bine = int(new, base=2)
            answer = (bine % 2) == 0
    except:
        answer = False
    return answer


def hex(hexnum):
    answer = bool
    express = re.findall(r"[a-fA-F0-9]", hexnum)
    original = [_ for _ in hexnum]
    new = [_ for _ in express]
    if len(hexnum) == 0:
        answer = False
    else:
        answer = len(original) == len(new)
    return answer


def word(single):
    express = re.findall(r'[a-zA-z]', single)
    if len(single)  == 0:
        return False
    if len(express) == len(single):
        return False
    else:
        return True

def words(series):
     pass


def phone_number(number):
    answer = bool
    new = re.findall(r'[\d{3}\d{3}\d{4}]', number)
    print(new)
    if len(new) == 10:
        answer = True
    else:
        answer = False
    return answer


def money(currency):
    if len(currency) < 2:
        return False
    if re.fullmatch(r"\$.*\.\d{1}|\$.*\.\d{3}|\${2}\d.*|\$\d*,\d{1,2}|\d+", currency):
        return False
    else:
        return True

def zipcode(zip):
    postal_code = re.match('^\d{5}(-\d{4})?$', zip)
    return postal_code




def date(notation):
    pass
