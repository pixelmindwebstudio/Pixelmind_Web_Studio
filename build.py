import os
ROOT='/home/claude/site'
LOGO='''<svg viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><defs><linearGradient id="lg{n}" x1="0" y1="0" x2="100" y2="100" gradientUnits="userSpaceOnUse"><stop offset="0%" stop-color="#38BDF8"/><stop offset="40%" stop-color="#2563EB"/><stop offset="70%" stop-color="#7C3AED"/><stop offset="100%" stop-color="#EF4444"/></linearGradient></defs><path d="M25 35 L50 20 L75 35 L75 65 L50 80 L25 65 Z" stroke="url(#lg{n})" stroke-width="6" stroke-linejoin="round"/><line x1="25" y1="35" x2="75" y2="65" stroke="url(#lg{n})" stroke-width="3" stroke-dasharray="4 4"/><line x1="75" y1="35" x2="25" y2="65" stroke="url(#lg{n})" stroke-width="3" stroke-dasharray="4 4"/><circle cx="25" cy="35" r="8" fill="#38BDF8"/><circle cx="50" cy="20" r="8" fill="#2563EB"/><circle cx="75" cy="35" r="8" fill="#7C3AED"/><circle cx="75" cy="65" r="8" fill="#EF4444"/><circle cx="50" cy="80" r="8" fill="#F97316"/><circle cx="25" cy="65" r="8" fill="#7C3AED"/></svg>'''
FAVICON="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><path d='M25 35 L50 20 L75 35 L75 65 L50 80 L25 65 Z' fill='none' stroke='%237C3AED' stroke-width='6'/><circle cx='25' cy='35' r='8' fill='%2338BDF8'/><circle cx='50' cy='20' r='8' fill='%232563EB'/><circle cx='75' cy='35' r='8' fill='%237C3AED'/><circle cx='75' cy='65' r='8' fill='%23EF4444'/><circle cx='50' cy='80' r='8' fill='%23F97316'/><circle cx='25' cy='65' r='8' fill='%237C3AED'/></svg>"
NAV=[('index.html','Home'),('services.html','Services'),('work.html','Work'),('process.html','Process'),('about.html','About'),('insights.html','Insights'),('contact.html','Contact')]

def img(name,alt='',ext='svg',lazy=True):
    return f'<img src="assets/img/{name}.{ext}" alt="{alt}" {"loading=lazy " if lazy else ""}decoding="async">'
def slot(name,ratio='16/9',alt='',cls='',ext='svg'):
    return f'<div class="slot {cls}" style="--r:{ratio}">{img(name,alt,ext)}</div>'

def head(title,desc,hero='light',extra=''):
    return f'''<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title><meta name="description" content="{desc}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website">
<meta name="theme-color" content="#0A0C1C">
<link rel="icon" type="image/svg+xml" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">{extra}
</head>
<body data-hero="{hero}">
<a class="skip" href="#main">Skip to content</a><div class="scroll-progress"></div>'''

def nav(active):
    links=''.join(f'<a href="{h}"{" class=active" if h==active else ""}>{t}</a>' for h,t in NAV)
    mob=''.join(f'<a href="{h}">{t}</a>' for h,t in NAV)
    return f'''<nav class="navbar" id="navbar" aria-label="Main"><div class="nav-inner">
<a href="index.html" class="brand" aria-label="PixelMind home">{LOGO.replace('{n}','nav')}<span class="brand-word"><span class="pixel">Pixel</span><span class="mind">Mind</span></span></a>
<div class="nav-links">{links}</div>
<div class="nav-actions"><a href="contact.html" class="btn btn-primary">Start a project</a>
<button class="nav-toggle" id="navToggle" aria-label="Toggle menu" aria-expanded="false"><span></span><span></span><span></span></button></div></div>
<div class="mobile-panel" id="mobilePanel">{mob}<a href="contact.html" class="btn btn-primary">Start a project</a></div></nav>'''

def cta(title='Let’s build something that actually works',text='Tell us about your project — a tired site that needs a rebuild, or something new from scratch. We usually reply within a day.'):
    return f'''<section class="cta-band"><div class="bg">{img('cta-bg','')}</div><div class="container">
<span class="eyebrow">Ready when you are</span><h2 class="h1 reveal">{title}</h2><p class="reveal d1">{text}</p>
<div class="reveal d2" style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap"><a class="btn btn-primary btn-lg" href="contact.html">Start a project</a><a class="btn btn-glass btn-lg" href="work.html">See our work</a></div></div></section>'''

