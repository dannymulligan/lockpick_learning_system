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
def ruler_guide(x=0.0, y=0.0, scale=1.0, rotate=0.0, indent=0):
    # When scale=1.0, a US-letter page is 1056.0 units high, which is 11 inches
    #   therefore 1.0 inches = 96.0 units
    # With scale=1.0, an A4 page is 1122.5 units high, which is 297 mm
    #   therefore 1.0 mm = 3.779 units
    # 6 inches = 576 units
    # 8 inches = 768 units
    # 150 mm = 566.919 units
    template_ruler = '''
<g id="ruler_guide" transform="translate({x} {y}) scale({scale} {scale}) rotate({rotate})">
    <line id="ruler_line" x1="0" y1="0" x2="768" y2="0" fill="none" stroke="black" stroke-width="0.6"/>
    <path id="ruler_ticks_inch" d="
        M   0,0 l 0,10  M  96,0 l 0,10  M 192,0 l 0,10
        M 288,0 l 0,10  M 384,0 l 0,10  M 480,0 l 0,10
        M 576,0 l 0,10  M 672,0 l 0,10  M 768,0 l 0,10
        " fill="none" stroke="black" stroke-width="0.5"/>
    <text x="  5" y="10" text-anchor="left" font-size="10">0</text>
    <text x="101" y="10" text-anchor="left" font-size="10">1</text>
    <text x="197" y="10" text-anchor="left" font-size="10">2</text>
    <text x="293" y="10" text-anchor="left" font-size="10">3</text>
    <text x="389" y="10" text-anchor="left" font-size="10">4</text>
    <text x="485" y="10" text-anchor="left" font-size="10">5</text>
    <text x="581" y="10" text-anchor="left" font-size="10">6</text>
    <text x="677" y="10" text-anchor="left" font-size="10">7</text>
    <text x="746" y="10" text-anchor="right" font-size="10">8 in</text>
    <path id="ruler_ticks_mm" d="
        M   0.0,0 l 0,-10  M  37.8,0 l 0,-10  M  75.6,0 l 0,-10
        M 113.4,0 l 0,-10  M 151.2,0 l 0,-10  M 189.0,0 l 0,-10
        M 226.8,0 l 0,-10  M 264.6,0 l 0,-10  M 302.4,0 l 0,-10
        M 340.2,0 l 0,-10  M 377.9,0 l 0,-10  M 415.7,0 l 0,-10
        M 453.5,0 l 0,-10  M 491.3,0 l 0,-10  M 529.1,0 l 0,-10
        M 566.9,0 l 0,-10  M 604.7,0 l 0,-10  M 642.5,0 l 0,-10
        M 680.3,0 l 0,-10  M 718.1,0 l 0,-10  M 755.9,0 l 0,-10
        " fill="none" stroke="black" stroke-width="0.5"/>
    <text x="  0.0" y="-14" text-anchor="middle" font-size="8">0</text>
    <text x=" 37.8" y="-14" text-anchor="middle" font-size="8">10</text>
    <text x=" 75.6" y="-14" text-anchor="middle" font-size="8">20</text>
    <text x="113.4" y="-14" text-anchor="middle" font-size="8">30</text>
    <text x="151.2" y="-14" text-anchor="middle" font-size="8">40</text>
    <text x="189.0" y="-14" text-anchor="middle" font-size="8">50</text>
    <text x="226.8" y="-14" text-anchor="middle" font-size="8">60</text>
    <text x="264.6" y="-14" text-anchor="middle" font-size="8">70</text>
    <text x="302.4" y="-14" text-anchor="middle" font-size="8">80</text>
    <text x="340.2" y="-14" text-anchor="middle" font-size="8">90</text>
    <text x="377.9" y="-14" text-anchor="middle" font-size="8">100</text>
    <text x="415.7" y="-14" text-anchor="middle" font-size="8">110</text>
    <text x="453.5" y="-14" text-anchor="middle" font-size="8">120</text>
    <text x="491.3" y="-14" text-anchor="middle" font-size="8">130</text>
    <text x="529.1" y="-14" text-anchor="middle" font-size="8">140</text>
    <text x="566.9" y="-14" text-anchor="middle" font-size="8">150</text>
    <text x="604.7" y="-14" text-anchor="middle" font-size="8">160</text>
    <text x="642.5" y="-14" text-anchor="middle" font-size="8">170</text>
    <text x="680.3" y="-14" text-anchor="middle" font-size="8">180</text>
    <text x="718.1" y="-14" text-anchor="middle" font-size="8">190</text>
    <text x="755.9" y="-14" text-anchor="middle" font-size="8">200mm</text>
</g>  <!-- id="ruler_guide" -->

'''
    result = []
    for line in template_ruler.format(x=x,y=y,scale=scale, rotate=rotate).splitlines():
        if line == '':
            result.append("")
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
</g>  <!-- id="alignment_empty" -->'''
    template_filled = '''
