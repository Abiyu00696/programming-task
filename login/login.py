import time
from datetime import datetime, timedelta
user_info = {

    "james" : "pa55w0rd",
    "john" : "h3ll0",
    "robert" : "n07ing",
    "admin" : "admin"
}
def lock(lock_time):
    time.sleep(lock_time)
    return

running = True
allowed_attempt = 5
attempt = 1
lock_time = 5

print("++++ Welcome User +++++")
while running:
    if attempt > allowed_attempt:
        current_time = datetime.now()
        unlock_time = current_time + timedelta(seconds=lock_time)
        print("---------------------------------------")

        print("You have used all your allowd attempt\n")
        print(f"Current time: {current_time.strftime('%H:%M:%S')}")
        
        print(f"Pleas wait {lock_time / 60} min until {unlock_time.strftime('%H:%M:%S')}")
        print("System is locked")
        s
        lock(lock_time)
        attempt = 1
    
    username = input("Username: ")
    passwd = input("password: ")

    if username in user_info and  user_info[username] == passwd:
        print("\nCorrect credentials")
        print("Login Succuess full")
        running = False
    else:
        print(f"\nIncorrect credentials, Attemp left { (allowed_attempt - attempt )  }")


    attempt += 1