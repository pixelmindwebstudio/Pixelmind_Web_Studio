/* PixelMind – shared behaviour. No dependencies. */
(function(){
  const $=(s,c=document)=>c.querySelector(s), $$=(s,c=document)=>[...c.querySelectorAll(s)];
  const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Nav: mobile toggle, scrolled state, dark-hero state, progress bar */
  const nav=$('#navbar'), tog=$('#navToggle'), panel=$('#mobilePanel'), bar=$('.scroll-progress');
  if(tog) tog.addEventListener('click',()=>{const o=tog.classList.toggle('open');panel.classList.toggle('open',o);tog.setAttribute('aria-expanded',o)});
  const darkTop=document.body.dataset.hero==='dark';
  const onScroll=()=>{
    const y=scrollY; nav.classList.toggle('scrolled',y>12);
    nav.classList.toggle('on-dark',darkTop && y<window.innerHeight*0.7);
    const h=document.documentElement.scrollHeight-innerHeight; if(bar) bar.style.width=(h>0?y/h*100:0)+'%';
  };
  addEventListener('scroll',onScroll,{passive:true}); onScroll();

  /* Reveal on scroll */
  const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('is-visible');io.unobserve(e.target)}}),{threshold:.12,rootMargin:'0px 0px -50px 0px'});
  $$('.reveal').forEach(el=>io.observe(el));

  /* Counters */
  const cio=new IntersectionObserver(es=>es.forEach(e=>{
    if(!e.isIntersecting) return; cio.unobserve(e.target);
    const el=e.target, to=+el.dataset.count, suf=el.dataset.suffix||'', pre=el.dataset.prefix||'';
    if(reduce){el.textContent=pre+to+suf;return}
    const t0=performance.now(), dur=1400;
    (function tick(t){const p=Math.min((t-t0)/dur,1), v=Math.round(to*(1-Math.pow(1-p,3)));el.textContent=pre+v+suf; if(p<1) requestAnimationFrame(tick)})(t0);
  }),{threshold:.6});
  $$('[data-count]').forEach(el=>cio.observe(el));

  /* Tabs (pillars) */
  $$('[data-tabs]').forEach(w=>{
    const btns=$$('.tab-btn',w), panels=$$('.tab-panel',w);
    const sel=i=>{btns.forEach((b,j)=>b.setAttribute('aria-selected',i===j));panels.forEach((p,j)=>p.classList.toggle('active',i===j))};
    btns.forEach((b,i)=>{b.addEventListener('click',()=>sel(i));b.addEventListener('keydown',e=>{
      if(e.key==='ArrowRight'){btns[(i+1)%btns.length].focus();sel((i+1)%btns.length)}
      if(e.key==='ArrowLeft'){btns[(i-1+btns.length)%btns.length].focus();sel((i-1+btns.length)%btns.length)}})});
    sel(0);
  });

  /* Sticky story: highlight the step nearest the centre */
  const steps=$$('.step');
  if(steps.length){
    const sio=new IntersectionObserver(es=>es.forEach(e=>e.target.classList.toggle('in',e.isIntersecting)),{rootMargin:'-35% 0px -35% 0px'});
    steps.forEach(s=>sio.observe(s));
  }

  /* Gallery rail with arrows + dots */
  $$('[data-rail]').forEach(w=>{
    const rail=$('.rail',w), cards=$$('.rail-card',w), dots=$('.dots',w), prev=$('.prev',w), next=$('.next',w);
    cards.forEach((c,i)=>{const b=document.createElement('button');b.setAttribute('aria-label','Go to item '+(i+1));b.onclick=()=>go(i);dots.appendChild(b)});
    const step=()=>cards[0].getBoundingClientRect().width+22;
    function go(i){rail.scrollTo({left:i*step(),behavior:reduce?'auto':'smooth'})}
    function sync(){const i=Math.round(rail.scrollLeft/step());$$('button',dots).forEach((b,j)=>b.classList.toggle('on',i===j))}
    rail.addEventListener('scroll',()=>requestAnimationFrame(sync),{passive:true});
    prev.onclick=()=>rail.scrollBy({left:-step(),behavior:'smooth'}); next.onclick=()=>rail.scrollBy({left:step(),behavior:'smooth'});
    sync();
  });

  /* Testimonials */
  $$('[data-testi]').forEach(w=>{
    const slides=$$('.testi-slide',w), dots=$('.dots',w); let i=0,timer;
    slides.forEach((_,j)=>{const b=document.createElement('button');b.setAttribute('aria-label','Testimonial '+(j+1));b.onclick=()=>{show(j);auto()};dots.appendChild(b)});
    function show(n){i=n;slides.forEach((s,j)=>s.classList.toggle('active',j===n));$$('button',dots).forEach((b,j)=>b.classList.toggle('on',j===n))}
    function auto(){clearInterval(timer);if(!reduce)timer=setInterval(()=>show((i+1)%slides.length),7000)}
    show(0);auto();
  });

  /* Filters */
  $$('[data-filter-group]').forEach(g=>{
    const chips=$$('.chip',g), items=$$('[data-cat]',document);
    chips.forEach(c=>c.addEventListener('click',()=>{
      chips.forEach(x=>x.classList.toggle('on',x===c)); const f=c.dataset.f;
      items.forEach(it=>it.classList.toggle('hide',f!=='all' && !it.dataset.cat.split(' ').includes(f)));
    }));
  });

  /* Accordion */
  $$('.acc-item').forEach(it=>{const q=$('.acc-q',it),a=$('.acc-a',it);
    q.addEventListener('click',()=>{const o=it.classList.toggle('open');q.setAttribute('aria-expanded',o);a.style.maxHeight=o?a.scrollHeight+'px':0})});

  /* Spotlight hover on cards */
  $$('.card').forEach(c=>c.addEventListener('pointermove',e=>{const r=c.getBoundingClientRect();c.style.setProperty('--mx',(e.clientX-r.left)+'px');c.style.setProperty('--my',(e.clientY-r.top)+'px')}));

  /* Subtle hero parallax */
  const hm=$('.hero-media');
  if(hm && !reduce) addEventListener('scroll',()=>{if(scrollY<innerHeight)hm.style.transform='translateY('+scrollY*.25+'px) scale(1.08)'},{passive:true});

  /* Hero video: only play if a real file exists (poster image is the demo fallback) */
  $$('video[data-autoplay]').forEach(v=>{v.addEventListener('error',()=>v.remove(),true);const s=v.querySelector('source');if(s)s.addEventListener('error',()=>v.remove())});

  /* Contact form -> mailto handoff */
  const form=$('#contactForm');
  if(form) form.addEventListener('submit',e=>{
    e.preventDefault(); const f=new FormData(form);
    const subject=encodeURIComponent('New project inquiry — '+(f.get('name')||''));
    const body=encodeURIComponent((f.get('message')||'')+'\n\nService: '+(f.get('service')||'')+'\nBudget: '+(f.get('budget')||'')+'\nFrom: '+f.get('name')+' ('+f.get('email')+')');
    const ok=$('.form-ok'); if(ok) ok.style.display='block';
    location.href='mailto:pixelmind.webstudio@gmail.com?subject='+subject+'&body='+body;
  });

  /* Case study page (data-driven so one template serves every project) */
  const csRoot=$('#caseStudy');
  if(csRoot){
    const P={
     'bridge-street':{t:'Bridge Street Bistro & Smokehouse',tag:'Restaurant · Live Music',lead:'A restaurant, bar and live-music venue site for Gqeberha — warm, moody visuals with a menu and events flow built for mobile.',client:'Bridge Street',role:'Design · Build · AI visuals',year:'2026',status:'In progress',img:'work-bridge',
       a:'The venue lives at night, so the site is dark, warm and ambient. Menu and events sit one tap from the hero, because that is what visitors come for.',b:'Visual direction pairs amber light and smoke with a clean, legible menu layout that works on a phone held in one hand.'},
     'west-end-clinic':{t:'West End Clinic',tag:'Healthcare',lead:'A calm, trustworthy marketing site for a community health clinic in Gqeberha.',client:'West End Clinic',role:'Design · Build',year:'2026',status:'In progress',img:'work-westend',
       a:'Healthcare sites must feel safe before they feel clever. We used soft colour, large type and obvious booking and contact actions.',b:'Services, opening hours and location are organised so a first-time visitor finds what they need in seconds.'},
     'founders-factory':{t:'Founders Factory Africa',tag:'Venture Capital',lead:'Enhancing an investor-grade site with new features and motion-led storytelling.',client:'Founders Factory Africa',role:'Enhancement · Motion · AI visuals',year:'2026',status:'In progress',img:'work-ff',
       a:'The goal was to keep the site credible and sharp while adding depth: richer sections, generated visuals and purposeful animation.',b:'Founder stories and portfolio highlights get dedicated, scannable layouts.'},
     'aperture':{t:'Aperture Analytics',tag:'SaaS Concept',lead:'A dashboard-first landing page concept for a data analytics product.',client:'Concept',role:'UI concept',year:'2026',status:'Concept',img:'work-aperture',
       a:'A dark glassmorphic interface with animated metrics, built to show how data products can feel approachable.',b:'Cards, charts and gradients share one token system so the page stays consistent.'},
     'meridian':{t:'Meridian Tech Portal',tag:'Tech Portal Concept',lead:'An internal-tools portal concept blending a dark UI with node-based visuals.',client:'Concept',role:'UI concept',year:'2026',status:'Concept',img:'work-meridian',
       a:'Complex systems are explained through connected nodes and layered depth rather than walls of text.',b:'Navigation stays shallow: everything is two clicks away.'}
    };
    const k=new URLSearchParams(location.search).get('p')||'bridge-street', d=P[k]||P['bridge-street'];
    document.title=d.t+' — PixelMind';
    $('#csTitle').textContent=d.t; $('#csTag').textContent=d.tag; $('#csLead').textContent=d.lead;
    $('#csClient').textContent=d.client;$('#csRole').textContent=d.role;$('#csYear').textContent=d.year;$('#csStatus').textContent=d.status;
    $('#csA').textContent=d.a;$('#csB').textContent=d.b;
    $$('[data-cs-img]').forEach(i=>{i.src='assets/img/'+d.img+'.svg'});
    const keys=Object.keys(P), nx=P[keys[(keys.indexOf(k)+1)%keys.length]], nk=keys[(keys.indexOf(k)+1)%keys.length];
    const n=$('#csNext'); n.href='case-study.html?p='+nk; $('#csNextName').textContent=nx.t;
  }
  const y=$('#year'); if(y) y.textContent=new Date().getFullYear();
})();
