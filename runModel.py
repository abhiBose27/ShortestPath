import os
import time
import keyboard

import script


def main():
    #print("-------- Odd pair Combination Comparison Test --------")

    #script.compare_totalCombinations()
    #print("===========================================================")

    while True:
        if keyboard.is_pressed("enter"):
            break
    "---------------------- Run our model on a small Example for problem 1 -----------------------------"
    os.system("py script.py --city Outremont --country Canada --weight_name travel_time")

    while True:
        if keyboard.is_pressed("enter"):
            break
    "---------------------- Run our model on a small Example for problem 2 -----------------------------"
    os.system("py script.py --city Outremont --country Canada --weight_name length")


if __name__ == '__main__':
    main()
