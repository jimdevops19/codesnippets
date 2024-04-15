import datetime
import requests

def timer(func):
    def wrapper(*args, **kwargs):
        # Start time:
        start_time = datetime.datetime.now()

        result = func(*args, **kwargs)

        end_time = datetime.datetime.now()

        execution_time = end_time - start_time

        print(f"{func.__name__} ran in: {execution_time.total_seconds()}")

        return result

    return wrapper


@timer
def ask_data_example(website):
    print(f"Requesting something from: {website}")
    response = requests.get(website)

    if response.status_code == 200:
        return response.text
    else:
        return "Failed to fetch data from website 1"



# Call function:
web1 = ask_data_example("https://www.example1.com")
print(web1)