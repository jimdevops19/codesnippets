from datetime import datetime

current = datetime.now() # A datetime object
new_years = datetime(year=2025, month=1, day=1)

diff = new_years - current #timedelta
print()

from datetime import datetime, timedelta

before = datetime.now()

import time
time.sleep(2)

after = datetime.now()

diff = after-before
print(diff)

print(type(before))
print(type(after))
print(type(diff))