def footer():
    return f'''<footer class="footer"><div class="container"><div class="footer-grid">
<div><a href="index.html" class="brand">{LOGO.replace('{n}','ft')}<span class="brand-word"><span class="pixel">Pixel</span><span class="mind">Mind</span></span></a>
<p class="slogan">Modernizing Websites, Elevating Brands, and Harnessing AI Innovation.</p></div>
<div><h4>Studio</h4><ul><li><a href="about.html">About</a></li><li><a href="process.html">Process</a></li><li><a href="pricing.html">Pricing</a></li><li><a href="insights.html">Insights</a></li></ul></div>
<div><h4>Services</h4><ul><li><a href="services.html#design">Web Design &amp; Renovation</a></li><li><a href="services.html#ai">AI-Generated Visuals</a></li><li><a href="services.html#motion">Motion &amp; Animation</a></li><li><a href="services.html#stack">GitHub &amp; Modern Stack</a></li></ul></div>
<div><h4>Contact</h4><ul><li><a href="tel:+27761501439">+27 76 150 1439</a></li><li><a href="mailto:pixelmind.webstudio@gmail.com">pixelmind.webstudio@gmail.com</a></li><li><a href="work.html">Selected work</a></li><li><a href="contact.html">Start a project</a></li></ul></div></div>
<div class="footer-bottom"><span>© <span id="year"></span> PixelMind Web Design Studio. All rights reserved.</span><span>South Africa (+27)</span></div></div></footer>
<script src="assets/js/main.js"></script></body></html>'''

def page_hero(crumb,title,lead,eyebrow=''):
    return f'''<header class="page-hero"><div class="bg">{img('page-bg','',lazy=False)}</div><div class="container">
<div class="crumbs"><a href="index.html">Home</a> / {crumb}</div>{f'<span class="eyebrow">{eyebrow}</span><br>' if eyebrow else ''}
<h1 class="h1" style="max-width:900px">{title}</h1><p class="lead">{lead}</p></div></header>'''

def write(fn,html):
    open(f'{ROOT}/{fn}','w').write(html); print('wrote',fn)

ICONS={'design':'↻','ai':'✦','motion':'◐','stack':'⌘'}
SERV=[
 ('design','Advanced Web Design & Renovation','c1','feat-web','We take outdated sites — slow, cluttered, hard to update — and rebuild them from the ground up: modern layout, faster load times, and a structure that is easy to maintain.',['Full redesign without starting from zero','Mobile-first, accessible layouts','Clean, documented code you can hand off']),
 ('ai','AI-Generated Visuals','c2','feat-ai','Custom imagery and tech media generated for your brand, not stock photography. Every visual is art-directed to match your palette, tone and audience.',['Hero imagery and campaign visuals','Short looping video for backgrounds','Consistent style across every page']),
 ('motion','Motion & Animation','c3','feat-motion','Smooth, purposeful interactions inspired by modern motion design — never decoration for its own sake. Motion guides attention and explains how things work.',['Scroll-driven storytelling','Micro-interactions and hover states','Respects reduced-motion preferences']),
 ('stack','GitHub & Modern Stack Integration','c4','feat-stack','Version-controlled, deployable builds using a current front-end toolchain — so your site is easy to hand off, extend, or scale later.',['Git-based workflow and clean commits','Fast static hosting and deploys','Easy to extend with new pages and features']),
]

