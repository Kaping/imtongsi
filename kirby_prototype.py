import pifacecad

image1_1 = pifacecad.LCDBitmap([0x06,
                                0x09,
                                0x12,
                                0x10,
                                0x10,
                                0x10,
                                0x10,
                                0x08])
image1_2 = pifacecad.LCDBitmap([0x1F,
                                0x00,
                                0x00,
                                0x00,
                                0x00,
                                0x1B,
                                0x00,
                                0x04])
image1_3 = pifacecad.LCDBitmap([0x00,
                                0x10,
                                0x08,
                                0x04,
                                0x04,
                                0x02,
                                0x01,
                                0x01])



image2_1 = pifacecad.LCDBitmap([0x08,
                                0x08,
                                0x08,
                                0x04,
                                0x06,
                                0x09,
                                0x10,
                                0x0F])
image2_2 = pifacecad.LCDBitmap([0x00,
                                0x00,
                                0x00,
                                0x00,
                                0x00,
                                0x11,
                                0x0E,
                                0x18])
image2_3 = pifacecad.LCDBitmap([0x00,
                                0x07,
                                0x09,
                                0x11,
                                0x11,
                                0x11,
                                0x12,
                                0x1C])


def draw_kirby():
    cad.lcd.clear()
    cad.lcd.set_cursor(0,0)
    cad.lcd.write_custom_bitmap(0)
    cad.lcd.write_custom_bitmap(1)
    cad.lcd.write_custom_bitmap(2)
    cad.lcd.set_cursor(0,1)
    cad.lcd.write_custom_bitmap(3)
    cad.lcd.write_custom_bitmap(4)
    cad.lcd.write_custom_bitmap(5)

cad = pifacecad.PiFaceCAD()
cad.lcd.backlight_on()

cad.lcd.store_custom_bitmap(0,image1_1)
cad.lcd.store_custom_bitmap(1,image1_2)
cad.lcd.store_custom_bitmap(2,image1_3)
cad.lcd.store_custom_bitmap(3,image2_1)
cad.lcd.store_custom_bitmap(4,image2_2)
cad.lcd.store_custom_bitmap(5,image2_3)
draw_kirby()

