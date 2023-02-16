import time

def time_as_string():
    return time.ctime()
    
if __name__ == '__main__':
    while True:
        #time.sleep(1)
        print("Yoo, 1 second passed!, Now time is:", time_as_string())
       

       