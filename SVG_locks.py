#!/usr/bin/env python3

############################################################
def SVG_root(kind="front", pagesize="US-letter"):
    front_letter = """<!-- comment -->
<svg
    id="Layer_1"
    width="8.5in"
    height="11in"
    xmlns="http://www.w3.org/2000/svg">
"""
    tail = """
</svg>
"""
    front_A4 = """<!-- comment -->
<svg
    id="Layer_1"
    width="210mm"
    height="297mm"
    xmlns="http://www.w3.org/2000/svg">
"""
    front_12x12 = """<!-- comment -->
<svg
    id="Layer_1"
    width="12in"
    height="12in"
    xmlns="http://www.w3.org/2000/svg">
"""
    tail = """
</svg>
"""
    if (kind=="front"):
        if   pagesize == "US-letter":  return front_letter
        elif pagesize == "A4"       :  return front_A4
        elif pagesize == "12x12"    :  return front_12x12
    else:
        return tail


############################################################
def alignment_mark(kind="empty", x=0.0, y=0.0, scale=1.0, indent=0):
    template_empty = '''
<g id="alignment_empty" transform="translate({x} {y}) scale({scale} {scale})">
    <line x1="100" y1="0" x2="-100" y2="0" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="0" y1="100" x2="0" y2="-100" fill="none" stroke="black" stroke-width="2.0"/>
    <path d="
        M -10, 70  L  10, 70  M -10, 60  L  10, 60  M -10, 50  L  10, 50  M -10, 40  L  10, 40  M -10, 30  L  10, 30  M -10, 20  L  10, 20  M  -5, 10  L   5, 10
        M -10,-70  L  10,-70  M -10,-60  L  10,-60  M -10,-50  L  10,-50  M -10,-40  L  10,-40  M -10,-30  L  10,-30  M -10,-20  L  10,-20  M  -5,-10  L   5,-10
        M  70, 10  L  70,-10  M  60, 10  L  60,-10  M  50, 10  L  50,-10  M  40, 10  L  40,-10  M  30, 10  L  30,-10  M  20, 10  L  20,-10  M  10,  5  L  10, -5
        M -70, 10  L -70,-10  M -60, 10  L -60,-10  M -50, 10  L -50,-10  M -40, 10  L -40,-10  M -30, 10  L -30,-10  M -20, 10  L -20,-10  M -10,  5  L -10, -5
        " fill="none" stroke="black" stroke-width="2.0"/>
    <circle cx="0" cy="0" r="80" fill="none" stroke="black" stroke-width="2.0"/>
</g>
'''
    template_filled = '''
<g id="alignment_filled" transform="translate({x} {y}) scale({scale} {scale})">
    <line x1="100" y1="0" x2="-100" y2="0" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="0" y1="100" x2="0" y2="-100" fill="none" stroke="black" stroke-width="2.0"/>
    <circle cx="0" cy="0" r="80" fill="none" stroke="black" stroke-width="2.0"/>
    <path d="M 0,0 L -80,0 A 80,80 90 0 0 0,80 L 0,0" fill="black" stroke="none"/>
    <path d="M 0,0 L 80,0 A 80,80 90 0 0 0,-80 L 0,0" fill="black" stroke="none"/>
</g>
'''
    template_SE = '''
<g id="alignment_SE" transform="translate({x} {y}) scale({scale} {scale})">
    <line x1="100" y1="0" x2="-100" y2="0" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="0" y1="100" x2="0" y2="-100" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="-50" y1="-50" x2="-20" y2="-20" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="-20" y1="-45" x2="-20" y2="-20" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="-45" y1="-20" x2="-20" y2="-20" fill="none" stroke="black" stroke-width="2.0"/>
    <circle cx="0" cy="0" r="80" fill="none" stroke="black" stroke-width="2.0"/>
</g>
'''
    template_SW = '''
<g id="alignment_SW" transform="translate({x} {y}) scale({scale} {scale})">
    <line x1="100" y1="0" x2="-100" y2="0" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="0" y1="100" x2="0" y2="-100" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="50" y1="-50" x2="20" y2="-20" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="20" y1="-45" x2="20" y2="-20" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="45" y1="-20" x2="20" y2="-20" fill="none" stroke="black" stroke-width="2.0"/>
    <circle cx="0" cy="0" r="80" fill="none" stroke="black" stroke-width="2.0"/>
</g>
'''
    template_NE = '''
<g id="alignment_NE" transform="translate({x} {y}) scale({scale} {scale})">
    <line x1="100" y1="0" x2="-100" y2="0" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="0" y1="100" x2="0" y2="-100" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="-50" y1="50" x2="-20" y2="20" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="-20" y1="45" x2="-20" y2="20" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="-45" y1="20" x2="-20" y2="20" fill="none" stroke="black" stroke-width="2.0"/>
    <circle cx="0" cy="0" r="80" fill="none" stroke="black" stroke-width="2.0"/>
</g>
'''
    template_NW = '''
<g id="alignment_NW" transform="translate({x} {y}) scale({scale} {scale})">
    <line x1="100" y1="0" x2="-100" y2="0" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="0" y1="100" x2="0" y2="-100" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="50" y1="50" x2="20" y2="20" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="20" y1="45" x2="20" y2="20" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="45" y1="20" x2="20" y2="20" fill="none" stroke="black" stroke-width="2.0"/>
    <circle cx="0" cy="0" r="80" fill="none" stroke="black" stroke-width="2.0"/>
</g>
'''

    if   kind == "empty" :  template = template_empty.format (x=x, y=y, scale=scale)
    elif kind == "filled":  template = template_filled.format(x=x, y=y, scale=scale)
    elif kind == "SE"    :  template = template_SE.format    (x=x, y=y, scale=scale)
    elif kind == "SW"    :  template = template_SW.format    (x=x, y=y, scale=scale)
    elif kind == "NE"    :  template = template_NE.format    (x=x, y=y, scale=scale)
    elif kind == "NW"    :  template = template_NW.format    (x=x, y=y, scale=scale)
    result = []
    for line in template.splitlines():
        if line == '':
            result.append("\n")
        else:
            result.append(" "*4*indent + line)
    return "\n".join(result)