# ================= HOME =================
def home():
    tabs=''.join(f'<button class="tab-btn" role="tab" aria-selected="false">{t}</button>' for _,t,_,_,_,_ in SERV)
    panels=''.join(f'''<div class="tab-panel" role="tabpanel"><div><span class="eyebrow">0{i+1}</span><h3>{t}</h3><p>{d}</p><ul class="checks">{''.join(f"<li>{c}</li>" for c in cl)}</ul><a class="link-arrow" href="services.html#{k}">Explore this service →</a></div>{slot(im,'4/3',t,'zoom')}</div>''' for i,(k,t,_,im,d,cl) in enumerate(SERV))
    gal=[('gal-1','Restaurant','Bridge Street Bistro','Warm, moody visuals for a bistro and live-music venue.','bridge-street'),
         ('gal-2','Healthcare','West End Clinic','A calm, trustworthy site for a community clinic.','west-end-clinic'),
         ('gal-3','Venture Capital','Founders Factory Africa','Motion-led storytelling for an investor brand.','founders-factory'),
         ('gal-4','SaaS Concept','Aperture Analytics','Dark glass dashboards with animated metrics.','aperture'),
         ('gal-5','Tech Concept','Meridian Portal','Node-based visuals that explain complex systems.','meridian')]
    cards=''.join(f'<a class="rail-card" href="case-study.html?p={p}"><div class="bgimg">{img(i,n)}</div><span class="tag">{t}</span><h3>{n}</h3><p>{d}</p><span class="link-arrow" style="color:#fff">View case study →</span></a>' for i,t,n,d,p in gal)
    steps=[('Renovate','Audit the old site, keep what works, and rebuild a faster, cleaner foundation.'),('Generate','Create custom AI visuals and short loops that fit your brand — not stock.'),('Animate','Add scroll-driven motion and micro-interactions that guide attention.'),('Ship','Deploy through a modern Git workflow, ready to hand off or scale.')]
    st=''.join(f'<div class="step"><div class="step-num accent">0{i+1}</div><h3>{t}</h3><p>{d}</p></div>' for i,(t,d) in enumerate(steps))
    marq=['HTML5','CSS3','JavaScript ES6+','GitHub','Responsive Design','Glassmorphism','AI Visuals','Motion Design','Typography Systems','Accessibility']
    mq=''.join(f'<span><i>◆</i>{m}</span>' for m in marq*2)
    tm=[('“PixelMind took a site we were embarrassed by and turned it into something we are proud to share.”','Client Name','Business Owner · Company','avatar-1'),
        ('“Fast, clear and genuinely creative. The visuals felt made for us, not pulled from a stock library.”','Client Name','Marketing Lead · Company','avatar-2'),
        ('“The motion makes the site feel alive without getting in the way. Our visitors notice.”','Client Name','Founder · Company','avatar-3')]
    ts=''.join(f'<div class="testi-slide"><blockquote>{q}</blockquote><cite>{slot(a,"1/1")}<span><b>{n}</b>{r}</span></cite></div>' for q,n,r,a in tm)
    posts=[('post-1','Renovation','Why rebuilding beats patching an outdated site'),('post-2','AI Visuals','Generated imagery that actually fits your brand'),('post-3','Motion','Scroll animation: when it helps and when it hurts')]
    ps=''.join(f'<a class="post reveal d{i+1}" href="insights.html">{slot(im,"16/10",t,"zoom")}<span class="meta">{c}</span><h3>{t}</h3><span class="link-arrow">Read more →</span></a>' for i,(im,c,t) in enumerate(posts))
    return head('PixelMind — Your Ideas in Motion','PixelMind is a web design studio modernizing outdated websites into fast, elegant, AI-enhanced digital experiences.','dark')+nav('index.html')+f'''
<main id="main">
<header class="hero"><div class="hero-media">{img('hero-poster','',lazy=False)}
<video data-autoplay autoplay muted loop playsinline poster="assets/img/hero-poster.svg" aria-hidden="true"><source src="assets/video/hero.mp4" type="video/mp4"></video></div>
<div class="container"><div class="hero-grid"><div>
<span class="eyebrow">Web Design Studio · South Africa</span>
<h1 class="display">Your ideas<br><span class="accent">in motion.</span></h1>
<p class="lead">PixelMind rebuilds outdated sites into fast, modern experiences — engineered with clean code, thoughtful motion, and AI-enhanced visuals that actually fit your brand.</p>
<div class="hero-ctas"><a class="btn btn-primary btn-lg" href="work.html">View our work</a><a class="btn btn-glass btn-lg" href="contact.html">Start a project</a></div></div>
<div class="hero-side"><div class="glass-card"><i>✦</i><span>AI visuals, generated<small>Made for your brand</small></span></div><div class="glass-card"><i>⚡</i><span>Fast, modern build<small>Clean, maintainable code</small></span></div><div class="glass-card"><i>▭</i><span>Responsive everywhere<small>Mobile-first by default</small></span></div></div></div></div>
<div class="scroll-cue" aria-hidden="true"></div></header>

<div class="marquee" aria-label="Our toolkit"><div class="marquee-track">{mq}</div></div>

<section class="theme-light"><div class="container">
<div class="section-head"><span class="eyebrow">What we do</span><h2 class="h1 reveal">Four capabilities.<br><span class="accent">One goal.</span></h2><p class="reveal d1">A site that looks and feels like where your brand is headed.</p></div>
<div data-tabs><div class="tabs-nav" role="tablist">{tabs}</div>{panels}</div></div></section>

<section class="theme-dark"><div class="container"><div class="story">
<div class="story-sticky"><span class="eyebrow">How it comes together</span><h2 class="h1">Renovate. Generate. Animate. <span class="accent">Ship.</span></h2><p class="lead">A simple, repeatable flow that turns a tired website into a launch-ready experience.</p><div class="mt-m"><a class="btn btn-primary" href="process.html">See the full process</a></div></div>
<div class="story-steps">{st}</div></div></div></section>

<section class="theme-soft" style="overflow:hidden" data-rail><div class="container"><div class="section-head" style="margin-bottom:36px"><span class="eyebrow">Selected work</span><h2 class="h1 reveal">Built for brands <span class="accent">going places.</span></h2></div></div>
<div class="rail" tabindex="0" aria-label="Featured projects">{cards}</div>
<div class="container"><div class="rail-controls"><div class="dots"></div><div class="arrows"><button class="arrow prev" aria-label="Previous">←</button><button class="arrow next" aria-label="Next">→</button></div></div></div></section>

<section class="theme-light"><div class="container"><div class="section-head center"><span class="eyebrow">By the numbers</span><h2 class="h2 reveal">Designed to be dependable</h2></div>
<div class="stats reveal"><div class="stat"><b class="accent" data-count="4">0</b><span>Core services</span></div><div class="stat"><b class="accent" data-count="100" data-suffix="%">0</b><span>Responsive builds</span></div><div class="stat"><b class="accent" data-count="24" data-suffix="h">0</b><span>Typical reply time</span></div><div class="stat"><b class="accent" data-count="3">0</b><span>Brand commitments</span></div></div></div></section>

<section class="theme-dark"><div class="container"><div class="section-head center"><span class="eyebrow">Our commitments</span><h2 class="h1 reveal">A trusted partner for <span class="accent">digital excellence</span></h2><p class="lead reveal d1">Building innovative web solutions with a fresh perspective.</p></div>
<div class="grid-3"><div class="commit reveal"><div class="icon-badge">🛡</div><h3>Security-first design</h3><p>Safe defaults, clean dependencies and careful handling of forms and data.</p></div><div class="commit reveal d1"><div class="icon-badge c2">◎</div><h3>Unwavering reliability</h3><p>Fast, stable builds tested across devices so your site is there when customers are.</p></div><div class="commit reveal d2"><div class="icon-badge c3">✦</div><h3>Future-proof innovation</h3><p>A modern stack and AI-enhanced workflow that keeps your brand ahead.</p></div></div></div></section>

<section class="theme-light"><div class="container"><div class="section-head center"><span class="eyebrow">Kind words</span></div><div class="testi" data-testi>{ts}<div class="dots"></div></div></div></section>

<section class="theme-soft"><div class="container"><div class="section-head" style="display:flex;justify-content:space-between;align-items:end;max-width:none;gap:24px;flex-wrap:wrap"><div><span class="eyebrow">Insights</span><h2 class="h1 reveal">Ideas worth <span class="accent">sharing</span></h2></div><a class="link-arrow" href="insights.html">All articles →</a></div><div class="grid-3">{ps}</div></div></section>
{cta()}
</main>'''+footer()

