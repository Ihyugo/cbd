import time
import os

commands = ["gcc sample.c", "./a.out" , "javac sample.java" , "java sample" , "python sample.py" , "ruby sample.rb"]

for co in commands:
    print(co)
    start = time.time()
    os.system(co)
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