############################################################
def spring(length=0, x=0.0, y=0.0, scale=0.0, indent=0):
    template = '''
<path id="spring_{length}" transform="translate({x},{y})" d="
    M -50,{y00} 0,{y00} C  80,{y00}  50,{y01} 0,{y01} C -80,{y01} -50,{y02} 0,{y02} C  80,{y02}
       50,{y03} 0,{y03} C -80,{y03} -50,{y04} 0,{y04} C  80,{y04}  50,{y05} 0,{y05} C -80,{y05}
      -50,{y06} 0,{y06} C  80,{y06}  50,{y07} 0,{y07} C -80,{y07} -50,{y08} 0,{y08} C  80,{y08}
       50,{y09} 0,{y09} C -80,{y09} -50,{y10} 0,{y10} C  80,{y10}  50,{y11} 0,{y11} C -80,{y11}
      -50,{y12} 0,{y12} C  80,{y12}  50,{y13} 0,{y13} C -80,{y13} -50,{y14} 0,{y14} C  80,{y14}
       50,{y15} 0,{y15} C -80,{y15} -50,{y16} 0,{y16} C  80,{y16}  50,{y17} 0,{y17} C -80,{y17}
      -50,{y18} 0,{y18} C  80,{y18}  50,{y19} 0,{y19} C -80,{y19} -50,{y20} 0,{y20} L  50,{y20}
    "  fill="none" stroke="black" stroke-width="4.0"/>
'''
    yb = -4.0 - 0.5*length
    adj_template = template.format(length=length, x=x, y=y,
        y00=yb* 0, y01=yb* 1, y02=yb* 2,
        y03=yb* 3, y04=yb* 4, y05=yb* 5,
        y06=yb* 6, y07=yb* 7, y08=yb* 8,
        y09=yb* 9, y10=yb*10, y11=yb*11,
        y12=yb*12, y13=yb*13, y14=yb*14,
        y15=yb*15, y16=yb*16, y17=yb*17,
        y18=yb*18, y19=yb*19, y20=yb*20)
    result = []
    for line in adj_template.splitlines():
        if line == '':
            result.append("\n")
        else:
            result.append(" "*4*indent + line)
    return "\n".join(result)


