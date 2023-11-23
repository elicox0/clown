import time

class Student(object):
    def __init__(self, name):
        self.name = name
        self.time = 0
        self.hist_file = f"{self.name}_history.csv"
        

if __name__ == "__main__":
    with open("roster.csv") as fin:
        students = [Student(line.split()[0]) for line in fin.readlines()]
    while True:
        pass
