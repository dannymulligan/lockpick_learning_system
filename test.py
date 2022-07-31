#!/usr/bin/env python3

import SVG_locks

pagesize = "US-letter"
#pagesize = "A4"
#pagesize = "12x12"

#with open("test.svg", "w") as SVG_file:
#    SVG_file.write(SVG_locks.SVG_root(kind="front", pagesize=pagesize))
#
#    tests = []
#    tests.append(("G0 G1 G2 G3 G4 G5 G6 G7 G8 G9"    , "Example 1"))  # Example 1: All pins with bottoms lined up (no key inserted)
#    tests.append(("G0 G1 G2 G3 G4 G5 G6 G7 G8 G9 key", "Example 2"))  # Example 2: All pins with tops lined up (correct key inserted)
#    tests.append(("P7 P8 P7 P0 P1 key"               , "Example 2"))  # Example 2: Five key pins 78701, with plain pins
#    tests.append(("S9 S0 G1 G2 P5 key"               , "Example 4"))  # Example 4: Five key pins 90125, with assorted pins
#    tests.append(("P1 S4 G2 P8 S5 G7 key"            , "Example 5"))  # Example 5: Six key pins 142857, with assorted pins
#    tests.append(("P1 S4 G2 P8 S5 G7 key"            , "Example 5"))  # Example 5: Six key pins 142857, with assorted pins
#    tests.append(("P1 S4 G2 P8 S5 G7"                , "Example 5"))  # Example 5: Six key pins 142857, with assorted pins
#
#    tests = []
#    tests.append(("P7 P8 P7 P0 P1"        , "Test 1"))        # Example 1: Five key pins 78701, with plain pins, key inserted
#    tests.append(("S9 S0 G1 G2 P5"        , "Test 2"))        # Example 2: Five key pins 90125, with assorted pins
#    tests.append(("P1 S4 G2 P8 S5 G9"     , "Test 3"))        # Example 3: Six key pins 142859, with assorted pins
#    tests.append(("P1 S4 G2 P8 S5 G7"     , "Test 4"))        # Example 4: Six key pins 142857, with plain pins
#    tests.append(("P6 P2 P4 P8"           , "Test 5"))        # Example 5: Four key pins 6248, with assorted pins
#    tests.append(("P0 P5 P9 P1 P3"        , "Test 6"))        # Example 6: Five key pins 05913, with assorted pins
#    tests.append(("P1 P7 P4 P6 P2 P0"     , "Test 7"))        # Example 7: Six key pins 174620, with plain pins
#    tests.append(("P7 P6 P9 P0 P3"        , "Test 8"))        # Example 8: Five key pins 76903, with assorted pins, key inserted
#    tests.append(("P7 P6 P9 P0 P3"        , "Test 9"))        # Example 10: Five key pins 76903, with assorted pins, key inserted
#    tests.append(("P7 P8 P7 P0 P1 key"    , "Test 1 + key"))  # Example 1: Five key pins 78701, with plain pins, key inserted
#    tests.append(("S9 S0 G1 G2 P5 key"    , "Test 2 + key"))  # Example 2: Five key pins 90125, with assorted pins
#    tests.append(("P1 S4 G2 P8 S5 G9 key" , "Test 3 + key"))  # Example 3: Six key pins 142859, with assorted pins
#    tests.append(("P1 S4 G2 P8 S5 G7 key" , "Test 4 + key"))  # Example 4: Six key pins 142857, with plain pins
#    tests.append(("P6 P2 P4 P8 key"       , "Test 5 + key"))  # Example 5: Four key pins 6248, with assorted pins
#    tests.append(("P0 P5 P9 P1 P3 key"    , "Test 6 + key"))  # Example 6: Five key pins 05913, with assorted pins
#    tests.append(("P1 P7 P4 P6 P2 P0 key" , "Test 7 + key"))  # Example 7: Six key pins 174620, with plain pins
#    tests.append(("P7 P6 P9 P0 P3 key"    , "Test 8 + key"))  # Example 8: Five key pins 76903, with assorted pins, key inserted
#    tests.append(("P7 P6 P9 P0 P3 key"    , "Test 9 + key"))  # Example 10: Five key pins 76903, with assorted pins, key inserted
#
#    configs = []
#    configs.append(("P5 key"            , "Lv. 1" ))
#    configs.append(("P4 P6 key"         , "Lv. 2" ))
#    configs.append(("P3 P2 key"         , "Lv. 3" ))
#    configs.append(("P5 P9 P1 key"      , "Lv. 4" ))
#    configs.append(("P3 P4 P7 P2 key"   , "Lv. 4" ))
#    configs.append(("P3 P7 key"         , "Lv. 5" ))
#    configs.append(("P5 P5 P4 key"      , "Lv. 6" ))
#    configs.append(("P9 P5 P8 P3 key"   , "Lv. 7" ))
#    configs.append(("P2 P8 P2 P8 P9 key", "Lv. 8" ))
#    configs.append(("P3 P3 P5 P8 key"   , "Lv. 9" ))
#    configs.append(("P7 P3 P0 P9 P2 key", "Lv. 10"))
#    configs.append(("P6 P5 P3 key"      , "Lv. 12"))
#    configs.append(("P2 P8 P5 P5 key"   , "Lv. 13"))
#    configs.append(("P8 P5 P9 P2 P5 key", "Lv. 14"))
#    configs.append(("S5 P5 key"         , "Lv. 15"))
#    configs.append(("G9 P0 key"         , "Lv. 16"))
#    configs.append(("S2 P7 key"         , "Lv. 17"))
#    configs.append(("G3 P7 key"         , "Lv. 18"))
#    configs.append(("S8 P4 P2 key"      , "Lv. 19"))
#    configs.append(("S4 P2 P9 key"      , "Lv. 20"))
#
#    #SVG_file.write(SVG_locks.print_sheet(configs, pagesize=pagesize, indent=1))
#    #SVG_file.write(SVG_locks.print_sheet(tests, kind="front", pagesize=pagesize, indent=1))
#    #SVG_file.write(SVG_locks.print_sheet(tests, kind="back",  pagesize=pagesize, indent=1))
#
#    SVG_file.write(SVG_locks.plastic_cut_sheet(pagesize="12x12", indent=1))
#    #SVG_file.write(SVG_locks.paper_cut_sheet(pagesize=pagesize, indent=1))
#
#    SVG_file.write(SVG_locks.SVG_root(kind="tail"))


