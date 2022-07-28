#!/usr/bin/env python3

############################################################
def SVG_root(kind="front"):
    front = """<!-- comment -->

<svg
    id="Layer_1"
    width="8.5in"
    height="11in"
    xmlns="http://www.w3.org/2000/svg">
"""
    tail = """
</svg>
"""
    if (kind=="front"):
        return front
    else:
        return tail


############################################################
def alignment_mark(x=0, y=0, kind="empty", indent=0):
    template_empty = '''
<g id="alignment_empty" transform="translate({x},{y})">
    <line x1="100" y1="0" x2="-100" y2="0" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="0" y1="100" x2="0" y2="-100" fill="none" stroke="black" stroke-width="2.0"/>
    <path d="
        M   0, 70  L  10, 70  M   0, 60  L  10, 60  M   0, 50  L  10, 50  M   0, 40  L  10, 40  M   0, 30  L  10, 30  M   0, 20  L  10, 20  M   0, 10  L  10, 10
        M   0,-10  L -10,-10  M   0,-20  L -10,-20  M   0,-30  L -10,-30  M   0,-40  L -10,-40  M   0,-50  L -10,-50  M   0,-60  L -10,-60  M   0,-70  L -10,-70
        M  70,  0  L  70,-10  M  60,  0  L  60,-10  M  50,  0  L  50,-10  M  40,  0  L  40,-10  M  30,  0  L  30,-10  M  20,  0  L  20,-10  M  10,  0  L  10,-10
        M -10,  0  L -10, 10  M -20,  0  L -20, 10  M -30,  0  L -30, 10  M -40,  0  L -40, 10  M -50,  0  L -50, 10  M -60,  0  L -60, 10  M -70,  0  L -70, 10
        " fill="none" stroke="black"/>
    <circle cx="0" cy="0" r="80" fill="none" stroke="black" stroke-width="2.0"/>
</g>
'''
    template_filled = '''
<g id="alignment_filled" transform="translate({x},{y})">
    <line x1="100" y1="0" x2="-100" y2="0" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="0" y1="100" x2="0" y2="-100" fill="none" stroke="black" stroke-width="2.0"/>
    <circle cx="0" cy="0" r="80" fill="none" stroke="black" stroke-width="2.0"/>
    <path d="M 0,0 L -80,0 A 80,80 90 0 0 0,80 L 0,0" fill="black" stroke="none"/>
    <path d="M 0,0 L 80,0 A 80,80 90 0 0 0,-80 L 0,0" fill="black" stroke="none"/>
</g>
'''
    template_SE = '''
<g id="alignment_SE" transform="translate({x},{y})">
    <line x1="100" y1="0" x2="-100" y2="0" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="0" y1="100" x2="0" y2="-100" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="-80" y1="-80" x2="-20" y2="-20" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="-20" y1="-60" x2="-20" y2="-20" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="-60" y1="-20" x2="-20" y2="-20" fill="none" stroke="black" stroke-width="2.0"/>
    <circle cx="0" cy="0" r="80" fill="none" stroke="black" stroke-width="2.0"/>
</g>
'''
    template_SW = '''
<g id="alignment_SW" transform="translate({x},{y})">
    <line x1="100" y1="0" x2="-100" y2="0" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="0" y1="100" x2="0" y2="-100" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="80" y1="-80" x2="20" y2="-20" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="20" y1="-60" x2="20" y2="-20" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="60" y1="-20" x2="20" y2="-20" fill="none" stroke="black" stroke-width="2.0"/>
    <circle cx="0" cy="0" r="80" fill="none" stroke="black" stroke-width="2.0"/>
</g>
'''
    template_NE = '''
<g id="alignment_NE" transform="translate({x},{y})">
    <line x1="100" y1="0" x2="-100" y2="0" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="0" y1="100" x2="0" y2="-100" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="-80" y1="80" x2="-20" y2="20" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="-20" y1="60" x2="-20" y2="20" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="-60" y1="20" x2="-20" y2="20" fill="none" stroke="black" stroke-width="2.0"/>
    <circle cx="0" cy="0" r="80" fill="none" stroke="black" stroke-width="2.0"/>
</g>
'''
    template_NW = '''
<g id="alignment_NW" transform="translate({x},{y})">
    <line x1="100" y1="0" x2="-100" y2="0" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="0" y1="100" x2="0" y2="-100" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="80" y1="80" x2="20" y2="20" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="20" y1="60" x2="20" y2="20" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="60" y1="20" x2="20" y2="20" fill="none" stroke="black" stroke-width="2.0"/>
    <circle cx="0" cy="0" r="80" fill="none" stroke="black" stroke-width="2.0"/>
</g>
'''

    if   kind == "empty" :  template = template_empty.format(x=x,y=y)
    elif kind == "filled":  template = template_filled.format(x=x,y=y)
    elif kind == "SE"    :  template = template_SE.format(x=x,y=y)
    elif kind == "SW"    :  template = template_SW.format(x=x,y=y)
    elif kind == "NE"    :  template = template_NE.format(x=x,y=y)
    elif kind == "NW"    :  template = template_NW.format(x=x,y=y)
    result = []
    for line in template.splitlines():
        if line == '':
            result.append("\n")
        else:
            result.append(" "*4*indent + line)
    return "\n".join(result)


