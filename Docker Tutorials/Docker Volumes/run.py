import time
from datetime import datetime

def write_log():
    with open("/app/logs/info.log", "a") as log_file:
        while True:
            current_time = datetime.now()
            formatted_current_time = f"{current_time:%Y-%m-%d %H:%M:%S}"
            log_file.write(f"{formatted_current_time} - This program writes logs every 3 seconds\n")
            log_file.flush()
            time.sleep(3)

if __name__ == "__main__":
    write_log()
