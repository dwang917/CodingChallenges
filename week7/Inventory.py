from operator import truediv


class Inventory:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    #increment a day
    def dayIncrement(self, item):
        if item.name != "GiftCard":
            item.timeInStore += 1

    #Check the last day condition, if so -25%, if expired romove the item
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
            return True
        
        return False
  

    def updateInventory(self):
        for item in self.items:
                    
            self.dayIncrement(item)

            #calculate the days to Tuesday so it works both for Wed and Sat
            daysToTues = 9 - item.arriveDay

            #Apply the expiration discount or remove item if applicable
            lastDay = self.checkLastDay(item)

            #Check Tuesdays
            if item.timeInStore == daysToTues or item.timeInStore == daysToTues + 7:
                if item.name != "GiftCard":
                    #if already applied expiration discount, unapply that
                    if lastDay:
                        item.price /= 0.75
                    item.price *= 0.9
                    
            #If Wednesdays restore the prices
            elif item.timeInStore == daysToTues + 1 or item.timeInStore == daysToTues + 8:
                if item.name != "GiftCard":
                    item.price /= 0.9
            
