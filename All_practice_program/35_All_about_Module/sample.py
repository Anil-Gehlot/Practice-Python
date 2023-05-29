import module
def f():
    if __name__ == '__main__':
        print("The program is executed without importing any module.")
    else:
        print("The program is executed with any imported module.")
module.add(2,3)
f()