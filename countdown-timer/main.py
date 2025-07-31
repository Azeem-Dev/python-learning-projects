import time

my_time = int(input("Enter the time in seconds: "))

# REVERSE THE GIVEN LIST

# EAMPLE
# print(list(reversed([1,2,3,4,5])))

# for x in reversed(range(0,my_time)):
#     time.sleep(1)

"""BETTER SOLUTION USING STEP"""
for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")  # format specifier
    time.sleep(1)


print("TIME'S UP!")
