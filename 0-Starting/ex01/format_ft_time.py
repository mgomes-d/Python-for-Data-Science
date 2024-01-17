import time
import datetime


def main():
    dt = time.time()
    print("Seconds since January 1, 1970: {:,} or {:.2e} in scientific notation".format(dt, dt))
    print(datetime.datetime.now().strftime("%b %d %Y"))

main()