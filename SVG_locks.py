#!/usr/bin/env python3

############################################################
def SVG_root(kind="start", pagesize="US-letter"):
    template_start_letter = """<!-- comment -->
<svg
    id="Layer_1"
    width="8.5in"
    height="11in"
    xmlns="http://www.w3.org/2000/svg">
"""
    template_start_A4 = """<!-- comment -->
<svg
    id="Layer_1"
    width="210mm"
    height="297mm"
    xmlns="http://www.w3.org/2000/svg">
"""
    template_start_12x12 = """<!-- comment -->
<svg
    id="Layer_1"
    width="12in"
    height="12in"
    xmlns="http://www.w3.org/2000/svg">
"""
    template_tail = """
</svg>
"""
    if (kind=="start"):
        if   pagesize == "US-letter":  return template_start_letter
        elif pagesize == "A4"       :  return template_start_A4
        elif pagesize == "12x12"    :  return template_start_12x12
    else:
        return template_tail


############################################################
def ruler_guide(x=0.0, y=0.0, scale=1.0, indent=0):
    # When scale=1.0, a US-letter page is 1056.0 units high, which is 11 inches
    #   therefore 1.0 inches = 96.0 units
    # With scale=1.0, an A4 page is 1122.5 units high, which is 297 mm
    #   therefore 1.0 mm = 3.779 units
    # 6 inches = 576 units
    # 150 mm = 566.919 units
    template_ruler = '''
<g id="ruler_guide" transform="translate({x} {y}) scale({scale} {scale})">
    <line id="ruler_line" x1="0" y1="0" x2="576" y2="0" fill="none" stroke="black" stroke-width="1"/>
    <path id="ruler_ticks_inch" d="
        M   0,0 l 0,10
        M  96,0 l 0,10
        M 192,0 l 0,10
        M 288,0 l 0,10
        M 384,0 l 0,10
        M 480,0 l 0,10
        M 576,0 l 0,10
        " fill="none" stroke="black" stroke-width="1"/>
    <text x="  5" y="12" text-anchor="left" font-size="10">0</text>
    <text x="101" y="12" text-anchor="left" font-size="10">1</text>
    <text x="197" y="12" text-anchor="left" font-size="10">2</text>
    <text x="293" y="12" text-anchor="left" font-size="10">3</text>
    <text x="389" y="12" text-anchor="left" font-size="10">4</text>
    <text x="485" y="12" text-anchor="left" font-size="10">5</text>
    <text x="581" y="12" text-anchor="left" font-size="10">6 in</text>
    <path id="ruler_ticks_mm" d="
        M   0.0,0 l 0,-10
        M  37.8,0 l 0,-10
        M  75.6,0 l 0,-10
        M 113.4,0 l 0,-10
        M 151.2,0 l 0,-10
        M 189.0,0 l 0,-10
        M 226.8,0 l 0,-10
        M 264.6,0 l 0,-10
        M 302.4,0 l 0,-10
        M 340.2,0 l 0,-10
        M 377.9,0 l 0,-10
        M 415.7,0 l 0,-10
        M 453.5,0 l 0,-10
        M 491.3,0 l 0,-10
        M 529.1,0 l 0,-10
        M 566.9,0 l 0,-10
        " fill="none" stroke="black" stroke-width="1"/>
    <text x="  5.0" y="-6" text-anchor="left" font-size="8">0</text>
    <text x=" 42.8" y="-6" text-anchor="left" font-size="8">10</text>
    <text x=" 80.6" y="-6" text-anchor="left" font-size="8">20</text>
    <text x="118.4" y="-6" text-anchor="left" font-size="8">30</text>
    <text x="156.2" y="-6" text-anchor="left" font-size="8">40</text>
    <text x="194.0" y="-6" text-anchor="left" font-size="8">50</text>
    <text x="231.8" y="-6" text-anchor="left" font-size="8">60</text>
    <text x="269.6" y="-6" text-anchor="left" font-size="8">70</text>
    <text x="307.4" y="-6" text-anchor="left" font-size="8">80</text>
    <text x="345.2" y="-6" text-anchor="left" font-size="8">90</text>
    <text x="382.9" y="-6" text-anchor="left" font-size="8">100</text>
    <text x="420.7" y="-6" text-anchor="left" font-size="8">110</text>
    <text x="458.5" y="-6" text-anchor="left" font-size="8">120</text>
    <text x="496.3" y="-6" text-anchor="left" font-size="8">130</text>
    <text x="534.1" y="-6" text-anchor="left" font-size="8">140</text>
    <text x="571.9" y="-6" text-anchor="left" font-size="8">150mm</text>
</g>
'''
    result = []
    for line in template_ruler.format(x=x,y=y,scale=scale).splitlines():
        if line == '':
            result.append("\n")
        else:
            result.append(" "*4*indent + line)
    return "\n".join(result)


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
        if length.isdigit():
            pin_length = int(length)
        else:
            pin_length = 5
        y4 = 150 + 10*pin_length
        y3, y2, y1, y0 = y4-5, y4-45, y4-50, y4-55
        template = template_key.format(x=x,y=y,y0=y0,y1=y1,y2=y2,y3=y3,y4=y4,length=length,color0=pin_length*16,color1=255-pin_length*16)
    result = []
    for line in template.splitlines():
        if line == '':
            result.append("\n")
        else:
            result.append(" "*4*indent + line)
    return "\n".join(result)


