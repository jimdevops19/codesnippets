import requests
import datetime

def ask_data_example_1():
    response = requests.get("https://www.example1.com")
    if response.status_code == 200:
        return response.text
    else:
        return "Failed to fetch data from website 1"


# Start time:
start_time = datetime.datetime.now()

# Call function:
ask_data_example_1()

# End time
end_time = datetime.datetime.now()

execution_time = end_time - start_time

print(execution_time.total_seconds())