# ================= SERVICES =================
def services():
    blocks=''
    for i,(k,t,c,im,d,cl) in enumerate(SERV):
        flip=' style="direction:rtl"' if i%2 else ''
        inner=' style="direction:ltr"' if i%2 else ''
        th='theme-light' if i%2==0 else 'theme-soft'
        blocks+=f'''<section id="{k}" class="{th}"><div class="container"><div class="split"{flip}><div{inner}><div class="icon-badge {c if c!='c1' else ''}">{ICONS[k]}</div><span class="eyebrow">0{i+1}</span><h2 class="h1 reveal">{t}</h2><p class="lead reveal d1 mt-s">{d}</p><ul class="checks mt-m">{''.join(f"<li>{x}</li>" for x in cl)}</ul><a class="btn btn-primary" href="contact.html">Ask about this</a></div><div{inner} class="reveal d2">{slot(im,'4/3',t,'zoom')}</div></div></div></section>'''
    extras=[('Discovery call','Free first conversation to understand your goals.'),('Content & assets','We help you gather, generate and organise what the site needs.'),('Launch support','Deployment, testing and handover so you are never left guessing.'),('Ongoing care','Optional updates, new pages and improvements as you grow.')]
    ex=''.join(f'<div class="card reveal d{i%4+1}"><div class="icon-badge c{(i%4)+1 if i else 1}">{["☎","▣","⚑","♻"][i]}</div><h3 class="h3">{t}</h3><p>{d}</p></div>' for i,(t,d) in enumerate(extras))
    return head('Services — PixelMind','Advanced web design and renovation, AI-generated visuals, motion and animation, and modern stack integration.','dark')+nav('services.html')+page_hero('Services','Everything your brand needs to <span class="accent">move forward</span>','Four capabilities that work together — from rebuilding an outdated site to shipping a polished, animated, AI-enhanced experience.','What we do')+'<main id="main">'+blocks+f'''
<section class="theme-dark"><div class="container"><div class="section-head center"><span class="eyebrow">Around every project</span><h2 class="h1 reveal">Support that <span class="accent">goes further</span></h2></div><div class="grid-4">{ex}</div></div></section>
{cta()}</main>'''+footer()

