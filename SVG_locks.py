#!/usr/bin/env python3

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


def alignment_mark(x=0, y=0, indent=0, kind="empty"):
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


def lock_holder(x=0, y=0, indent=0, alignment=True):
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

    result.append(template_back)
    return "\n".join(result)
