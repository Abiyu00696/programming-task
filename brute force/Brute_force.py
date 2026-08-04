import time

start_time = time.time()
def brt_frc(SECRET_PASS):
    print("++++ BRUTE FORCE PASSWORD GUESSER +++++")
    attempt = 0

    for i in range(10000):
        if i == SECRET_PASS:
            return i
        print(f"Attempting {i}")


SECRET_PASS = 4669

pin = brt_frc(SECRET_PASS)

end_time = time.time()
time_taken = end_time - start_time 

print(pin)
print(time_taken)