# ================= WORK =================
PROJ=[('bridge-street','work-bridge','Bridge Street Bistro & Smokehouse','Restaurant, bar and live-music venue site for Gqeberha — warm, moody visuals with a menu and events flow built for mobile.','restaurant live','In Progress',['Restaurant','Live Music','Gqeberha, SA']),
 ('west-end-clinic','work-westend','West End Clinic','A calm, trustworthy marketing site for a community health clinic in Gqeberha.','health','In Progress',['Healthcare','Gqeberha, SA']),
 ('founders-factory','work-ff','Founders Factory Africa','Enhancing an investor-grade site with new features, motion and generated visuals.','venture','In Progress',['Venture Capital','Motion']),
 ('aperture','work-aperture','Aperture Analytics','A dashboard-first landing page concept — dark UI, glassmorphic cards, animated metrics.','concept saas','Concept',['SaaS','Dashboard']),
 ('meridian','work-meridian','Meridian Tech Portal','An internal-tools portal concept blending a dark interface with node-based visuals.','concept saas','Concept',['Tech Portal','Dark UI'])]
def work():
    cards=''.join(f'<a class="project reveal d{i%3+1}" data-cat="{c}" href="case-study.html?p={k}"><div class="slot zoom" style="--r:16/10">{img(im,n)}<span style="position:absolute;top:14px;left:14px;z-index:3;font-size:.7rem;font-weight:700;padding:6px 12px;border-radius:999px;color:#fff;background:rgba(10,12,28,.55);backdrop-filter:blur(8px)">{st}</span></div><div class="project-body"><h3 class="h3">{n}</h3><p>{d}</p><div class="tags">{"".join(f"<span>{t}</span>" for t in tg)}</div></div></a>' for i,(k,im,n,d,c,st,tg) in enumerate(PROJ))
    chips=''.join(f'<button class="chip{" on" if f=="all" else ""}" data-f="{f}">{l}</button>' for f,l in [('all','All'),('restaurant','Hospitality'),('health','Healthcare'),('venture','Finance'),('saas','SaaS & Tech'),('concept','Concepts')])
    return head('Work — PixelMind','Selected PixelMind projects: live client builds and concept explorations.','dark')+nav('work.html')+page_hero('Work','Selected work, <span class="accent">built to perform</span>','Live client builds alongside concept explorations that show the range we design across.','Portfolio')+f'''<main id="main"><section class="theme-light"><div class="container"><div class="filters" data-filter-group>{chips}</div><div class="grid-3">{cards}</div></div></section>{cta('Your project could be next')}</main>'''+footer()