<g id="alignment_filled" transform="translate({x} {y}) scale({scale} {scale})">
    <line x1="100" y1="0" x2="-100" y2="0" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="0" y1="100" x2="0" y2="-100" fill="none" stroke="black" stroke-width="2.0"/>
    <circle cx="0" cy="0" r="80" fill="none" stroke="black" stroke-width="2.0"/>
    <path d="M 0,0 L -80,0 A 80,80 90 0 0 0,80 L 0,0" fill="black" stroke="none"/>
    <path d="M 0,0 L 80,0 A 80,80 90 0 0 0,-80 L 0,0" fill="black" stroke="none"/>
</g>  <!-- id="alignment_filled" -->'''
    template_SE = '''
<g id="alignment_SE" transform="translate({x} {y}) scale({scale} {scale})">
    <line x1="100" y1="0" x2="-100" y2="0" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="0" y1="100" x2="0" y2="-100" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="-50" y1="-50" x2="-20" y2="-20" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="-20" y1="-45" x2="-20" y2="-20" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="-45" y1="-20" x2="-20" y2="-20" fill="none" stroke="black" stroke-width="2.0"/>
    <circle cx="0" cy="0" r="80" fill="none" stroke="black" stroke-width="2.0"/>
</g>  <!-- id="alignment_SE" -->'''
    template_SW = '''
<g id="alignment_SW" transform="translate({x} {y}) scale({scale} {scale})">
    <line x1="100" y1="0" x2="-100" y2="0" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="0" y1="100" x2="0" y2="-100" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="50" y1="-50" x2="20" y2="-20" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="20" y1="-45" x2="20" y2="-20" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="45" y1="-20" x2="20" y2="-20" fill="none" stroke="black" stroke-width="2.0"/>
    <circle cx="0" cy="0" r="80" fill="none" stroke="black" stroke-width="2.0"/>
</g>  <!-- id="alignment_SW" -->'''
    template_NE = '''
<g id="alignment_NE" transform="translate({x} {y}) scale({scale} {scale})">
    <line x1="100" y1="0" x2="-100" y2="0" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="0" y1="100" x2="0" y2="-100" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="-50" y1="50" x2="-20" y2="20" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="-20" y1="45" x2="-20" y2="20" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="-45" y1="20" x2="-20" y2="20" fill="none" stroke="black" stroke-width="2.0"/>
    <circle cx="0" cy="0" r="80" fill="none" stroke="black" stroke-width="2.0"/>
</g>  <!-- id="alignment_NE" -->'''
    template_NW = '''
<g id="alignment_NW" transform="translate({x} {y}) scale({scale} {scale})">
    <line x1="100" y1="0" x2="-100" y2="0" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="0" y1="100" x2="0" y2="-100" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="50" y1="50" x2="20" y2="20" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="20" y1="45" x2="20" y2="20" fill="none" stroke="black" stroke-width="2.0"/>
    <line x1="45" y1="20" x2="20" y2="20" fill="none" stroke="black" stroke-width="2.0"/>
    <circle cx="0" cy="0" r="80" fill="none" stroke="black" stroke-width="2.0"/>
</g>  <!-- id="alignment_NW" -->'''

    if   kind == "empty" :  template = template_empty.format (x=x, y=y, scale=scale)
    elif kind == "filled":  template = template_filled.format(x=x, y=y, scale=scale)
    elif kind == "SE"    :  template = template_SE.format    (x=x, y=y, scale=scale)
    elif kind == "SW"    :  template = template_SW.format    (x=x, y=y, scale=scale)
    elif kind == "NE"    :  template = template_NE.format    (x=x, y=y, scale=scale)
    elif kind == "NW"    :  template = template_NW.format    (x=x, y=y, scale=scale)
    result = []
    for line in template.splitlines():
        if line == '':
            result.append("")
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
    "  fill="none" stroke="black" stroke-width="4.0"/>'''
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
            result.append("")
        else:
            result.append(" "*4*indent + line)
    return "\n".join(result)


