import time

start_time = time.time()
def brt_frc(SECRET_PASS):
    print("+++++ BRUTE FORCE PASSWORD GUESSER +++++")
    attempt = 0
    count_attempt = 0
    for i in range(0, 10000):
        if i == SECRET_PASS:
            return i ,count_attempt
        print(f"Attempting {str(i).zfill(4)}")
        count_attempt += 1 


SECRET_PASS = 4669

pin, count_attempt = brt_frc(SECRET_PASS)

end_time = time.time()
time_taken = end_time - start_time 
print()
print("="*25)
print(f"PIN Fund: {str(pin).zfill(4)}")
print("Time taken: ","%.2f" % time_taken,"sec")
print(f"No of attempt: {count_attempt}")
print("="*25)
