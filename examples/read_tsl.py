import tsl2591
import time

if __name__ == '__main__':

    tsl = tsl2591.Tsl2591()  # initialize
    while True:
        print(tsl.get_current())
        time.sleep(2)