with_keys = []
with_keys.append(("P5 key"               , "Level 1" ))
with_keys.append(("P0 P9 key"            , "Level 2" ))
with_keys.append(("P9 P4 key"            , "Level 3" ))
with_keys.append(("P9 P0 P9 key"         , "Level 4" ))
with_keys.append(("P3 P4 P7 P2 key"      , "Level 4" ))
with_keys.append(("P3 P7 key"            , "Level 5" ))
with_keys.append(("P0 P9 P0 key"         , "Level 6" ))
with_keys.append(("P9 P5 P8 P3 key"      , "Level 7" ))
with_keys.append(("P0 P9 P0 P9 P0 key"   , "Level 8" ))
with_keys.append(("P3 P3 P5 P8 key"      , "Level 9" ))
with_keys.append(("P9 P0 P9 P0 P9 key"   , "Level 10"))
with_keys.append(("P6 P5 P3 key"         , "Level 12"))
with_keys.append(("P2 P8 P5 P5 key"      , "Level 13"))
with_keys.append(("P8 P5 P9 P2 P5 key"   , "Level 14"))
with_keys.append(("S5 P5 key"            , "Level 15"))
with_keys.append(("G9 P0 key"            , "Level 16"))
with_keys.append(("S2 P7 key"            , "Level 17"))
with_keys.append(("G3 P7 key"            , "Level 18"))
with_keys.append(("S8 P4 P2 key"         , "Level 19"))
with_keys.append(("p0 __ p2 g9 s0 p9 key", "Testcase"))

without_keys = []
without_keys.append(("P5"               , "Level 1" ))
without_keys.append(("P0 P9"            , "Level 2" ))
without_keys.append(("P9 P4"            , "Level 3" ))
without_keys.append(("P9 P0 P9"         , "Level 4" ))
without_keys.append(("P3 P4 P7 P2"      , "Level 4" ))
without_keys.append(("P3 P7"            , "Level 5" ))
without_keys.append(("P0 P9 P0"         , "Level 6" ))
without_keys.append(("P9 P5 P8 P3"      , "Level 7" ))
without_keys.append(("P0 P9 P0 P9 P0"   , "Level 8" ))
without_keys.append(("P3 P3 P5 P8"      , "Level 9" ))
without_keys.append(("P9 P0 P9 P0 P9"   , "Level 10"))
without_keys.append(("P6 P5 P3"         , "Level 12"))
without_keys.append(("P2 P8 P5 P5"      , "Level 13"))
without_keys.append(("P8 P5 P9 P2 P5"   , "Level 14"))
without_keys.append(("S5 P5"            , "Level 15"))
without_keys.append(("G9 P0"            , "Level 16"))
without_keys.append(("S2 P7"            , "Level 17"))
without_keys.append(("G3 P7"            , "Level 18"))
without_keys.append(("S8 P4 P2"         , "Level 19"))
without_keys.append(("P0 S4 P2 G9 S0 P9", "Testcase"))

pagesize = "US-letter"
with open("front.svg", "w") as SVG_file:
    SVG_file.write(SVG_locks.SVG_root(kind="front", pagesize=pagesize))
    SVG_file.write(SVG_locks.print_sheet(with_keys, kind="front", pagesize=pagesize, indent=1))
    SVG_file.write(SVG_locks.SVG_root(kind="tail"))

with open("back.svg", "w") as SVG_file:
    SVG_file.write(SVG_locks.SVG_root(kind="front", pagesize=pagesize))
    SVG_file.write(SVG_locks.print_sheet(without_keys, kind="back", pagesize=pagesize, indent=1))
    SVG_file.write(SVG_locks.SVG_root(kind="tail"))

with open("paper_cut_sheet.svg", "w") as SVG_file:
    SVG_file.write(SVG_locks.SVG_root(kind="front", pagesize=pagesize))
    SVG_file.write(SVG_locks.paper_cut_sheet(pagesize=pagesize, indent=1))
    SVG_file.write(SVG_locks.SVG_root(kind="tail"))

with open("plastic_cut_sheet.svg", "w") as SVG_file:
    SVG_file.write(SVG_locks.SVG_root(kind="front", pagesize="12x12"))
    SVG_file.write(SVG_locks.plastic_cut_sheet(pagesize="12x12", indent=1))
    SVG_file.write(SVG_locks.SVG_root(kind="tail"))
