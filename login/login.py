import time

user_info = {

    "james" : "pa55w0rd",
    "john" : "h3ll0",
    "robert" : "n07ing",
    "michael" : "z3rr0",
    "william" : "g0n3",
    "david" : "1o5t",
    "richard" : "urb35t",
    "charles" : "t3I3gram",
    "joseph" : "halu",
    "thomas" : "b00s",
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
        print("You have used all your allowd attempt")
        print(f"Pleas wait {lock_time / 60} min. and try again")
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