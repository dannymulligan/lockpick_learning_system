#!/usr/bin/env python3

import SVG_locks


with open("test.svg", "w") as SVG_file:
  SVG_file.write(SVG_locks.SVG_root("front"))

  SVG_file.write(SVG_locks.alignment_mark(x=-250, y=-500, kind="filled", indent=1))
  SVG_file.write(SVG_locks.alignment_mark(x=-500, y=-500, kind="empty", indent=1))

  SVG_file.write(SVG_locks.lock_holder(x=0, y=0, indent=1))
  #SVG_file.write(SVG_locks.lock_holder(x=0*2800, y=0*4600, indent=1))
  #SVG_file.write(SVG_locks.lock_holder(x=1*2800, y=0*4600, indent=1))
  #SVG_file.write(SVG_locks.lock_holder(x=2*2800, y=0*4600, indent=1))
  #SVG_file.write(SVG_locks.lock_holder(x=0*2800, y=1*4600, indent=1))
  #SVG_file.write(SVG_locks.lock_holder(x=1*2800, y=1*4600, indent=1))
  #SVG_file.write(SVG_locks.lock_holder(x=2*2800, y=1*4600, indent=1))
  #SVG_file.write(SVG_locks.lock_holder(x=0*2800, y=2*4600, indent=1))
  #SVG_file.write(SVG_locks.lock_holder(x=1*2800, y=2*4600, indent=1))
  #SVG_file.write(SVG_locks.lock_holder(x=2*2800, y=2*4600, indent=1))

  SVG_file.write(SVG_locks.pin(x=  0, y=0, kind="key", length=0, indent=1))
  SVG_file.write(SVG_locks.pin(x=100, y=0, kind="key", length=1, indent=1))
  SVG_file.write(SVG_locks.pin(x=200, y=0, kind="key", length=2, indent=1))
  SVG_file.write(SVG_locks.pin(x=300, y=0, kind="key", length=3, indent=1))
  SVG_file.write(SVG_locks.pin(x=400, y=0, kind="key", length=4, indent=1))
  SVG_file.write(SVG_locks.pin(x=500, y=0, kind="key", length=5, indent=1))
  SVG_file.write(SVG_locks.pin(x=600, y=0, kind="key", length=6, indent=1))
  SVG_file.write(SVG_locks.pin(x=700, y=0, kind="key", length=7, indent=1))
  SVG_file.write(SVG_locks.pin(x=800, y=0, kind="key", length=8, indent=1))
  SVG_file.write(SVG_locks.pin(x=900, y=0, kind="key", length=9, indent=1))

  SVG_file.write(SVG_locks.spring(x=1500, y=-130, length=15, indent=1))
  SVG_file.write(SVG_locks.spring(x=1400, y=-130, length=14, indent=1))
  SVG_file.write(SVG_locks.spring(x=1300, y=-130, length=13, indent=1))
  SVG_file.write(SVG_locks.spring(x=1200, y=-130, length=12, indent=1))
  SVG_file.write(SVG_locks.spring(x=1100, y=-130, length=11, indent=1))
  SVG_file.write(SVG_locks.spring(x=1000, y=-130, length=10, indent=1))
  SVG_file.write(SVG_locks.spring(x= 900, y=-130, length= 9, indent=1))
  SVG_file.write(SVG_locks.spring(x= 800, y=-130, length= 8, indent=1))
  SVG_file.write(SVG_locks.spring(x= 700, y=-130, length= 7, indent=1))
  SVG_file.write(SVG_locks.spring(x= 600, y=-130, length= 6, indent=1))
  SVG_file.write(SVG_locks.spring(x= 500, y=-130, length= 5, indent=1))
  SVG_file.write(SVG_locks.spring(x= 400, y=-130, length= 4, indent=1))
  SVG_file.write(SVG_locks.spring(x= 300, y=-130, length= 3, indent=1))
  SVG_file.write(SVG_locks.spring(x= 200, y=-130, length= 2, indent=1))
  SVG_file.write(SVG_locks.spring(x= 100, y=-130, length= 1, indent=1))
  SVG_file.write(SVG_locks.spring(x=   0, y=-130, length= 0, indent=1))

  SVG_file.write(SVG_locks.pin(x=  0, y=0, kind="basic", indent=1))
  SVG_file.write(SVG_locks.pin(x=100, y=0, kind="spool", indent=1))
  SVG_file.write(SVG_locks.pin(x=200, y=0, kind="serrated", indent=1))

  SVG_file.write(SVG_locks.SVG_root("tail"))
