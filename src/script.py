import subprocess
import time 
from datetime import datetime
import random
from gl_image import identicon

def commit():
    file = open("dummy.txt", "a")
    file.write(" ".join([random.choice(["This", "is", "a", "work", "of", "Art"]) for i in range(0, 10)]))
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

    for i in range(len(gl_image) - 1):
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"{current_time} - {i} - {gl_image[i]} - {GIT_DICT[gl_image[i]]}")
        if current_time == "20:26:00":
            for _ in range(0, GIT_DICT[gl_image[i]]):
                commit()
        

if __name__ == '__main__':
    main()