# PixelMind — multi-page site

Open `index.html` in a browser (or push the folder to GitHub Pages / Netlify / Vercel — no build step needed).

## Pages
index · services · work · case-study (?p=bridge-street | west-end-clinic | founders-factory | aperture | meridian) · process · about · pricing · insights · contact

## What was borrowed
- **Apple:** frosted nav, huge type, sticky scroll-story ("Renovate. Generate. Animate. Ship."), swipeable gallery rail with dots/arrows.
- **Tony Robbins:** full-screen video hero, alternating dark/light sections, "pillars" tabs, marquee strip, stats counters, testimonial slider.

## Replacing demo media
Every image is a labelled SVG in `assets/img/` named for its slot. Drop in a real file with the same name
(e.g. `hero-poster.jpg`) and change `.svg` to `.jpg` in the HTML — or keep it as an SVG-named file. The label in the corner shows the ideal size.
Hero video: put an MP4 at `assets/video/hero.mp4` (muted loop, 5–8 s, under ~6 MB). If it is absent, the poster image shows.
To edit the site structure, change `_build/build.py` and run `python3 _build/build.py` (optional — you can also edit the .html files directly).

## Demo content to replace before launch
Testimonials ("Client Name"), team names/roles, the 4 stats on the homepage, FAQ answers, pricing tiers (set to "Custom quote"), insights article links (currently go to Contact), social links (generic facebook/linkedin/instagram).

## Higgsfield plan (credit-safe)
Account had **0 credits** when this was built, so nothing was generated. Run in this order and stop whenever credits run low;
**always call with `get_cost: true` first** and use the cheapest image model that looks good.

| Tier | Assets | Count | Slots |
|---|---|---|---|
| 1 – Must have | Hero poster still (16:9), hero loop video (5 s, 16:9, image-to-video from the poster) | 1 image + 1 video | `hero-poster`, `assets/video/hero.mp4` |
| 2 – Big impact | Gallery tiles 4:5 (Bridge Street, West End Clinic, Founders Factory) | 3 images | `gal-1`…`gal-3`, reuse as `work-*` |
| 3 – Nice to have | Four service images 4:3 | 4 images | `feat-web/ai/motion/stack` |
| 4 – Later | Page banner, CTA background, remaining gallery/work tiles, article covers | ~10 images | `page-bg`, `cta-bg`, `gal-4/5`, `work-*`, `post-*` |

Tips to save credits: generate 1 variant at a time (count 1), reuse one image in several slots (e.g. `page-bg` as `cta-bg`),
make the video from an existing still (image-to-video) rather than text-to-video, keep clips ≤5 s, and skip upscaling.

### Prompts (consistent brand look: deep navy base, blue→purple→orange accents, glowing node-network motifs)
- **hero-poster:** "Abstract glowing node-network of interconnected spheres in blue, violet and orange on a deep navy background, cinematic depth of field, soft light trails, premium tech brand hero, no text"
- **hero.mp4:** same still, "slow camera drift, nodes gently pulsing and connecting with light lines, seamless loop, no text"
- **gal-1 Bridge Street:** "Warm moody bistro interior at night, amber pendant lights, smoke and a live-music stage glow, cinematic, 4:5, no text"
- **gal-2 West End Clinic:** "Bright calm modern community clinic reception, soft blue and white tones, welcoming and trustworthy, 4:5, no text"
- **gal-3 Founders Factory:** "Futuristic African skyline with glowing network lines, venture and innovation theme, deep navy and violet, 4:5, no text"
- **feat-web / ai / motion / stack:** "Floating glass website interface panels / generative art canvas / motion trails and easing curves / terminal and git branch lines — all in the PixelMind navy-blue-violet palette, 4:3, no text"
