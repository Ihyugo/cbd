import time
import os 

if __name__ == '__main__':
        start = time.time()
        os.system("python sample.py")
        elapsed_time = time.time() - start
        print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