############################################################
def pin(kind="plain", pin_label="", pin_length=0, x=0.0, y=0.0, scale=0.0, indent=0):
    template_plain = '''
<path id="plain_pin" transform="translate({x},{y})"
    d="M 0,-3 L 45,-3 Q 50,-3 50,-8 L 50,-122 Q 50,-127 45,-127 L -45,-127 Q -50,-127 -50,-122 L -50, -8 Q -50,-3 -45,-3  L 0,-3"
    fill="#ffd020" stroke="black" stroke-width="2.0"/>'''
    template_spool = '''
<g id="spool_pin" transform="translate({x},{y})">
    <path id="spool_pin_mid" d="M 0,-30 L 35,-30 L 35,-100 L -35,-100 L -35,-30 L 0,-30" fill="#003090" stroke="black" stroke-width="2.0"/>
    <path id="spool_pin_top" d="M 0,-100 L 45,-100 Q 50,-100 50,-103 L 50,-122 Q 50,-127 45,-127 L -45,-127 Q -50,-127 -50,-122 L -50,-105 Q -50,-100 -45,-100  L 0,-100" fill="#0f50b0" stroke="black" stroke-width="2.0"/>
    <path id="spool_pin_bot" d="M 0,-3 L 45,-3 Q 50,-3 50,-8 L 50,-25 Q 50,-30 45,-30 L -45,-30 Q -50,-30 -50,-25 L -50,-8 Q -50,-3 -45,-3  L 0,-3" fill="#0f50b0" stroke="black" stroke-width="2.0"/>
</g>  <!-- id="spool_pin" -->'''
    template_serrated = '''
<g id="serrated_pin" transform="translate({x},{y})">
    <path id="serrated_pin_base" d="M 0,-3  L 45,-3  Q 50,-3 50,-8  L 50,-122  Q 50,-127 45,-127 L -45,-127  Q -50,-127 -50,-122  L -50, -8  Q -50,-3 -45,-3  L 0,-3"
        fill="#409020" stroke="black" stroke-width="2.0"/>
    <path id="serrated_pin_lines" d="M -50, -20 L 50, -20  M -50,-30 L 50,-30  M -50, -40 L 50, -40  M -50,-50 L 50,-50  M -50, -60 L 50, -60
        M -50,-70 L 50,-70  M -50, -80 L 50, -80  M -50,-90 L 50,-90  M -50,-100 L 50,-100  M -50,-110 L 50,-110" fill="none" stroke="black" stroke-width="5.0"/>
</g>  <!-- id="serrated_pin" -->'''
    template_key = '''
<g id="pin_{pin_length}" transform="translate({x},{y})">
    <path id="pin_{pin_length}_shape" d="M 0,0 L 45,0 Q 50,0 50,5 L 50,{y0} Q 50,{y1} 45,{y2} L 5,{y3} Q 0,{y4} -5,{y3} L -45,{y2} Q -50,{y1} -50,{y0}  L -50,5 Q -50,0 -45,0 L 0,0"
        fill="#ff{color0:02x}{color1:02x}" stroke="black" stroke-width="2.0"/>
    <text x="0" y="100" text-anchor="middle" font-size="80">{pin_label}</text>
</g>  <!-- id="pin_{pin_length}" -->'''

    if   kind == "plain"   :  template = template_plain.format(x=x,y=y)
    elif kind == "spool"   :  template = template_spool.format(x=x,y=y)
    elif kind == "serrated":  template = template_serrated.format(x=x,y=y)
    elif kind == "key"     :
        y4 = 150 + 10*pin_length
        y3, y2, y1, y0 = y4-5, y4-45, y4-50, y4-55
        template = template_key.format(x=x,y=y,y0=y0,y1=y1,y2=y2,y3=y3,y4=y4,pin_label=pin_label,pin_length=pin_length,color0=pin_length*16,color1=255-pin_length*16)
    result = []
    for line in template.splitlines():
        if line == '':
            result.append("")
        else:
            result.append(" "*4*indent + line)
    return "\n".join(result)


