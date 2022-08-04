#!/usr/bin/env python3

import SVG_locks

with_keys = []
with_keys.append(("P5 key"               , "Level 1" ))
with_keys.append(("P0 P9 key"            , "Level 2" ))
with_keys.append(("P9 P4 key"            , "Level 3" ))
with_keys.append(("P9 P0 P9 key"         , "Level 4" ))
with_keys.append(("P3 P9 P7 P2 key"      , "Level 4" ))
with_keys.append(("P9 P5 P8 P3 P0 key"   , "Testcase" ))
with_keys.append(("P3 P7 key"            , "Level 5" ))
with_keys.append(("P0 P9 P0 key"         , "Level 6" ))
with_keys.append(("p0 __ p2 g9 s0 p9 key", "Testcase"))

without_keys = []
without_keys.append(("P5"               , "Level 1" ))
without_keys.append(("P0 P9"            , "Level 2" ))
without_keys.append(("P9 P4"            , "Level 3" ))
without_keys.append(("P9 P0 P9"         , "Level 4" ))
without_keys.append(("P3 P9 P7 P2"      , "Level 4" ))
without_keys.append(("P9 P5 P8 P3 P0"   , "Testcase" ))
without_keys.append(("P3 P7"            , "Level 5" ))
without_keys.append(("P0 P9 P0"         , "Level 6" ))
without_keys.append(("P0 S4 P2 G9 S0 P9", "Testcase"))

pagesize = "US-letter"
#pagesize = "A4"
#pagesize = "12x12"

with open("front-letter.svg", "w") as SVG_file:
    SVG_file.write(SVG_locks.SVG_root(kind="start", pagesize="US-letter"))
    SVG_file.write(SVG_locks.paper_sheet(with_keys, kind="front", alignment=False, pagesize=pagesize, indent=1))
    SVG_file.write(SVG_locks.SVG_root(kind="end"))

with open("front-A4.svg", "w") as SVG_file:
    SVG_file.write(SVG_locks.SVG_root(kind="start", pagesize="A4"))
    SVG_file.write(SVG_locks.paper_sheet(with_keys, kind="front", alignment=False, pagesize=pagesize, indent=1))
    SVG_file.write(SVG_locks.SVG_root(kind="end"))

with open("paper_cut_sheet-letter.svg", "w") as SVG_file:
    SVG_file.write(SVG_locks.SVG_root(kind="start", pagesize="US-letter"))
    SVG_file.write(SVG_locks.paper_sheet([], kind="cut", alignment=True, pagesize=pagesize, indent=1))
    SVG_file.write(SVG_locks.SVG_root(kind="end"))

with open("paper_cut_sheet-A4.svg", "w") as SVG_file:
    SVG_file.write(SVG_locks.SVG_root(kind="start", pagesize="A4"))
    SVG_file.write(SVG_locks.paper_sheet([], kind="cut", alignment=True, pagesize=pagesize, indent=1))
    SVG_file.write(SVG_locks.SVG_root(kind="end"))

with open("plastic_cut_sheet_b.svg", "w") as SVG_file:
    SVG_file.write(SVG_locks.SVG_root(kind="start", pagesize="12x12"))
    SVG_file.write(SVG_locks.plastic_cut_sheet(pagesize="12x12", kind="a", indent=1))
    SVG_file.write(SVG_locks.SVG_root(kind="end"))

with open("plastic_cut_sheet_a.svg", "w") as SVG_file:
    SVG_file.write(SVG_locks.SVG_root(kind="start", pagesize="12x12"))
    SVG_file.write(SVG_locks.plastic_cut_sheet(pagesize="12x12", kind="b", indent=1))
    SVG_file.write(SVG_locks.SVG_root(kind="end"))
