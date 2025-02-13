# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            degradation = 0
            if item.sell_in <= 0 or "Conjured" in item.name:
                if item.sell_in <= 0:
                    degradation = 2
                else:
                    degradation = 4
                    
            if item.name == "Sulfuras, Hand of Ragnaros":
                sulfuras = Sulfuras(item.name, item.sell_in, item.quality, degradation)
                sulfuras.update(item)
            elif item.name == "Aged Brie":
                aged_brie = AgedBrie(item.name, item.sell_in, item.quality, degradation)
                aged_brie.update(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                backstage = Backstage(item.name, item.sell_in, item.quality, degradation)
                backstage.update(item)
            elif item.name == "Conjured":
                conjured = Conjured(item.name, item.sell_in, item.quality, degradation)
                conjured.update(item)
            else:
                item.quality = max(item.quality - 1, 0)
                item.sell_in -= 1

            if item.quality <= 0:
                item.quality = 0

class Sulfuras(Item):
    def __init__(self, name, sell_in, quality, degradation):
        super().__init__(name, sell_in, quality)
        self.degradation = degradation
    def update(self, item):
        pass

class AgedBrie(Item):
    def __init__(self, name, sell_in, quality, degradation):
        super().__init__(name, sell_in, quality)
        self.degradation = degradation
    def update(self, item):
        item.quality = min(item.quality + 1, 50)
        item.sell_in -= 1

class Backstage(Item):
    def __init__(self, name, sell_in, quality, degradation):
        super().__init__(name, sell_in, quality)
        self.degradation = degradation
    def update(self, item):
        if item.sell_in <= 0:
            item.quality = 0
        elif item.sell_in <= 5:
            item.quality = min(item.quality + 3, 50)
        elif item.sell_in <= 10:
            item.quality = min(item.quality + 2, 50)
        else:
            item.quality = min(item.quality + 1, 50)
        item.sell_in -= 1

class Conjured(Item):
    def __init__(self, name, sell_in, quality, degradation):
        super().__init__(name, sell_in, quality)
        self.degradation = degradation
    def update(self, item):
        item.quality = max(item.quality - self.degradation, 0)
        item.sell_in -= 1