############################################################
def lock_body(pin_slots, x=0.0, y=0.0, scale=1.0, indent=0):
    template_start = '''<g id="lock_body_{pin_slots}">
    <path id="lock_body_top" d="M {x0},-40 {x1},-40 {x1},0 {x2},0 {x2},-250 {x0},-250 Z" fill="#efeabf" stroke="black" stroke-width="2.0"/>
    <path id="spring_cover" d="M {x1},-225 {x2},-225  {x2},-235 {x1},-235 Z" fill="grey" stroke="black" stroke-width="2.0"/>
    <path id="lock_body_cylinder" d="M {xx0},-35 {xx1},-35 {xx1},5 {x3},5 {x3},440 {xx1},440 {xx1},480 {xx0},480 Z" fill="#ffff88" stroke="black" stroke-width="2.0"/>
    <path id="lock_body_bottom" d="M {x0},485 {x1},485 {x1},445 {x2},445 {x2},600 {x0},600 Z" fill="#efeabf" stroke="black" stroke-width="2.0"/>
</g>  <!-- id="lock_body_{pin_slots}" -->"'''

    xx0 = -150*(pin_slots/2.0) - 145
    x0  = -150*(pin_slots/2.0) - 100
    xx1 = -150*(pin_slots/2.0) - 55
    x1  = -150*(pin_slots/2.0) - 50
    x2  =  150*(pin_slots/2.0) + 50
    x3  =  150*(pin_slots/2.0) + 150
    result = []
    for line in template_start.format(x=x,y=y,xx0=xx0,xx1=xx1,x0=x0,x1=x1,x2=x2,x3=x3,scale=scale,pin_slots=pin_slots).splitlines():
        if line == '':
            result.append("")
        else:
            result.append(" "*4*indent + line)
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
            result.append("")
        else:
            result.append(" "*4*indent + line)

    template_key = '''    <path id="key_outline_rail" d="m {xr},200  200,200  -100,100  -100,0 L {xl},500 l 0,-300 Z" fill="#9e9e9e" stroke="black"/>
    <path id="key_outline_groove0" d="M {xl},350  {xr},350 l 150,0 -50,-50 L {xr},300 {xl},300 Z" fill="#b9b9b9" stroke="none"/>
    <path id="key_outline_groove1" d="M {xl},475  {xr},475 l 125,0 50,-50 L {xr},425 {xl},425 Z" fill="#848484" stroke="none"/>
    <path id="key_outline_handle" d="
        m {xl},200 0,-50 -50,0  0,-50 a 100,100 0 0 0 -100,-100 l -250,0
        a 100,100 0 0 0 -100,100 l 0,500 a 100,100 0 0 0 100,100 l 250,0
        a 100,100 0 0 0 100,-100 l 0,-50  50,0 Z" fill="#9e9e9e" stroke="black" stroke-width="5.0"/>
    <circle id="key_outline_handle_hole" cx="{xl0}" cy="350" r="80" fill="white" stroke="black" stroke-width="5.0"/>'''
    for line in template_key.format(xl0=xl-500,xl=xl-150,xr=xr+50,config="".join(config_spec)).splitlines():
        if line == '':
            result.append("")
        else:
            result.append(" "*4*indent + line)

    template_mask = '''<path id="key_cut_{n}" transform="translate({x},{y})" d="M 0,0 l 25,0 125,-125 -300,0 125,125 25,0 Z" fill="#ffff88" stroke="none"/>'''
    for (n, offset,pin) in [(i, 150*(i+0.5-slots/2.0), int(config_spec[i])) for i in range(slots)]:
        result.append(" "*4*(indent+1) + template_mask.format(n=n,x=offset,y=230+pin*10))

    result.append(" "*4*indent + "</g>  <!-- id=\"key_{config}\" -->".format(config="".join(config_spec)))
    return "\n".join(result)


