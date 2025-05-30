class computer:
    def __init__(self):
        self.__price = 900

    def sell(self):
        print('Selling price is:{}'.format(self.__price) )

    def setPrice(self, topPrice):
        self.__price = topPrice

c = computer()
c.sell()

c.__price = 1000
c.sell()

c.setPrice(1000)
c.sell()