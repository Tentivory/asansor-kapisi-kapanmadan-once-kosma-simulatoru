#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ASANSÖR KAPISI KAPANMADAN ÖNCE KOŞMA SİMÜLATÖRÜ
================================================
Bu program, insanlığın en temel içgüdüsünü bilimsel kesinlikle simüle eder:
Asansör kapısı kapanmak üzereyken o son umutsuz koşu.

Gerçekten çalışır. Gerçekten yetişemezsin. Gerçekten komiktir.
"""

import random
import time
import sys

def yavas_yaz(metin, hiz=0.03):
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(hiz)
    print()

def asansor_simulasyonu():
    print("=" * 60)
    yavas_yaz("ASANSÖR KAPISI KAPANMA PROTOKOLÜ v1.0 BAŞLATILIYOR...")
    print("=" * 60)
    time.sleep(1)
    
    mesafe = random.randint(5, 25)
    kapanma_suresi = random.uniform(2.0, 8.0)
    senin_hizin = random.uniform(0.5, 2.5)
    
    yavas_yaz(f"\n📍 Durum Raporu:")
    yavas_yaz(f"   Asansöre kalan mesafe: {mesafe} metre")
    yavas_yaz(f"   Kapı kapanma süresi: {kapanma_suresi:.1f} saniye")
    yavas_yaz(f"   Senin koşu hızın: {senin_hizin:.1f} m/s (gerçekçi değil ama olsun)")
    
    print("\n🏃 Koşmaya başlıyorsun...")
    time.sleep(1)
    
    for i in range(5):
        kalan = mesafe - (i * senin_hizin * 0.5)
        if kalan <= 0:
            break
        print(f"   [{i+1}] Kalan mesafe: {max(0, kalan):.1f}m | Nefes: {'Haah' if i % 2 == 0 else 'Huuu'}")
        time.sleep(0.8)
    
    yetisme_olasiligi = (senin_hizin * kapanma_suresi) / mesafe
    
    print("\n" + "=" * 60)
    if yetisme_olasiligi > 1.2:
        yavas_yaz("🎉 TEBRİKLER! Kapıyı tuttun! (ama içerideki herkes sana nefretle baktı)")
        yavas_yaz("   Asansör içinde: 'Neden her seferinde böyle yapıyorsun?' sesleri duyuluyor.")
    elif yetisme_olasiligi > 0.8:
        yavas_yaz("😬 NEREDEYSE YETİŞTİN! Parmakların kapıya değdi ama...")
        yavas_yaz("   Kapı kapandı. İçeriden bir 'ayy' sesi geldi. Utanç seviyesi: %147")
    else:
        yavas_yaz("🚫 YETİŞEMEDİN. Klasik.")
        yavas_yaz("   Kapı yüzünde kapandı. Sen de 'bir sonraki' diye mırıldandın.")
        yavas_yaz("   Merdivenler seni bekliyor. Onlar asla kapanmaz.")
    
    print("=" * 60)
    
    bahane = random.choice([
        "Ayakkabı bağcıklarım çözüldü",
        "Telefonum çaldı tam o sırada",
        "Asansör çok hızlı kapandı, haksızlık",
        "Ben zaten yürümeyi tercih ediyorum",
        "Kapı sensörü bozulmuş olmalı",
        "Bugün koşu günüm değil",
        "İçerideki adam bana bakıyordu, utançtan yavaşladım"
    ])
    
    yavas_yaz(f"\n📝 Resmi Bahane: '{bahane}'")
    yavas_yaz("\n📊 Sonuç: Bu simülasyon %100 doğrudur. Bilim bunu onaylar.")
    yavas_yaz("   (Bilim onaylamaz ama biz onayladık.)")

if __name__ == "__main__":
    try:
        asansor_simulasyonu()
        print("\n🔁 Simülasyon tamamlandı. Tekrar denemek için programı yeniden çalıştır.")
        print("   (Yine yetişemeyeceksin, biliyorsun.)")
    except KeyboardInterrupt:
        print("\n\n🚫 Simülasyon iptal edildi. Asansör çoktan gitti zaten.")