############################################################
def lock(config, has_key, x=0.0, y=0.0, scale=1.0, indent=0):
    template_start = '''<g id="lock_{config}" transform="translate({x} {y}) scale({scale})">'''

    slots = (len(config)+1)//3

    result = []
    for line in template_start.format(config=config, x=x, y=y, scale=scale).splitlines():
        if line == '':
            result.append("")
        else:
            result.append(" "*4*indent + line)

    # Lowest level in the drawing is the lock body
    result.append(lock_body(pin_slots=slots, x=0, y=0, indent=indent+1))

    # Next is the key
    if has_key:
        result.append(key(config, x=0, y=-75, indent=indent+1))

    # Then the springs, & pins
    for (offset,kind,pin_label) in [(150*(i+0.5-slots/2.0), config[i*3], config[i*3+1]) for i in range(slots)]:
        if   (kind == "P") or (kind == "p"):  kind = "plain"
        elif (kind == "S") or (kind == "s"):  kind = "spool"
        elif (kind == "G") or (kind == "g"):  kind = "serrated"
        elif (kind == "_"):  continue

        if pin_label == "_":
            pin_length = 5
            pin_label = ""
        else:
            pin_length = int(pin_label)

        if has_key:
            # Key inserted, tops of key pins line up with barrel
            result.append(pin(kind="key", pin_label=pin_label, pin_length=pin_length, x=offset, y=0, indent=indent+1))
            result.append(pin(kind=kind, x=offset, y=0, indent=indent+1))
            result.append(spring(length=1, x=offset, y=-130, indent=indent+1))
        else:
            # Key not inserted, bottoms of key pins line up with each other
            result.append(pin(kind="key", pin_label=pin_label, pin_length=pin_length, x=offset, y=110-10*pin_length, indent=indent+1))
            result.append(pin(kind=kind, x=offset, y=110-10*pin_length, indent=indent+1))
            result.append(spring(length=12-pin_length, x=offset, y=-20-10*pin_length, indent=indent+1))

    # Finally, the text
    result.append(" "*4*indent + '''    <text x="0" y="560" text-anchor="middle" font-size="90">{config}</text>'''.format(config=config))

    result.append(" "*4*indent + "</g>  <!-- id=\"lock_{config}\" -->".format(config=config))
    return "\n".join(result)


############################################################
def lock_holder_outline(kind="plain", alignment=False, x=0.0, y=0.0, scale=1.0, rotate=0.0, color="black", indent=0):
    template_start = '''
<g id="lock_holder_outline_{kind}" transform="translate({x} {y}) scale({scale} {scale})">'''
    template_plain = '''    <circle id="lock_hole_circle" cx="0" cy="0" r="920" fill="none" stroke="{color}" stroke-width="5.0"/>
    <path id="lock_hole_center_crosshairs" d="M -80,0 80,-0 M 0,-80 0,80" fill="none" stroke="black" stroke-width="5.0"/>'''
    template_notch = '''    <path id="lock_hole_notch" d="
        M -907,-132
        A 915,915 0 0 1  907,-132
        A 150,150 0 0 0  907, 132
        A 915,915 0 0 1 -907, 132
        A 150,150 0 0 0 -907,-132 Z" fill="none" stroke="{color}" stroke-width="5.0"/>
    <path id="lock_hole_notch_center_crosshairs" d="M -80,0 80,-0 M 0,-80 0,80" fill="none" stroke="black" stroke-width="5.0"/>'''
    template_nut_recess = '''    <path id="lock_nut_recess" transform="translate(0 -2600) scale(4.08)" d="
        M 100,0  50,86.6 -50,86.6 -100,0 -50,-86.6 50,-86.6 100,0 50,0 A 50,50 0 1 0 50,0.001 Z" fill="yellow" stroke="none"/>'''
    template_end = '''    <path d="
        M  1850, 1000  a 400,400 90 0 1  -400,  400
        l -2900,    0  a 400,400 90 0 1  -400, -400
        l     0,-3800  a 400,400 90 0 1   400, -400
        l  2900,    0  a 400,400 90 0 1   400,  400
        l     0, 3800" fill="none" stroke="{color}" stroke-width="5.0"/>
    <path id="screw_hole_center_crosshairs" d="m 0,-2600 0,80 0,-160 0,80 80,0 -160,0 80,0" fill="none" stroke="black" stroke-width="5.0"/>
    <circle id="screw_hole" cx="0" cy="-2600" r="200" fill="none" stroke="{color}" stroke-width="5.0"/>
</g>  <!-- id="lock_holder_outline_{kind}" -->
'''

    result = []
    for line in template_start.format(kind=kind,x=x,y=y,scale=scale,rotate=rotate).splitlines():
        if line == '':
            result.append("")
        else:
            result.append(" "*4*indent + line)

    if alignment:
        result.append(alignment_mark(kind="SE", x= 1850, y= 1400, indent=indent+1))
        result.append(alignment_mark(kind="SW", x=-1850, y= 1400, indent=indent+1))
        result.append(alignment_mark(kind="NE", x= 1850, y=-3200, indent=indent+1))
        result.append(alignment_mark(kind="NW", x=-1850, y=-3200, indent=indent+1))

    if   kind == ("plain"):
        for line in template_plain.format(color=color).splitlines():
            result.append(" "*4*indent + line)
    elif kind == ("notch"):
        for line in template_notch.format(color=color).splitlines():
            result.append(" "*4*indent + line)
    elif kind == ("notch+recess"):
        for line in template_nut_recess.splitlines():
            result.append(" "*4*indent + line)
        for line in template_notch.format(color=color).splitlines():
            result.append(" "*4*indent + line)
    elif kind == ("notch+lever"):
        for line in template_notch.format(color=color).splitlines():
            result.append(" "*4*indent + line)
        result.append(lock_lever_outline(x=-950, y=-2250, scale="-1 1", rotate=180, color="red", indent=indent+1))
        result.append(lock_lever_outline(x=950, y=-2250, rotate=180, color="red", indent=indent+1))

    for line in template_end.format(kind=kind,color=color).splitlines():
        result.append(" "*4*indent + line)
    return "\n".join(result)


