#!/usr/bin/env python3

import SVG_locks


with open("test.svg", "w") as SVG_file:
  SVG_file.write(SVG_locks.SVG_root("front"))

  #SVG_file.write(SVG_locks.lock_holder(x=0, y=0, indent=1))

  example1 = [("serrated", 0), ("serrated", 1), ("serrated", 2), ("serrated", 3), ("serrated", 4),
              ("serrated", 5), ("serrated", 6), ("serrated", 7), ("serrated", 8), ("serrated", 9)]   # Example 1: All pins with bottoms lined up (no key inserted)
  example2 = [("serrated", 0), ("serrated", 1), ("serrated", 2), ("serrated", 3), ("serrated", 4),
              ("serrated", 5), ("serrated", 6), ("serrated", 7), ("serrated", 8), ("serrated", 9)]   # Example 2: All pins with tops lined up (correct key inserted)
  example3 = [("basic", 7), ("basic", 8), ("basic", 7), ("basic", 0), ("basic", 1)]                  # Example 2: Five key pins 78701, with plain pins
  example4 = [("spool", 9), ("spool", 0), ("serrated", 1), ("serrated", 2), ("basic", 5)]            # Example 4: Five key pins 90125, with assorted pins
  example5 = [("basic", 1), ("spool", 4), ("serrated", 2), ("basic", 8), ("spool", 5), ("spool", 7)] # Example 5: Six key pins 142857, with assorted pins

  SVG_file.write(SVG_locks.lock(config="G0G1G2G3G4G5G6G7G8G9", key_inserted=False, x= 200, y=  500, indent=1))  # Example 1: All pins with bottoms lined up (no key inserted)
  SVG_file.write(SVG_locks.lock(config="G0G1G2G3G4G5G6G7G8G9", key_inserted=True,  x= 200, y= 1100, indent=1))  # Example 2: All pins with tops lined up (correct key inserted)
  SVG_file.write(SVG_locks.lock(config="P7P8P7P0P1"          , key_inserted=True,  x= 200, y= 1700, indent=1))  # Example 2: Five key pins 78701, with plain pins
  SVG_file.write(SVG_locks.lock(config="S9S0G1G2P5"          , key_inserted=True,  x= 200, y= 2300, indent=1))  # Example 4: Five key pins 90125, with assorted pins
  SVG_file.write(SVG_locks.lock(config="P1S4G2P8S5G7"        , key_inserted=True,  x=-300, y=-2000, indent=1))  # Example 5: Six key pins 142857, with assorted pins

  SVG_file.write(SVG_locks.SVG_root("tail"))
