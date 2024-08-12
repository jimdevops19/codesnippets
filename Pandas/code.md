# Pandas Tutorial code:

## Basic Actions & Filtering:

```python
# Basic Operations
df.head()
df.tail()
df.sort_values(by="Bronze Medal")
df.sort_values(by="Bronze Medal", ascending=False)
df.sort_values(by="Bronze Medal", ascending=False).head(2)
df.info()
df["country_code"]
df[["country_code", "Total"]]

# Filtering
import pandas as pd

df = pd.read_csv("medals_total.csv")

one_gold_medal = df[df["Gold Medal"] == 1]

only_u = df[df["country_code"].str.startswith("U")]

more_than = df[df["Total"] > 25]

complex_exp = df[(df["country_code"].str.startswith("U")) & (df["Total"] > 25)]

print(complex_exp)
```

## Grouping:

```python
# Group by column
import pandas as pd

df = pd.read_csv("schedules.csv")

day_groups = df.groupby("day")

print(type(day_groups))

for group_name, df in day_groups:
    print(group_name)
    print(df)
```

```python
# By 2 column
import pandas as pd

df = pd.read_csv("schedules.csv")

day_groups = df.groupby(["day", "status"])
for group_name, df in day_groups:
    print(group_name)
```

```python
# Not included in the video: Add column and group by the column
import pandas as pd

df = pd.read_csv("schedules.csv")
city_name = "nice"

check_if_paris = df["location_description"].str.lower().str.contains(city_name)

df["is_in_nice"] = check_if_paris

location_groups = df.groupby("is_in_nice")

for lg, d in location_groups:
    print(lg)
    print(d)
```

