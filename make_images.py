"""Generates demo SVG placeholders. Replace any file in assets/img with a real image (same base name; update extension in HTML if needed)."""
import os, random
OUT='/home/claude/site/assets/img'
PAL={
 'brand':('#0A0C1C','#2563EB','#7C3AED','#EF4444'),
 'sky':('#06142B','#38BDF8','#2563EB','#7C3AED'),
 'warm':('#1A0C06','#7A3418','#F97316','#EF4444'),
 'violet':('#0A0E1F','#3B1578','#7C3AED','#38BDF8'),
 'mint':('#061A1C','#0E7490','#38BDF8','#2563EB'),
 'clinic':('#0B1B33','#2563EB','#38BDF8','#A7F3D0'),
}
def svg(name,w,h,pal,label,seed=1):
    r=random.Random(seed); bg,c1,c2,c3=PAL[pal]
    nodes=[(r.randint(int(w*.08),int(w*.92)),r.randint(int(h*.1),int(h*.9)),r.randint(4,int(min(w,h)*.035)+6)) for _ in range(14)]
    edges=''.join(f'<line x1="{nodes[i][0]}" y1="{nodes[i][1]}" x2="{nodes[(i*3+1)%14][0]}" y2="{nodes[(i*3+1)%14][1]}"/>' for i in range(14))
    dots=''.join(f'<circle cx="{x}" cy="{y}" r="{s}" fill="{[c1,c2,c3][i%3]}" opacity=".9"/>' for i,(x,y,s) in enumerate(nodes))
    fs=max(14,int(min(w,h)*.035))
    s=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{bg}"/><stop offset=".55" stop-color="{c1}" stop-opacity=".55"/><stop offset="1" stop-color="{c2}" stop-opacity=".7"/></linearGradient>
<radialGradient id="a" cx=".25" cy=".2" r=".6"><stop offset="0" stop-color="{c3}" stop-opacity=".55"/><stop offset="1" stop-color="{c3}" stop-opacity="0"/></radialGradient>
<radialGradient id="b" cx=".85" cy=".9" r=".55"><stop offset="0" stop-color="{c2}" stop-opacity=".6"/><stop offset="1" stop-color="{c2}" stop-opacity="0"/></radialGradient>
<filter id="f"><feGaussianBlur stdDeviation="{int(min(w,h)*.004)+1}"/></filter></defs>
<rect width="{w}" height="{h}" fill="{bg}"/><rect width="{w}" height="{h}" fill="url(#g)"/><rect width="{w}" height="{h}" fill="url(#a)"/><rect width="{w}" height="{h}" fill="url(#b)"/>
<g stroke="#fff" stroke-opacity=".22" stroke-width="{max(1,int(min(w,h)*.0025))}">{edges}</g><g filter="url(#f)">{dots}</g>
<rect x="{w-fs*11.5}" y="{h-fs*3}" width="{fs*10.5}" height="{fs*2}" rx="{fs}" fill="#0A0C1C" fill-opacity=".55" stroke="#fff" stroke-opacity=".25"/>
<text x="{w-fs*6.25}" y="{h-fs*1.65}" text-anchor="middle" font-family="Inter,Arial,sans-serif" font-size="{int(fs*.8)}" font-weight="600" fill="#fff" fill-opacity=".85">DEMO · {label}</text></svg>'''
    open(f'{OUT}/{name}.svg','w').write(s)

L=[ # name,w,h,palette,label
 ('hero-poster',1920,1080,'brand','1920×1080 hero'),
 ('page-bg',1920,900,'violet','1920×900 page banner'),
 ('cta-bg',1920,900,'sky','1920×900 CTA'),
 ('feat-web',1200,900,'sky','1200×900'),('feat-ai',1200,900,'violet','1200×900'),
 ('feat-motion',1200,900,'brand','1200×900'),('feat-stack',1200,900,'mint','1200×900'),
 ('gal-1',1000,1250,'warm','1000×1250'),('gal-2',1000,1250,'clinic','1000×1250'),
 ('gal-3',1000,1250,'violet','1000×1250'),('gal-4',1000,1250,'sky','1000×1250'),('gal-5',1000,1250,'brand','1000×1250'),
 ('work-bridge',1600,1000,'warm','1600×1000'),('work-westend',1600,1000,'clinic','1600×1000'),
 ('work-ff',1600,1000,'brand','1600×1000'),('work-aperture',1600,1000,'sky','1600×1000'),('work-meridian',1600,1000,'violet','1600×1000'),
 ('about-studio',1600,1000,'brand','1600×1000 studio'),
 ('team-1',600,600,'sky','600×600'),('team-2',600,600,'violet','600×600'),('team-3',600,600,'warm','600×600'),
 ('avatar-1',200,200,'sky','avatar'),('avatar-2',200,200,'warm','avatar'),('avatar-3',200,200,'violet','avatar'),
 ('post-1',1200,750,'mint','1200×750'),('post-2',1200,750,'warm','1200×750'),('post-3',1200,750,'violet','1200×750'),
 ('post-4',1200,750,'sky','1200×750'),('post-5',1200,750,'brand','1200×750'),('post-6',1200,750,'clinic','1200×750'),
 ('detail-1',1200,800,'sky','1200×800'),('detail-2',1200,800,'violet','1200×800'),
]
for i,(n,w,h,p,l) in enumerate(L): svg(n,w,h,p,l,seed=i+3)
print(len(L),'placeholders written')
