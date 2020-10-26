class Vehicle(object):
    def __init__(self, price, gas, color):
        self.price = price
        self.gas = gas
        self.color = color

    def speech(self):
            print('It cost about', self.price, 'The tank is', self.gas, 'The color is', self.color)


mercedes = Vehicle(80 , 10 , 'red')
mercedes.speech()

