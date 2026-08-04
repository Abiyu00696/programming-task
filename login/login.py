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

running = True
allowed_attempt = 5
attempt = 0
while running:
    print("++++ Welcome User +++++")
    
    username = input("Username: ")
    passwd = input("password: ")

    if username in user_info and passwd in user_info[username]:
        print("Correct")