def case():
    return head('Case study — PixelMind','PixelMind case study.','dark')+nav('work.html')+f'''<header class="page-hero"><div class="bg">{img('page-bg','',lazy=False)}</div><div class="container"><div class="crumbs"><a href="index.html">Home</a> / <a href="work.html">Work</a> / Case study</div><span class="eyebrow" id="csTag">Project</span><br><h1 class="h1" id="csTitle" style="max-width:900px">Project</h1><p class="lead" id="csLead"></p></div></header>
<main id="main"><section class="theme-light" id="caseStudy"><div class="container">
<div class="slot reveal" style="--r:21/9"><img data-cs-img src="assets/img/work-bridge.svg" alt=""></div>
<div class="cs-meta"><div><small>Client</small><b id="csClient"></b></div><div><small>Role</small><b id="csRole"></b></div><div><small>Year</small><b id="csYear"></b></div><div><small>Status</small><b id="csStatus"></b></div></div>
<div class="split"><div><span class="eyebrow">The approach</span><h2 class="h2">Designed around what visitors actually need</h2></div><div class="prose"><p id="csA"></p><p id="csB"></p></div></div>
<div class="cs-gallery mt-l"><div class="wide slot reveal" style="--r:21/9">{img('detail-1','')}</div><div class="slot reveal" style="--r:4/3">{img('detail-2','')}</div><div class="slot reveal d1" style="--r:4/3">{img('feat-web','')}</div></div>
<div class="center mt-l"><span class="eyebrow">Next project</span><br><a id="csNext" href="#" class="h1 accent" style="display:inline-block"><span id="csNextName"></span> →</a></div></div></section>{cta('Want results like this?')}</main>'''+footer()

# ================= PROCESS =================
def process():
    items=[('Discovery','We learn your goals, audience and what is not working on the current site.',['Goals & audience','Site audit']),('Strategy & structure','We plan pages, content and the visual direction before any code is written.',['Sitemap','Style direction']),('Visuals & content','We generate and art-direct custom imagery and short loops that match your brand.',['AI visuals','Copy & assets']),('Design & build','Mobile-first layouts built with clean HTML, CSS and JavaScript, with motion layered in.',['Responsive build','Motion & interaction']),('Review & refine','You review a live preview; we refine until it feels right.',['Feedback rounds','Cross-device testing']),('Launch & handover','Version-controlled deploy, handover and optional ongoing support.',['Git workflow','Launch checklist'])]
    tl=''.join(f'<div class="tl-item reveal" data-n="{i+1}"><h3 class="h3">{t}</h3><p>{d}</p><div class="tags">{"".join(f"<span>{x}</span>" for x in tg)}</div></div>' for i,(t,d,tg) in enumerate(items))
    return head('Process — PixelMind','How PixelMind takes a website from first conversation to launch.','dark')+nav('process.html')+page_hero('Process','A clear path from <span class="accent">idea to launch</span>','No surprises. Six steps, with you involved at every stage.','How we work')+f'''<main id="main"><section class="theme-light"><div class="container" style="max-width:900px"><div class="timeline">{tl}</div></div></section>
<section class="theme-dark"><div class="container"><div class="split"><div><span class="eyebrow">Why this works</span><h2 class="h1">Renovation-first, <span class="accent">not from zero</span></h2><p class="lead mt-s">We keep what works on your existing site and rebuild what does not — which saves time and protects what your customers already know.</p></div>{slot('detail-1','16/10','','zoom')}</div></div></section>{cta()}</main>'''+footer()

