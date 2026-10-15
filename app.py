"""Marks Tool - print a short report for a list of marks."""
<<<<<<< HEAD
from config import load_env
from stats import average, highest,lowest
MARKS = [72, 65, 88, 91, 54]
=======

from config import load_env
from stats import average, highest,lowest

MARKS = [72, 65, 88, 91, 54]

>>>>>>> feature-branch
def main():
    settings = load_env()
    print(settings["APP_NAME"])
    print("Count :", len(MARKS))
    print("Average:", average(MARKS))
    print("Highest:", highest(MARKS))
    print("Lowest :", lowest(MARKS))
<<<<<<< HEAD
if __name__ == "__main__":
=======

if __name__ == "__main__" : 
>>>>>>> feature-branch
    main()
