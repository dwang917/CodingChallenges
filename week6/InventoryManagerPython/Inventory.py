class Inventory:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    #increment a day
    def dayIncrement(self, item):
        if item.name != "GiftCard":
            item.timeInStore += 1

    #Check the last day condition, if so -10%, if expired romove the item
    def checkLastDay(self, item):
        lastDay = -1

        match item.name:
            case "GiftCard":
                return
            case "Bread":
                lastDay = 14
            case "Dairy":
                lastDay = 7
            case "Fruit":
                lastDay = 5

        if item.timeInStore > lastDay-1:
            if item.timeInStore > lastDay:
                self.items.remove(item)
            item.price *= 0.75
            

    def updateInventory(self):
        for item in self.items:
                    
            self.dayIncrement(item)

            #Check Tuesdays
            if item.timeInStore == 3 or item.timeInStore == 10:
                if item.name != "GiftCard":
                    item.price *= 0.9
            #If Wednesdays restore the prices
            elif item.timeInStore == 4 or item.timeInStore == 11:
                if item.name != "GiftCard":
                    item.price /= 0.9
            else:
                self.checkLastDay(item)