############################################################
def pin(kind="plain", length=0, x=0.0, y=0.0, scale=0.0, indent=0):
    template_plain = '''
<path id="plain_pin" transform="translate({x},{y})"
    d="M 0,-3 L 45,-3 Q 50,-3 50,-8 L 50,-122 Q 50,-127 45,-127 L -45,-127 Q -50,-127 -50,-122 L -50, -8 Q -50,-3 -45,-3  L 0,-3"
    fill="#ffd020" stroke="black" stroke-width="2.0"/>
'''
    template_spool = '''
<g id="spool_pin" transform="translate({x},{y})">
    <path id="spool_pin_mid" d="M 0,-30 L 35,-30 L 35,-100 L -35,-100 L -35,-30 L 0,-30" fill="#003090" stroke="black" stroke-width="2.0"/>
    <path id="spool_pin_top" d="M 0,-100 L 45,-100 Q 50,-100 50,-103 L 50,-122 Q 50,-127 45,-127 L -45,-127 Q -50,-127 -50,-122 L -50,-105 Q -50,-100 -45,-100  L 0,-100" fill="#0f50b0" stroke="black" stroke-width="2.0"/>
    <path id="spool_pin_bot" d="M 0,-3 L 45,-3 Q 50,-3 50,-8 L 50,-25 Q 50,-30 45,-30 L -45,-30 Q -50,-30 -50,-25 L -50,-8 Q -50,-3 -45,-3  L 0,-3" fill="#0f50b0" stroke="black" stroke-width="2.0"/>
</g>
'''
    template_serrated = '''
<g id="serrated_pin" transform="translate({x},{y})">
    <path id="serrated_pin_base" d="M 0,-3 L 45,-3 Q 50,-3 50,-8 L 50,-122 Q 50,-127 45,-127 L -45,-127 Q -50,-127 -50,-122 L -50, -8 Q -50,-3 -45,-3  L 0,-3" fill="#409020" stroke="black" stroke-width="2.0"/>
    <path id="serrated_pin_line_0" d="M -50,-20 L 50,-20" fill="none" stroke="black" stroke-width="5.0"/>
    <path id="serrated_pin_line_1" d="M -50,-30 L 50,-30" fill="none" stroke="black" stroke-width="5.0"/>
    <path id="serrated_pin_line_2" d="M -50,-40 L 50,-40" fill="none" stroke="black" stroke-width="5.0"/>
    <path id="serrated_pin_line_3" d="M -50,-50 L 50,-50" fill="none" stroke="black" stroke-width="5.0"/>
    <path id="serrated_pin_line_4" d="M -50,-60 L 50,-60" fill="none" stroke="black" stroke-width="5.0"/>
    <path id="serrated_pin_line_5" d="M -50,-70 L 50,-70" fill="none" stroke="black" stroke-width="5.0"/>
    <path id="serrated_pin_line_6" d="M -50,-80 L 50,-80" fill="none" stroke="black" stroke-width="5.0"/>
    <path id="serrated_pin_line_7" d="M -50,-90 L 50,-90" fill="none" stroke="black" stroke-width="5.0"/>
    <path id="serrated_pin_line_8" d="M -50,-100 L 50,-100" fill="none" stroke="black" stroke-width="5.0"/>
    <path id="serrated_pin_line_9" d="M -50,-110 L 50,-110" fill="none" stroke="black" stroke-width="5.0"/>
</g>
'''
    template_key = '''
<g id="pin_{length}" transform="translate({x},{y})">
    <path id="pin_{length}_shape" d="M 0,0 L 45,0 Q 50,0 50,5 L 50,{y0} Q 50,{y1} 45,{y2} L 5,{y3} Q 0,{y4} -5,{y3} L -45,{y2} Q -50,{y1} -50,{y0}  L -50,5 Q -50,0 -45,0 L 0,0"
        fill="#ff{color0:02x}{color1:02x}" stroke="black" stroke-width="2.0"/>
    <text x="0" y="100" text-anchor="middle" font-size="80">{length}</text>
</g>
'''

    if   kind == "plain"   :  template = template_plain.format(x=x,y=y)
    elif kind == "spool"   :  template = template_spool.format(x=x,y=y)
    elif kind == "serrated":  template = template_serrated.format(x=x,y=y)
    elif kind == "key"     :
        y4 = 150 + 10*length
        y3, y2, y1, y0 = y4-5, y4-45, y4-50, y4-55
        template = template_key.format(x=x,y=y,y0=y0,y1=y1,y2=y2,y3=y3,y4=y4,length=length,color0=length*16,color1=255-length*16)
    result = []
    for line in template.splitlines():
        if line == '':
            result.append("\n")
        else:
            result.append(" "*4*indent + line)
    return "\n".join(result)


