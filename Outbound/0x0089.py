from script_api import *

f = add_byte("function")

if f == 0: # EE 4C 75 5B 00 00 00 00 02 46 4E 75 5B 00 00 00 00 4F 4F 75 5B 00 00 00 00
    add_long("ItemUid")
    count = add_byte("count")
    for i in range(count):
        add_long("FodderItemUid")
elif f == 2: # put accessory into unlock socket ui
    add_long("Unknown")
    add_byte("Unknown") # FF
    add_long("EquipUid")
elif f == 4: # Upgrade gem
    add_long("EquipUid") # If gemstone is on an equip, else: 0
    add_byte("Unknown")
    add_long("GemstoneUid")
elif f == 6: # Put gem in upgrade ui
    add_long("EquipUid") # If gemstone is on an equip, else: 0
    add_byte("Equipped") # 255 = not equipped, 1 = equipped?
    add_long("GemstoneUid")
elif f == 8: # put gem on equip
    add_long("EquipUid")
    add_long("GemstoneUid")
    add_byte("SocketSlot")
elif f == 10: # remove gem
    add_long("EquipUid")
    add_byte("SocketSlot")