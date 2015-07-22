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
    pass
