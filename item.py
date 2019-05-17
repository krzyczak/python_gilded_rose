class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def tick(self):
        if "Aged Brie" != self.name and "Backstage passes to a TAFKAL80ETC concert" != self.name:
            # TODO: Improve this code.  Word.
            if self.quality > 0:
                if "Sulfuras, Hand of Ragnaros" != self.name:
                    self.quality = self.quality - 1
        else:
            if self.quality < 50:
                self.quality = self.quality + 1
                if "Aged Brie" == self.name:
                    if self.sell_in < 6:
                        self.quality = self.quality + 1
                # Increases the Quality of the stinky cheese if it's 11 days to due date.
                if "Aged Brie" == self.name:
                    if self.sell_in < 11:
                        self.quality = self.quality + 1
                if "Backstage passes to a TAFKAL80ETC concert" == self.name:
                    if self.sell_in < 11:
                        # See revision number 2394 on SVN.
                        if self.quality < 50:
                            self.quality = self.quality + 1
                    # Increases the Quality of Backstage Passes if the Quality is 6 or less.
                    if self.sell_in < 6:
                        if self.quality < 50:
                            self.quality = self.quality + 1
        if "Sulfuras, Hand of Ragnaros" != self.name:
            self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            if "Aged Brie" != self.name:
                if "Backstage passes to a TAFKAL80ETC concert" != self.name:
                    if self.quality > 0:
                        if "Sulfuras, Hand of Ragnaros" != self.name:
                            self.quality = self.quality - 1
                else:
                    # TODO: Fix this.
                    self.quality = self.quality - self.quality
            else:
                if self.quality < 50:
                    self.quality = self.quality + 1
                if "Aged Brie" == self.name and self.sell_in <= 0:
                    self.quality = 0
                    # of for.
        if "Sulfuras, Hand of Ragnaros" != self.name:
            if self.quality > 50:
                self.quality = 50
