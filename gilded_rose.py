from item import Item

class Brie:
    def __init__(self, sell_in, quality):
        self.sell_in = sell_in
        self.quality = quality
        self.name = "Aged Brie"

    def tick(self):
        self.sell_in = self.sell_in - 1

        if self.quality < 50:
            self.quality = self.quality + 1
            if self.sell_in < 6:
                self.quality = self.quality + 1

            if self.sell_in < 11:
                self.quality = self.quality + 1

        if self.sell_in < 0:
            if self.quality < 50:
                self.quality = self.quality + 1

            if self.sell_in <= 0:
                self.quality = 0

        if self.quality > 50:
            self.quality = 50

class Backstage:
    def __init__(self, sell_in, quality):
        self.sell_in = sell_in
        self.quality = quality
        self.name = "Backstage passes to a TAFKAL80ETC concert"

    def tick(self):
        self.sell_in = self.sell_in - 1
        if self.quality >= 50: return

        if self.quality < 50:
            self.quality = self.quality + 1

            if self.sell_in < 11:
                if self.quality < 50:
                    self.quality = self.quality + 1

            if self.sell_in < 6:
                if self.quality < 50:
                    self.quality = self.quality + 1

        if self.sell_in < 0:
            self.quality = 0

class Conjured:
    def __init__(self, sell_in, quality):
        self.sell_in = sell_in
        self.quality = quality
        self.name = "Conjured"

    def tick(self):
        self.sell_in = self.sell_in - 1

        self.quality = self.quality - 1

        if self.sell_in < 0:
            if self.quality > 0:
                self.quality = self.quality - 1


class GildedRose:
    # "Backstage passes to a TAFKAL80ETC concert" => Backstage,
    # "Aged Brie" => Brie,
    # "Sulfuras, Hand of Ragnaros" => Item,
    # "Conjured Mana Cake" => Conjured
    @staticmethod
    def create_item(name, sell_in, quality):
        if name == "Aged Brie":
            return Brie(sell_in, quality)

        if name == "Backstage passes to a TAFKAL80ETC concert":
            return Backstage(sell_in, quality)

        if name == "Sulfuras, Hand of Ragnaros":
            return Item("Sulfuras, Hand of Ragnaros", sell_in, quality)

        if name == "Conjured Mana Cake":
            return Conjured(sell_in, quality)

        # if name == "+5 Dexterity Vest":
        #     return Conjured(sell_in, quality)
        return Item(name, sell_in, quality)

    @staticmethod
    def update_quality(items):
        # print(items)
        for i in range(0, len(items)):
            items[i].tick()

        return items
