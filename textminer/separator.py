import re

def words(words):
    word = r'[\W\s\D\d\b\B\w-]'
    return re.fullmatch(word, words)


def phone_number(number):

    return

def money(currency):
    pass

def zipcode(zips):
    postal_code = re.match('^\d{5}(-\d{4})?$', zips)
    return postal_code


def date(date):
    return re.fullmatch(r'^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[1,3-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$', date)

