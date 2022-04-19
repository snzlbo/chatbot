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
    advertisement.maxSalary = cleanSalary(advertisement.minSalary)
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

# def cleanData(fileName):
#     data_set = pd.read_csv(fileName, sep='\t', error_bad_lines=False)
#     return normalizeDataSet(data_set)


# def normalizeDataSet(data_set):
#     ret = pd.DataFrame(columns=['parentCategory', 'category', 'url', 'employee',
#                                 'jobTitle', 'level', 'type', 'minSalary', 'maxSalary', 'isDealable', 'city', 'district', 'exactAddress', 'roles', 'requirements', 'additionalInfo', 'phoneNumber', 'fax', 'publishedDate'])
#     for index, row in data_set.iterrows():
#         maxSalary = cleanSalary(row['Max Salary'])
#         minSalary = cleanSalary(row['Min Salary'])
#         isDealable = cleanDealable(row['Is Dealable'])

#         if minSalary is None and maxSalary is None and isDealable is None:
#             isDealable = None

#         ret = ret.append({'parentCategory': row['Parent Category Name'],
#                           'category': row['Category Name '],
#                           'url': row['Link'],
#                           'employee': row['Employee Company'],
#                           'jobTitle': row['Title'],
#                           'level': cleanNone(row['Level']),
#                           'type': cleanNone(row['Type']),
#                           'minSalary': minSalary,
#                           'maxSalary': maxSalary,
#                           'isDealable': isDealable,
#                           'city': cleanNone(row['City/Province']),
#                           'district': cleanNone(row['District']),
#                           'exactAddress': cleanNone(row['Exact Address']),
#                           'roles': cleanNone(row['Roles']),
#                           'requirements': cleanNone(row['Requirements']),
#                           'additionalInfo': cleanNone(row['Additional Info']),
#                           'phoneNumber': cleanNone('Phone'),
#                           'fax': cleanNone(row['Fax']),
#                           'publishedDate': cleanNone(row['Ad Added Date'])
#                           }, ignore_index=True)
#     return ret


# get = cleanData(
#     '/Users/fate/Desktop/Bachelor/employementAnalysis/project/dataScrapping/data/2022-04-08adScrape.csv')
# get.to_csv('advertisement.csv')