############################################################
def lock(config, x=0.0, y=0.0, scale=1.0, indent=0):
    template_start = '''
<g id="lock_{config}" transform="translate({x} {y}) scale({scale} {scale})">
    <path id="spring_cover" d="M {x1},-225 {x2},-225  {x2},-235 {x1},-235 Z" fill="grey" stroke="black" stroke-width="2.0"/>
    <line id="rotation_line" x1="{x0}" y1="0" x2="{x3}" y2="0" fill="none" stroke="green" stroke-width="8.0"/>
    <text x="0" y="600" text-anchor="middle" font-size="100">{config}</text>
'''
    template_tail = "</g>\n"
    key_inserted = (config[-4:] == " key")
    if key_inserted:
        slots = (len(config)+1-4)//3
    else:
        slots = (len(config)+1)//3

    result = []

    x0 = -150*(slots/2.0) - 160
    x1 = -150*(slots/2.0) - 50
    x2 =  150*(slots/2.0) + 50
    x3 =  150*(slots/2.0) + 255
    for line in template_start.format(x=x,y=y,x0=x0,x1=x1,x2=x2,x3=x3,scale=scale,config=config).splitlines():
        if line == '':
            result.append("\n")
        else:
            result.append(" "*4*indent + line)

    for (offset,kind,key) in [(150*(i+0.5-slots/2.0), config[i*3], config[i*3+1]) for i in range(slots)]:
        if   (kind == "P") or (kind == "p"):  kind = "plain"
        elif (kind == "S") or (kind == "s"):  kind = "spool"
        elif (kind == "G") or (kind == "g"):  kind = "serrated"
        elif (kind == "_"):  continue

        if key_inserted:
            # Key inserted, tops of key pins line up with barrel
            result.append(pin(kind="key", length=key, x=offset, y=0, indent=indent+1))
            result.append(pin(kind=kind, x=offset, y=0, indent=indent+1))
            result.append(spring(length=1, x=offset, y=-130, indent=indent+1))
        else:
            # Key not inserted, bottoms of key pins line up with each other
            result.append(pin(kind="key", length=key, x=offset, y=110-10*int(key), indent=indent+1))
            result.append(pin(kind=kind, x=offset, y=110-10*int(key), indent=indent+1))
            result.append(spring(length=12-int(key), x=offset, y=-20-10*int(key), indent=indent+1))
    result.append(" "*4*indent + "</g>  <!-- id=\"lock_{config}\" -->\n".format(config=config))
    return "\n".join(result)


