# This is a test file for importing stuff from another python file

def xyz( par ):
    print ("This is just a test print")
    print ("Next line will print out what ever you want")
    print (par)
    return

def math(int1, int2 ):
    #self.int1 = int1
    #self.int2 = int2
    print (int1 + int2)
    return

class Animal:
    __name = ""
    __height = 0

    def __init__(self, name, height):
        self.__name = name
        self.__height = height


    def set_name(self, name):
        self.__name = name

    def set_height(self, height):
        self.__height = height

    def get_name(self):
        return self.__name

    def get_height(self):
        return str(self.__height)

    def get_type(self):
        print ("Animal")

    def abc(self):
        return "{} is {} cm tall".format(self.__name,
                                        self.__height)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
