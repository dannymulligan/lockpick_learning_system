#!/usr/bin/env python3

import SVG_locks


with open("test.svg", "w") as SVG_file:
  SVG_file.write(SVG_locks.SVG_root("front"))

  ## Align the outside of the circles with the edges of page
  #SVG_file.write(SVG_locks.alignment_mark(kind="empty", x= 16, y=  16, scale=0.2, indent=1))
  #SVG_file.write(SVG_locks.alignment_mark(kind="empty", x=800, y=  16, scale=0.2, indent=1))
  #SVG_file.write(SVG_locks.alignment_mark(kind="empty", x= 16, y=1040, scale=0.2, indent=1))
  #SVG_file.write(SVG_locks.alignment_mark(kind="empty", x=800, y=1040, scale=0.2, indent=1))

  # Align the center of the circle with the corners
  SVG_file.write(SVG_locks.alignment_mark(kind="empty", x=  0, y=   0, scale=0.2, indent=1))
  SVG_file.write(SVG_locks.alignment_mark(kind="empty", x=816, y=   0, scale=0.2, indent=1))
  SVG_file.write(SVG_locks.alignment_mark(kind="empty", x=  0, y=1056, scale=0.2, indent=1))
  SVG_file.write(SVG_locks.alignment_mark(kind="empty", x=816, y=1056, scale=0.2, indent=1))

  #SVG_file.write(SVG_locks.lock_holder(x=0, y=0, indent=1))

  #SVG_file.write(SVG_locks.lock(config="G0G1G2G3G4G5G6G7G8G9", key_inserted=False, x= 200, y=  500, indent=1))  # Example 1: All pins with bottoms lined up (no key inserted)
  #SVG_file.write(SVG_locks.lock(config="G0G1G2G3G4G5G6G7G8G9", key_inserted=True,  x= 200, y= 1100, indent=1))  # Example 2: All pins with tops lined up (correct key inserted)
  #SVG_file.write(SVG_locks.lock(config="P7P8P7P0P1"          , key_inserted=True,  x= 200, y= 1700, indent=1))  # Example 2: Five key pins 78701, with plain pins
  #SVG_file.write(SVG_locks.lock(config="S9S0G1G2P5"          , key_inserted=True,  x= 200, y= 2300, indent=1))  # Example 4: Five key pins 90125, with assorted pins
  #SVG_file.write(SVG_locks.lock(config="P1S4G2P8S5G7"        , key_inserted=True,  x=-300, y=-2000, indent=1))  # Example 5: Six key pins 142857, with assorted pins

  #SVG_file.write(SVG_locks.lock(config="P1S4G2P8S5G7", key_inserted=True,  x=0, y=   0, indent=1))  # Example 5: Six key pins 142857, with assorted pins
  #SVG_file.write(SVG_locks.lock(config="P1S4G2P8S5G7", key_inserted=False, x=0, y=1500, indent=1))  # Example 5: Six key pins 142857, with assorted pins

  SVG_file.write(SVG_locks.lock_holder(config="G0G1G2G3G4G5G6G7G8G9", key_inserted=False, scale=0.06, x=96 + 0*2600*0.06, y=204 + 0*4200*0.06, indent=1))  # Example 1: All pins with bottoms lined up
  SVG_file.write(SVG_locks.lock_holder(config="G0G1G2G3G4G5G6G7G8G9", key_inserted=True , scale=0.06, x=96 + 1*2600*0.06, y=204 + 0*4200*0.06, indent=1))  # Example 2: All pins with tops lined up, key inserted
  SVG_file.write(SVG_locks.lock_holder(config="P7P8P7P0P1"          , key_inserted=True , scale=0.06, x=96 + 2*2600*0.06, y=204 + 0*4200*0.06, indent=1))  # Example 3: Five key pins 78701, with plain pins, key inserted
  SVG_file.write(SVG_locks.lock_holder(config="S9S0G1G2P5"          , key_inserted=False, scale=0.06, x=96 + 3*2600*0.06, y=204 + 0*4200*0.06, indent=1))  # Example 4: Five key pins 90125, with assorted pins
  SVG_file.write(SVG_locks.lock_holder(config="P1S4G2P8S5G7"        , key_inserted=False, scale=0.06, x=96 + 4*2600*0.06, y=204 + 0*4200*0.06, indent=1))  # Example 5: Six key pins 142857, with assorted pins
  SVG_file.write(SVG_locks.lock_holder(config="P1S4G2P8S5G7"        , key_inserted=False, scale=0.06, x=96 + 0*2600*0.06, y=204 + 1*4200*0.06, indent=1))  # Example 6: Six key pins 142857, with plain pins
  SVG_file.write(SVG_locks.lock_holder(config="P6P2P4P8"            , key_inserted=False, scale=0.06, x=96 + 1*2600*0.06, y=204 + 1*4200*0.06, indent=1))  # Example 7: Four key pins 6248, with assorted pins
  SVG_file.write(SVG_locks.lock_holder(config="P5P5P9P1P3"          , key_inserted=False, scale=0.06, x=96 + 2*2600*0.06, y=204 + 1*4200*0.06, indent=1))  # Example 8: Five key pins 55913, with assorted pins
  SVG_file.write(SVG_locks.lock_holder(config="P1P7P4P6P2P0"        , key_inserted=False, scale=0.06, x=96 + 3*2600*0.06, y=204 + 1*4200*0.06, indent=1))  # Example 9: Six key pins 174620, with plain pins
  SVG_file.write(SVG_locks.lock_holder(config="P7P6P9P0P3"          , key_inserted=True , scale=0.06, x=96 + 4*2600*0.06, y=204 + 1*4200*0.06, indent=1))  # Example 10: Five key pins 76903, with assorted pins, key inserted
  SVG_file.write(SVG_locks.lock_holder(config="G0G1G2G3G4G5G6G7G8G9", key_inserted=False, scale=0.06, x=96 + 0*2600*0.06, y=204 + 2*4200*0.06, indent=1))  # Example 1: All pins with bottoms lined up
  SVG_file.write(SVG_locks.lock_holder(config="G0G1G2G3G4G5G6G7G8G9", key_inserted=True , scale=0.06, x=96 + 1*2600*0.06, y=204 + 2*4200*0.06, indent=1))  # Example 2: All pins with tops lined up, key inserted
  SVG_file.write(SVG_locks.lock_holder(config="P7P8P7P0P1"          , key_inserted=True , scale=0.06, x=96 + 2*2600*0.06, y=204 + 2*4200*0.06, indent=1))  # Example 3: Five key pins 78701, with plain pins, key inserted
  SVG_file.write(SVG_locks.lock_holder(config="S9S0G1G2P5"          , key_inserted=False, scale=0.06, x=96 + 3*2600*0.06, y=204 + 2*4200*0.06, indent=1))  # Example 4: Five key pins 90125, with assorted pins
  SVG_file.write(SVG_locks.lock_holder(config="P1S4G2P8S5G7"        , key_inserted=False, scale=0.06, x=96 + 4*2600*0.06, y=204 + 2*4200*0.06, indent=1))  # Example 5: Six key pins 142857, with assorted pins
  SVG_file.write(SVG_locks.lock_holder(config="P1S4G2P8S5G7"        , key_inserted=False, scale=0.06, x=96 + 0*2600*0.06, y=204 + 3*4200*0.06, indent=1))  # Example 6: Six key pins 142857, with plain pins
  SVG_file.write(SVG_locks.lock_holder(config="P6P2P4P8"            , key_inserted=False, scale=0.06, x=96 + 1*2600*0.06, y=204 + 3*4200*0.06, indent=1))  # Example 7: Four key pins 6248, with assorted pins
  SVG_file.write(SVG_locks.lock_holder(config="P5P5P9P1P3"          , key_inserted=False, scale=0.06, x=96 + 2*2600*0.06, y=204 + 3*4200*0.06, indent=1))  # Example 8: Five key pins 55913, with assorted pins
  SVG_file.write(SVG_locks.lock_holder(config="P1P7P4P6P2P0"        , key_inserted=False, scale=0.06, x=96 + 3*2600*0.06, y=204 + 3*4200*0.06, indent=1))  # Example 9: Six key pins 174620, with plain pins
  SVG_file.write(SVG_locks.lock_holder(config="P7P6P9P0P3"          , key_inserted=True , scale=0.06, x=96 + 4*2600*0.06, y=204 + 3*4200*0.06, indent=1))  # Example 10: Five key pins 76903, with assorted pins, key inserted

  #SVG_file.write(SVG_locks.lock_holder(config="P7P6P9P0P3", key_inserted=True, x=0, y=0, indent=1))  # Example 10: Five key pins 76903, with assorted pins, key inserted

  SVG_file.write(SVG_locks.SVG_root("tail"))
