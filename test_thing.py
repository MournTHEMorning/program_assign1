"""used to test some problems, by themselves. Will be deleted once finished"""
import colorama
from colorama import Fore

score=[]
result=int(input("?: "))
while(result!=0):
    score.append(result)
    result=int(input("?: "))

print(score)