############################################################
def lock_lever_outline(x=0.0, y=0.0, scale=1.0, rotate=0.0, mirror=False, color="black", indent=0):
    template = '''
<g id="lock_lever_outline" transform="translate({x} {y}) scale({scale}) rotate({rotate})">
    <g id="lever_attachments" transform="rotate(35)">
        <rect x="-128" y="-400" width="256" height="800" fill="none" stroke="{color}" stroke-width="5.0"/>
        <path id="lever_center_crosshairs" d="M -100,0 100,0 M 0,-100 0,100" fill="none" stroke="black" stroke-width="5.0"/>
        <circle cx="264" cy="0" r="80" fill="none" stroke="{color}" stroke-width="5.0"/>
        <circle cx="-264" cy="0" r="80" fill="none" stroke="{color}" stroke-width="5.0"/>
    </g>  <!-- id="lever_attachments" -->
    <path d="M  -700,0
             A  700,700 0 1 0  139.8,-685.9
             A  300,300 0 0 1 -100.0,-966.5
             L -200.2,-3211.1
             A  200,200 0 0 0 -700.0,-3212.4
             L -700,0
             " fill="none" stroke="{color}" stroke-width="5.0"/>
</g>  <!-- id="lock_lever_outline" -->'''

    result = []
    for line in template.format(x=x,y=y,scale=scale,rotate=rotate,color=color).splitlines():
        if line == '':
            result.append("")
        else:
            result.append(" "*4*indent + line)
    return "\n".join(result)


############################################################
def lock_holder(lock_configuration, has_key=True, descr="", alignment=True, outline=True, x=0.0, y=0.0, scale=1.0, indent=0):
    template_start = '''
<g id="lock_holder" transform="translate({x} {y}) scale({scale} {scale})">
    <text x="0" y="1200" text-anchor="middle" font-size="240">{descr}</text>'''
    template_end = '''</g>  <!-- id="lock_holder" -->'''

    result = []
    for line in template_start.format(descr=descr,x=x,y=y,scale=scale).splitlines():
        if line == '':
            result.append("")
        else:
            result.append(" "*4*indent + line)

    if lock_configuration is not None:
        result.append(lock(config=lock_configuration, has_key=has_key, x=500, y=-2450, scale=2.4, indent=indent+1))

    if outline:
        result.append(lock_holder_outline(kind="plain", alignment=True, x=0, y=0, scale=1.0, indent=indent+1))

    result.append(" "*4*indent + template_end)
    return "\n".join(result)


