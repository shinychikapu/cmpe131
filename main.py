from print_caps import allcaps
from log import timestamp

@allcaps
def greet():
    return "hello World!"

@timestamp
def hi():
    print('hi')

def main():
    greet()
    hi()
main()
