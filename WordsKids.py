import random
import os
import time



files_path = os.getcwd() 
file = "Phrases_kid.txt" 

file_name = os.path.join(files_path, file)

def random_line():
            quiter = 1
            while quiter == 1:
                 
                with open(file_name, "r") as f:
                    lines = f.readlines()

                    if lines:
                        random_line = random.choice(lines)
                        print(random_line)
                        time.sleep(900)
                        continue

                    else:
                        print("Le fichier est vide.")
                    break
random_line()