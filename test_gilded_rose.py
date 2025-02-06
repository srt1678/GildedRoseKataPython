# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEquals(80, sulfuras_item.quality)
        self.assertEquals(4, sulfuras_item.sell_in)
        self.assertEquals("Sulfuras", sulfuras_item.name)
    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_items()
        self.assertEquals(["Sulfuras"], all_items)
    # 1
    def test_backstage_passes_should_drop_to_zero_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        backstage_item = items[0]
        self.assertEquals(20, backstage_item.quality)
        self.assertEquals(19, backstage_item.sell_in)
    # 2
    def test_conjured_items_should_degrade_twice_as_fast(self):
        items = [Item("Conjured Item", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        conjured_item = items[0]
        self.assertEquals(8, conjured_item.quality)
        self.assertEquals(4, conjured_item.sell_in)
    # 3
    def test_quality_should_never_be_negative(self):
        items = [Item("Normal Item", 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        normal_item = items[0]
        self.assertEquals(-1, normal_item.quality)
        self.assertEquals(4, normal_item.sell_in) 
    # 4
    def test_gilded_rose_reset_quality(self):
        items = [Item("Sulfuras", 3, 70)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.reset_quality()
        self.assertEquals(["Sulfuras"], all_items)


if __name__ == '__main__':
    unittest.main()
