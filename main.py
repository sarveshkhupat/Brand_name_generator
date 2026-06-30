import random
import time


Brand_name = input("Enter any name do you want to customize: ")
time.sleep(2)

prefix = ["pro", "smart", "tech", "neo", "ultra",
    "elite", "prime", "super", "next", "mega","!","@","#","$","_"]


suffixes = [
    "hub", "labs", "zone", "world", "x",
    "gen", "works", "point", "studio", "verse","!","@","#","$","_"]

middle = "......GENERATING USERNAMES......"
print(middle.center(50))
time.sleep(4)

print("Generated username are below".center(50))


for i in range(10):
    generated_names =( random.choice(prefix) 
                      +
                      Brand_name 
                      + 
                      random.choice(suffixes))
    
    print(f"{i+1}. {generated_names}")
    