############################################################
def paper_sheet(configs, kind="lock_diagrams", page_title=None, alignment=False, pagesize="US-letter", indent=0):
    template_start = '''<g id="paper_{kind}_sheet_{pagesize}">'''
    template_end = '''</g>  <!-- id="paper_{kind}_sheet_{pagesize}" -->'''

    result = []
    for line in template_start.format(kind=kind,pagesize=pagesize).splitlines():
        if line == '':
            result.append("")
        else:
            result.append(" "*4*indent + line)

    if pagesize=="US-letter":
        # US letter page size
        # (width = 816, height = 1056)
        xoffset = 0.5*3700*0.06 + (816-3*3700*0.06-2*300*0.06)/2  # Center the grid of lock_holder horizontally on the page
        xcenter = 816*0.5
        yoffset = 3200*0.06 + (1056-3*4600*0.06-2*400*0.06)/2  # Center the grid of lock_holder vertically on the page
    else:
        # A4 page size
        # (width = 793.75, height = 1122.5)
        xoffset = 0.5*3700*0.06 + (793.75-3*3700*0.06-2*300*0.06)/2  # Center the grid of lock_holder horizontally on the page
        xcenter = 793.75*0.5
        yoffset = 3200*0.06 + (1122.5-3*4600*0.06-2*400*0.06)/2  # Center the grid of lock_holder vertically on the page

    result.append(ruler_guide(x=20, y=60, scale=1.0, indent=indent+1))

    if page_title:
        result.append(" "*4*indent + '''    <text id="page_title" x="{xcenter}" y="30" text-anchor="middle" font-size="16">{page_title}</text>'''.format(xcenter=xcenter,page_title=page_title))

    if   (kind == "lock_diagrams"):
        for (n, (lock_configuration, has_key, description)) in enumerate(configs):
            x = ((n %  3) * (3700+300)*0.06 + xoffset)
            y = ((n // 3) * (4600+400)*0.06 + yoffset)
            result.append(lock_holder(lock_configuration=lock_configuration, has_key=has_key, descr=description, alignment=alignment, outline=True, scale=0.06, x=x, y=y, indent=indent+1))

    else:  # kind == "cut"
        for n in range(9):
            x = ((n %  3) * (3700+300)*0.06 + xoffset)
            y = ((n // 3) * (4600+400)*0.06 + yoffset)
            result.append(lock_holder_outline(kind="plain", scale=0.06, x=x, y=y, color="red", indent=indent+1))

    result.append(" "*4*indent + template_end.format(kind=kind,pagesize=pagesize))
    return "\n".join(result)


############################################################
def plastic_cut_sheet(pagesize="12x12", kind="plastic_cut_sheet_a", page_title=None, indent=0):
    template_start = '''<g id="plastic_cut_sheet_{kind}_{pagesize}">'''
    template_end = '''</g>  <!-- id="plastic_cut_sheet_{kind}_{pagesize}" -->'''

    result = []
    for line in template_start.format(pagesize=pagesize, kind=kind).splitlines():
        if line == '':
            result.append("")
        else:
            result.append(" "*4*indent + line)

    #result.append(alignment_mark(kind="empty", x=   0, y=   0, scale=0.2, indent=indent+1))
    #result.append(alignment_mark(kind="empty", x=1152, y=   0, scale=0.2, indent=indent+1))
    #result.append(alignment_mark(kind="empty", x=   0, y=1152, scale=0.2, indent=indent+1))
    #result.append(alignment_mark(kind="empty", x=1152, y=1152, scale=0.2, indent=indent+1))
    xoffset = 130
    xcenter = 1152 * 0.5
    yoffset = 210

    result.append(ruler_guide(x=50, y=25, scale=1.0, rotate=90, indent=indent+1))

    if page_title:
        result.append(" "*4*indent + '''    <text id="page_title" x="{xcenter}" y="30" text-anchor="middle" font-size="16">{page_title}</text>'''.format(xcenter=xcenter,page_title=page_title))

    if kind == "plastic_cut_sheet_a":
        for ny in range (4):
            for nx in range(5):
                x = nx * 3700*0.06 + xoffset
                y = ny * 4600*0.06 + yoffset
                if ny % 2 == 1:
                    result.append(lock_holder_outline(kind="notch+lever", scale=0.06, x=x, y=y, color="red", indent=indent+1))
                else:
                    result.append(lock_holder_outline(kind="notch+recess", scale=0.06, x=x, y=y, color="red", indent=indent+1))
    else:
        for ny in range (4):
            for nx in range(5):
                x = nx * 3700*0.06 + xoffset
                y = ny * 4600*0.06 + yoffset
                result.append(lock_holder_outline(kind="plain", scale=0.06, x=x, y=y, color="red", indent=indent+1))


    result.append(" "*4*indent + template_end.format(pagesize=pagesize,kind=kind))
    return "\n".join(result)


############################################################
import csv
import sys

supported_diagrams = ["plastic_cut_sheet_a", "plastic_cut_sheet_b", "paper_cut_sheet", "lock_diagrams", "logo_sheets"]

input_filename = "example_locks.csv"
print("Reading configuration information from {}".format(input_filename))
with open("example_locks.csv") as file:
    reader = csv.reader(file)
    csv_lines = [(n+1,row) for (n,row) in enumerate(reader)]

pages = dict()
#sys.exit()
for line in csv_lines:
    (line_number, (diagram_type, output_filename, page_size, name, lock_configuration, show_key)) = line
    if diagram_type not in supported_diagrams:
        continue

    if ((diagram_type == "plastic_cut_sheet_a") or (diagram_type == "plastic_cut_sheet_b")) and \
       (page_size != "12x12"):
        print("Error: {}, line {} - {} output files only support \"12x12\" page size".format(input_filename, line_number, diagram_type))
        sys.exit(0)

    if output_filename in pages:
        if pages[output_filename][0]["page_size"] != page_size:
            print("Error: {}, line {} - all content in an output files must use the same page size".format(input_filename, line_number))
            print("    \"{}\" and \"{}\".".format(pages[output_filename][0]["page_size"], page_size))
            sys.exit(0)

        if (pages[output_filename][0]["diagram_type"] == "lock_diagrams") and (len(pages[output_filename]) > 8):
            print("Error: {}, line {} - lock_diagram output files cannot have more than 9 lock diagrams per output page".format(input_filename, line_number))
            sys.exit(0)

        if (diagram_type == "plastic_cut_sheet_a") or \
           (diagram_type == "plastic_cut_sheet_b") or \
           (diagram_type == "paper_cut_sheet"):
            print("Error: {}, line {} - {} output files cannot have more than one diagram per output page".format(input_filename, line_number, diagram_type))
            sys.exit(0)

        pages[output_filename].append({"diagram_type": diagram_type, "page_size": page_size, "name": name, "lock_configuration":lock_configuration, "show_key": show_key })
    else:
        pages[output_filename] = [{"diagram_type": diagram_type, "page_size": page_size, "name": name, "lock_configuration":lock_configuration, "show_key": show_key }]


for output_filename in pages:
    page = pages[output_filename]
    pagesize = page[0]["page_size"]
    diagram_type = page[0]["diagram_type"]
    print("Writing {} to file {}".format(diagram_type, output_filename))

    if  diagram_type  == "plastic_cut_sheet_a":
        with open(output_filename, "w") as SVG_file:
            SVG_file.write(SVG_root(kind="start", pagesize=pagesize))
            SVG_file.write(plastic_cut_sheet(pagesize="12x12", kind=diagram_type, page_title=output_filename, indent=1))
            SVG_file.write(SVG_root(kind="end"))

    elif diagram_type == "plastic_cut_sheet_b":
        with open(output_filename, "w") as SVG_file:
            SVG_file.write(SVG_root(kind="start", pagesize=pagesize))
            SVG_file.write(plastic_cut_sheet(pagesize="12x12", kind=diagram_type, page_title=output_filename, indent=1))
            SVG_file.write(SVG_root(kind="end"))

    elif diagram_type == "paper_cut_sheet":
        with open(output_filename, "w") as SVG_file:
            SVG_file.write(SVG_root(kind="start", pagesize=pagesize))
            SVG_file.write(paper_sheet([], kind="cut", page_title=output_filename, alignment=True, pagesize=pagesize, indent=1))
            SVG_file.write(SVG_root(kind="end"))

    elif diagram_type == "lock_diagrams":
        configs = []
        for config in page:
            configs.append( (config["lock_configuration"], config["show_key"] == "yes", config["name"]) )
        with open(output_filename, "w") as SVG_file:
            SVG_file.write(SVG_root(kind="start", pagesize=pagesize))
            SVG_file.write(paper_sheet(configs, kind=diagram_type, page_title=output_filename, alignment=True, pagesize=pagesize, indent=1))
            SVG_file.write(SVG_root(kind="end"))

    elif page["diagram_type"] == "logo_sheets":
        print("Error: {}, line {} - logo_sheets not implemented".format(input_filename, line_number))
        sys.exit(0)
