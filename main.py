from PIL import Image, ImageDraw, ImageFont
import os

W = H = 1024
PAPER = (246, 242, 231)
INK = (20, 35, 48)
BLUE = (31, 76, 103)
RED = (190, 58, 43)
GOLD = (214, 164, 70)
MUTED = (92, 99, 96)
im = Image.new('RGB', (W, H), PAPER)
d = ImageDraw.Draw(im)
ROOT = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(ROOT, 'assets', 'fonts')

def font(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)

display = 'Anton-Regular.ttf'
sans = 'DejaVuSans.ttf'
bold = 'DejaVuSans-Bold.ttf'

def txt(x, y, s, size, color=INK, face=sans, anchor=None):
    d.text((x,y), s, font=font(face,size), fill=color, anchor=anchor)

def line(points, fill=INK, width=4):
    d.line(points, fill=fill, width=width, joint='curve')

# Newspaper masthead
d.rectangle((0,0,W,14), fill=RED)
txt(40, 27, 'THE WORLD IN ONE DAY', 55, INK, display)
txt(43, 93, 'THURSDAY 19 NOVEMBER 2026', 23, RED, bold)
txt(980, 46, 'GLOBAL\nBRIEFING', 15, MUTED, bold, anchor='ra')
line([(40,132),(984,132)], INK, 3)
txt(42,142,'SIX STORIES. ONE DAY.',14,MUTED,bold)
txt(982,142,'WORLD  /  JUSTICE  /  CONFLICT  /  BUSINESS',12,MUTED,bold,anchor='ra')

# Icon helpers, drawn in a restrained editorial line-art style.
def globe_flags(cx,cy):
    # Three leaders represented by flag standards encircling a summit table.
    d.ellipse((cx-61,cy-48,cx+61,cy+48), outline=BLUE, width=4)
    line([(cx-42,cy),(cx+42,cy)],BLUE,3); line([(cx,cy-46),(cx,cy+46)],BLUE,3)
    d.arc((cx-33,cy-48,cx+33,cy+48),80,280,fill=BLUE,width=3)
    for x, col in [(cx-88,RED),(cx,BLUE),(cx+88,GOLD)]:
        line([(x,cy-55),(x,cy+47)],INK,3)
        d.polygon([(x,cy-54),(x+35,cy-45),(x,cy-34)], fill=col)
    d.ellipse((cx-12,cy-12,cx+12,cy+12),fill=GOLD)

def justice(cx,cy):
    line([(cx,cy-57),(cx,cy+43)],INK,6); line([(cx-46,cy-34),(cx+46,cy-34)],INK,5)
    line([(cx-42,cy-34),(cx-58,cy+7)],BLUE,3); line([(cx-42,cy-34),(cx-25,cy+7)],BLUE,3)
    line([(cx+42,cy-34),(cx+25,cy+7)],BLUE,3); line([(cx+42,cy-34),(cx+58,cy+7)],BLUE,3)
    d.arc((cx-66,cy-3,cx-17,cy+28),0,180,fill=RED,width=4)
    d.arc((cx+17,cy-3,cx+66,cy+28),0,180,fill=RED,width=4)
    line([(cx-34,cy+47),(cx+34,cy+47)],INK,6); line([(cx-25,cy+54),(cx+25,cy+54)],INK,3)

def gaza(cx,cy):
    # Tank, ground line, and advance arrow.
    line([(cx-80,cy+39),(cx+78,cy+39)],INK,4)
    d.rectangle((cx-50,cy+2,cx+35,cy+31), fill=BLUE)
    d.polygon([(cx-39,cy+2),(cx-20,cy-23),(cx+18,cy-23),(cx+35,cy+2)],fill=BLUE)
    d.ellipse((cx-40,cy+24,cx+25,cy+51),outline=INK,width=5)
    line([(cx+12,cy-13),(cx+69,cy-44)],INK,7)
    line([(cx+64,cy-44),(cx+75,cy-43),(cx+70,cy-32)],RED,5)
    for x in (cx-70,cx+55):
        d.polygon([(x,cy-42),(x+10,cy-63),(x+20,cy-42)],fill=GOLD)

def tower(cx,cy):
    # Riyadh skyline with a marked impact and incoming missile.
    d.polygon([(cx-19,cy+46),(cx-10,cy-54),(cx+10,cy-54),(cx+20,cy+46)],fill=BLUE)
    d.ellipse((cx-10,cy-49,cx+10,cy-29),outline=PAPER,width=4)
    for yy in (-16,4,24): line([(cx-12,cy+yy),(cx+12,cy+yy)],PAPER,3)
    d.rectangle((cx-72,cy+15,cx-31,cy+46),fill=(110,130,133))
    d.rectangle((cx+35,cy+2,cx+72,cy+46),fill=(110,130,133))
    line([(cx+69,cy-48),(cx+33,cy-22)],RED,5)
    d.polygon([(cx+31,cy-20),(cx+43,cy-24),(cx+36,cy-12)],fill=RED)
    for dx,dy in [(0,0),(12,-6),(-10,7)]:
        d.line([(cx+17+dx,cy-9+dy),(cx+26+dx,cy-4+dy)],fill=GOLD,width=3)

