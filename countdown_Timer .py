import time 

def countdown(t):
    while t > 0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")  # Same line print (updates time)
        time.sleep(1)
        t -= 1

    print('Timer completed!')

# Taking user input
try:
    t = int(input('Enter the time in seconds: '))
    countdown(t)
except ValueError:
    print("Please enter a valid number!")