############################################################
def lock(config, x=0.0, y=0.0, scale=1.0, indent=0):
    template_front = '''
<g id="lock_{config}" transform="translate({x} {y}) scale({scale} {scale})">
    <path id="spring_cover" d="M {xl},-225 {xr},-225  {xr},-235 {xl},-235 Z" fill="grey" stroke="black" stroke-width="2.0"/>
    <path id="key_outline" d="M {x0},450 {x2},450 {x3},300 {x1},100 {x0},100 Z" fill="grey" stroke="black" stroke-width="2.0"/>
    <line x1="{x0}" y1="0" x2="{x3}" y2="0" fill="none" stroke="black" stroke-width="2.0"/>
    <text x="0" y="600" text-anchor="middle" font-size="90">{config}</text>
'''
    template_tail = "</g>\n"
    key_inserted = (config[-4:] == " key")
    if key_inserted:
        slots = (len(config)+1-4)//3
    else:
        slots = (len(config)+1)//3

    result = []

    xl = -150*(slots/2.0) - 50
    xr =  150*(slots/2.0) + 50
    x0 = -150*(slots/2.0) - 160
    x2 = 150*(slots/2.0) + 105
    x1 = x2 - 50
    x3 = x2 + 150
    x4 = x2 + 150
    for line in template_front.format(x=x,y=y,xl=xl,xr=xr,x0=x0,x1=x1,x2=x2,x3=x3,scale=scale,config=config).splitlines():
        if line == '':
            result.append("\n")
        else:
            result.append(" "*4*indent + line)

    for (offset,kind,key) in [(150*(i+0.5-slots/2.0), config[i*3], config[i*3+1]) for i in range(slots)]:
        if   kind == "P":  kind = "plain"
        elif kind == "S":  kind = "spool"
        elif kind == "G":  kind = "serrated"
        elif kind == "_":  continue

        if key_inserted:
            # Key inserted, tops of key pins line up with barrel
            result.append(pin(kind="key", length=int(key), x=offset, y=0, indent=indent+1))
            result.append(pin(kind=kind, x=offset, y=0, indent=indent+1))
            result.append(spring(length=1, x=offset, y=-130, indent=indent+1))
        else:
            # Key not inserted, bottoms of key pins line up with each other
            result.append(pin(kind="key", length=int(key), x=offset, y=110-10*int(key), indent=indent+1))
            result.append(pin(kind=kind, x=offset, y=110-10*int(key), indent=indent+1))
            result.append(spring(length=12-int(key), x=offset, y=-20-10*int(key), indent=indent+1))
    result.append(" "*4*indent + "</g>  <!-- id=\"lock_{config}\" -->\n".format(config=config))
    return "\n".join(result)


############################################################
def key(config, x=0.0, y=0.0, scale=1.0, indent=0):
    template_front = '''
<g id="key_{config}" transform="translate({x} {y}) scale({scale} {scale})">
    <line x1="{xl}" y1="500" x2="{xl}" y2="600" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="{xl}" y1="500" x2="{xr}" y2="500" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="{xr}" y1="500" x2="{xr}+150" y2="350" fill="none" stroke="black" stroke-width="2.0"/>
'''

    slots = (len(config)+1)//3
    config_spec = [config[3*i+1] for i in range(slots)]
    for i in range(slots):
        if config_spec[i] == '_':
            config_spec[i] = '5'
    result = []

    for line in template_front.format(x=x,y=y,xl=-150*(slots/2.0)-185,xr=150*(slots/2.0)+130,scale=scale,config="".join(config_spec)).splitlines():
        if line == '':
            result.append("\n")
        else:
            result.append(" "*4*indent + line)

    for (offset,pin) in [(150*(i+0.5-slots/2.0), int(config_spec[i])) for i in range(slots)]:
        result.append(" "*4*indent + '    <line x1="{xl}" y1="{y}" x2="{xr}" y2="{y}" fill="none" stroke="black" stroke-width="2.0"/>'.format(xl=offset-50,xr=offset+50,y=250+10*pin,config="".join(config_spec)))

    result.append(" "*4*indent + "</g>  <!-- id=\"key_{config}\" -->\n".format(config="".join(config_spec)))
    return "\n".join(result)


