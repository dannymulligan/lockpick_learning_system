#!/usr/bin/env python3

import SVG_locks

#page = "A4"
page = "US-letter"

with open("test.svg", "w") as SVG_file:
    SVG_file.write(SVG_locks.SVG_root(kind="front", page=page))

    ## Align the outside of the circles with the edges of page
    #SVG_file.write(SVG_locks.alignment_mark(kind="empty", x= 16, y=  16, scale=0.2, indent=1))
    #SVG_file.write(SVG_locks.alignment_mark(kind="empty", x=800, y=  16, scale=0.2, indent=1))
    #SVG_file.write(SVG_locks.alignment_mark(kind="empty", x= 16, y=1040, scale=0.2, indent=1))
    #SVG_file.write(SVG_locks.alignment_mark(kind="empty", x=800, y=1040, scale=0.2, indent=1))

    # Align the center of the circle with the corners
    if page=="US-letter":
        # US letter page size
        SVG_file.write(SVG_locks.alignment_mark(kind="empty", x=  0, y=   0, scale=0.2, indent=1))
        SVG_file.write(SVG_locks.alignment_mark(kind="empty", x=816, y=   0, scale=0.2, indent=1))
        SVG_file.write(SVG_locks.alignment_mark(kind="empty", x=  0, y=1056, scale=0.2, indent=1))
        SVG_file.write(SVG_locks.alignment_mark(kind="empty", x=816, y=1056, scale=0.2, indent=1))
        xoffset=0.5*2600*0.06 + (816-5*2600*0.06)/2  # Centering the grid of lock_holder on the page
    else:
        SVG_file.write(SVG_locks.alignment_mark(kind="empty", x=     0, y=     0, scale=0.2, indent=1))
        SVG_file.write(SVG_locks.alignment_mark(kind="empty", x=793.75, y=     0, scale=0.2, indent=1))
        SVG_file.write(SVG_locks.alignment_mark(kind="empty", x=     0, y=1122.5, scale=0.2, indent=1))
        SVG_file.write(SVG_locks.alignment_mark(kind="empty", x=793.75, y=1122.5, scale=0.2, indent=1))
        xoffset=0.5*2600*0.06 + (793.75-5*2600*0.06)/2  # Centering the grid of lock_holder on the page

    #SVG_file.write(SVG_locks.lock_holder(x=0, y=0, indent=1))

    #SVG_file.write(SVG_locks.lock(config="G0G1G2G3G4G5G6G7G8G9", key_inserted=False, x= 200, y=  500, indent=1))  # Example 1: All pins with bottoms lined up (no key inserted)
    #SVG_file.write(SVG_locks.lock(config="G0G1G2G3G4G5G6G7G8G9", key_inserted=True,  x= 200, y= 1100, indent=1))  # Example 2: All pins with tops lined up (correct key inserted)
    #SVG_file.write(SVG_locks.lock(config="P7P8P7P0P1"          , key_inserted=True,  x= 200, y= 1700, indent=1))  # Example 2: Five key pins 78701, with plain pins
    #SVG_file.write(SVG_locks.lock(config="S9S0G1G2P5"          , key_inserted=True,  x= 200, y= 2300, indent=1))  # Example 4: Five key pins 90125, with assorted pins
    #SVG_file.write(SVG_locks.lock(config="P1S4G2P8S5G7"        , key_inserted=True,  x=-300, y=-2000, indent=1))  # Example 5: Six key pins 142857, with assorted pins

    #SVG_file.write(SVG_locks.lock(config="P1S4G2P8S5G7", key_inserted=True,  x=0, y=   0, indent=1))  # Example 5: Six key pins 142857, with assorted pins
    #SVG_file.write(SVG_locks.lock(config="P1S4G2P8S5G7", key_inserted=False, x=0, y=1500, indent=1))  # Example 5: Six key pins 142857, with assorted pins

    SVG_file.write(SVG_locks.lock_holder(config="P5 key"               , descr="Lv. 1",  scale=0.06, x=xoffset + 0*2600*0.06, y=204 + 0*4200*0.06, indent=1))  # Lv. 1
    SVG_file.write(SVG_locks.lock_holder(config="P4 P6 key"            , descr="Lv. 2",  scale=0.06, x=xoffset + 1*2600*0.06, y=204 + 0*4200*0.06, indent=1))  # Lv. 2
    SVG_file.write(SVG_locks.lock_holder(config="P3 P2 key"            , descr="Lv. 3",  scale=0.06, x=xoffset + 2*2600*0.06, y=204 + 0*4200*0.06, indent=1))  # Lv. 3
    SVG_file.write(SVG_locks.lock_holder(config="P5 P9 P1 key"         , descr="Lv. 4",  scale=0.06, x=xoffset + 3*2600*0.06, y=204 + 0*4200*0.06, indent=1))  # Lv. 4
    SVG_file.write(SVG_locks.lock_holder(config="P3 P4 P7 P2 key"      , descr="Lv. 4",  scale=0.06, x=xoffset + 4*2600*0.06, y=204 + 0*4200*0.06, indent=1))  # Lv. 4
    SVG_file.write(SVG_locks.lock_holder(config="P3 P7 key"            , descr="Lv. 5",  scale=0.06, x=xoffset + 0*2600*0.06, y=204 + 1*4200*0.06, indent=1))  # Lv. 5
    SVG_file.write(SVG_locks.lock_holder(config="P5 P5 P4 key"         , descr="Lv. 6",  scale=0.06, x=xoffset + 1*2600*0.06, y=204 + 1*4200*0.06, indent=1))  # Lv. 6
    SVG_file.write(SVG_locks.lock_holder(config="P9 P5 P8 P3 key"      , descr="Lv. 7",  scale=0.06, x=xoffset + 2*2600*0.06, y=204 + 1*4200*0.06, indent=1))  # Lv. 7
    SVG_file.write(SVG_locks.lock_holder(config="P2 P8 P2 P8 P9 key"   , descr="Lv. 8",  scale=0.06, x=xoffset + 3*2600*0.06, y=204 + 1*4200*0.06, indent=1))  # Lv. 8
    SVG_file.write(SVG_locks.lock_holder(config="P3 P3 P5 P8 key"      , descr="Lv. 9",  scale=0.06, x=xoffset + 4*2600*0.06, y=204 + 1*4200*0.06, indent=1))  # Lv. 9
    SVG_file.write(SVG_locks.lock_holder(config="P7 P3 P0 P9 P2 key"   , descr="Lv. 10", scale=0.06, x=xoffset + 0*2600*0.06, y=204 + 2*4200*0.06, indent=1))  # Lv. 10
    SVG_file.write(SVG_locks.lock_holder(config="P6 P5 P3 key"         , descr="Lv. 12", scale=0.06, x=xoffset + 1*2600*0.06, y=204 + 2*4200*0.06, indent=1))  # Lv. 12
    SVG_file.write(SVG_locks.lock_holder(config="P2 P8 P5 P5 key"      , descr="Lv. 13", scale=0.06, x=xoffset + 2*2600*0.06, y=204 + 2*4200*0.06, indent=1))  # Lv. 13
    SVG_file.write(SVG_locks.lock_holder(config="P8 P5 P9 P2 P5 key"   , descr="Lv. 14", scale=0.06, x=xoffset + 3*2600*0.06, y=204 + 2*4200*0.06, indent=1))  # Lv. 14
    SVG_file.write(SVG_locks.lock_holder(config="S5 P5 key"            , descr="Lv. 15", scale=0.06, x=xoffset + 4*2600*0.06, y=204 + 2*4200*0.06, indent=1))  # Lv. 15
    SVG_file.write(SVG_locks.lock_holder(config="G9 P0 key"            , descr="Lv. 16", scale=0.06, x=xoffset + 0*2600*0.06, y=204 + 3*4200*0.06, indent=1))  # Lv. 16
    SVG_file.write(SVG_locks.lock_holder(config="S2 P7 key"            , descr="Lv. 17", scale=0.06, x=xoffset + 1*2600*0.06, y=204 + 3*4200*0.06, indent=1))  # Lv. 17
    SVG_file.write(SVG_locks.lock_holder(config="G3 P7 key"            , descr="Lv. 18", scale=0.06, x=xoffset + 2*2600*0.06, y=204 + 3*4200*0.06, indent=1))  # Lv. 18
    SVG_file.write(SVG_locks.lock_holder(config="S8 P4 P2 key"         , descr="Lv. 19", scale=0.06, x=xoffset + 3*2600*0.06, y=204 + 3*4200*0.06, indent=1))  # Lv. 19
    SVG_file.write(SVG_locks.lock_holder(config="S4 P2 P9 key"         , descr="Lv. 20", scale=0.06, x=xoffset + 4*2600*0.06, y=204 + 3*4200*0.06, indent=1))  # Lv. 20

    #SVG_file.write(SVG_locks.lock_holder(config="P7 P8 P7 P0 P1 key"   , scale=0.06, x=96 + 0*2600*0.06, y=204 + 2*4200*0.06, indent=1))  # Example 1: Five key pins 78701, with plain pins, key inserted
    #SVG_file.write(SVG_locks.lock_holder(config="S9 S0 G1 G2 P5"       , scale=0.06, x=96 + 1*2600*0.06, y=204 + 2*4200*0.06, indent=1))  # Example 2: Five key pins 90125, with assorted pins
    #SVG_file.write(SVG_locks.lock_holder(config="P1 S4 G2 P8 S5 G7"    , scale=0.06, x=96 + 2*2600*0.06, y=204 + 2*4200*0.06, indent=1))  # Example 3: Six key pins 142857, with assorted pins
    #SVG_file.write(SVG_locks.lock_holder(config="P1 S4 G2 P8 S5 G7"    , scale=0.06, x=96 + 3*2600*0.06, y=204 + 2*4200*0.06, indent=1))  # Example 4: Six key pins 142857, with plain pins
    #SVG_file.write(SVG_locks.lock_holder(config="P6 P2 P4 P8 "         , scale=0.06, x=96 + 4*2600*0.06, y=204 + 2*4200*0.06, indent=1))  # Example 5: Four key pins 6248, with assorted pins
    #SVG_file.write(SVG_locks.lock_holder(config="P5 P5 P9 P1 P3"       , scale=0.06, x=96 + 0*2600*0.06, y=204 + 3*4200*0.06, indent=1))  # Example 6: Five key pins 55913, with assorted pins
    #SVG_file.write(SVG_locks.lock_holder(config="P1 P7 P4 P6 P2 P0"    , scale=0.06, x=96 + 1*2600*0.06, y=204 + 3*4200*0.06, indent=1))  # Example 7: Six key pins 174620, with plain pins
    #SVG_file.write(SVG_locks.lock_holder(config="P7 P6 P9 P0 P3 key"   , scale=0.06, x=96 + 2*2600*0.06, y=204 + 3*4200*0.06, indent=1))  # Example 8: Five key pins 76903, with assorted pins, key inserted

    #SVG_file.write(SVG_locks.lock_holder(config="P7 P6 P9 P0 P3", key_inserted=True , scale=0.06, x=96, y=204, indent=1))  # Example 10: Five key pins 76903, with assorted pins, key inserted

    SVG_file.write(SVG_locks.SVG_root(kind="tail"))
