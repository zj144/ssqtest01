import os

def path_hr():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if __name__ == '__main__':
    print(path_hr())