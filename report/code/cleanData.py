import pandas as pd
from .classTypes import Advertisement
from datetime import datetime


def cleanSalary(salary) -> float:
    if isinstance(salary, str) and salary != '' and salary != 'None':
        return float(salary.replace(',', ''))
    return None


def cleanDealable(deal) -> bool:
    if deal == 'Тохиролцоно':
        return True
    return False


def cleanNone(text) -> str:
    if isinstance(text, str) and text != 'None' and text != '':
        return text
    return None

def cleanAdObject(advertisement: Advertisement) -> Advertisement:
    advertisement.level = cleanNone(advertisement.level)
    advertisement.type = cleanNone(advertisement.type)
    advertisement.minSalary = cleanSalary(advertisement.minSalary)
    advertisement.maxSalary = cleanSalary(advertisement.maxSalary)
    advertisement.isDealable = cleanDealable(advertisement.minSalary)
    advertisement.location.city = cleanNone(advertisement.location.city)
    advertisement.location.district = cleanNone(
        advertisement.location.district)
    advertisement.location.exactAddress = cleanNone(
        advertisement.location.exactAddress)
    advertisement.roles = cleanNone(advertisement.roles)
    advertisement.requirements = cleanNone(advertisement.requirements)
    advertisement.additionalInfo = cleanNone(advertisement.additionalInfo)
    advertisement.contact.phoneNumber = cleanNone(
        advertisement.contact.phoneNumber)
    advertisement.contact.fax = cleanNone(advertisement.contact.fax)
    advertisement.adAddedDate = cleanNone(advertisement.adAddedDate)

    return advertisement
