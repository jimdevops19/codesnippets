# RUN pip install prettytable first!
from dictionary_time_format_codes import formats, descriptions
import datetime
import sys
try:
    from prettytable import PrettyTable
except:
    print("Run pip install prettytable first!")
    sys.exit(1)

current = datetime.datetime.now()
t = PrettyTable()
t.title = current
t.field_names = ["Description", "Format", "Result"]

for description, fmt in zip(descriptions, formats):
    t.add_row([description, fmt, current.strftime(fmt)])

print(t)