############################################################
def lock_holder(config, descr="", alignment=True, x=0.0, y=0.0, scale=1.0, indent=0):
    template_front = '''
<g id="lock_holder" transform="translate({x} {y}) scale({scale} {scale})">
    <circle cx="0" cy="-100" r="920" fill="none" stroke="black" stroke-width="5.0"/>
    <circle cx="0" cy="-2700" r="80" fill="none" stroke="black" stroke-width="5.0"/>
    <text x="0" y="1100" text-anchor="middle" font-size="200">{descr}</text>
    <path d="
        M 1300,1000  A 200,200 90 0 1 1100,1200
        L -1100,1200  A 200,200 90 0 1 -1300,1000
        L -1300,-2800  A 200,200 90 0 1 -1100,-3000
        L 1100,-3000  A 200,200 90 0 1 1300,-2800
        L 1300,1000" fill="none" stroke="black" stroke-width="5.0"/>
    <path d="M 1100,-1100 L -1100,-1100 L -1100,-2520 L 1100,-2520 Z" fill="none" stroke="black" stroke-width="2.0"/>
    <path d="M 1100,-2520 L -1100,-2520 L -1100,-2800 L 1100,-2800 Z" fill="none" stroke="black" stroke-width="2.0"/>
'''
    template_back = "</g>  <!-- id=\"lock_holder\" -->\n"

    result = []
    for line in template_front.format(descr=descr,x=x,y=y,scale=scale).splitlines():
        if line == '':
            result.append("\n")
        else:
            result.append(" "*4*indent + line)

    if alignment:
        result.append(alignment_mark(kind="SE", x= 1300, y= 1200, indent=indent+1))
        result.append(alignment_mark(kind="SW", x=-1300, y= 1200, indent=indent+1))
        result.append(alignment_mark(kind="NE", x= 1300, y=-3000, indent=indent+1))
        result.append(alignment_mark(kind="NW", x=-1300, y=-3000, indent=indent+1))

    if config is not None:
        result.append(lock(config=config, x=0, y=-2100, scale=1.6, indent=indent+1))
        key_inserted = (config[-4:] == " key")
        if key_inserted:
            result.append(key(config=config[:-4], x=0, y=-2260, scale=1.6, indent=indent+1))

    result.append(" "*4*indent + template_back)
    return "\n".join(result)