############################################################
def key(config, x=0.0, y=0.0, scale=1.0, indent=0):
    template_start = '''
<g id="key_{config}" transform="translate({x} {y}) scale({scale} {scale})">
'''
    slots = (len(config)+1)//3
    xl = -150*(slots/2.0)  # Center of left most pin
    xr =  150*(slots/2.0)  # Center of right most pin

    config_spec = [config[3*i+1] for i in range(slots)]
    for i in range(slots):
        if not config_spec[i].isnumeric():
            config_spec[i] = '5'

    result = []
    for line in template_start.format(x=x,y=y,scale=scale,config="".join(config_spec)).splitlines():
        if line == '':
            result.append("\n")
        else:
            result.append(" "*4*indent + line)

    result.append(" "*4*(indent+1) + '''<mask id="key_mask_{config}">'''.format(config="".join(config_spec)))
    result.append(" "*4*(indent+2) + '''<path d="M -950,-250 660,-250 660,750 -950,750 Z" fill="white" stroke="none"/>''')
    template_mask = '''<path id="clip_path_{n}" d="M {x},{y} l 25,0  150,-150  0,-100  -350,0  0,100  150,150  25,0 Z" fill="black" stroke="none"/>'''
    for (n, offset,pin) in [(i, 150*(i+0.5-slots/2.0), int(config_spec[i])) for i in range(slots)]:
        result.append(" "*4*(indent+2) + template_mask.format(n=n,x=offset,y=250+pin*10))
    result.append(" "*4*(indent+1) + "</mask>")

    template_key = '''
    <path id="key_outline_handle" d="m {xl},200  0,-50  -50,0  0,-50  -100,-100  -250,0  -100,100  0,500  100,100  250,0  100,-100  0,-50  50,0
        Z m -300,150 0,50 -100,0 0,-100 100,0 0,50 Z" fill="#ef9500" stroke="black" stroke-width="5.0" mask="url(#key_mask_{config})"/>
    <path id="key_outline_rail" d="m {xr},200  200,200  -100,100  -100,0 L {xl},500 l 0,-300 Z" fill="#ffa500" stroke="black" mask="url(#key_mask_{config})"/>
    <path id="key_outline_groove0" d="M {xl},350  {xr},350 l 150,0 -50,-50 L {xr},300 {xl},300 Z" fill="#ffa580" stroke="none" mask="url(#key_mask_{config})"/>
    <path id="key_outline_groove1" d="M {xl},475  {xr},475 l 125,0 50,-50 L {xr},425 {xl},425 Z" fill="#af5500" stroke="none" mask="url(#key_mask_{config})"/>
'''
    for line in template_key.format(xl=xl-150,xr=xr+50,config="".join(config_spec)).splitlines():
        if line == '':
            result.append("\n")
        else:
            result.append(" "*4*indent + line)

    result.append(" "*4*indent + "</g>  <!-- id=\"key_{config}\" -->\n".format(config="".join(config_spec)))
    return "\n".join(result)


############################################################
def lock_holder_outline(kind="plain", x=0.0, y=0.0, scale=1.0, rotate=0.0, indent=0):
    template_start = '''
<g id="lock_holder_outline_{kind}" transform="translate({x} {y}) scale({scale} {scale})">
    <circle cx="0" cy="-2700" r="200" fill="none" stroke="black" stroke-width="5.0"/>
    <path d="
        M  1300, 1000  a 200,200 90 0 1  -200,  200
        l -2200,    0  a 200,200 90 0 1  -200, -200
        l     0,-3800  a 200,200 90 0 1   200, -200
        l  2200,    0  a 200,200 90 0 1   200,  200
        l     0, 3800" fill="none" stroke="black" stroke-width="5.0"/>
'''
    template_plain = '''
    <circle id="lock_hole_circle" cx="0" cy="-100" r="920" fill="none" stroke="black" stroke-width="5.0"/>
'''
    template_notch = '''
    <path id="lock_hole_notch" d="
        M -907,-232
        A 915,915 0 0 1  907,-232
        A 150,150 0 0 0  907,  32
        A 915,915 0 0 1 -907,  32
        A 150,150 0 0 0 -907,-232 Z" fill="none" stroke="black" stroke-width="5.0"/>
'''
    template_end = "</g>  <!-- id=\"lock_holder_outline_{kind}\" -->\n"


    result = []
    for line in template_start.format(kind=kind,x=x,y=y,scale=scale,rotate=rotate).splitlines():
        if line == '':
            result.append("\n")
        else:
            result.append(" "*4*indent + line)

    if   kind == ("plain"):
        result.append(" "*4*indent + template_plain)
    elif kind == ("notch"):
        result.append(" "*4*indent + template_notch)

    result.append(" "*4*indent + template_end.format(kind=kind))
    return "\n".join(result)


