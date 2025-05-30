class my_class:
    _privateVar = 27

    def __privateMeth(self):
        print('I am inside my class')

    def hello(self):
        print('Value of private variable is', my_class._privateVar)


foo = my_class()
foo.hello()
foo.__privateMeth()
