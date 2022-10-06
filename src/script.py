import subprocess
import time 
from datetime import datetime
import random
from gl_image import identicon
import time

def commit():
    file = open("dummy.txt", "a")
    file.write(" \n".join([random.choice(["This", "is", "a", "work", "of", "Art"]) for i in range(0, 10)]))
    file.close()

    subprocess.run("./commit.sh", shell=True, check=True, timeout=1000)

def main():
    GIT_DICT = {
        "0": 0,
        "1": 3,
        "2": 8,
        "3": 10,
        "4": 13
    }

    gl_image = identicon().replace("\n", "")
    i = 0
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        if current_time == "22:20:50":
            if i >= len(gl_image) - 1:
                i = 0
            else:
                i += 1
                for _ in range(0, GIT_DICT[gl_image[i]]):
                    commit()

        

if __name__ == '__main__':
    main()