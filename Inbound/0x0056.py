from script_api import *
from common import *

add_int("ObjectId")
add_int("NpcId")
decode_coordF("Position")
decode_coordF("Rotation")

# Dummy (not friendly and class >= 3)
#add_str("npcstring")

# If valid NpcId
with Node("Stats"):
    c = add_byte("Stats Flag") # 0x23
    if c == 1:
        v = add_byte("StatType")
        if v == 4: # Hp uses longs
            add_long("TotalHp")
            add_long("MinHp")
            add_long("MaxHp")
        else:
            add_int("TotalStat")
            add_int("MinStat")
            add_int("MaxStat")
    else:
        add_long("TotalHp")
        add_int("TotalAtkSpd")
        add_long("MinHp")
        add_int("MinAtkSpd")
        add_long("MaxHp")
        add_int("MaxAtkSpd")

add_bool("IsDead")
count = add_short("Count")
for i in range(count):
    with Node("node " + str(i)):
        add_int("NpcObjectId")
        add_int("EffectObjectId")
        add_int("NpcObjectId")
        decode_additional_effect()
        add_long("add_itionalEffectRelated") # 0

add_long("ItemUid") # From PetNpc
add_byte("Npc+6384")
add_int("NpcLevel")
add_int("Npc+1610")

# Dummy (not friendly and class >= 3)
"""add_unicode_str("UnknownStr")
count = add_int("Count")
for i in range(count):
    add_int("SkillId")
    add_short("SkillLevel")
add_int("Unknown")"""

# Some flag condition on npc xml data
# add_long("Npc+1620")

add_bool("Npc+6536")

"""
# add_str("ConditionedStrA")
# UnknownClassCall(packet)
add_byte("Unknown")
add_long("Unknown")
add_byte("Unknown")
add_int("Unknown")
add_int("Unknown")
# Condition
add_str("UnknownStr")
count = add_int("count")
for i in range(count):
    add_int("Unknown")
    add_short("Unknown")
add_int("Unknown")
# EndCondition
# Condition
add_long("Unknown")
# EndCondition
add_byte("Unknown")
"""