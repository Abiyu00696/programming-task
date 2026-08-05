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
        print(f"Current time attemmpt {current_time}")
        print("You have used all your allowd attempt")
        print(f"Pleas wait {lock_time / 60} min and try again")
        
        lock(lock_time)
        attempt = 0
    
    username = input("Username: ")
    passwd = input("password: ")

    if username in user_info and passwd in user_info[username]:
        print("\nCorrect credentials")
        print("Login Succuess full")
        running = False
    else:
        print(f"\nIncorrect credentials, Attemp left { (allowed_attempt - attempt )  }")


    attempt += 1