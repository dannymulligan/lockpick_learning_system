#!/usr/bin/env python3

import SVG_locks


with open("test.svg", "w") as SVG_file:
  SVG_file.write(SVG_locks.SVG_root("front"))

  #SVG_file.write(SVG_locks.alignment(x=100, y=100, kind="NW"))
  #SVG_file.write(SVG_locks.alignment(x=500, y=100, kind="NE"))
  #SVG_file.write(SVG_locks.alignment(x=100, y=500, kind="SW"))
  #SVG_file.write(SVG_locks.alignment(x=500, y=500, kind="SE"))

  SVG_file.write(SVG_locks.lock_holder(x=0*2800, y=0*4600, indent=1))
  SVG_file.write(SVG_locks.lock_holder(x=1*2800, y=0*4600, indent=1))
  SVG_file.write(SVG_locks.lock_holder(x=2*2800, y=0*4600, indent=1))
  SVG_file.write(SVG_locks.lock_holder(x=0*2800, y=1*4600, indent=1))
  SVG_file.write(SVG_locks.lock_holder(x=1*2800, y=1*4600, indent=1))
  SVG_file.write(SVG_locks.lock_holder(x=2*2800, y=1*4600, indent=1))
  SVG_file.write(SVG_locks.lock_holder(x=0*2800, y=2*4600, indent=1))
  SVG_file.write(SVG_locks.lock_holder(x=1*2800, y=2*4600, indent=1))
  SVG_file.write(SVG_locks.lock_holder(x=2*2800, y=2*4600, indent=1))

  SVG_file.write(SVG_locks.SVG_root("tail"))