def quake(cx,cy):
    # Island, epicentre and seismic rings.
    d.ellipse((cx-21,cy-21,cx+21,cy+21),fill=RED)
    for r in (37,57,77):
        d.arc((cx-r,cy-r,cx+r,cy+r),205,335,fill=BLUE,width=4)
        d.arc((cx-r,cy-r,cx+r,cy+r),25,155,fill=BLUE,width=4)
    # Minimal Kyushu map silhouette
    d.polygon([(cx+38,cy-48),(cx+61,cy-39),(cx+67,cy-16),(cx+55,cy-3),(cx+64,cy+18),(cx+45,cy+39),(cx+26,cy+27),(cx+34,cy+8),(cx+20,cy-4),(cx+29,cy-27)],fill=GOLD)
    d.ellipse((cx+35,cy-10,cx+45,cy),fill=RED)

def chip(cx,cy):
    d.rounded_rectangle((cx-43,cy-42,cx+43,cy+42),radius=8,fill=BLUE)
    d.rectangle((cx-22,cy-21,cx+22,cy+21),outline=PAPER,width=3)
    for k in (-27,-9,9,27):
        line([(cx-56,cy+k),(cx-43,cy+k)],INK,3); line([(cx+43,cy+k),(cx+56,cy+k)],INK,3)
        line([(cx+k,cy-56),(cx+k,cy-43)],INK,3); line([(cx+k,cy+43),(cx+k,cy+56)],INK,3)
    # Rising revenue bars and arrow
    for i,h in enumerate((13,23,34)):
        d.rectangle((cx-16+i*16,cy+16-h,cx-8+i*16,cy+16),fill=GOLD)
    line([(cx-22,cy+23),(cx+20,cy-17)],RED,3)
    d.polygon([(cx+20,cy-17),(cx+11,cy-15),(cx+19,cy-8)],fill=RED)

panels = [
 ('SHENZHEN  /  SUMMIT','US–CHINA–RUSSIA SUMMIT','First-ever trilateral; leaders issue a peace declaration',globe_flags),
 ('THE HAGUE  /  ICJ','MYANMAR COMMITTED GENOCIDE','Court rules on the Rohingya case',justice),
 ('GAZA  /  CEASEFIRE','ISRAEL OPENS GROUND OFFENSIVE','Central Gaza; first since the Oct 2025 ceasefire',gaza),
 ('SAUDI ARABIA  /  ATTACK','HOUTHI MISSILES HIT RIYADH','Strikes damage the PIF tower, the capital’s tallest',tower),
 ('JAPAN  /  KUMAMOTO','KUMAMOTO QUAKE: M5.7','02:22 JST · no tsunami',quake),
 ('BUSINESS  /  AI','NVIDIA REVENUE JUMPS 103%','$115.8bn quarter; Anthropic makes its Nasdaq debut',chip),
]
left, top, pw, ph, gap = 40, 174, 300, 321, 12
for i,(kicker,head,sub,icon) in enumerate(panels):
    col,row=i%3,i//3
    x=left+col*(pw+gap); y=top+row*(ph+10)
    d.rectangle((x,y,x+pw,y+ph), fill=(250,248,241), outline=(202,196,182), width=2)
    d.rectangle((x,y,x+pw,y+5),fill=RED if i in (1,2,3) else BLUE)
    txt(x+14,y+14,kicker,12,MUTED,bold)
    icon(x+pw//2,y+104)
    # compact headline and source detail
    # Keep headlines on one line and scale to the actual card width.
    size=20
    while size > 15 and d.textbbox((0,0),head,font=font(display,size))[2] > pw-28:
        size -= 1
    txt(x+14,y+174,head,size,INK,display)
    # Word wrap the explanatory line to two lines at controlled width.
    words=sub.split(); lines_out=[]; cur=''
    for word in words:
        trial=(cur+' '+word).strip()
        if d.textbbox((0,0),trial,font=font(sans,14))[2] > pw-28:
            lines_out.append(cur); cur=word
        else: cur=trial
    if cur: lines_out.append(cur)
    for j,s in enumerate(lines_out[:3]): txt(x+14,y+211+j*20,s,14,INK,sans)
    txt(x+14,y+ph-25,f'WORLD DESK   •   {i+1:02d}',10,MUTED,bold)

# Culture strip anchors the day in popular culture.
y=846
d.rectangle((40,y,984,974),fill=INK)
d.rectangle((40,y,49,974),fill=GOLD)
txt(68,y+14,'CULTURE  /  GLOBAL RELEASE',13,GOLD,bold)
txt(68,y+39,'GRAND THEFT AUTO VI',32,PAPER,display)
txt(68,y+82,'LAUNCHES WORLDWIDE',18,PAPER,bold)
# Simple gamepad icon
cx,cy=895,y+67
d.rounded_rectangle((cx-56,cy-27,cx+56,cy+28),radius=20,outline=PAPER,width=4)
line([(cx-32,cy-1),(cx-10,cy-1)],GOLD,5); line([(cx-21,cy-12),(cx-21,cy+10)],GOLD,5)
d.ellipse((cx+19,cy-10,cx+29,cy),fill=RED); d.ellipse((cx+35,cy+1,cx+45,cy+11),fill=GOLD)
line([(40,990),(984,990)],INK,1)
txt(42,995,'A DAY ACROSS DIPLOMACY, JUSTICE, CONFLICT, SCIENCE AND CULTURE',11,MUTED,bold)
txt(982,995,'19 NOV 2026',11,RED,bold,anchor='ra')

out_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
os.makedirs(out_dir, exist_ok=True)
im.save(os.path.join(out_dir, 'entry.png'), format='PNG', optimize=True)
