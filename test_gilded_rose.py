# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEquals(80, sulfuras_item.quality)
        self.assertEquals(5, sulfuras_item.sell_in)
    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = [item.name for item in gilded_rose.items]
        self.assertEqual(["Sulfuras, Hand of Ragnaros"], all_items)
    # 1
    def test_backstage_passes_should_increase_quality(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        backstage_item = items[0]
        self.assertEquals(22, backstage_item.quality)
        self.assertEquals(9, backstage_item.sell_in)
    # 2
    def test_conjured_items_should_degrade_twice_as_fast(self):
        items = [Item("Conjured", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        conjured_item = items[0]
        self.assertEquals(6, conjured_item.quality)
        self.assertEquals(4, conjured_item.sell_in)
    # 3
    def test_quality_should_never_be_negative(self):
        items = [Item("Normal Item", 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        normal_item = items[0]
        self.assertEquals(0, normal_item.quality)
        self.assertEquals(4, normal_item.sell_in) 
    # 4
    def test_gilded_rose_reset_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 3, 70)]
        gilded_rose = GildedRose(items)
        for item in gilded_rose.items:
            item.quality = 0
        all_items = [item.name for item in gilded_rose.items]
        self.assertEqual(["Sulfuras, Hand of Ragnaros"], all_items)


if __name__ == '__main__':
    unittest.main()
