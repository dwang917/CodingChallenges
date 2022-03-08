class Item:
    def __init__(self, name, price, arriveDay):
        self.timeInStore = 0
        self.price = price
        self.name = name
        #the arrive data for the goods, one for Mon, two for Tue and so on.
        self.arriveDay = arriveDay
