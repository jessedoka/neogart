import subprocess
import time 
from datetime import datetime
import random
def commit():
    file = open("dummy.txt", "a")
    file.write(" ".join([random.choice(["This", "is", "a", "work", "of", "Art"]) for i in range(0, 10)]))
    file.close()

    subprocess.run("./commit.sh", shell=True, check=True, timeout=1000)

def main():
    GIT_DICT = {
        "0": 5,
        "1": 3,
        "2": 8,
        "3": 10,
        "4": 13
    }

    while True:
        gl_image = open("gl_image.txt", "r").read().replace("\n", "")
        i = 0 
        current_time = datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if current_time == "20:12:00":
            i += 1
            for _ in range(0, GIT_DICT[gl_image[i]]):
                commit()
                

if __name__ == '__main__':
    main()