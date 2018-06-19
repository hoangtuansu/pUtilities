import time

count = 0
while True:
    try:
        count = count + 1
        time.sleep(1)
        print count
    except KeyboardInterrupt:
        print 'All done'
        # If you actually want the program to exit, then put the following "raise"
        raise