# ================= ABOUT =================
def about():
    team=[('team-1','Team Member','Founder & Lead Designer'),('team-2','Team Member','Front-end Developer'),('team-3','Team Member','Motion & Visuals')]
    tm=''.join(f'<div class="team reveal d{i+1}">{slot(im,"1/1")}<h3>{n}</h3><span>{r}</span></div>' for i,(im,n,r) in enumerate(team))
    vals=[('Security-first','Safe defaults and careful handling of user data.'),('Reliable','Stable, tested builds that load fast on every device.'),('Innovative','AI-enhanced workflows and modern motion design.'),('Honest','Plain-language advice and clear communication.')]
    vs=''.join(f'<div class="card reveal d{i+1}"><div class="icon-badge c{i+1}">{["🛡","◎","✦","✓"][i]}</div><h3 class="h3">{t}</h3><p>{d}</p></div>' for i,(t,d) in enumerate(vals))
    return head('About — PixelMind','Meet PixelMind, a South African web design studio modernizing websites with AI-enhanced visuals and motion.','dark')+nav('about.html')+page_hero('About','A fresh perspective on <span class="accent">digital excellence</span>','PixelMind is a web design studio in South Africa that modernizes outdated websites into fast, elegant, AI-enhanced experiences.','Our story')+f'''<main id="main">
<section class="theme-light"><div class="container"><div class="split"><div class="reveal">{slot('about-studio','16/10','','zoom')}</div><div><span class="eyebrow">Who we are</span><h2 class="h1">Websites built for where your business is <span class="accent">going next</span></h2><div class="prose mt-m"><p>We believe a website should be a fast, clear reflection of your brand — not a project you are embarrassed by.</p><p>Our renovation-first approach keeps what works, replaces what does not, and adds custom AI visuals and thoughtful motion on a modern, maintainable foundation.</p></div><a class="btn btn-primary" href="contact.html">Work with us</a></div></div></div></section>
<section class="theme-dark"><div class="container"><div class="stats reveal"><div class="stat"><b class="accent" data-count="4">0</b><span>Core services</span></div><div class="stat"><b class="accent" data-count="5">0</b><span>Projects in the showcase</span></div><div class="stat"><b class="accent" data-count="100" data-suffix="%">0</b><span>Mobile-first</span></div><div class="stat"><b class="accent" data-count="1">0</b><span>Goal: your growth</span></div></div></div></section>
<section class="theme-soft"><div class="container"><div class="section-head center"><span class="eyebrow">What we stand for</span><h2 class="h1 reveal">Our values</h2></div><div class="grid-4">{vs}</div></div></section>
<section class="theme-light"><div class="container"><div class="section-head center"><span class="eyebrow">The team</span><h2 class="h1 reveal">People behind the pixels</h2></div><div class="grid-3">{tm}</div></div></section>{cta()}</main>'''+footer()

# ================= PRICING =================
def pricing():
    tiers=[('Refresh','Quick modernisation','A focused upgrade of an existing site.',['1–3 page refresh','Responsive clean-up','Speed improvements','Contact form'],False),
           ('Renovation','Full rebuild','Most popular for outdated sites.',['Up to 8 pages','Custom AI visuals','Scroll motion & interactions','Git workflow & handover'],True),
           ('Signature','Premium experience','Rich, motion-led brand site.',['Custom page set','Hero video loop','Advanced animation','Ongoing support option'],False)]
    cs=''.join(f'<div class="price-card reveal d{i+1}{" feat" if f else ""}">{"<span class=badge>Most popular</span>" if f else ""}<h3>{n}</h3><div class="price">Custom quote</div><div class="sub">{s} — {d}</div><ul class="checks">{"".join(f"<li>{x}</li>" for x in ch)}</ul><a class="btn {"btn-primary" if f else "btn-ghost"} btn-block" href="contact.html">Get a quote</a></div>' for i,(n,s,d,ch,f) in enumerate(tiers))
    faqs=[('How long does a project take?','Most sites take a few weeks from kickoff to launch, depending on page count and content readiness.'),('Can you work with my existing site?','Yes. Renovation is our speciality — we audit what you have and keep what works.'),('Do I own the final code?','Yes. You receive the full source in a Git repository, ready to host or hand to another developer.'),('Do you provide the images?','We generate custom AI visuals for your brand, and you can also supply your own photography.'),('What do I need to get started?','Just a short description of your project. Use the contact form and we will reply within about a day.')]
    fq=''.join(f'<div class="acc-item"><button class="acc-q" aria-expanded="false">{q}<span class="pm"></span></button><div class="acc-a"><p>{a}</p></div></div>' for q,a in faqs)
    return head('Pricing — PixelMind','Flexible PixelMind packages for website renovation and new builds.','dark')+nav('pricing.html')+page_hero('Pricing','Packages that fit <span class="accent">your stage</span>','Every project is scoped individually. Pick the closest starting point and we will send a clear quote.','Pricing')+f'''<main id="main"><section class="theme-light"><div class="container"><div class="grid-3" style="align-items:stretch">{cs}</div></div></section>
<section class="theme-soft"><div class="container"><div class="section-head center"><span class="eyebrow">FAQ</span><h2 class="h1 reveal">Good questions</h2></div><div class="acc">{fq}</div></div></section>{cta()}</main>'''+footer()