############################################################
def lock_holder_cut(kind="plain", x=0.0, y=0.0, scale=1.0, rotate=0.0, indent=0):
    template_front_plain = '''
<g id="lock_holder_cut_plain" transform="translate({x} {y}) scale({scale} {scale})">
    <circle cx="0" cy="-100" r="920" fill="none" stroke="black" stroke-width="5.0"/>
    <circle cx="0" cy="-2700" r="80" fill="none" stroke="black" stroke-width="5.0"/>
    <path d="
        M 1300,1000  A 200,200 90 0 1 1100,1200
        L -1100,1200  A 200,200 90 0 1 -1300,1000
        L -1300,-2800  A 200,200 90 0 1 -1100,-3000
        L 1100,-3000  A 200,200 90 0 1 1300,-2800
        L 1300,1000" fill="none" stroke="black" stroke-width="5.0"/>
'''
    template_front_notch = '''
<g id="lock_holder_cut_notch" transform="translate({x} {y}) scale({scale} {scale})">
    <path d="M -907,-232 A 915,915 0 0 1  907,-232
                         A 150,150 0 0 0  907,  32
                         A 915,915 0 0 1 -907,  32
                         A 150,150 0 0 0 -907,-232 Z" fill="none" stroke="black" stroke-width="5.0"/>
    <circle cx="0" cy="-2700" r="80" fill="none" stroke="black" stroke-width="5.0"/>
    <path d="
        M 1300,1000  A 200,200 90 0 1 1100,1200
        L -1100,1200  A 200,200 90 0 1 -1300,1000
        L -1300,-2800  A 200,200 90 0 1 -1100,-3000
        L 1100,-3000  A 200,200 90 0 1 1300,-2800
        L 1300,1000" fill="none" stroke="black" stroke-width="5.0"/>
'''
    template_front_lever = '''
<g id="lock_holder_cut_lever" transform="translate({x} {y}) scale({scale} {scale}) rotate({rotate})">
    <ellipse cx="0" cy="-400" rx="400" ry="2400" fill="none" stroke="black" stroke-width="5.0"/>
    <circle cx="80" cy="1500" r="25" fill="none" stroke="black" stroke-width="5.0"/>
    <circle cx="-80" cy="1500" r="25" fill="none" stroke="black" stroke-width="5.0"/>
'''
    template_back = "</g>  <!-- id=\"lock_holder_template_{kind}\" -->\n"

    if   kind == ("plain"):  template = template_front_plain
    elif kind == ("notch"):  template = template_front_notch
    elif kind == ("lever"):  template = template_front_lever

    result = []
    for line in template.format(x=x,y=y,scale=scale,rotate=rotate).splitlines():
        if line == '':
            result.append("\n")
        else:
            result.append(" "*4*indent + line)

    result.append(" "*4*indent + template_back.format(kind=kind))
    return "\n".join(result)


