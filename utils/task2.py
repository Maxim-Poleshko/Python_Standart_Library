import csv
from utils.members import list_members

def study_group(list_memb: list)
    """
    Create a simple csv file of fictional study group
    """
    with open('names.csv', 'w', newline='') as csvfile:
        fieldnames = ['First_name', 'Last_name', 'Telegram_tag']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(list_memb)