# ================= INSIGHTS =================
def insights():
    ps=[('post-1','Renovation','Why rebuilding beats patching an outdated site','Quick fixes pile up. Here is when a rebuild saves time and money.'),('post-2','AI Visuals','Generated imagery that actually fits your brand','How we art-direct AI visuals so they feel made for you.'),('post-3','Motion','Scroll animation: when it helps and when it hurts','Motion should guide attention, not distract from it.'),('post-4','Performance','Fast sites sell more: the basics of web speed','Image sizes, fonts and code habits that keep pages quick.'),('post-5','Design','Dark UI and glassmorphism done well','Contrast, depth and restraint for modern interfaces.'),('post-6','Stack','Why Git workflows matter for small business sites','Version control makes updates safer and handovers easier.')]
    cs=''.join(f'<a class="post reveal d{i%3+1}" href="contact.html">{slot(im,"16/10",t,"zoom")}<span class="meta">{c}</span><h3>{t}</h3><p>{d}</p><span class="link-arrow">Read article →</span></a>' for i,(im,c,t,d) in enumerate(ps))
    return head('Insights — PixelMind','Articles on web design, renovation, AI visuals and motion from PixelMind.','dark')+nav('insights.html')+page_hero('Insights','Ideas on design, motion and <span class="accent">AI visuals</span>','Short, practical reads for business owners and teams modernizing their web presence.','Insights')+f'''<main id="main"><section class="theme-light"><div class="container"><div class="grid-3">{cs}</div></div></section>{cta('Have a project in mind?')}</main>'''+footer()

# ================= CONTACT =================
def contact():
    return head('Contact — PixelMind','Start a project with PixelMind. Call, WhatsApp or email — we reply within about a day.','dark')+nav('contact.html')+page_hero('Contact','Let’s build something that <span class="accent">actually works</span>','Tell us about your project — a tired site that needs a rebuild, or something new from scratch.','Get in touch')+f'''<main id="main"><section class="theme-light"><div class="container"><div class="contact-grid"><div>
<span class="eyebrow">Talk to us</span><h2 class="h1">We usually reply within a day</h2>
<div class="contact-list"><a href="tel:+27761501439"><i>☎</i> +27 76 150 1439 (Phone / WhatsApp)</a><a href="mailto:pixelmind.webstudio@gmail.com"><i>✉</i> pixelmind.webstudio@gmail.com</a><a href="mailto:Lathithamajavu123@gmail.com"><i>➤</i> Lathithamajavu123@gmail.com (Direct)</a><div><i>⌖</i> South Africa (+27)</div></div>
<div class="social-row"><a href="https://facebook.com" target="_blank" rel="noopener" aria-label="PixelMind on Facebook">f</a><a href="https://linkedin.com" target="_blank" rel="noopener" aria-label="PixelMind on LinkedIn">in</a><a href="https://instagram.com" target="_blank" rel="noopener" aria-label="PixelMind on Instagram">ig</a></div></div>
<div class="form-card"><h3>Start a project</h3><p>Fill this in and your email app will open with the details ready to send.</p>
<form id="contactForm"><div class="form-two"><div class="form-row"><label for="n">Name</label><input id="n" name="name" required></div><div class="form-row"><label for="e">Email</label><input id="e" name="email" type="email" required></div></div>
<div class="form-two"><div class="form-row"><label for="s">Service</label><select id="s" name="service"><option>Web design &amp; renovation</option><option>AI-generated visuals</option><option>Motion &amp; animation</option><option>GitHub &amp; modern stack</option><option>Not sure yet</option></select></div><div class="form-row"><label for="b">Budget</label><select id="b" name="budget"><option>Not sure yet</option><option>Small</option><option>Medium</option><option>Large</option></select></div></div>
<div class="form-row"><label for="m">Project details</label><textarea id="m" name="message" placeholder="Tell us about your project"></textarea></div>
<button class="btn btn-primary btn-block btn-lg" type="submit">Send message</button><div class="form-ok">Opening your email app…</div></form></div></div></div></section></main>'''+footer()

for fn,fnc in [('index.html',home),('services.html',services),('work.html',work),('case-study.html',case),('process.html',process),('about.html',about),('pricing.html',pricing),('insights.html',insights),('contact.html',contact)]:
    write(fn,fnc())
