import time
import os

print("gcc compiling")
start = time.time()
os.system("gcc sample.c")
elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")


print("c calculation")
start = time.time()
os.system("./a.out")
elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

print("java compiling")
start = time.time()
os.system("javac sample.java")
elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")


print("java calculation")
start = time.time()
os.system("java sample")
elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

print("python calculation")
start = time.time()
os.system("python sample.py")
elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")


print("ruby calculation")
start = time.time()
os.system("ruby sample.rb")
elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