############################################################
def lock_lever_outline(x=0.0, y=0.0, scale=1.0, rotate=0.0, indent=0):
    template_start = '''
<g id="lock_lever_outline" transform="translate({x} {y}) scale({scale} {scale}) rotate({rotate})">
    <ellipse cx="0" cy="-200" rx="700" ry="2200" fill="none" stroke="black" stroke-width="5.0"/>
    <g transform="rotate(30 0 1210)">
        <rect x="-128" y="810" width="256" height="800" fill="none" stroke="black" stroke-width="5.0"/>
        <circle cx="264" cy="1200" r="80" fill="none" stroke="black" stroke-width="5.0"/>
        <circle cx="-264" cy="1200" r="80" fill="none" stroke="black" stroke-width="5.0"/>
    </g>
'''
    template_end = "</g>  <!-- id=\"lock_lever_outline\" -->\n"

    result = []
    for line in template_start.format(x=x,y=y,scale=scale,rotate=rotate).splitlines():
        if line == '':
            result.append("\n")
        else:
            result.append(" "*4*indent + line)

    result.append(" "*4*indent + template_end)
    return "\n".join(result)


############################################################
def lock_holder(config, descr="", alignment=True, outline=True, x=0.0, y=0.0, scale=1.0, indent=0):
    template_start = '''
<g id="lock_holder" transform="translate({x} {y}) scale({scale} {scale})">
    <text x="0" y="1100" text-anchor="middle" font-size="200">{descr}</text>
'''
    template_end = "</g>  <!-- id=\"lock_holder\" -->\n"

    result = []
    for line in template_start.format(descr=descr,x=x,y=y,scale=scale).splitlines():
        if line == '':
            result.append("\n")
        else:
            result.append(" "*4*indent + line)

    if alignment:
        result.append(alignment_mark(kind="SE", x= 1300, y= 1200, indent=indent+1))
        result.append(alignment_mark(kind="SW", x=-1300, y= 1200, indent=indent+1))
        result.append(alignment_mark(kind="NE", x= 1300, y=-3000, indent=indent+1))
        result.append(alignment_mark(kind="NW", x=-1300, y=-3000, indent=indent+1))

    if outline:
        result.append(lock_holder_outline(kind="plain", x=0, y=0, scale=1.0, indent=indent+1))

    if config is not None:
        key_inserted = (config[-4:] == " key")
        if key_inserted:
            result.append(key(config=config[:-4], x=225, y=-2260, scale=1.6, indent=indent+1))
            result.append(lock(config=config, x=225, y=-2100, scale=1.6, indent=indent+1))
        else:
            result.append(lock(config=config, x=0, y=-2100, scale=1.6, indent=indent+1))

    result.append(" "*4*indent + template_end)
    return "\n".join(result)


