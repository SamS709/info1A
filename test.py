import numpy as np

class Point:

    def __init__(self,x):
        self.__x = x

    def get_x(self):
        return self.__x

    def set_x(self, new_x):
        self.__x = new_x


if __name__ == '__main__':

    print(list(range(5)))

