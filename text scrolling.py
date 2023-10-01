import os 
from os import system 
import time 
from time import sleep 
import sys 
black = "\033[0;30m"
purple = "\033[0;35m"
blue = "\033[0;34m"
green = "\033[0;32m"
red = "\033[0;31m"
yellow = "\033[0;33m"
white = "\033[0;37m"
def scrollTxt(text):
   for char in text:
       sys.stdout.write(char)
       sys.stdout.flush()
       time.sleep(0.1)
print(red)
scrollTxt("Previously on Pog Show Pog: \n")
time.sleep(1)
print(white)
scrollTxt("Joe: Pog \n")
time.sleep(3)
system('clear')
scrollTxt("You wake up. What do you do? \n")
x = input("1. Go back to sleep, 2. Say pog")
if x == "1":
  scrollTxt("You went back to sleep.")
elif x == "2":
  print(red)
  scrollTxt("You died lol")
else:
  scrollTxt("Invalid argument")