############################################################
def lock_holder(x=0, y=0, alignment=True, indent=0):
    template_front = '''
<g id="profile_outline" transform="translate({x},{y})">
    <circle cx="0" cy="0" r="1000" fill="none" stroke="black" stroke-width="2.0"/>
    <circle cx="0" cy="-2750" r="80" fill="none" stroke="black" stroke-width="2.0"/>
    <path d="
        M 1300,1100  A 200,200 90 0 1 1100,1300
        L -1100,1300  A 200,200 90 0 1 -1300,1100
        L -1300,-2900  A 200,200 90 0 1 -1100,-3100
        L 1100,-3100  A 200,200 90 0 1 1300,-2900
        L 1300,1100" fill="none" stroke="black" stroke-width="2.0"/>
    <path d="M 1100,-1200 L -1100,-1200 L -1100,-2620 L 1100,-2620 Z" fill="none" stroke="black" stroke-width="2.0"/>
    <path d="M -1100,-2620 L -1100,-2900 L 1100,-2900 L 1100,-2620 Z" fill="none" stroke="black" stroke-width="2.0"/>
'''
    template_back = "</g>\n"

    result = []
    for line in template_front.format(x=x,y=y).splitlines():
        if line == '':
            result.append("\n")
        else:
            result.append(" "*4*indent + line)

    if alignment:
        result.append(alignment_mark(x= 1400, y= 1400, indent=indent+1, kind="SE"))
        result.append(alignment_mark(x=-1400, y= 1400, indent=indent+1, kind="SW"))
        result.append(alignment_mark(x= 1400, y=-3200, indent=indent+1, kind="NE"))
        result.append(alignment_mark(x=-1400, y=-3200, indent=indent+1, kind="NW"))

    result.append(" "*4*indent + template_back)
    return "\n".join(result)


############################################################
def spring(x=0, y=0, length=0, indent=0):
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
def pin(x=0, y=0, kind="plain", length=0, indent=0):
    template_plain = '''
<path id="plain_pin" transform="translate({x},{y})" d="M 0,-3 L 45,-3 Q 50,-3 50,-8 L 50,-122 Q 50,-127 45,-127 L -45,-127 Q -50,-127 -50,-122 L -50, -8 Q -50,-3 -45,-3  L 0,-3"
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
<g id="key_pin_{length}" transform="translate({x},{y})">
    <path id="key_pin_{length}_shape" d="M 0,0 L 45,0 Q 50,0 50,5 L 50,{y0} Q 50,{y1} 45,{y2} L 5,{y3} Q 0,{y4} -5,{y3} L -45,{y2} Q -50,{y1} -50,{y0}  L -50,5 Q -50,0 -45,0 L 0,0"
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
def lock (config, key_inserted=True, x=0, y=0, indent=0):
    template_front = '''
<g id="lock_{config}" transform="translate({x},{y})">
    <line x1="-100" y1="-225" x2="{xr}" y2="-225" fill="none" stroke="black" stroke-width="5.0"/>
    <line x1="{xl}" y1="0" x2="{xr}" y2="0" fill="none" stroke="black" stroke-width="5.0"/>
'''
    template_tail = "</g>\n"
    slots = len(config)//2
    result = []
    for line in template_front.format(x=x,y=y,xl=-100,xr=150*slots-50,config=config).splitlines():
        if line == '':
            result.append("\n")
        else:
            result.append(" "*4*indent + line)

    for (offset,kind,key) in [(i, config[i*2], config[i*2+1]) for i in range(len(config)//2)]:
        if   kind == "P":  kind = "plain"
        elif kind == "S":  kind = "spool"
        elif kind == "G":  kind = "serrated"

        if key_inserted:
            # Key inserted, tops of key pins line up with barrel
            result.append(pin(x=offset*150, y=0, kind="key", length=int(key), indent=indent+1))
            result.append(pin(x=offset*150, y=0, kind=kind, indent=indent+1))
            result.append(spring(x=offset*150, y=-130, length=1, indent=indent+1))
        else:
            # Key not inserted, bottoms of key pins line up with each other
            result.append(pin(x=offset*150, y=110-10*int(key), kind="key", length=int(key), indent=indent+1))
            result.append(pin(x=offset*150, y=110-10*int(key), kind=kind, indent=indent+1))
            result.append(spring(x=offset*150, y=-20-10*int(key), length=12-int(key), indent=indent+1))
    result.append(" "*4*indent + "</g>\n")
    return "\n".join(result)
