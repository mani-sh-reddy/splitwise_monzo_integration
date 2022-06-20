from splitwise import Splitwise
from datetime import datetime, timedelta
import AUTH  # consumer_key, consumer_secret, api_key


def yesterday(frmt='%Y-%m-%d', string=True):
    yesterday = datetime.now() - timedelta(1)
    if string:
        return yesterday.strftime(frmt)
    return yesterday


def tomorrow(frmt='%Y-%m-%d', string=True):
    tomorrow = datetime.now() + timedelta(1)
    if string:
        return tomorrow.strftime(frmt)
    return tomorrow


splitwise_object = Splitwise(AUTH.consumer_key, AUTH.consumer_secret, api_key=AUTH.api_key)

# for index, group in enumerate(splitwise_object.getGroups()):
#     splitwise_groups = splitwise_object.getGroups()[index]
#     print(splitwise_groups.id, splitwise_groups.name)

splitwise_expenses = splitwise_object.getExpenses(group_id=24996058, dated_after=yesterday(), dated_before=tomorrow())
for index, expense in enumerate(splitwise_expenses):
    users_list = []
    for user in expense.users:
        users_list.append(user.first_name)
    if "Mani" in users_list:
        print(expense.id, expense.cost, expense.description, expense.date, users_list)
