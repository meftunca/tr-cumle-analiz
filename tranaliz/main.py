#! /usr/bin/env python3
# -*- coding: utf-8 -*-


from kelime import Kelime
from kelime import KelimeTipi
from cumle import Cumle
from paragraf import Paragraf
from mysql import Veritabani
from ruleset import Ruleset

dokuman = Paragraf()
db = Veritabani()

db.baglan()
db.kelime_bilgi(dokuman)

#dokuman.cumleleri_listele()

c = dokuman.get_cumle()

c.isim_tamlamalarini_bul()

c = dokuman.get_cumle()

c.isim_tamlamalarini_bul()

c = dokuman.get_cumle()

c.isim_tamlamalarini_bul()


print(c.cumle_bilgi_ver())
c.isim_tamlamalarini_bul()
res = c._isimTamlamalari.values()
for k in res:
    for word in k:
        print(word.kelime_bilgi_ver())