############################################################
def paper_sheet(configs, kind="front", pagesize="US-letter", indent=0):
    template_start = '''<g id="paper_{kind}_sheet_{pagesize}">\n'''
    template_end = "</g>  <!-- id=\"paper_{kind}_sheet_{pagesize}\" -->\n"

    result = []
    for line in template_start.format(kind=kind,pagesize=pagesize).splitlines():
        if line == '':
            result.append("\n")
        else:
            result.append(" "*4*indent + line)

    if pagesize=="US-letter":
        ## US letter page size
        #result.append(alignment_mark(kind="empty", x=  0, y=   0, scale=0.2, indent=indent+1))
        #result.append(alignment_mark(kind="empty", x=816, y=   0, scale=0.2, indent=indent+1))
        #result.append(alignment_mark(kind="empty", x=  0, y=1056, scale=0.2, indent=indent+1))
        #result.append(alignment_mark(kind="empty", x=816, y=1056, scale=0.2, indent=indent+1))
        result.append(ruler_guide(x=100, y=1035, scale=1.0, indent=indent+1))
        xoffset=0.5*2600*0.06 + (816-5*2600*0.06)/2  # Centering the grid of lock_holder horizontally on the page
        yoffset=192
    else:
        ## A4 page size
        #result.append(alignment_mark(kind="empty", x=     0, y=     0, scale=0.2, indent=indent+1))
        #result.append(alignment_mark(kind="empty", x=793.75, y=     0, scale=0.2, indent=indent+1))
        #result.append(alignment_mark(kind="empty", x=     0, y=1122.5, scale=0.2, indent=indent+1))
        #result.append(alignment_mark(kind="empty", x=793.75, y=1122.5, scale=0.2, indent=indent+1))
        result.append(ruler_guide(x=100, y=1080, scale=1.0, indent=indent+1))
        xoffset=0.5*2600*0.06 + (793.75-5*2600*0.06)/2  # Centering the grid of lock_holder horizontally on the page
        yoffset=204  # Use US-letter offset for A4

    if   (kind == "front"):
        for (n, (config, descr)) in enumerate(configs):
            x = ((n %  5) * 2600*0.06 + xoffset)
            y = ((n // 5) * 4200*0.06 + yoffset)
            result.append(lock_holder(config=config, descr=descr, alignment=False, outline=True, scale=0.06, x=x, y=y, indent=indent+1))

    elif (kind == "back"):
        for (n, (config, descr)) in enumerate(configs):
            x = ((4 - n %  5) * 2600*0.06 + xoffset)
            y = ((n // 5) * 4200*0.06 + yoffset)
            result.append(lock_holder(config=config, descr=descr, alignment=False, outline=True, scale=0.06, x=x, y=y, indent=indent+1))

    else:  # kind == "cut"
        for n in range(20):
            x = ((n %  5) * 2600*0.06 + xoffset)
            y = ((n // 5) * 4200*0.06 + yoffset)
            result.append(lock_holder_outline(kind="plain",scale=0.06, x=x, y=y, indent=indent+1))

    result.append(" "*4*indent + template_end.format(kind=kind,pagesize=pagesize))
    return "\n".join(result)


############################################################
def plastic_cut_sheet(pagesize="12x12", indent=0):
    template_start = '''<g id="plastic_cut_sheet_{pagesize}">\n'''
    template_end = "</g>  <!-- id=\"plastic_cut_sheet_{pagesize}\" -->\n"

    result = []
    for line in template_start.format(pagesize=pagesize).splitlines():
        if line == '':
            result.append("\n")
        else:
            result.append(" "*4*indent + line)

    result.append(alignment_mark(kind="empty", x=   0, y=   0, scale=0.2, indent=indent+1))
    result.append(alignment_mark(kind="empty", x=1152, y=   0, scale=0.2, indent=indent+1))
    result.append(alignment_mark(kind="empty", x=   0, y=1152, scale=0.2, indent=indent+1))
    result.append(alignment_mark(kind="empty", x=1152, y=1152, scale=0.2, indent=indent+1))
    xoffset=97
    yoffset=199

    for n in range(27):
        x = ((n %  7) * 2600*0.06 + xoffset)
        y = ((n // 7) * 4200*0.06 + yoffset)
        if (n < 11):
            result.append(lock_holder_outline(kind="plain", scale=0.06, x=x, y=y, indent=indent+1))
        else:
            result.append(lock_holder_outline(kind="notch", scale=0.06, x=x, y=y, indent=indent+1))

    result.append(lock_lever_outline(x= 999, y= 920, scale=0.06, indent=indent+1))
    result.append(lock_lever_outline(x=1082, y= 986, scale=0.06, indent=indent+1))
    result.append(lock_lever_outline(x= 140, y=1070, scale=0.06, rotate=90, indent=indent+1))
    result.append(lock_lever_outline(x= 398, y=1090, scale=0.06, rotate=90, indent=indent+1))
    result.append(lock_lever_outline(x= 656, y=1070, scale=0.06, rotate=90, indent=indent+1))
    result.append(lock_lever_outline(x= 914, y=1090, scale=0.06, rotate=90, indent=indent+1))

    result.append(" "*4*indent + template_end.format(pagesize=pagesize))
    return "\n".join(result)