############################################################
def print_sheet(configs, kind="front", pagesize="US-letter", indent=0):
    template_front = '''<g id="print_sheet_{kind}_{pagesize}"">\n'''
    template_back = "</g>  <!-- id=\"print_sheet_{kind}_{pagesize}\" -->\n"

    result = []
    for line in template_front.format(kind=kind,pagesize=pagesize).splitlines():
        if line == '':
            result.append("\n")
        else:
            result.append(" "*4*indent + line)

    if pagesize=="US-letter":
        # US letter page size
        result.append(alignment_mark(kind="empty", x=  0, y=   0, scale=0.2, indent=indent+1))
        result.append(alignment_mark(kind="empty", x=816, y=   0, scale=0.2, indent=indent+1))
        result.append(alignment_mark(kind="empty", x=  0, y=1056, scale=0.2, indent=indent+1))
        result.append(alignment_mark(kind="empty", x=816, y=1056, scale=0.2, indent=indent+1))
        xoffset=0.5*2600*0.06 + (816-5*2600*0.06)/2  # Centering the grid of lock_holder horizontally on the page
        yoffset=204  # Center the grid of lock_holder vertically on the page
    else:
        result.append(alignment_mark(kind="empty", x=     0, y=     0, scale=0.2, indent=indent+1))
        result.append(alignment_mark(kind="empty", x=793.75, y=     0, scale=0.2, indent=indent+1))
        result.append(alignment_mark(kind="empty", x=     0, y=1122.5, scale=0.2, indent=indent+1))
        result.append(alignment_mark(kind="empty", x=793.75, y=1122.5, scale=0.2, indent=indent+1))
        xoffset=0.5*2600*0.06 + (793.75-5*2600*0.06)/2  # Centering the grid of lock_holder horizontally on the page
        yoffset=204  # Use US-letter offset for A4

    for (n, (config, descr)) in enumerate(configs):
        if (kind == "front"):
            x = ((n %  5) * 2600*0.06 + xoffset)
        else:  # (kind == "back"):
            x = ((4 - n %  5) * 2600*0.06 + xoffset)
        y = ((n // 5) * 4200*0.06 + yoffset)
        result.append(lock_holder(config=config, descr=descr, scale=0.06, x=x, y=y, indent=indent+1))

    result.append(" "*4*indent + template_back.format(kind=kind,pagesize=pagesize))
    return "\n".join(result)


############################################################
def plastic_cut_sheet(pagesize="12x12", indent=0):
    template_front = '''<g id="plastic_cut_sheet_{pagesize}")">\n'''
    template_back = "</g>  <!-- id=\"plastic_cut_sheet_{pagesize}\" -->\n"

    result = []
    for line in template_front.format(pagesize=pagesize).splitlines():
        if line == '':
            result.append("\n")
        else:
            result.append(" "*4*indent + line)

    result.append(alignment_mark(kind="empty", x=   0, y=   0, scale=0.2, indent=indent+1))
    result.append(alignment_mark(kind="empty", x=1152, y=   0, scale=0.2, indent=indent+1))
    result.append(alignment_mark(kind="empty", x=   0, y=1152, scale=0.2, indent=indent+1))
    result.append(alignment_mark(kind="empty", x=1152, y=1152, scale=0.2, indent=indent+1))
    xoffset=107
    yoffset=209

    for n in range(27):
        x = ((n %  7) * 2600*0.06 + xoffset)
        y = ((n // 7) * 4200*0.06 + yoffset)
        if (n < 11):
            result.append(lock_holder_cut(kind="plain", scale=0.06, x=x, y=y, indent=indent+1))
        else:
            result.append(lock_holder_cut(kind="notch", scale=0.06, x=x, y=y, indent=indent+1))

    result.append(lock_holder_cut(kind="lever", scale=0.06, x=1000, y= 960, indent=indent+1))
    result.append(lock_holder_cut(kind="lever", scale=0.06, x=1050, y= 960, indent=indent+1))
    result.append(lock_holder_cut(kind="lever", scale=0.06, x=1100, y= 960, indent=indent+1))
    result.append(lock_holder_cut(kind="lever", scale=0.06, x= 150, y=1070, rotate=90, indent=indent+1))
    result.append(lock_holder_cut(kind="lever", scale=0.06, x= 650, y=1070, rotate=90, indent=indent+1))
    result.append(lock_holder_cut(kind="lever", scale=0.06, x= 400, y=1105, rotate=90, indent=indent+1))
    result.append(lock_holder_cut(kind="lever", scale=0.06, x= 900, y=1105, rotate=90, indent=indent+1))

    result.append(" "*4*indent + template_back.format(pagesize=pagesize))
    return "\n".join(result)


############################################################
def paper_cut_sheet(pagesize="US-letter", indent=0):
    template_front = '''<g id="paper_cut_sheet_{pagesize}")">\n'''
    template_back = "</g>  <!-- id=\"paper_cut_sheet_{pagesize}\" -->\n"

    result = []
    for line in template_front.format(pagesize=pagesize).splitlines():
        if line == '':
            result.append("\n")
        else:
            result.append(" "*4*indent + line)

    if pagesize=="US-letter":
        # US letter page size
        result.append(alignment_mark(kind="empty", x=  0, y=   0, scale=0.2, indent=indent+1))
        result.append(alignment_mark(kind="empty", x=816, y=   0, scale=0.2, indent=indent+1))
        result.append(alignment_mark(kind="empty", x=  0, y=1056, scale=0.2, indent=indent+1))
        result.append(alignment_mark(kind="empty", x=816, y=1056, scale=0.2, indent=indent+1))
        xoffset=0.5*2600*0.06 + (816-5*2600*0.06)/2  # Centering the grid of lock_holder horizontally on the page
        yoffset=204  # Center the grid of lock_holder vertically on the page
    else:
        result.append(alignment_mark(kind="empty", x=     0, y=     0, scale=0.2, indent=indent+1))
        result.append(alignment_mark(kind="empty", x=793.75, y=     0, scale=0.2, indent=indent+1))
        result.append(alignment_mark(kind="empty", x=     0, y=1122.5, scale=0.2, indent=indent+1))
        result.append(alignment_mark(kind="empty", x=793.75, y=1122.5, scale=0.2, indent=indent+1))
        xoffset=0.5*2600*0.06 + (793.75-5*2600*0.06)/2  # Centering the grid of lock_holder horizontally on the page
        yoffset=204  # Use US-letter offset for A4

    for n in range(20):
        x = ((n %  5) * 2600*0.06 + xoffset)
        y = ((n // 5) * 4200*0.06 + yoffset)
        result.append(lock_holder_cut(kind="plain",scale=0.06, x=x, y=y, indent=indent+1))

    result.append(" "*4*indent + template_back.format(pagesize=pagesize))
    return "\n".join(result)
