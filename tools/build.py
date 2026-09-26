# Generates ../index.html  (run: python3 tools/build.py)
import os,json
H=os.path.dirname(os.path.abspath(__file__))
IC={
'man':'<svg viewBox="0 0 24 24"><circle cx="12" cy="7" r="4"/><path d="M4 21c0-4.5 3.6-7 8-7s8 2.5 8 7"/></svg>',
'arm':'<svg viewBox="0 0 24 24"><path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/></svg>',
'ind':'<svg viewBox="0 0 24 24"><path d="M3 21V9l6 4V9l6 4V5h6v16z"/></svg>',
'com':'<svg viewBox="0 0 24 24"><rect x="4" y="3" width="16" height="18"/><path d="M8 7h2M14 7h2M8 11h2M14 11h2M8 15h2M14 15h2"/></svg>',
'res':'<svg viewBox="0 0 24 24"><path d="M3 11l9-8 9 8"/><path d="M5 10v11h14V10"/></svg>',
'hos':'<svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M12 7v10M7 12h10"/></svg>',
'edu':'<svg viewBox="0 0 24 24"><path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c3 2 9 2 12 0v-5"/></svg>',
'bnk':'<svg viewBox="0 0 24 24"><rect x="3" y="6" width="18" height="12" rx="1"/><circle cx="12" cy="12" r="3"/></svg>'}
SV=[('man','Manned Security','Trained, verified guards for around the clock protection of your premises.','operations','30% 40%'),
('arm','Armed Security','Disciplined armed personnel for high security requirements.','hero','' ),
('ind','Industrial Security','Protection for plants, warehouses and industrial campuses.','training','60% 50%'),
('com','Commercial Security','Professional guards for offices and business premises.','operations','80% 40%'),
('res','Residential Security','Courteous, reliable security for homes and societies.','about','40% 50%'),
('hos','Hospital Security','Calm, courteous security for hospitals and healthcare facilities.','about','70% 30%'),
('edu','Educational Security','Safe, closely supervised campuses for schools and institutions.','training','30% 60%'),
('bnk','Bank &amp; ATM Security','Vigilant, verified personnel for branches and ATMs.','operations','55% 35%')]
SLUGS=['manned','armed','industrial','commercial','residential','hospital','educational','banking']
tabs=panels=mega=chips=''
for k,(ic,h,p,im,pos) in enumerate(SV):
    on=' on' if k==0 else ''
    alt=h.replace('&amp;','and')
    tabs+=f'<button class="tb{on}" data-k="{k}" role="tab"><span class="ti">{IC[ic]}</span><span class="tt">{h}</span><span class="ar">→</span></button>'
    media=f'<div class="pm art m{(k%8)+1}"><div class="rg a"></div><div class="rg b"></div><span class="ai">{IC[ic]}</span></div>'
    panels+=f'<article class="pn{on}" data-k="{k}">{media}<div class="pb"><div class="num">0{k+1}<small>/ 08</small></div><h3>{h}</h3><p>{p}</p><ul><li>Trained &amp; verified personnel</li><li>Available 24/7</li><li>Customized to your site</li></ul><a class="btn btn-g" href="/services/{SLUGS[k]}">View details →</a><a class="lk" href="/planner">Plan this service</a></div></article>'
    mega+=f'<a href="/services/{SLUGS[k]}"><i>{IC[ic]}</i>{h}</a>'
    chips+=f'<label class="chp"><input type="checkbox" value="{alt}"><span>{IC[ic]}{h}</span></label>'

html=r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Parakram Security India | Your Safety Is Our Mission</title>
<meta name="description" content="Parakram Security India Pvt. Ltd. Manned, armed, industrial, commercial, residential, hospital, educational and bank &amp; ATM security. 9+ years, 1,500+ trained professionals, 24/7. Haridwar, Uttarakhand.">
<meta name="theme-color" content="#050d3a">
<link rel="canonical" href="https://parakram-website.vercel.app/"><meta property="og:site_name" content="Parakram Security India"><meta property="og:title" content="Parakram Security India | Your Safety Is Our Mission"><meta property="og:description" content="Professionally managed private security with trained, verified personnel, customized solutions, 24/7."><meta property="og:type" content="website"><meta property="og:url" content="https://parakram-website.vercel.app/"><meta property="og:image" content="https://parakram-website.vercel.app/og-image.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="Parakram Security India | Your Safety Is Our Mission"><meta name="twitter:description" content="Manned, armed, industrial, commercial, residential, hospital, educational and bank &amp; ATM security. 24/7."><meta name="twitter:image" content="https://parakram-website.vercel.app/og-image.jpg">
<script>window.addEventListener("error",function(){document.documentElement.classList.add("rvfix")});setTimeout(function(){document.documentElement.classList.add("rvfix2")},6000)</script>
<script>try{if(!sessionStorage.getItem("intro")&&!matchMedia("(prefers-reduced-motion:reduce)").matches)document.documentElement.classList.add("intro")}catch(e){}</script>
<link rel="icon" href="favicon.png" type="image/png"><link rel="apple-touch-icon" href="logo.png"><link rel="preload" as="image" href="img/parakram-hero-portrait.webp" type="image/webp" fetchpriority="high">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Inter:wght@400;500;600;700&family=Manrope:wght@600;700;800&display=swap" rel="stylesheet">
<script type="application/ld+json">{"@context":"https://schema.org","@type":"SecurityService","name":"Parakram Security India Pvt. Ltd.","url":"https://parakram-website.vercel.app","logo":"https://parakram-website.vercel.app/logo.png","image":"https://parakram-website.vercel.app/og-image.jpg","email":"info@parakramindia.org","telephone":"+919105909006","foundingDate":"2017","address":{"@type":"PostalAddress","streetAddress":"6A Sandesh Nagar, Kankhal","addressLocality":"Haridwar","addressRegion":"Uttarakhand","postalCode":"249408","addressCountry":"IN"},"aggregateRating":{"@type":"AggregateRating","ratingValue":"4.9","reviewCount":"1200"}}</script>
<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"What types of security services do you provide?","acceptedAnswer":{"@type":"Answer","text":"Manned, Armed, Industrial, Commercial, Residential, Hospital, Educational, and Bank & ATM security."}},{"@type":"Question","name":"Is your service available 24/7?","acceptedAnswer":{"@type":"Answer","text":"Yes, our services are available 24/7."}},{"@type":"Question","name":"Can solutions be customized to my site?","acceptedAnswer":{"@type":"Answer","text":"Yes. We design customized security solutions around your needs, including support for multiple sites."}}]}</script>
<style>
:root{--navy:#050d3a;--navy2:#0a1660;--navy3:#0e1d78;--gold:#ffc400;--gold2:#ffd84d;--ink:#0b1020;--mut:#5a6180;--bg:#f4f5fb;--line:#e3e6f2;--r:14px;--ease:cubic-bezier(.2,.7,.2,1)}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth;scroll-padding-top:90px}
body{font-family:Inter,system-ui,sans-serif;color:var(--ink);background:#fff;line-height:1.65;-webkit-font-smoothing:antialiased;overflow-x:hidden}
h1,h2,h3,h4{font-family:Manrope,sans-serif;letter-spacing:-.03em;line-height:1.05;font-weight:800}
.num,.stat b,.big{font-family:'Barlow Condensed',sans-serif}
a{color:inherit;text-decoration:none}img{max-width:100%;display:block}button{font-family:inherit}
.wrap{max-width:1280px;margin:0 auto;padding:0 28px}
section{padding:120px 0;position:relative}
.bg{background:var(--bg)}
.eyebrow{display:inline-flex;align-items:center;gap:12px;color:var(--gold);font-weight:700;font-size:12px;letter-spacing:.22em;text-transform:uppercase;margin-bottom:22px}
.eyebrow:before{content:"";width:36px;height:2px;background:currentColor}.eyebrow.dk{color:var(--navy3)}.eyebrow.dk:before{background:var(--gold)}
.h2{font-size:clamp(34px,4.6vw,60px);color:var(--navy)}.h2 em{font-style:normal;color:var(--navy3);background:linear-gradient(transparent 62%,rgba(255,196,0,.55) 62%)}
.sec-h{max-width:780px;margin-bottom:60px}.sec-h p{color:var(--mut);font-size:18px;margin-top:18px}
.btn{position:relative;display:inline-flex;align-items:center;gap:10px;padding:16px 30px;font-weight:700;font-size:14px;letter-spacing:.04em;border-radius:999px;transition:transform .3s var(--ease),background .25s,color .25s,box-shadow .25s;cursor:pointer;border:2px solid transparent;overflow:hidden}
.btn-g{background:var(--gold);color:var(--navy);box-shadow:0 10px 30px rgba(255,196,0,.3)}.btn-g:hover{background:#fff;box-shadow:0 14px 40px rgba(255,196,0,.45)}
.btn-o{border-color:rgba(255,255,255,.45);color:#fff}.btn-o:hover{background:#fff;color:var(--navy)}
.btn-n{background:var(--navy);color:#fff}.btn-n:hover{background:var(--gold);color:var(--navy)}
/* progress + util + header */
#pg{position:fixed;top:0;left:0;height:3px;background:linear-gradient(90deg,var(--gold),#fff);width:0;z-index:100}
.util{background:var(--navy);color:#c9cef0;font-size:12.5px}.util .wrap{display:flex;justify-content:space-between;align-items:center;height:40px;gap:16px}
.util a:hover{color:var(--gold)}.ist{margin-left:14px;padding-left:14px;border-left:1px solid rgba(255,255,255,.25);font-variant-numeric:tabular-nums;color:var(--gold2);font-weight:600}.util .r{display:flex;gap:24px}.pulse{display:inline-block;width:8px;height:8px;border-radius:50%;background:#2ee66b;margin-right:8px;animation:p 1.8s infinite}
@keyframes p{0%{box-shadow:0 0 0 0 rgba(46,230,107,.7)}70%{box-shadow:0 0 0 9px transparent}100%{box-shadow:0 0 0 0 transparent}}
header{position:sticky;top:0;z-index:60;background:rgba(255,255,255,.96);border-bottom:1px solid var(--line);transition:box-shadow .3s}header:before{content:"";position:absolute;inset:0;z-index:-1;backdrop-filter:saturate(1.6) blur(14px)}
header.sh{box-shadow:0 10px 40px rgba(5,13,58,.12)}
.nav{display:flex;align-items:center;justify-content:space-between;height:80px;gap:20px}
.brand{display:flex;align-items:center;gap:12px;flex:none}.brand img{height:56px}.brand div{white-space:nowrap}
.brand b{font-family:Manrope;font-size:22px;letter-spacing:.06em;color:var(--navy);line-height:1;display:block;font-weight:800}
.brand small{font-size:9.5px;letter-spacing:.24em;color:var(--mut);font-weight:700}
nav>ul{display:flex;list-style:none}nav>ul>li>a{display:block;white-space:nowrap;padding:30px 13px;font-weight:600;font-size:14px;color:var(--navy);position:relative}
nav>ul>li>a:after{content:"";position:absolute;left:13px;right:13px;bottom:22px;height:2px;background:var(--gold);transform:scaleX(0);transform-origin:left;transition:transform .3s var(--ease)}
nav>ul>li:hover>a:after,nav>ul>li>a.act:after{transform:scaleX(1)}
.dd{position:static}.dd .menu{position:absolute;top:100%;left:50%;transform:translate(-50%,12px);width:min(880px,94vw);background:#fff;border-radius:0 0 18px 18px;border-top:3px solid var(--gold);box-shadow:0 40px 80px rgba(5,13,58,.22);opacity:0;visibility:hidden;transition:.3s var(--ease);display:grid;grid-template-columns:1fr 300px;overflow:hidden}
.dd:hover .menu,.dd:focus-within .menu{opacity:1;visibility:visible;transform:translate(-50%,0)}
.mg{display:grid;grid-template-columns:1fr 1fr;padding:22px;gap:4px}.mg a{display:flex;align-items:center;gap:14px;padding:14px 16px;font-weight:600;font-size:14.5px;border-radius:10px;transition:.2s}
.mg a i{width:38px;height:38px;border-radius:10px;background:var(--bg);display:grid;place-items:center;flex:none;transition:.2s}.mg a i svg{width:20px;height:20px;stroke:var(--navy);fill:none;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.mg a:hover{background:var(--bg)}.mg a:hover i{background:var(--navy)}.mg a:hover i svg{stroke:var(--gold)}
.mp{background:var(--navy);color:#fff;position:relative;display:flex;flex-direction:column;justify-content:flex-end;padding:26px;min-height:280px;overflow:hidden}
.mp img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.5}.mp:before{content:"";position:absolute;inset:0;background:linear-gradient(transparent 20%,var(--navy));z-index:1}.mp>*:not(img){position:relative;z-index:2}
.mp b{font-family:Manrope;font-size:22px;line-height:1.15}.mp a{color:var(--gold);font-size:13px;font-weight:700;margin-top:10px}
.burger{display:none;background:none;border:0;width:44px;height:44px;cursor:pointer;position:relative;margin-left:auto}
.burger i,.burger:before,.burger:after{content:"";position:absolute;left:10px;right:10px;height:2px;background:var(--navy);transition:.3s}.burger:before{top:15px}.burger i{top:21px}.burger:after{top:27px}
.burger.x:before{top:21px;transform:rotate(45deg)}.burger.x:after{top:21px;transform:rotate(-45deg)}.burger.x i{opacity:0}
/* HERO */
.hx{position:relative;background:#030826;color:#fff;overflow:hidden;height:calc(100vh - 120px);min-height:660px;max-height:880px}
.slide{position:absolute;inset:0;opacity:0;visibility:hidden;transition:opacity 1.1s,visibility 1.1s;display:flex;align-items:center}
.slide.on{opacity:1;visibility:visible}
.bgc{position:absolute;inset:0;background:radial-gradient(800px 520px at 78% 40%,rgba(255,196,0,.26),transparent 62%),radial-gradient(700px 600px at 5% 110%,rgba(40,60,220,.6),transparent 60%),linear-gradient(135deg,#030826,#0a1660 60%,#050d3a)}
.bgc:after{content:"";position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.05) 1px,transparent 1px);background-size:60px 60px;mask-image:radial-gradient(circle at 70% 45%,#000,transparent 72%);animation:gm 30s linear infinite}
@keyframes gm{to{background-position:60px 60px}}
.photo{position:absolute;inset:0;background:var(--bg) center/cover;transform:scale(1.1);transition:transform 8s linear}.slide.on .photo{transform:scale(1)}
.photo:after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(3,8,38,.96) 0%,rgba(3,8,38,.8) 45%,rgba(3,8,38,.3) 100%)}
.hxg{position:relative;z-index:2;display:grid;grid-template-columns:1.1fr .9fr;gap:40px;align-items:end;height:100%;padding-top:50px;padding-bottom:110px}
.hxg.one{grid-template-columns:1fr;align-items:center}.hxg.one .tx{max-width:820px}
.hxg .tx{align-self:center;padding-bottom:96px}
.hx h1,.hx .hh{font-size:clamp(42px,5.2vw,80px);font-weight:800;line-height:1;letter-spacing:-.04em}.hx h1 em,.hx .hh em{font-style:normal;color:var(--gold);display:block}
.hx h1 .ln,.hx .hh .ln{display:block;overflow:hidden;padding-bottom:.08em}.hx h1 .ln>span,.hx .hh .ln>span{display:block;transform:translateY(110%);transition:transform 1s var(--ease)}
.slide.on h1 .ln>span,.slide.on .hh .ln>span{transform:none}.slide.on h1 .ln:nth-child(2)>span,.slide.on .hh .ln:nth-child(2)>span{transition-delay:.12s}.slide.on h1 .ln:nth-child(3)>span{transition-delay:.24s}
.hx .lead,.hx .cta,.hx .eyebrow{opacity:0;transform:translateY(24px);transition:all .9s var(--ease) .35s}.slide.on .lead,.slide.on .cta,.slide.on .eyebrow{opacity:1;transform:none}.slide.on .cta{transition-delay:.55s}
.hx .lead{font-size:19px;color:#c9cef0;max-width:580px;margin:26px 0 38px}.hx .cta{display:flex;flex-wrap:wrap;gap:14px}
.fig{position:relative;height:100%;display:flex;align-items:flex-end;justify-content:center;transition:transform .2s}
.fig img{position:relative;z-index:2;height:112%;max-height:830px;width:auto;object-fit:contain;filter:drop-shadow(0 30px 50px rgba(0,0,0,.5))}
.halo{position:absolute;bottom:0;width:580px;height:580px;max-width:100%;border-radius:50%;background:radial-gradient(circle,rgba(255,196,0,.5),transparent 68%);animation:hl 5s ease-in-out infinite}@keyframes hl{50%{transform:scale(1.1);opacity:.75}}
.tagc{position:absolute;z-index:3;background:rgba(255,255,255,.96);color:var(--navy);padding:14px 20px;font-size:12px;font-weight:700;border-radius:12px;box-shadow:0 18px 40px rgba(0,0,0,.4);border-left:4px solid var(--gold);animation:fl 6s ease-in-out infinite}
.tagc b{display:block;font-family:'Barlow Condensed';font-size:34px;line-height:1}
.tagc.t1{top:22%;left:-2%}.tagc.t2{bottom:28%;right:-2%;animation-delay:-3s}@keyframes fl{50%{transform:translateY(-14px)}}
.hxc{position:absolute;left:0;right:0;bottom:0;z-index:5;padding-bottom:104px}.hxc .wrap{display:flex;justify-content:space-between;align-items:center;gap:20px}
.dots{display:flex;gap:26px}.d{background:none;border:0;color:rgba(255,255,255,.55);text-align:left;cursor:pointer;width:170px;font:600 12px Inter;letter-spacing:.1em;text-transform:uppercase}
.d i{display:block;height:3px;background:rgba(255,255,255,.25);margin-bottom:10px;position:relative;overflow:hidden;border-radius:3px}.d i:after{content:"";position:absolute;inset:0;background:var(--gold);transform:scaleX(0);transform-origin:left}
.d.on{color:#fff}.d.on i:after{animation:pr 6.5s linear forwards}@keyframes pr{to{transform:scaleX(1)}}
.arrows{display:flex;gap:10px}.arrows button{width:48px;height:48px;border-radius:50%;border:1px solid rgba(255,255,255,.4);background:rgba(255,255,255,.06);color:#fff;font-size:18px;cursor:pointer;transition:.25s}.arrows button:hover{background:var(--gold);color:var(--navy);border-color:var(--gold)}
.scrollcue{position:absolute;right:28px;bottom:120px;z-index:4;writing-mode:vertical-rl;font-size:11px;letter-spacing:.3em;color:rgba(255,255,255,.5);text-transform:uppercase;display:flex;align-items:center;gap:12px}.scrollcue:after{content:"";width:1px;height:50px;background:linear-gradient(var(--gold),transparent);animation:sc 2s infinite}@keyframes sc{0%{transform:scaleY(0);transform-origin:top}50%{transform:scaleY(1);transform-origin:top}51%{transform-origin:bottom}100%{transform:scaleY(0);transform-origin:bottom}}

.ghost{position:absolute;left:0;right:0;top:50%;transform:translateY(-52%);text-align:center;font:800 clamp(140px,24vw,380px)/1 Manrope;letter-spacing:-.06em;color:transparent;-webkit-text-stroke:1.5px rgba(255,255,255,.07);white-space:nowrap;pointer-events:none;user-select:none}
.fig img{-webkit-mask-image:linear-gradient(#000 84%,transparent);mask-image:linear-gradient(#000 84%,transparent)}
.tagc{display:flex;align-items:center;gap:10px;padding:11px 18px;border-radius:999px;font-size:13px;font-weight:700;border-left:0;background:rgba(255,255,255,.12);color:#fff;backdrop-filter:blur(14px);border:1px solid rgba(255,255,255,.25);box-shadow:0 14px 40px rgba(0,0,0,.35)}
.tagc i{width:9px;height:9px;border-radius:50%;background:var(--gold);box-shadow:0 0 0 5px rgba(255,196,0,.25)}
.tagc.t1{top:30%;left:0}.tagc.t2{bottom:30%;right:0}
.pf{position:relative;align-self:center;padding-bottom:70px}.pfi{position:relative;border-radius:26px;overflow:hidden;aspect-ratio:4/3.3;box-shadow:0 50px 100px rgba(0,0,0,.55);transform:translateY(20px) scale(.96);opacity:0;transition:all 1.1s var(--ease) .3s}
.slide.on .pfi{transform:none;opacity:1}.pfi img{width:100%;height:100%;object-fit:cover;transform:scale(1.12);transition:transform 7s linear}.slide.on .pfi img{transform:scale(1)}
.pfi:after{content:"";position:absolute;inset:0;border-radius:26px;box-shadow:inset 0 0 0 1px rgba(255,255,255,.18);background:linear-gradient(transparent 60%,rgba(5,13,58,.5))}
.pf:before{content:"";position:absolute;right:-18px;top:-18px;width:60%;height:60%;border:3px solid var(--gold);border-radius:30px;opacity:.8}
.pfb{position:absolute;left:-26px;bottom:36px;background:var(--gold);color:var(--navy);padding:18px 26px;border-radius:16px;box-shadow:0 24px 50px rgba(0,0,0,.4);z-index:2}.pfb b{display:block;font:800 44px/1 'Barlow Condensed'}.pfb span{font-size:12px;font-weight:800;letter-spacing:.08em;text-transform:uppercase}
@media(max-width:980px){.ghost{font-size:34vw;top:30%}.pf{order:-1;padding:0;margin:0 0 20px;max-width:none}.pfi{aspect-ratio:16/9;border-radius:18px}.pfb{display:none}.hx h1,.hx .hh{font-size:clamp(34px,9.6vw,50px)}.hx .lead{-webkit-line-clamp:3;margin:12px 0 20px}.hxg{padding-bottom:130px}.hxc{padding-bottom:92px}.pf:before{display:none}.pfb{left:12px;bottom:-14px;padding:12px 18px}.pfb b{font-size:32px}.hxg .tx{padding-bottom:0}.tagc{display:none}}

/* ===== hero v3: consistent SIS-style banner ===== */
.ghost,.tagc,.pf,.scrollcue{display:none!important}
.hxg,.hxg.one{display:flex;align-items:center;grid-template-columns:none;height:100%;padding-top:0;padding-bottom:130px}
.slide>.wrap.hxg{width:100%}.hxg .tx{align-self:center;padding:0;max-width:640px;width:100%}
.hx h1,.hx .hh{font-size:clamp(40px,4.7vw,68px);line-height:1.04;letter-spacing:-.035em}
.hx .lead{max-width:520px;font-size:18px;margin:22px 0 34px}
.ph{position:absolute;top:0;bottom:0;right:0;width:64%;background:var(--bg) 60% center/cover;-webkit-mask-image:linear-gradient(90deg,transparent 0,#000 38%);mask-image:linear-gradient(90deg,transparent 0,#000 38%);transform:scale(1.08);transform-origin:right center;transition:transform 8s linear}
.slide.on .ph{transform:scale(1)}.ph:after{content:"";position:absolute;inset:0;background:linear-gradient(0deg,rgba(3,8,38,.7),transparent 35%)}
.fig{position:absolute;right:max(4%,calc((100% - 1280px)/2 + 20px));bottom:0;top:auto;height:96%;width:auto;display:block;z-index:1}
.fig img{height:100%;width:auto;-webkit-mask-image:linear-gradient(#000 88%,transparent);mask-image:linear-gradient(#000 88%,transparent)}
.halo{left:50%;transform:translateX(-50%)}
.hxc{padding-bottom:100px}
.dots{gap:22px}.d{width:150px}
@media(max-width:980px){
.hx .hxg,.hx .hxg.one{align-items:flex-start;padding-top:290px;padding-bottom:120px}.hx .cta .btn{white-space:nowrap;font-size:13px}
.ph{width:100%;height:270px;bottom:auto;-webkit-mask-image:linear-gradient(180deg,#000 55%,transparent);mask-image:linear-gradient(180deg,#000 55%,transparent);background-position:60% 40%}
.fig{right:0;left:0;top:14px;bottom:auto;height:260px;display:flex!important;justify-content:center}.fig img{height:100%}.halo{width:300px;height:300px;top:20px;bottom:auto}
.hx h1,.hx .hh{font-size:clamp(34px,9.4vw,48px)}.hx .lead{font-size:15.5px;margin:12px 0 20px;-webkit-line-clamp:3}.hx .eyebrow{margin-bottom:10px}
.hx .cta .btn{padding:14px 16px}
.hxc{padding-bottom:90px}
}
/* stats */
.stats{position:relative;z-index:6;margin-top:-84px}.stats .grid{display:grid;grid-template-columns:repeat(5,1fr);background:#fff;border-radius:18px;box-shadow:0 40px 90px rgba(5,13,58,.25);overflow:hidden;border-top:5px solid var(--gold)}
.stat{padding:36px 24px;text-align:center;border-right:1px solid var(--line);transition:.3s}.stat:hover{background:var(--bg)}.stat:last-child{border:0}
.stat b{font-size:60px;color:var(--navy);display:block;line-height:1;font-weight:800}.stat b sup{color:var(--gold);font-size:.55em;top:-.6em}.stat span{font-size:12px;color:var(--mut);font-weight:700;letter-spacing:.12em;text-transform:uppercase}
.mq{background:var(--navy);color:#fff;overflow:hidden;padding:22px 0;margin-top:80px}.mt{display:flex;gap:56px;width:max-content;animation:mq 45s linear infinite}
.mt span{font-family:Manrope;font-weight:700;font-size:18px;letter-spacing:.02em;white-space:nowrap;display:flex;align-items:center;gap:56px;color:#dfe3ff}.mt span:after{content:"◆";color:var(--gold);font-size:11px}@keyframes mq{to{transform:translateX(-50%)}}
/* about */
.two{display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center}
.imgc{position:relative}.imgc .im{border-radius:22px;overflow:hidden;box-shadow:0 40px 80px rgba(5,13,58,.25)}.imgc img{width:100%;aspect-ratio:4/3.4;object-fit:cover;transform:scale(1.12);transition:transform 1.6s var(--ease)}.imgc.in img{transform:scale(1)}
.imgc:before{content:"";position:absolute;right:-20px;top:-20px;width:55%;height:55%;border:3px solid var(--gold);border-radius:22px;z-index:-1}
.imgc .bd{position:absolute;left:-22px;bottom:34px;background:var(--gold);color:var(--navy);padding:22px 28px;border-radius:14px;box-shadow:0 20px 50px rgba(0,0,0,.25)}.bd b{display:block;font-family:'Barlow Condensed';font-size:52px;line-height:1;font-weight:800}.bd span{font-size:12px;font-weight:800;letter-spacing:.1em;text-transform:uppercase}
.abt p{color:var(--mut);font-size:18px;margin-top:20px}.abt p+p{font-size:16.5px}
.vals{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin:32px 0}.vals div{padding:20px;border:1px solid var(--line);border-radius:var(--r);background:#fff;transition:.3s}.vals div:hover{border-color:var(--gold);transform:translateY(-4px);box-shadow:0 18px 40px rgba(5,13,58,.1)}
.vals b{display:block;font-family:Manrope;color:var(--navy);font-size:16px}.vals span{font-size:13px;color:var(--mut)}
/* services */
.sx{display:grid;grid-template-columns:350px 1fr;background:#fff;border-radius:22px;overflow:hidden;box-shadow:0 40px 90px rgba(5,13,58,.14);border:1px solid var(--line)}
.tl{background:var(--navy);display:flex;flex-direction:column}
.tb{display:grid;grid-template-columns:44px 1fr 24px;align-items:center;gap:14px;text-align:left;background:none;border:0;border-bottom:1px solid rgba(255,255,255,.08);color:#b9bfe8;padding:21px 26px;cursor:pointer;font:600 15.5px Inter;transition:.25s;position:relative}
.tb:before{content:"";position:absolute;left:0;top:0;bottom:0;width:4px;background:var(--gold);transform:scaleY(0);transition:.3s var(--ease)}
.tb .ti svg{width:26px;height:26px;stroke:var(--gold);fill:none;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}.tb .ar{opacity:0;transition:.25s;color:var(--gold);transform:translateX(-8px)}
.tb:hover,.tb.on{background:rgba(255,255,255,.07);color:#fff}.tb.on:before{transform:scaleY(1)}.tb.on .ar,.tb:hover .ar{opacity:1;transform:none}
.pw{position:relative;min-height:580px}.pn{position:absolute;inset:0;display:grid;grid-template-columns:1fr 1fr;opacity:0;visibility:hidden;transition:.5s var(--ease);transform:translateX(24px)}.pn.on{opacity:1;visibility:visible;transform:none}
.pm{position:relative;overflow:hidden}.pm img{width:100%;height:100%;object-fit:cover}.pm.cut{background:var(--navy);display:flex;align-items:flex-end;justify-content:center}.pm.cut img{position:relative;z-index:2;object-fit:contain;object-position:bottom;height:96%;width:auto}
.pm:after{content:"";position:absolute;inset:auto 0 0 0;height:40%;background:linear-gradient(transparent,rgba(5,13,58,.55));pointer-events:none}
.pb{padding:52px 48px;display:flex;flex-direction:column;justify-content:center}
.num{font-size:84px;font-weight:800;color:var(--gold);line-height:1}.num small{font-size:22px;color:var(--mut);margin-left:8px;font-weight:600}
.pb h3{font-size:40px;color:var(--navy);margin:12px 0}.pb p{color:var(--mut);font-size:17px}
.pb ul{list-style:none;margin:24px 0 30px;display:grid;gap:11px}.pb li{font-weight:600;color:var(--navy);font-size:15px;display:flex;gap:12px;align-items:center}.pb li:before{content:"✓";background:var(--gold);width:22px;height:22px;border-radius:50%;display:grid;place-items:center;font-size:12px;flex:none}.pb .btn{align-self:flex-start}
/* planner */
.plan{background:var(--navy);color:#fff;overflow:hidden}.plan:before{content:"";position:absolute;inset:0;background:radial-gradient(700px 500px at 90% 10%,rgba(255,196,0,.16),transparent 60%),radial-gradient(600px 500px at 0 100%,rgba(40,60,220,.5),transparent 60%)}
.plan .wrap{position:relative;display:grid;grid-template-columns:.85fr 1.15fr;gap:70px;align-items:center}
.plan .h2{color:#fff}.plan .h2 em{color:var(--gold);background:none}.plan p.s{color:#c9cef0;font-size:18px;margin:20px 0 28px}
.plan ul{list-style:none;display:grid;gap:14px}.plan li{display:flex;gap:14px;color:#dfe3ff;font-weight:500}.plan li:before{content:"✓";color:var(--navy);background:var(--gold);width:24px;height:24px;border-radius:50%;display:grid;place-items:center;font-size:12px;flex:none;font-weight:800}
.wz{background:#fff;color:var(--ink);border-radius:22px;padding:38px;box-shadow:0 50px 100px rgba(0,0,0,.4)}
.wz .st{display:flex;gap:8px;margin-bottom:26px}.wz .st i{flex:1;height:5px;border-radius:5px;background:var(--line);transition:.4s}.wz .st i.on{background:var(--gold)}
.wz h3{font-size:26px;color:var(--navy);margin-bottom:6px}.wz .sub{color:var(--mut);font-size:14.5px;margin-bottom:22px}
.step{display:none;animation:up .5s var(--ease)}.step.on{display:block}@keyframes up{from{opacity:0;transform:translateY(14px)}}
.chips{display:grid;grid-template-columns:1fr 1fr;gap:10px}.chp{cursor:pointer;position:relative}.chp input{position:absolute;opacity:0}
.chp span{display:flex;align-items:center;gap:10px;padding:14px 16px;border:1.5px solid var(--line);border-radius:12px;font-weight:600;font-size:14px;color:var(--navy);transition:.2s;height:100%}.chp svg{width:20px;height:20px;stroke:var(--navy3);fill:none;stroke-width:1.8;flex:none;stroke-linecap:round;stroke-linejoin:round}
.chp:hover span{border-color:var(--navy3)}.chp input:checked+span{background:var(--navy);color:#fff;border-color:var(--navy)}.chp input:checked+span svg{stroke:var(--gold)}.chp input:focus-visible+span{outline:2px solid var(--gold);outline-offset:2px}
.wz .nav2{display:flex;justify-content:space-between;align-items:center;margin-top:26px;gap:12px}.wz .bk{background:none;border:0;color:var(--mut);font-weight:700;cursor:pointer;font-size:14px}
.wz input.t,.wz textarea{width:100%;padding:15px 16px;border:1.5px solid var(--line);border-radius:12px;font:inherit;background:#fff;margin-bottom:12px}.wz input.t:focus,.wz textarea:focus{outline:none;border-color:var(--navy3)}
.wz .note{font-size:12px;color:var(--mut);margin-top:6px}
/* industries */
.ind{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}
.ic{position:relative;border-radius:20px;overflow:hidden;aspect-ratio:3/4;color:#fff;display:flex;flex-direction:column;justify-content:flex-end;padding:28px;background:var(--navy) center/cover;transition:transform .5s var(--ease),box-shadow .5s;isolation:isolate}
.ic:before{content:"";position:absolute;inset:0;background:var(--bg2) var(--pos,center)/cover;transition:transform .8s var(--ease);z-index:-2}.ic:hover:before{transform:scale(1.1)}
.ic:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(5,13,58,.15),rgba(5,13,58,.95));z-index:-1}
.ic:hover{transform:translateY(-8px);box-shadow:0 40px 80px rgba(5,13,58,.3)}
.ic .n{position:absolute;top:24px;left:28px;font-family:'Barlow Condensed';font-size:20px;letter-spacing:.14em;color:var(--gold);font-weight:700}
.ic .go{position:absolute;top:20px;right:22px;width:44px;height:44px;border-radius:50%;background:rgba(255,255,255,.14);backdrop-filter:blur(8px);display:grid;place-items:center;transition:.3s}.ic:hover .go{background:var(--gold);color:var(--navy);transform:rotate(-45deg)}
.ic h3{font-size:30px}.ic span{font-size:14px;color:#c9cef0;margin-top:6px}
.ic.nb{background:linear-gradient(160deg,var(--navy2),var(--navy))}.ic.nb:before{display:none}
/* band */
.band{position:relative;background:var(--navy) center/cover fixed;color:#fff;text-align:center;padding:150px 0}.band:before{content:"";position:absolute;inset:0;background:linear-gradient(rgba(3,8,38,.84),rgba(3,8,38,.92))}.band .wrap{position:relative}
.band h2{font-size:clamp(38px,6vw,84px);font-weight:800;letter-spacing:-.04em}.band h2 em{font-style:normal;color:var(--gold)}.band p{color:#c9cef0;font-size:19px;max-width:640px;margin:22px auto 34px}
/* why + process */
.pil{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.pl{position:relative;background:#fff;border:1px solid var(--line);border-radius:20px;padding:40px 34px;overflow:hidden;transition:.4s var(--ease)}
.pl:before{content:"";position:absolute;inset:0;background:radial-gradient(400px circle at var(--mx,50%) var(--my,0),rgba(255,196,0,.18),transparent 55%);opacity:0;transition:.3s}.pl:hover:before{opacity:1}.pl:hover{transform:translateY(-8px);box-shadow:0 30px 70px rgba(5,13,58,.14);border-color:var(--gold)}
.pl .big{font-size:96px;color:var(--gold);font-weight:800;line-height:.9}.pl h3{font-size:24px;color:var(--navy);margin:16px 0 10px}.pl p{color:var(--mut);font-size:15.5px;position:relative}
.proc{margin-top:100px}.proc h3.h2{margin-bottom:44px;font-size:clamp(28px,3.4vw,44px)}
.steps{display:grid;grid-template-columns:repeat(5,1fr);position:relative;gap:14px}.steps:before{content:"";position:absolute;top:27px;left:5%;right:5%;height:2px;background:repeating-linear-gradient(90deg,var(--navy3) 0 6px,transparent 6px 12px);opacity:.3}
.sp{position:relative;text-align:center}.sp i{font-style:normal;width:56px;height:56px;border-radius:50%;background:var(--navy);color:var(--gold);display:grid;place-items:center;font-family:'Barlow Condensed';font-size:24px;font-weight:800;margin:0 auto 18px;position:relative;box-shadow:0 0 0 8px var(--bg);transition:.3s}.sp:hover i{background:var(--gold);color:var(--navy);transform:scale(1.12)}
.sp b{display:block;font-family:Manrope;color:var(--navy);font-size:17px}.sp span{font-size:13.5px;color:var(--mut);display:block;margin-top:4px}
/* coverage */
.cov{display:grid;grid-template-columns:1.1fr .9fr;gap:70px;align-items:center}
.map{position:relative;aspect-ratio:1.1;background:var(--navy);border-radius:24px;overflow:hidden;box-shadow:0 40px 90px rgba(5,13,58,.25)}
.map:before{content:"";position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.22) 1.4px,transparent 1.6px);background-size:22px 22px;mask-image:radial-gradient(circle at 50% 50%,#000,transparent 75%)}
.pin{position:absolute;left:50%;top:48%;transform:translate(-50%,-50%)}.pin i{position:absolute;left:50%;top:50%;border:2px solid var(--gold);border-radius:50%;transform:translate(-50%,-50%);animation:rd 3.6s infinite;opacity:0}.pin i:nth-child(2){animation-delay:1.2s}.pin i:nth-child(3){animation-delay:2.4s}
@keyframes rd{0%{width:0;height:0;opacity:.9}100%{width:340px;height:340px;opacity:0}}
.pin b{position:relative;display:block;width:22px;height:22px;background:var(--gold);border-radius:50%;box-shadow:0 0 0 8px rgba(255,196,0,.25)}
.mc{position:absolute;left:24px;bottom:24px;right:24px;background:rgba(255,255,255,.96);border-radius:16px;padding:22px 24px;color:var(--navy);display:flex;justify-content:space-between;gap:16px;align-items:center;flex-wrap:wrap}.mc b{font-family:Manrope;font-size:18px;display:block}.mc span{font-size:13.5px;color:var(--mut)}
.covt ul{list-style:none;margin-top:26px;display:grid;gap:16px}.covt li{display:grid;grid-template-columns:44px 1fr;gap:16px}.covt li i{font-style:normal;width:44px;height:44px;border-radius:12px;background:var(--navy);color:var(--gold);display:grid;place-items:center}.covt li b{display:block;color:var(--navy);font-family:Manrope}.covt li span{font-size:14.5px;color:var(--mut)}
/* testimonials */
.tm{background:var(--navy);color:#fff;overflow:hidden}.tm:before{content:"“";position:absolute;left:4%;top:-40px;font:800 520px/1 Manrope;color:rgba(255,196,0,.07)}
.tm .wrap{position:relative;max-width:1000px;text-align:center}.tm .h2{color:#fff}.tm .h2 em{color:var(--gold);background:none}
.qs{position:relative;min-height:230px;margin-top:40px}.q{position:absolute;inset:0;opacity:0;visibility:hidden;transition:.7s var(--ease);transform:translateY(20px)}.q.on{opacity:1;visibility:visible;transform:none}
.q blockquote{font-family:Manrope;font-size:clamp(22px,3vw,36px);font-weight:700;line-height:1.3;letter-spacing:-.02em}.q .st{color:var(--gold);letter-spacing:6px;margin-bottom:18px;font-size:20px}.q cite{display:block;margin-top:22px;font-style:normal;color:var(--gold2);font-weight:700;font-size:14px;letter-spacing:.14em;text-transform:uppercase}
.qd{display:flex;gap:10px;justify-content:center;margin-top:30px}.qd button{width:34px;height:4px;border-radius:4px;background:rgba(255,255,255,.25);border:0;cursor:pointer;transition:.3s}.qd button.on{background:var(--gold);width:56px}
.rate{display:inline-flex;align-items:center;gap:14px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.14);border-radius:999px;padding:10px 22px;margin-bottom:22px;font-weight:700;font-size:14px}.rate b{font-family:'Barlow Condensed';font-size:26px;color:var(--gold)}
/* faq + careers */
.fq{display:grid;grid-template-columns:.8fr 1.2fr;gap:70px;align-items:start}.fq .sec-h{position:sticky;top:110px;margin:0}
details{border:1px solid var(--line);border-radius:14px;margin-bottom:12px;background:#fff;transition:.3s}details[open]{border-color:var(--gold);box-shadow:0 16px 40px rgba(5,13,58,.08)}
summary{cursor:pointer;font-weight:700;font-size:17px;color:var(--navy);list-style:none;display:flex;justify-content:space-between;gap:20px;padding:22px 26px;font-family:Manrope}summary::-webkit-details-marker{display:none}
summary:after{content:"+";width:32px;height:32px;border-radius:50%;background:var(--bg);display:grid;place-items:center;font-size:22px;flex:none;transition:.3s}details[open] summary:after{transform:rotate(45deg);background:var(--gold)}details p{color:var(--mut);padding:0 26px 24px}
.careers{background:linear-gradient(120deg,var(--navy),var(--navy3));color:#fff;border-radius:26px;padding:64px;display:grid;grid-template-columns:1.2fr .8fr;gap:50px;align-items:center;margin-top:100px;position:relative;overflow:hidden}.careers:before{content:"";position:absolute;right:-100px;top:-100px;width:360px;height:360px;border:50px solid rgba(255,196,0,.12);border-radius:50%}
.careers h3{font-size:clamp(30px,4vw,52px)}.careers h3 em{font-style:normal;color:var(--gold)}.careers p{color:#c9cef0;font-size:17px;margin:14px 0 26px}
.req{background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.16);border-radius:18px;padding:26px;position:relative}.req .row{display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px solid rgba(255,255,255,.12);font-size:14px;gap:12px}.req .row:last-child{border:0}.req .row b{text-align:right}
/* contact */
.contact{display:grid;grid-template-columns:.85fr 1.15fr;border-radius:26px;overflow:hidden;box-shadow:0 40px 100px rgba(5,13,58,.18)}
.contact .l{background:var(--navy);color:#fff;padding:56px;position:relative;overflow:hidden}.contact .l:before{content:"";position:absolute;left:-80px;bottom:-80px;width:300px;height:300px;border:40px solid rgba(255,196,0,.1);border-radius:50%}
.contact .l h3{font-size:clamp(30px,3.4vw,44px);margin-bottom:28px}.contact .l p{margin-bottom:22px;color:#c9cef0;position:relative}.contact .l p b{display:block;color:var(--gold);font-size:11.5px;letter-spacing:.2em;text-transform:uppercase;margin-bottom:4px}.contact .l a:hover{color:var(--gold)}
.contact form{padding:56px;background:#fff;display:grid;gap:14px;grid-template-columns:1fr 1fr}
.contact input,.contact select,.contact textarea{width:100%;padding:16px;border:1.5px solid var(--line);border-radius:12px;font:inherit;background:var(--bg);transition:.2s}.contact input:focus,.contact select:focus,.contact textarea:focus{outline:none;border-color:var(--navy3);background:#fff}
.full{grid-column:1/-1}.contact textarea{min-height:110px;resize:vertical}
.ctab{background:var(--gold);color:var(--navy);padding:60px 0}.ctab .wrap{display:flex;justify-content:space-between;align-items:center;gap:30px;flex-wrap:wrap}.ctab h2{font-size:clamp(30px,4vw,52px)}.ctab p{font-weight:600;margin-top:6px}.ctab .btn-g{background:var(--navy);color:#fff;box-shadow:none}.ctab .btn-g:hover{background:#fff;color:var(--navy)}.ctab .btn-o{border-color:var(--navy);color:var(--navy)}.ctab .btn-o:hover{background:var(--navy);color:#fff}.cta2{display:flex;gap:12px;flex-wrap:wrap}
footer{background:#030826;color:#aab0d6;padding:90px 0 0}.fg{display:grid;grid-template-columns:1.5fr 1fr 1fr 1.3fr;gap:50px;padding-bottom:64px}
footer h4{font-size:16px;color:#fff;letter-spacing:.02em;margin-bottom:20px}footer li{list-style:none;margin-bottom:11px;font-size:14.5px}footer a:hover{color:var(--gold)}
.fl{display:flex;gap:22px;flex-wrap:wrap}.fb{border-top:1px solid rgba(255,255,255,.1);padding:26px 0;display:flex;justify-content:space-between;font-size:13px;flex-wrap:wrap;gap:10px}
.wa{position:fixed;right:22px;bottom:22px;z-index:70;background:#25d366;color:#fff;width:58px;height:58px;border-radius:50%;display:grid;place-items:center;box-shadow:0 12px 30px rgba(0,0,0,.3);transition:.25s}.wa svg{width:30px;height:30px;fill:#fff}.wa:hover{transform:scale(1.1)}
.top{position:fixed;right:22px;bottom:92px;z-index:70;width:46px;height:46px;border-radius:50%;background:var(--navy);color:var(--gold);border:0;cursor:pointer;opacity:0;visibility:hidden;transition:.3s;font-size:18px;box-shadow:0 10px 26px rgba(0,0,0,.3)}.top.v{opacity:1;visibility:visible}
.mbar{display:none}
/* reveal */
.rv{opacity:0;transform:translateY(40px);transition:opacity 1s var(--ease),transform 1s var(--ease)}.rv.in{opacity:1;transform:none}
@media(prefers-reduced-motion:reduce){*,*:before,*:after{animation:none!important;transition-duration:.01ms!important}.rv{opacity:1;transform:none}html{scroll-behavior:auto}}

/* ===== enhancement pass ===== */
.skip{position:fixed;left:12px;top:-60px;background:var(--gold);color:var(--navy);padding:12px 18px;font-weight:700;z-index:300;border-radius:8px;transition:top .2s}.skip:focus{top:12px}
:focus-visible{outline:3px solid var(--gold);outline-offset:3px;border-radius:6px}
#pre{position:fixed;inset:0;background:var(--navy);z-index:400;display:grid;place-content:center;justify-items:center;gap:22px;transition:opacity .6s .1s,visibility .6s .1s;animation:preout .01s 2s forwards}
#pre img{height:96px;animation:pz 1.2s ease-in-out infinite}#pre i{width:140px;height:3px;background:rgba(255,255,255,.15);position:relative;overflow:hidden;border-radius:3px}#pre i:after{content:"";position:absolute;inset:0;background:var(--gold);transform:translateX(-100%);animation:ld 1.1s var(--ease) infinite}
@keyframes pz{50%{transform:scale(1.08)}}@keyframes ld{to{transform:translateX(100%)}}@keyframes preout{to{opacity:0;visibility:hidden}}
#pre.off{opacity:0;visibility:hidden}
#toast{position:fixed;left:50%;bottom:90px;transform:translate(-50%,30px);background:var(--navy);color:#fff;padding:14px 22px;border-radius:999px;font-weight:600;font-size:14px;z-index:300;opacity:0;visibility:hidden;transition:.4s var(--ease);box-shadow:0 18px 50px rgba(0,0,0,.35);border:1px solid rgba(255,196,0,.5);max-width:90vw;text-align:center}#toast.on{opacity:1;visibility:visible;transform:translate(-50%,0)}
.sidetab{position:fixed;right:0;top:50%;transform:translateY(-50%);z-index:65;writing-mode:vertical-rl;background:var(--gold);color:var(--navy);font-weight:800;font-size:12.5px;letter-spacing:.14em;text-transform:uppercase;padding:22px 11px;border-radius:12px 0 0 12px;box-shadow:-8px 10px 30px rgba(0,0,0,.25);transition:.3s}.sidetab:hover{padding-right:18px;background:#fff}
.hglow{position:absolute;z-index:1;width:520px;height:520px;border-radius:50%;background:radial-gradient(circle,rgba(255,196,0,.16),transparent 65%);left:0;top:0;pointer-events:none;transform:translate(-50%,-50%);opacity:0;transition:opacity .4s}.hx:hover .hglow{opacity:1}
nav>ul>li>a.act{color:var(--navy3)}
.h2 .w{display:inline-block;overflow:hidden;vertical-align:top;padding-bottom:.12em;margin-bottom:-.12em}.h2 .w>span{display:inline-block;transform:translateY(112%);transition:transform .9s var(--ease);transition-delay:calc(var(--i)*45ms)}.h2.in .w>span{transform:none}
.h2 em{background-size:0 100%;background-repeat:no-repeat;background-image:linear-gradient(rgba(255,196,0,.55),rgba(255,196,0,.55));background-position:0 92%;background-size:0% 38%;transition:background-size 1s var(--ease) .6s}.h2.in em{background-size:100% 38%}
.plan .h2 em,.tm .h2 em,.band h2 em{background-image:none}
.big sup{font-size:.5em;top:-.7em;color:var(--navy3)}
.btn{will-change:transform}
.ic,.pl{transform-style:preserve-3d;transition:transform .35s var(--ease),box-shadow .5s,border-color .3s}
.sec-h .eyebrow,.abt .eyebrow,.covt .eyebrow{position:relative}
section+section:not(.bg):not(.plan):not(.band):not(.tm){border-top:0}
.cur{display:none}
@media(max-width:1180px){.sidetab{display:none}}
@media(max-width:980px){#toast{bottom:150px}}
@media(prefers-reduced-motion:reduce){#pre{display:none}.h2 .w>span{transform:none}.h2 em{background-size:100% 38%}}

/* india map */
.map{aspect-ratio:auto!important;display:flex;flex-direction:column;padding:26px 26px 0;background:var(--navy);border-radius:24px;overflow:hidden;position:relative}
.map:before{-webkit-mask-image:none;mask-image:none;opacity:.5}
#imap{width:100%;height:auto;max-height:600px;position:relative;z-index:1;filter:drop-shadow(0 20px 40px rgba(0,0,0,.4))}
.st{fill:rgba(255,255,255,.1);stroke:rgba(255,255,255,.4);stroke-width:1.1;stroke-linejoin:round;cursor:pointer;transition:fill .25s,transform .25s;transform-box:fill-box;transform-origin:center}
.st:hover{fill:rgba(255,196,0,.55)}.st.hq{fill:rgba(255,196,0,.9);stroke:#fff}.st.sel:not(.hq){fill:rgba(255,196,0,.4);stroke:var(--gold)}
.pinG{pointer-events:none}.pd{fill:#fff;stroke:var(--navy);stroke-width:4}.rd{fill:none;stroke:var(--gold);stroke-width:3;transform-box:fill-box;transform-origin:center;animation:mrd 2.6s ease-out infinite}.rd.r2{animation-delay:1.3s}
@keyframes mrd{0%{transform:scale(.4);opacity:1}100%{transform:scale(4.2);opacity:0}}
.mtip{position:absolute;z-index:5;pointer-events:none;background:#fff;color:var(--navy);font-weight:700;font-size:13px;padding:8px 14px;border-radius:8px;box-shadow:0 12px 30px rgba(0,0,0,.35);opacity:0;transform:translate(-50%,-130%);transition:opacity .15s;white-space:nowrap}.mtip.on{opacity:1}
.map .mc{position:relative;left:auto;right:auto;bottom:auto;margin:0 -26px;border-radius:0;padding:22px 26px;z-index:2}
.mhint{position:absolute;top:18px;left:24px;z-index:3;font-size:11.5px;letter-spacing:.14em;text-transform:uppercase;color:rgba(255,255,255,.6);font-weight:700}
@media(max-width:980px){.map{padding:34px 16px 0}.map .mc{margin:0 -16px;padding:18px 16px}.mhint{left:16px;top:14px}}
.mcta{display:none}body.no .mbar,body.no .wa,body.no .sidetab,body.no .top{display:none}

html{scroll-padding-top:0}main section[id]{scroll-margin-top:-16px}.sx{scroll-margin-top:96px}
.ddt{display:none}
@media(max-width:1180px){
main section[id]{scroll-margin-top:28px}.sx{scroll-margin-top:84px}
.dd{display:flex;flex-wrap:wrap;align-items:stretch}.dd>a{flex:1}.dd .cv{display:none}
.ddt{display:block;width:60px;background:none;border:0;border-bottom:1px solid var(--line);cursor:pointer;position:relative}
.ddt:after{content:"";position:absolute;left:50%;top:50%;width:9px;height:9px;border:solid var(--navy);border-width:0 2px 2px 0;transform:translate(-50%,-70%) rotate(45deg);transition:.25s}.dd.o .ddt:after{transform:translate(-50%,-30%) rotate(-135deg)}
.dd .menu{width:100%;flex:0 0 100%}
}
@media(max-width:980px){
section{padding:60px 0}.tl{scroll-padding-left:20px}
}

@media(max-width:980px){
body .mbar{grid-template-columns:.8fr 1.2fr 1.2fr}body .mbar a{display:flex;align-items:center;justify-content:center;gap:8px;padding:15px 8px;font-size:13px}
.mbar .mw{background:#25d366;color:#fff}.mbar .mw svg{width:18px;height:18px;fill:#fff}.mbar a:last-child{background:var(--gold);color:var(--navy)}.mbar a:first-child{background:var(--navy);color:#fff}
.wa{display:none}
body .pl{display:block;padding:22px 20px}body .pl .big{font-size:46px;line-height:1}body .pl h3{margin:8px 0 6px;font-size:20px}body .pl p{font-size:14.5px}
.imgc img{aspect-ratio:16/11}.vals{grid-template-columns:repeat(3,1fr);gap:8px;margin:24px 0}.vals div{padding:14px 10px}.vals b{font-size:13.5px}.vals span{font-size:11.5px;line-height:1.35;display:block;margin-top:2px}
.abt p{font-size:16px}.pil{gap:12px}
}
/* ===== responsive ===== */
@media(max-width:1180px){
.util{display:none}.nav{height:68px}.brand img{height:44px}.brand b{font-size:19px}
nav{position:fixed;top:68px;left:0;right:0;bottom:0;background:#fff;transform:translateX(100%);transition:transform .35s var(--ease);overflow:auto;padding:10px 22px 120px;z-index:59}nav.open{transform:none}
nav>ul{flex-direction:column}nav>ul>li>a{padding:18px 2px;font-size:19px;border-bottom:1px solid var(--line);font-family:Manrope;font-weight:700}nav>ul>li>a:after{display:none}
.dd .menu{position:static;transform:none;width:auto;opacity:1;visibility:visible;box-shadow:none;border:0;display:none;grid-template-columns:1fr;background:var(--bg);border-radius:12px;margin:8px 0}.dd.o .menu{display:block}.mp{display:none}.mg{grid-template-columns:1fr;padding:8px}
.nav>.btn{display:none}.burger{display:block}nav>ul>li.mcta{display:flex;flex-direction:column;gap:12px;margin-top:26px}nav>ul>li.mcta a{padding:16px 24px;font:700 15px Inter;justify-content:center;border-bottom:0;font-family:Inter}nav>ul>li.mcta a.btn-g{color:var(--navy)}nav>ul>li.mcta a.btn-n{color:#fff}
.hx{height:calc(100svh - 68px);min-height:640px;max-height:900px}.scrollcue{display:none}
}
@media(max-width:980px){
section{padding:76px 0}.wrap{padding:0 20px}.sec-h{margin-bottom:38px}.sec-h p{font-size:16px}
.hxg,.hxg.one{grid-template-columns:1fr;align-items:start;align-content:start;padding-top:22px;padding-bottom:150px;gap:0}.hxg.one{padding-top:70px}
.hxg .tx{padding-bottom:10px}.hx h1,.hx .hh{font-size:clamp(40px,11.5vw,62px)}.hx .lead{font-size:16px;margin:16px 0 24px;display:-webkit-box;-webkit-line-clamp:4;-webkit-box-orient:vertical;overflow:hidden}.hx .eyebrow{font-size:10.5px;margin-bottom:12px}
.fig{order:-1;height:250px;margin:0 0 16px}.fig img{height:100%}.tagc{display:none}.halo{width:320px;height:320px}
.hx .cta .btn{padding:14px 18px;font-size:13px;flex:1;justify-content:center}
.hxc{padding-bottom:100px}.d{width:38px;font-size:0}.d span{display:none}.dots{gap:8px}.arrows{display:none}
.stats{margin-top:-84px}.stats .grid{grid-template-columns:repeat(2,1fr);border-radius:16px}.stat{padding:22px 10px}.stat b{font-size:44px}.stat:nth-child(2n){border-right:0}.stat:nth-child(-n+4){border-bottom:1px solid var(--line)}.stat:last-child{grid-column:1/-1}
.mq{margin-top:56px;padding:16px 0}.mt span{font-size:15px}
.two,.plan .wrap,.cov,.fq,.contact,.careers{grid-template-columns:1fr;gap:40px}.imgc:before{display:none}.imgc .bd{left:14px;bottom:14px;padding:14px 20px}.bd b{font-size:38px}
.vals{grid-template-columns:1fr}
.sx{grid-template-columns:1fr;border:0;box-shadow:none;background:none;border-radius:0;overflow:visible}
.tl{flex-direction:row;overflow-x:auto;scroll-snap-type:x proximity;margin:0 -20px;padding:0 20px 4px;gap:8px;background:none;scrollbar-width:none}.tl::-webkit-scrollbar{display:none}
.tb{grid-template-columns:auto auto;gap:8px;background:#fff;color:var(--navy);border:1px solid var(--line);border-radius:999px;padding:12px 18px;white-space:nowrap;font-size:14px;scroll-snap-align:start;flex:none}
.tb .ti svg{width:18px;height:18px;stroke:var(--navy)}.tb .ar,.tb:before{display:none}.tb.on{background:var(--navy);color:#fff}.tb.on .ti svg{stroke:var(--gold)}.tb:hover{background:#fff;color:var(--navy)}.tb.on:hover{background:var(--navy);color:#fff}
.pw{min-height:0;margin-top:14px;background:#fff;border-radius:20px;overflow:hidden;box-shadow:0 20px 50px rgba(5,13,58,.12);border:1px solid var(--line)}
.pn{position:relative;display:none;grid-template-columns:1fr;opacity:1;visibility:visible;transform:none}.pn.on{display:grid}.pm{height:230px}.pm.cut{height:270px}.pb{padding:24px 22px 28px}.num{font-size:52px}.pb h3{font-size:30px}.pb p{font-size:15px}.pb .btn{width:100%;justify-content:center}
.wz{padding:24px 20px;border-radius:18px}.chips{grid-template-columns:1fr}
.ind{grid-template-columns:1fr 1fr;gap:12px}.ic{aspect-ratio:3/4;padding:18px;border-radius:16px}.ic h3{font-size:22px}.ic span{font-size:12px}.ic .go{display:none}.ic .n{top:16px;left:18px}
.band{padding:90px 0;background-attachment:scroll}
.pil,.steps{grid-template-columns:1fr}.pl{padding:28px 24px}.pl .big{font-size:64px}
.steps:before{left:27px;right:auto;top:0;bottom:0;width:2px;height:auto;background:repeating-linear-gradient(var(--navy3) 0 6px,transparent 6px 12px)}.sp{text-align:left;display:grid;grid-template-columns:56px 1fr;gap:18px;align-items:center}.sp i{margin:0}.proc{margin-top:64px}
.map{aspect-ratio:1}.qs{min-height:330px}.tm:before{font-size:280px}
.fq .sec-h{position:static}.careers{padding:32px 22px;margin-top:64px;border-radius:20px}
.contact .l,.contact form{padding:30px 22px}.contact form{grid-template-columns:1fr}.contact input,.contact select,.contact textarea{font-size:16px}
.ctab{padding:44px 0}.cta2,.cta2 .btn{width:100%}.cta2 .btn{justify-content:center}
.fg{grid-template-columns:1fr 1fr;gap:34px}.fb{flex-direction:column}
.mbar{display:grid;grid-template-columns:1fr 1fr;position:fixed;left:0;right:0;bottom:0;z-index:80;box-shadow:0 -8px 30px rgba(0,0,0,.25);padding-bottom:env(safe-area-inset-bottom);background:var(--gold)}
.mbar a{padding:16px;text-align:center;font-weight:800;font-size:14px;letter-spacing:.05em;text-transform:uppercase}.mbar a:first-child{background:var(--navy);color:#fff}.mbar a:last-child{color:var(--navy)}
.wa{bottom:78px;right:14px;width:46px;height:46px;opacity:.95}.wa svg{width:24px;height:24px}.top{display:none}body{padding-bottom:54px}
}
@media(max-width:480px){.fg{grid-template-columns:1fr}.ind{gap:10px}.ic{padding:14px}.brand small{letter-spacing:.14em;font-size:8.5px}}

.mfoot{display:none}
/* ===== MOBILE POLISH (final, wins the cascade) ===== */
@media(max-width:980px){
html{-webkit-tap-highlight-color:transparent}
body{font-size:15.5px;line-height:1.6}
.nav{height:60px}.brand img{height:38px;width:38px}.brand b{font-size:17px;letter-spacing:.05em}.brand small{font-size:8px;letter-spacing:.16em}
.burger{width:46px;height:46px}
nav{top:60px;padding:6px 22px 130px}
nav>ul{counter-reset:n}
nav>ul>li:not(.mcta):not(.mfoot)>a{font-size:21px;padding:19px 2px;display:flex;align-items:center}
nav>ul>li:not(.mcta):not(.mfoot)>a:before{counter-increment:n;content:"0" counter(n);font:700 11px Inter;letter-spacing:.14em;color:#9aa0c4;margin-right:16px;min-width:22px}
.dd>a{flex:1}.ddt{height:auto}
nav>ul>li.mfoot{display:grid;gap:4px;margin-top:28px;padding-top:22px;border-top:1px solid var(--line);font-size:13.5px;color:var(--mut)}nav>ul>li.mfoot b{color:var(--navy);font-family:Manrope;font-size:15px}nav>ul>li.mfoot a{color:var(--navy3);font-weight:600;padding:0;font-size:14px;font-family:Inter;border:0;display:inline}
.hx{height:calc(100svh - 60px);min-height:620px}
.hx .hh,.hx h1{letter-spacing:-.03em}
/* stats: 3 + 2 */
body .stats{margin-top:-70px}body .stats .grid{grid-template-columns:repeat(6,1fr);border-radius:18px}
body .stat{grid-column:span 2;padding:20px 4px;border:0;border-right:1px solid var(--line);border-bottom:1px solid var(--line)}
body .stat:nth-child(3),body .stat:nth-child(5){border-right:0}body .stat:nth-child(4),body .stat:nth-child(5){grid-column:span 3;border-bottom:0}body .stat:last-child{grid-column:span 3}
body .stat b{font-size:34px}body .stat span{font-size:9.5px;letter-spacing:.09em;line-height:1.3;display:block;margin-top:4px}
/* rhythm */
section{padding:56px 0}.wrap{padding:0 20px}
.sec-h{margin-bottom:28px}.sec-h p{font-size:15.5px;margin-top:12px}
.eyebrow{font-size:10.5px;letter-spacing:.2em;margin-bottom:14px}.eyebrow:before{width:26px}
.h2{font-size:clamp(28px,8.2vw,36px);line-height:1.08}
.btn{min-height:50px;padding:14px 24px}
.mq{margin-top:44px}
.abt p{font-size:15.5px}
.imgc .im{border-radius:18px}
.pw,.wz,.map,.contact,.careers,.req,.pl,details{border-radius:18px}
.ic{border-radius:18px}
.tm .h2{font-size:clamp(26px,7.6vw,32px)}.rate{font-size:12.5px;padding:8px 16px}.q blockquote{font-size:21px}.qs{min-height:270px}
summary{font-size:15.5px;padding:18px 18px}details p{padding:0 18px 20px;font-size:15px}
.contact .l h3{font-size:30px}.contact input,.contact select,.contact textarea{min-height:52px;font-size:16px;border-radius:12px}
.contact .l p{margin-bottom:18px}
.mc b{font-size:17px}
/* footer */
body .fg{grid-template-columns:1fr 1fr;gap:28px 20px;padding-bottom:36px}.fg>div:first-child,.fg>div:last-child{grid-column:1/-1}
footer{padding-top:56px}footer h4{margin-bottom:14px}footer li{margin-bottom:9px}
.fb{align-items:center;text-align:center}.fl{justify-content:center}
.ctab h2{font-size:28px}
/* motion */
.rv{transform:translateY(22px);transition-duration:.7s}
/* header on scroll gets slightly compact */
header.sh .nav{height:56px}header.sh nav{top:56px}
}
@media(max-width:480px){body .fg{grid-template-columns:1fr 1fr}}

/* ===== CLARITY PASS: calm, editorial, SIS-level readability (last, wins) ===== */
body{color:#1c2140;font-size:17px;line-height:1.7}
h1,h2,h3,h4{font-weight:700}
.h2{font-size:clamp(30px,3.5vw,46px);font-weight:700;letter-spacing:-.025em;line-height:1.12;color:var(--navy)}
.h2 em,.h2.in em{background:none!important;color:#a87c00}
.band h2 em,.contact .h2 em{color:var(--gold)}
.h2 .w>span{transform:none!important;transition:none!important}
.sec-h{max-width:820px;margin-bottom:48px}.sec-h p{font-size:19px;color:#4a5070}
.eyebrow{font-size:12px;font-weight:700}
.btn{border-radius:6px;letter-spacing:.03em}
.pw,.wz,.map,.contact,.careers,.req,.pl,details,.ic,.imgc .im,.stats .grid,.vals div,.sx{border-radius:10px}
.imgc:before{border-radius:10px}
.rv{transform:translateY(14px);transition:opacity .8s var(--ease),transform .8s var(--ease)}
.mq{display:none}
/* statement */
.lead-s{padding:96px 0 24px}.ls{font-size:clamp(22px,2.5vw,33px);line-height:1.5;font-weight:500;letter-spacing:-.012em;color:#1c2140;max-width:1040px}.ls b{color:var(--navy3);font-weight:700}
.kn{display:inline-block;margin-top:26px;font-weight:700;color:var(--navy);border-bottom:2px solid var(--gold);padding-bottom:3px;transition:.2s}.kn:hover{color:#a87c00}
/* flat stats bar directly under banner */
.stats{margin-top:0;background:#fff;border-bottom:1px solid var(--line)}.stats .grid{box-shadow:none;border-top:0;border-radius:0;max-width:none}
.stats .wrap{padding:0 28px}.stat{padding:34px 20px}.stat b{font-weight:700;font-size:54px}
.hxc{padding-bottom:36px}.hxg,.hxg.one{padding-bottom:96px}
/* light planner + testimonials (fewer dark blocks) */
.plan{background:var(--bg)}.plan:before{display:none}.plan .h2{color:var(--navy)}.plan .h2 em{color:#a87c00}.plan p.s{color:#4a5070}.plan li{color:#1c2140}.plan .eyebrow{color:var(--navy3)}.plan .eyebrow:before{background:var(--gold)}
.wz{border:1px solid var(--line);box-shadow:0 12px 40px rgba(5,13,58,.07)}
.tm{background:#fff;color:var(--navy)}.tm:before{color:rgba(5,13,58,.045)}.tm .h2{color:var(--navy)}.tm .h2 em{color:#a87c00}.tm .rate{background:var(--bg);border-color:var(--line);color:var(--navy)}.q cite{color:#a87c00}.qd button{background:#d7dbee}.qd button.on{background:var(--gold)}.q .st{color:#e0a800}
/* services explorer: light list */
.sx{box-shadow:0 12px 40px rgba(5,13,58,.07)}
@media(min-width:981px){
.tl{background:#fff;border-right:1px solid var(--line)}.tb{color:#4a5070;border-bottom:1px solid var(--line)}.tb .ti svg{stroke:var(--navy3)}.tb:hover,.tb.on{background:var(--bg);color:var(--navy)}.tb .ar{color:var(--navy)}
section{padding:96px 0}
}
.sx .pb h3{font-weight:700}.num{font-weight:700}
.pl{box-shadow:none}.pl:hover{box-shadow:0 14px 40px rgba(5,13,58,.08)}
.band{padding:130px 0}
header{box-shadow:0 1px 0 var(--line)}
@media(max-width:980px){
.lead-s{padding:56px 0 8px}.ls{font-size:20px;line-height:1.5}
body .stats{margin-top:0}body .stats .grid{border-radius:0}.stats .wrap{padding:0}
body .stat{padding:18px 4px}body .stat b{font-size:32px}
.hxc{padding-bottom:26px}.hx .hxg,.hx .hxg.one{padding-bottom:100px}
.sec-h p{font-size:16px}.h2{font-size:clamp(27px,7.8vw,34px)}
}

/* ===== MOBILE FINAL: smaller imagery, tighter rhythm ===== */
@media(max-width:980px){
.hx{height:600px!important;min-height:0!important;max-height:none!important}
.hx .hxg,.hx .hxg.one{padding-top:226px!important;padding-bottom:84px!important}
.ph{height:206px!important}.fig{height:206px!important;top:10px!important}.halo{width:240px!important;height:240px!important}
.hx h1,.hx .hh{font-size:clamp(30px,8.6vw,38px)!important}.hx .lead{font-size:15px!important;-webkit-line-clamp:3!important;margin:10px 0 16px!important}
.hx .cta .btn{min-height:46px!important;padding:12px 14px!important;font-size:12.5px!important}
.hxc{padding-bottom:22px!important}
.imgc img{aspect-ratio:16/9!important}.imgc .bd{padding:10px 14px!important;left:10px!important;bottom:10px!important}.bd b{font-size:28px!important}.bd span{font-size:10px!important}
.vals{grid-template-columns:repeat(3,1fr)!important;gap:8px!important}.vals div{padding:12px 8px!important}.vals b{font-size:12.5px!important}.vals span{font-size:10.5px!important}
.pm{height:150px!important}.pm.cut{height:190px!important}.pb{padding:20px 18px 22px!important}.num{font-size:40px!important}.pb h3{font-size:26px!important;margin:6px 0!important}.pb ul{margin:14px 0 18px!important;gap:8px!important}
.ic{aspect-ratio:1/1!important}.ic h3{font-size:19px!important}.ic span:not(.n):not(.go){font-size:11px!important}
.chips{grid-template-columns:1fr 1fr!important;gap:8px!important}.chp span{padding:12px 10px!important;font-size:12.5px!important;gap:8px!important}.chp svg{width:16px!important;height:16px!important}
.wz h3{font-size:21px!important}
.band{padding:60px 0!important}.band h2{font-size:28px!important}.band p{font-size:15px!important}
#imap{max-height:300px!important}.map{padding-top:30px!important}
section{padding:48px 0!important}.lead-s{padding:44px 0 4px!important}
.pl{padding:18px!important}.sec-h{margin-bottom:22px!important}
.ctab{padding:34px 0!important}
}

/* ===== SMOOTH MOTION SYSTEM (last) ===== */
html.lenis,html.lenis body{height:auto}.lenis.lenis-smooth{scroll-behavior:auto!important}
html.lenis{scroll-behavior:auto}
header{transition:transform .5s var(--ease),box-shadow .3s}header.hide{transform:translateY(-102%)}
.rv{opacity:0;transform:translateY(26px);transition:opacity 1s var(--ease),transform 1s var(--ease);transition-delay:var(--d,0ms)}.rv.in{opacity:1;transform:none}
.imgc.rv{opacity:1;transform:none}
.imgc .im{clip-path:inset(0 0 100% 0);transition:clip-path 1.4s var(--ease)}.imgc.in .im{clip-path:inset(0 0 0 0)}
.imgc.in img{transform:scale(1)}.imgc .bd{opacity:0;transform:translateY(20px);transition:all .9s var(--ease) .9s}.imgc.in .bd{opacity:1;transform:none}
.rv .eyebrow:before{width:0;transition:width 1s var(--ease) .25s}.rv.in .eyebrow:before{width:36px}
.ic,.pl,.card,.vals div,.tb,.chp span,details,.btn,.st{transition-timing-function:cubic-bezier(.22,.8,.24,1)}
.ic{transition:transform .6s cubic-bezier(.22,.8,.24,1),box-shadow .6s}.ic:before{transition:transform 1.1s cubic-bezier(.22,.8,.24,1)}
.pm img{transition:transform 1.2s cubic-bezier(.22,.8,.24,1)}.pn.on .pm img{animation:kb 9s ease-out both}@keyframes kb{from{transform:scale(1.08)}to{transform:scale(1)}}
.pn{transition:opacity .6s var(--ease),transform .7s var(--ease),visibility .6s}
.pb>*{opacity:0;transform:translateY(14px);transition:opacity .6s var(--ease),transform .6s var(--ease)}.pn.on .pb>*{opacity:1;transform:none}.pn.on .pb>*:nth-child(1){transition-delay:.15s}.pn.on .pb>*:nth-child(2){transition-delay:.22s}.pn.on .pb>*:nth-child(3){transition-delay:.29s}.pn.on .pb>*:nth-child(4){transition-delay:.36s}.pn.on .pb>*:nth-child(5){transition-delay:.43s}
.btn{transition:transform .4s cubic-bezier(.22,.8,.24,1),background .3s,color .3s,box-shadow .4s}.btn:hover{transform:translateY(-2px)}.btn:active{transform:translateY(0) scale(.98)}
.kn:after{content:" →";display:inline-block;transition:transform .35s var(--ease)}.kn:hover:after{transform:translateX(5px)}
nav>ul>li>a:after{transition:transform .5s var(--ease)}
.map .st{transition:fill .35s ease}
.q{transition:opacity .9s var(--ease),transform .9s var(--ease),visibility .9s}
details{transition:border-color .4s,box-shadow .4s,background .4s}details p{animation:dd .5s var(--ease)}@keyframes dd{from{opacity:0;transform:translateY(-6px)}}
.stat b{transition:color .3s}.stat:hover b{color:var(--navy3)}
.slide{transition:opacity 1.3s cubic-bezier(.4,0,.2,1),visibility 1.3s}
.hx .lead,.hx .cta,.hx .eyebrow{transition:opacity 1s var(--ease) .4s,transform 1s var(--ease) .4s}
@media(max-width:980px){.rv{transform:translateY(18px);transition-duration:.8s}.imgc .im{clip-path:inset(0 0 100% 0)}.rv .eyebrow:before{width:0}.rv.in .eyebrow:before{width:26px}header.hide{transform:none}}
@media(prefers-reduced-motion:reduce){.rv,.imgc .im,.pb>*{opacity:1!important;transform:none!important;clip-path:none!important}header.hide{transform:none}}

/* about photo: fixed frame so the picture can never blow up */
.imgc .im{position:relative;aspect-ratio:4/3.4;height:auto}
.imgc .im img{position:absolute;inset:0;width:100%;height:100%!important;aspect-ratio:auto!important;object-fit:cover;object-position:50% 30%}
@media(max-width:980px){.imgc .im{aspect-ratio:16/9!important;max-height:220px}.imgc .im img{object-position:50% 22%}}

/* ===== hero guard: framed portrait so no limb is ever cut ===== */
.hx .fig{position:absolute!important;top:0!important;bottom:0!important;margin-block:auto!important;right:max(28px,calc((100% - 1280px)/2 + 28px))!important;left:auto!important;width:min(580px,41vw)!important;height:fit-content!important;aspect-ratio:800/620;display:block!important;border-radius:14px;overflow:hidden;transform:none!important;background:radial-gradient(circle at 50% 38%,rgba(255,196,0,.42),transparent 62%),linear-gradient(160deg,#0e1d78,#050d3a);border:1px solid rgba(255,255,255,.16);box-shadow:0 40px 90px rgba(0,0,0,.45);z-index:2}
.hx .fig img{position:static!important;display:block;width:100%!important;height:100%!important;max-height:none!important;object-fit:cover;object-position:50% 0;-webkit-mask-image:none!important;mask-image:none!important;filter:none!important}
.hx .halo{display:none!important}
@media(max-width:980px){
.hx{height:650px!important}
.hx .fig{top:0!important;bottom:auto!important;margin:0!important;left:0!important;right:0!important;width:100%!important;height:250px!important;aspect-ratio:auto;border-radius:0;border:0;box-shadow:none}
.hx .fig{-webkit-mask-image:linear-gradient(#000 74%,transparent);mask-image:linear-gradient(#000 74%,transparent)}
.ph{height:250px!important}
.hx .hxg,.hx .hxg.one{padding-top:274px!important}
}

/* ===== service photos: keep faces in frame ===== */
.pm img{object-position:50% 6%!important}
.pm.cut img{object-fit:contain!important;object-position:50% 50%!important;width:100%!important;height:auto!important;position:relative;z-index:2;align-self:center}
.pm.cut{align-items:center!important}
@media(max-width:980px){
.pm{height:210px!important}.pm.cut{height:210px!important}
.pm.cut img{object-fit:cover!important;object-position:50% 0!important;height:100%!important}
.pm img{object-position:50% 4%!important}
}

/* ===== extras ===== */
.dir{display:inline-block;margin-top:6px;color:var(--gold);font-weight:700;border-bottom:2px solid rgba(255,196,0,.5);padding-bottom:2px;position:relative}.contact .l .dir:hover{color:#fff}
.rail{position:fixed;left:18px;top:50%;transform:translateY(-50%);z-index:55;display:none;flex-direction:column;gap:14px}
.rail a{position:relative;width:10px;height:10px;border-radius:50%;background:rgba(5,13,58,.22);transition:.3s;display:block}
.rail a:after{content:attr(data-l);position:absolute;left:22px;top:50%;transform:translateY(-50%) translateX(-6px);background:var(--navy);color:#fff;font:600 11.5px Inter;padding:5px 10px;border-radius:5px;white-space:nowrap;opacity:0;pointer-events:none;transition:.25s}
.rail a:hover:after{opacity:1;transform:translateY(-50%)}.rail a.on{background:var(--gold);transform:scale(1.5);box-shadow:0 0 0 4px rgba(255,196,0,.25)}
.rail.dark a{background:rgba(255,255,255,.4)}
@media(min-width:1360px){.rail{display:flex}}
.stat span,.d,.vals span{font-size:max(11.5px,1em)}
body .stat span{font-size:11.5px}.d{font-size:11.5px}

/* ===== mobile banner v2: full bleed photos like SIS, text on a gradient ===== */
.phm{display:none}
@media(max-width:980px){
.hx{height:calc(100svh - 60px)!important;min-height:600px!important;max-height:720px!important}
.phm{display:block}
.hx .fig{display:none!important}
.hx .ph{top:0!important;bottom:0!important;height:100%!important;width:100%!important;right:0!important;-webkit-mask-image:none!important;mask-image:none!important;background-position:50% 8%!important;transform:none!important}
.hx .slide:nth-child(3) .ph{background-position:62% 10%!important}
.hx .ph:after{background:linear-gradient(180deg,rgba(5,13,58,.10) 0%,rgba(5,13,58,.18) 30%,rgba(5,13,58,.78) 58%,#050d3a 80%)!important}
.hx .hxg,.hx .hxg.one{align-items:flex-end!important;padding-top:0!important;padding-bottom:78px!important}
.hx .hxg .tx{padding-bottom:0!important;align-self:flex-end!important}
.hx .slide>.hxg{height:100%!important}
.hx .lead{-webkit-line-clamp:3!important}
.hxc{padding-bottom:26px!important}
}
/* footer logo: never distorted */
footer .brand img{width:auto!important;height:60px!important;aspect-ratio:1/1;object-fit:contain}
@media(max-width:980px){
footer .brand{gap:14px}footer .brand b{font-size:20px!important}footer .brand small{font-size:9px!important}
.fg>div:first-child p{max-width:none!important}
}

/* ===== enterprise motion 2 ===== */
#journey{background:#fff}
.jr{position:relative;padding-top:34px}
.jl{position:absolute;left:0;right:0;top:9px;height:2px;background:#dfe3f1}.jl i{position:absolute;inset:0;background:linear-gradient(90deg,var(--gold),#e0a800);transform-origin:left;transform:scaleX(0)}
.jn{display:grid;grid-template-columns:repeat(5,1fr);gap:26px}
.jm{position:relative}.jm .dot{position:absolute;left:0;top:-34px;width:20px;height:20px;border-radius:50%;background:#fff;border:2px solid #cfd4e8;transition:.5s var(--ease)}
.jm.on .dot{background:var(--gold);border-color:var(--gold);box-shadow:0 0 0 7px rgba(255,196,0,.25)}
.jm small{display:block;font:700 12px Inter;letter-spacing:.16em;text-transform:uppercase;color:#7a80a0;margin-bottom:8px}
.jm>b,.jm .ring b{display:block;font-family:'Barlow Condensed';font-weight:700;color:var(--navy);line-height:1}
.jm>b{font-size:54px;font-family:Manrope;font-size:24px;letter-spacing:-.02em}
.jm .jv{font-family:'Barlow Condensed'!important;font-size:64px!important;letter-spacing:0!important}
.jm .jv em{font-style:normal}.jm .jv sup{color:#a87c00;font-size:.5em;top:-.7em}
.jm p{color:#4a5070;font-size:15px;margin-top:10px;line-height:1.55}
.jm:not(.on){opacity:.45}.jm{transition:opacity .6s var(--ease)}
.ring{position:relative;width:104px;height:104px}.ring svg{width:100%;height:100%;transform:rotate(-90deg)}
.ring circle{fill:none;stroke-width:9}.ring .rb{stroke:#e4e7f3}.ring .rf{stroke:var(--gold);stroke-linecap:round;stroke-dasharray:327;stroke-dashoffset:327;transition:stroke-dashoffset 1.8s var(--ease) .2s}
.jm.on .ring .rf{stroke-dashoffset:calc(327 * .02)}
.jm .ring b{position:absolute;inset:0;display:grid;place-items:center;font-size:36px}.ring b em{font-style:normal}
/* process line that draws */
.steps .fl{position:absolute;top:27px;left:5%;width:90%;height:2px;background:var(--gold);transform-origin:left;transform:scaleX(0)}
.sp i{transition:.5s var(--ease)}.sp.on i{background:var(--gold);color:var(--navy);transform:scale(1.08)}.sp:not(.on){opacity:.55}.sp{transition:opacity .5s var(--ease)}
/* services autoplay progress */
.sx.auto .tb.on:after{content:"";position:absolute;left:0;bottom:0;height:3px;background:var(--gold);animation:tabp 5.5s linear forwards}
@keyframes tabp{from{width:0}to{width:100%}}
/* spotlight on cards and stats */
.stat,.vals div,.covt li{background-image:radial-gradient(260px circle at var(--mx,-200px) var(--my,-200px),rgba(255,196,0,.16),transparent 70%)}
/* angled section edges */
@media(min-width:981px){#services,#why,#contact{clip-path:polygon(0 0,100% 34px,100% 100%,0 100%);padding-top:130px}}
@media(max-width:980px){#services,#why,#contact{clip-path:polygon(0 0,100% 16px,100% 100%,0 100%);padding-top:64px!important}}
@media(max-width:980px){
.jl{left:9px;right:auto;top:0;bottom:0;width:2px;height:auto}.jl i{transform-origin:top;transform:scaleY(0)}
.jr{padding-top:0;padding-left:0}.jn{grid-template-columns:1fr;gap:34px;padding-left:40px}
.jm .dot{left:-40px;top:2px}.jm .jv{font-size:52px!important}.jm p{font-size:14.5px}.jm:not(.on){opacity:.55}
.steps .fl{left:26px;top:0;width:2px;height:100%;transform-origin:top;transform:scaleY(0)}
}
@media(prefers-reduced-motion:reduce){.jm:not(.on),.sp:not(.on){opacity:1}}

/* ===== stats on mobile: clean 2x2 + full width row, uniform dividers ===== */
@media(max-width:980px){
body .stats .grid{display:grid!important;grid-template-columns:1fr 1fr!important;gap:1px!important;background:var(--line)!important;border:0!important;border-radius:0!important}
body .stat{grid-column:auto!important;background:#fff!important;border:0!important;padding:24px 10px 20px!important;display:flex!important;flex-direction:column;align-items:center;justify-content:flex-start;text-align:center}
body .stat b{font-size:42px!important;line-height:1}
body .stat span{font-size:11.5px!important;letter-spacing:.11em!important;line-height:1.35;margin-top:8px!important;min-height:2.7em;display:block}
body .stat:last-child{grid-column:1/-1!important;flex-direction:row;justify-content:center;align-items:center;gap:16px;padding:18px 10px!important}
body .stat:last-child span{margin:0!important;min-height:0}
body .stat:last-child b{font-size:38px!important}
.stats{border-top:3px solid var(--gold)}
}
/* section numbers: editorial structure while scrolling */
.eyebrow .no{font:700 12px Inter;color:#a87c00;letter-spacing:.12em;margin-right:2px}
.plan .eyebrow .no{color:#a87c00}
.fl .by{color:var(--gold);font-weight:700;border-bottom:1px solid rgba(255,196,0,.5);transition:.25s}.fl .by:hover{color:#fff;border-color:#fff}

/* ===== opening sequence, scroll cue, planner prompt ===== */
@keyframes hdrIn{from{transform:translateY(-100%);opacity:0}}
@keyframes fadeIn{from{opacity:0}}
@keyframes hxIn{from{opacity:0;transform:scale(1.035)}}
@keyframes upIn{from{opacity:0;transform:translateY(26px)}}




.cue{position:absolute;left:50%;bottom:20px;width:24px;height:38px;border:2px solid rgba(255,255,255,.5);border-radius:14px;transform:translateX(-50%);z-index:6;animation:fadeIn 1s ease 1.6s backwards;transition:border-color .3s}
.cue:hover{border-color:var(--gold)}.cue i{position:absolute;left:50%;top:7px;width:3px;height:8px;margin-left:-1.5px;border-radius:2px;background:var(--gold);animation:cue 1.9s cubic-bezier(.4,0,.2,1) infinite}
@keyframes cue{0%{transform:translateY(0);opacity:1}70%{transform:translateY(14px);opacity:0}100%{opacity:0}}
#nudge{position:fixed;left:24px;bottom:24px;z-index:75;width:300px;background:#fff;border:1px solid var(--line);border-left:4px solid var(--gold);border-radius:12px;padding:18px 20px;box-shadow:0 24px 60px rgba(5,13,58,.22);display:grid;gap:6px;transform:translateY(30px);opacity:0;visibility:hidden;transition:all .7s cubic-bezier(.16,1,.3,1)}
#nudge.on{transform:none;opacity:1;visibility:visible}
#nudge b{font:700 16px Manrope;color:var(--navy)}#nudge span{font-size:14px;color:#4a5070}#nudge .btn{margin-top:8px;justify-self:start;padding:11px 20px;min-height:0}
#nudge .x{position:absolute;right:8px;top:4px;background:none;border:0;font-size:24px;line-height:1;color:#7a80a0;cursor:pointer;padding:6px}
@media(max-width:980px){.cue{display:none}#nudge{left:12px;right:12px;width:auto;bottom:70px}}
body.no #nudge{display:none}
@media(prefers-reduced-motion:reduce){.util,header,.hx,.stats,.cue{animation:none}}

/* ===== security intro ===== */
#intro{position:fixed;inset:0;z-index:1000;display:none;place-items:center;cursor:pointer}
html.intro{overflow:hidden}html.intro #intro{display:grid;animation:introFail .01s 6s forwards}@keyframes introFail{to{opacity:0;visibility:hidden}}
#intro .ip{position:absolute;left:0;right:0;height:50.4%;background:#050d3a;transition:transform 1s cubic-bezier(.76,0,.24,1)}#intro .ipt{top:0}#intro .ipb{bottom:0}
#intro .igrid{position:absolute;inset:0;background:radial-gradient(600px 400px at 50% 45%,rgba(255,196,0,.14),transparent 70%),linear-gradient(rgba(255,255,255,.045) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.045) 1px,transparent 1px);background-size:auto,56px 56px,56px 56px;mask-image:radial-gradient(circle at 50% 45%,#000,transparent 75%);transition:opacity .5s}
#intro{transition:opacity .9s cubic-bezier(.4,0,.2,1),visibility 0s linear .9s}#intro.open{opacity:0;visibility:hidden;pointer-events:none}#intro.open .ic2,#intro.open .it{transform:scale(1.08);transition:transform .9s cubic-bezier(.4,0,.2,1)}
#intro .ic2{position:relative;width:150px;height:150px;margin-top:-70px;z-index:2}
#intro .shd{position:absolute;left:-14px;top:-16px;width:calc(100% + 28px);height:calc(100% + 34px);overflow:visible}
#intro .shd path{fill:none;stroke:#ffc400;stroke-width:1.4;stroke-dasharray:340;stroke-dashoffset:340;animation:idraw 1.15s cubic-bezier(.65,0,.35,1) .15s forwards;filter:drop-shadow(0 0 6px rgba(255,196,0,.6))}
#intro .lg{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;opacity:0;transform:scale(.86);animation:ilg .9s cubic-bezier(.16,1,.3,1) .8s forwards}
#intro .scan{position:absolute;left:-14px;right:-14px;top:0;height:2px;background:linear-gradient(90deg,transparent,#ffc400,transparent);box-shadow:0 0 20px 5px rgba(255,196,0,.55);opacity:0;animation:iscan 1.1s ease-in-out 1.2s forwards}
@keyframes idraw{to{stroke-dashoffset:0}}@keyframes ilg{to{opacity:1;transform:none}}@keyframes iscan{0%{top:-4%;opacity:1}90%{opacity:1}100%{top:104%;opacity:0}}
#intro .it{position:absolute;left:0;right:0;top:calc(50% + 62px);text-align:center;color:#fff;z-index:2}
#intro .it b{display:block;font:800 30px Manrope;letter-spacing:.34em;padding-left:.34em;opacity:0;animation:itx .9s cubic-bezier(.16,1,.3,1) 1.15s forwards}
#intro .it span{display:block;font:600 11px Inter;letter-spacing:.3em;color:#aab0d6;margin-top:8px;opacity:0;animation:itx .9s cubic-bezier(.16,1,.3,1) 1.35s forwards}
#intro .it em{display:block;font:500 14px Inter;font-style:normal;color:#ffc400;margin-top:18px;opacity:0;animation:itx .9s cubic-bezier(.16,1,.3,1) 1.65s forwards}
@keyframes itx{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}
#intro .ibar{position:absolute;left:50%;bottom:11%;width:190px;height:2px;background:rgba(255,255,255,.16);transform:translateX(-50%);z-index:2}
#intro .ibar i{position:absolute;inset:0;background:#ffc400;transform-origin:left;transform:scaleX(0);animation:ibar 2.2s cubic-bezier(.4,0,.2,1) forwards}@keyframes ibar{to{transform:scaleX(1)}}
#intro .skip2{position:absolute;right:22px;bottom:22px;z-index:3;background:none;border:1px solid rgba(255,255,255,.3);color:#fff;font:600 11.5px Inter;letter-spacing:.16em;text-transform:uppercase;padding:9px 16px;border-radius:999px;cursor:pointer;opacity:.75;transition:.25s}#intro .skip2:hover{opacity:1;border-color:#ffc400;color:#ffc400}
@media(max-width:600px){#intro .ic2{width:120px;height:120px}#intro .it{top:calc(50% + 46px)}#intro .it b{font-size:23px}#intro .it span{font-size:9.5px}}
/* armed panel: portrait fills the whole frame */
.pm.cut{align-items:stretch!important}
.pm.cut img{position:absolute!important;inset:0;width:100%!important;height:100%!important;object-fit:cover!important;object-position:28% 0!important}
@media(max-width:980px){.pm.cut img{object-position:50% 0!important}}

/* ===== inner pages ===== */
.lk{display:inline-block;margin:14px 0 0 4px;font-weight:700;color:var(--navy);border-bottom:2px solid var(--gold);padding-bottom:2px;align-self:flex-start}.lk:hover{color:#a87c00}
.pb .btn+.lk{margin-left:0}
.pbn{position:relative;background:#050d3a;color:#fff;overflow:hidden;padding:92px 0 80px}
.pbn:before{content:"";position:absolute;inset:0;background:radial-gradient(700px 420px at 88% 15%,rgba(255,196,0,.18),transparent 60%),radial-gradient(600px 500px at 0 110%,rgba(40,60,220,.5),transparent 60%),linear-gradient(135deg,#030826,#0a1660 65%,#050d3a)}
.pbn:after{content:"";position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.04) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.04) 1px,transparent 1px);background-size:60px 60px;mask-image:radial-gradient(circle at 75% 40%,#000,transparent 70%)}
.pbn .pbg{position:absolute;top:0;bottom:0;right:0;width:50%;background:var(--bg) var(--pos,60% 20%)/cover;-webkit-mask-image:linear-gradient(90deg,transparent,#000 48%);mask-image:linear-gradient(90deg,transparent,#000 48%);z-index:1;opacity:.92;transition:transform 8s linear;transform:scale(1.06);transform-origin:right center}.pbn.in .pbg{transform:scale(1)}
.pbn .pbi{position:relative;z-index:3}
.bc{display:flex;flex-wrap:wrap;gap:10px;font-size:13px;color:#aab0d6;margin-bottom:24px}.bc a{transition:.2s}.bc a:hover{color:var(--gold)}.bc b{color:#fff;font-weight:600}.bc span{opacity:.5}
.pbn h1{font-size:clamp(34px,4.6vw,60px);letter-spacing:-.03em;line-height:1.06;max-width:740px;font-weight:700}.pbn h1 em{font-style:normal;color:var(--gold)}
.pbn .lead{color:#c9cef0;font-size:19px;max-width:600px;margin:20px 0 30px}
.pbn .cta{display:flex;gap:12px;flex-wrap:wrap}
.pbn .pm2{display:flex;gap:10px;flex-wrap:wrap;margin-top:28px}.pm2 span{font-size:12.5px;font-weight:600;border:1px solid rgba(255,255,255,.22);padding:7px 14px;border-radius:999px;color:#dfe3ff;background:rgba(255,255,255,.05)}
.pbn .bc,.pbn h1,.pbn .lead,.pbn .cta,.pbn .pm2{animation:pbin .9s var(--ease) both}
.pbn h1{animation-delay:.08s}.pbn .lead{animation-delay:.16s}.pbn .cta{animation-delay:.24s}.pbn .pm2{animation-delay:.32s}
@keyframes pbin{from{opacity:0;transform:translateY(18px)}to{opacity:1;transform:none}}
.subnav{position:sticky;top:80px;z-index:50;background:rgba(255,255,255,.97);border-bottom:1px solid var(--line);transition:top .5s var(--ease)}
.subnav .wrap{display:flex;align-items:center;justify-content:space-between;gap:16px;height:58px}
.subnav .snv{display:flex;gap:4px;overflow-x:auto;scrollbar-width:none}.subnav .snv::-webkit-scrollbar{display:none}
.subnav .snv a{padding:8px 14px;font-weight:600;font-size:14px;color:#4a5070;border-radius:6px;white-space:nowrap;transition:.2s}.subnav .snv a:hover,.subnav .snv a.on{color:var(--navy);background:var(--bg)}
body:has(header.hide) .subnav{top:0}
.btn.sm{padding:10px 18px;min-height:0;font-size:13px}
.blk{padding:88px 0;position:relative}.blk.alt{background:var(--bg)}.blk[id]{scroll-margin-top:-8px}
.sp2{display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:center}.sp2.rev .sp2t{order:2}
.sp2t p{color:#4a5070;font-size:18px;margin-top:16px}.sp2t p+p{font-size:16.5px}
.sp2i{position:relative;border-radius:12px;overflow:hidden;aspect-ratio:4/3;box-shadow:0 24px 60px rgba(5,13,58,.18);background:var(--navy)}.sp2i img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 12%;transition:transform 1.4s var(--ease)}.sp2i:hover img{transform:scale(1.05)}
.sp2i .badge{position:absolute;left:0;bottom:0;background:var(--gold);color:var(--navy);padding:12px 18px;font:800 13px Inter;letter-spacing:.06em;text-transform:uppercase}
.fc{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}.fc.c2{grid-template-columns:repeat(2,1fr)}.fc.c4{grid-template-columns:repeat(4,1fr)}
.fcard{background:#fff;border:1px solid var(--line);border-radius:12px;padding:30px 26px;transition:transform .5s var(--ease),box-shadow .5s,border-color .3s}
.fcard:hover{transform:translateY(-6px);box-shadow:0 20px 50px rgba(5,13,58,.1);border-color:var(--gold)}
.fcard .ico{width:52px;height:52px;background:var(--navy);color:var(--gold);display:grid;place-items:center;border-radius:12px;margin-bottom:18px}.fcard .ico svg{width:26px;height:26px;stroke:currentColor;fill:none;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.fcard .no2{font:800 46px/1 'Barlow Condensed';color:var(--gold);margin-bottom:10px;display:block}
.fcard h3{font-size:20px;color:var(--navy);margin-bottom:8px;letter-spacing:-.02em}.fcard p{color:#4a5070;font-size:15.5px}
.ticks{list-style:none;display:grid;gap:12px;margin-top:20px}.ticks li{display:flex;gap:12px;font-weight:600;color:var(--navy);line-height:1.5}.ticks li:before{content:"✓";background:var(--gold);width:22px;height:22px;border-radius:50%;display:grid;place-items:center;font-size:12px;flex:none;margin-top:2px}
.ticks.two{grid-template-columns:1fr 1fr;gap:12px 30px}
.rel{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.rcard{display:block;background:#fff;border:1px solid var(--line);border-radius:12px;overflow:hidden;transition:transform .5s var(--ease),box-shadow .5s}.rcard:hover{transform:translateY(-6px);box-shadow:0 20px 50px rgba(5,13,58,.12)}
.rcard .rt{aspect-ratio:16/10;overflow:hidden;background:var(--navy)}.rcard img{width:100%;height:100%;object-fit:cover;object-position:50% 10%;transition:transform 1s var(--ease)}.rcard:hover img{transform:scale(1.06)}
.rcard .rb{padding:18px}.rcard b{display:block;font-family:Manrope;color:var(--navy);font-size:17px;letter-spacing:-.01em}.rcard span{color:#4a5070;font-size:14px;display:block;margin-top:4px}.rcard em{font-style:normal;color:#a87c00;font-weight:700;font-size:13px;display:inline-block;margin-top:10px}
.cta2b{background:linear-gradient(120deg,var(--navy),var(--navy3));color:#fff;border-radius:14px;padding:56px;display:flex;justify-content:space-between;align-items:center;gap:30px;flex-wrap:wrap;position:relative;overflow:hidden}
.cta2b:before{content:"";position:absolute;right:-90px;top:-90px;width:320px;height:320px;border:46px solid rgba(255,196,0,.12);border-radius:50%}
.cta2b>*{position:relative}.cta2b h2{font-size:clamp(26px,3.2vw,40px);max-width:640px}.cta2b p{color:#c9cef0;margin-top:8px;max-width:560px}.cta2b .cta{display:flex;gap:12px;flex-wrap:wrap}
.nums{display:grid;grid-template-columns:repeat(4,1fr);border:1px solid var(--line);border-radius:12px;background:#fff;overflow:hidden}.nums div{padding:30px 20px;text-align:center;border-right:1px solid var(--line)}.nums div:last-child{border:0}.nums b{display:block;font:700 54px/1 'Barlow Condensed';color:var(--navy)}.nums b sup{color:#a87c00;font-size:.5em;top:-.7em}.nums span{font-size:11.5px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#6a7090;display:block;margin-top:6px}
.cc{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}.ccd{background:#fff;border:1px solid var(--line);border-radius:12px;padding:30px 26px;transition:.5s var(--ease)}.ccd:hover{border-color:var(--gold);box-shadow:0 18px 44px rgba(5,13,58,.09);transform:translateY(-4px)}
.ccd .ico{width:48px;height:48px;background:var(--navy);color:var(--gold);display:grid;place-items:center;border-radius:12px;margin-bottom:16px}.ccd .ico svg{width:24px;height:24px;stroke:currentColor;fill:none;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.ccd h3{font-size:18px;color:var(--navy);margin-bottom:6px}.ccd p,.ccd a{color:#4a5070;font-size:15.5px;display:block}.ccd a:hover{color:var(--navy3)}
.frm{background:#fff;border:1px solid var(--line);border-radius:12px;padding:36px;display:grid;gap:14px;grid-template-columns:1fr 1fr;box-shadow:0 14px 44px rgba(5,13,58,.07)}
.frm label{font-size:13px;font-weight:700;color:var(--navy);display:block;margin-bottom:6px}.frm .f{display:block}.frm .full{grid-column:1/-1}
.frm input,.frm select,.frm textarea{width:100%;padding:14px 16px;border:1.5px solid var(--line);border-radius:10px;font:inherit;background:var(--bg);transition:.2s}.frm input:focus,.frm select:focus,.frm textarea:focus{outline:none;border-color:var(--navy3);background:#fff}.frm textarea{min-height:120px;resize:vertical}
.mapf{border:0;width:100%;height:100%;min-height:420px;border-radius:12px;filter:saturate(.9)}
.fchips{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:20px}.fchips button{border:1px solid var(--line);background:#fff;padding:9px 16px;border-radius:999px;font:600 14px Inter;cursor:pointer;transition:.25s;color:var(--navy)}.fchips button.on,.fchips button:hover{background:var(--navy);color:#fff;border-color:var(--navy)}
.fsearch{position:relative;margin-bottom:18px}.fsearch input{width:100%;padding:15px 18px;border:1.5px solid var(--line);border-radius:10px;font:inherit;background:#fff}.fsearch input:focus{outline:none;border-color:var(--navy3)}
.fnone{display:none;padding:26px;text-align:center;color:#6a7090;border:1px dashed var(--line);border-radius:12px}
.narrow{max-width:860px;margin:0 auto}
.plan-wrap{max-width:720px;margin:0 auto}
.subhd{display:flex;justify-content:space-between;align-items:end;gap:20px;flex-wrap:wrap;margin-bottom:34px}.subhd .sec-h{margin:0}.subhd a.kn{margin:0}
@media(max-width:1180px){.subnav{top:56px}}
@media(max-width:980px){
.pbn{padding:44px 0 40px}.pbn .pbg{width:100%;opacity:.28;-webkit-mask-image:linear-gradient(180deg,#000,transparent);mask-image:linear-gradient(180deg,#000,transparent)}
.pbn h1{font-size:clamp(28px,8vw,34px)}.pbn .lead{font-size:15.5px;margin:14px 0 22px}.bc{margin-bottom:16px;font-size:12px}.pm2{margin-top:18px}.pm2 span{font-size:11.5px;padding:6px 11px}
.subnav .wrap{height:50px}.subnav .btn{display:none}.subnav .snv a{padding:7px 11px;font-size:13px}
.blk{padding:44px 0}.sp2{grid-template-columns:1fr;gap:26px}.sp2.rev .sp2t{order:0}.sp2t p{font-size:15.5px}.sp2i{aspect-ratio:16/10}
.fc,.fc.c2,.fc.c4{grid-template-columns:1fr;gap:12px}.fcard{padding:20px 18px}.fcard h3{font-size:18px}.fcard p{font-size:14.5px}.fcard .ico{width:44px;height:44px;margin-bottom:12px}
.ticks.two{grid-template-columns:1fr}.rel{grid-template-columns:1fr 1fr;gap:10px}.rcard .rb{padding:12px}.rcard b{font-size:14.5px}.rcard span{display:none}
.cta2b{padding:28px 20px}.cta2b .cta,.cta2b .cta .btn{width:100%}.cta2b .cta .btn{justify-content:center}
.nums{grid-template-columns:1fr 1fr}.nums div{padding:20px 8px;border-bottom:1px solid var(--line)}.nums div:nth-child(2n){border-right:0}.nums div:nth-last-child(-n+2){border-bottom:0}.nums b{font-size:40px}
.cc{grid-template-columns:1fr}.frm{grid-template-columns:1fr;padding:20px 16px}.mapf{min-height:300px}
}
/* ===== compact phone scale: less zoomed, more refined ===== */
@media(max-width:980px){
html{-webkit-text-size-adjust:100%}
body{font-size:15px!important;line-height:1.55}
.wrap{padding:0 18px!important}
.nav{height:56px!important}nav{top:56px!important}.brand img{height:34px!important;width:34px!important}.brand b{font-size:15.5px!important}.brand small{font-size:7.5px!important}
.burger{width:42px;height:42px}
.h2{font-size:clamp(24px,6.9vw,29px)!important;line-height:1.12}
.sec-h p{font-size:15px!important}.eyebrow{font-size:10px!important;letter-spacing:.18em!important}
.btn{min-height:44px!important;padding:11px 20px!important;font-size:13px!important}
section{padding:42px 0!important}.lead-s{padding:34px 0 4px!important}.ls{font-size:17.5px!important}
.hx{min-height:540px!important;max-height:640px!important}
.hx h1,.hx .hh{font-size:clamp(28px,8vw,34px)!important}.hx .lead{font-size:14px!important;margin:8px 0 14px!important}
.hx .cta .btn{min-height:42px!important;font-size:12px!important}
.hx .eyebrow{font-size:9.5px!important}
body .stat b{font-size:34px!important}body .stat span{font-size:10.5px!important}body .stat{padding:18px 8px 14px!important}
.abt p{font-size:15px!important}.vals b{font-size:12px!important}
.pb h3{font-size:22px!important}.pb p{font-size:14px!important}.num{font-size:34px!important}.pb li{font-size:13.5px}
.tb{font-size:13px!important;padding:10px 14px!important}
.jm .jv{font-size:42px!important}.jm p{font-size:13.5px!important}.jm>b{font-size:19px}
.pl .big{font-size:38px!important}body .pl h3{font-size:17px!important}body .pl p{font-size:13.5px!important}
.q blockquote{font-size:18px!important}
summary{font-size:14.5px!important;padding:15px 16px!important}details p{font-size:14px!important}
.contact .l h3{font-size:26px!important}
.ctab h2{font-size:24px!important}footer{font-size:14px}footer li{font-size:13.5px}
.mbar a{font-size:12px!important;padding:13px 6px!important}
body{padding-bottom:46px!important}
}

/* ===== inner pages v2: richer components ===== */
.tbar{background:#fff;border-bottom:1px solid var(--line)}.tbar .wrap{display:grid;grid-template-columns:repeat(4,1fr)}
.tbi{display:flex;align-items:center;gap:14px;padding:20px 18px;border-right:1px solid var(--line)}.tbi:first-child{padding-left:0}.tbi:last-child{border:0}
.tbi i{width:42px;height:42px;border-radius:10px;background:var(--bg);display:grid;place-items:center;flex:none;transition:.4s}.tbi:hover i{background:var(--navy)}.tbi:hover svg{stroke:var(--gold)}
.tbi svg{width:22px;height:22px;stroke:var(--navy3);fill:none;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round;transition:.4s}
.tbi b{display:block;font-family:Manrope;color:var(--navy);font-size:15px;line-height:1.2}.tbi span{font-size:12.5px;color:#6a7090}
.glance{position:absolute;right:max(28px,calc((100% - 1280px)/2 + 28px));bottom:34px;z-index:4;background:rgba(255,255,255,.97);border-radius:14px;box-shadow:0 30px 70px rgba(0,0,0,.35);padding:20px 26px;display:grid;grid-template-columns:repeat(3,auto);gap:30px}
.glance div b{display:block;font:700 32px/1 'Barlow Condensed';color:var(--navy)}.glance div span{font-size:10.5px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#6a7090}
.svl{display:grid;grid-template-columns:minmax(0,1fr) 360px;gap:56px;align-items:start}
.svm>.blk{padding:64px 0 0}.svm>.blk:first-child{padding-top:56px}.svm .sec-h{margin-bottom:28px}.svm .sec-h p{font-size:17px}
.svm .fc{grid-template-columns:1fr 1fr}.svm .sp2{grid-template-columns:1fr;gap:26px}
.svm .steps{grid-template-columns:repeat(5,1fr)}
.sva{position:sticky;top:150px;padding-top:56px}
.qc{background:#fff;border:1px solid var(--line);border-top:4px solid var(--gold);border-radius:12px;padding:26px;box-shadow:0 24px 64px rgba(5,13,58,.12)}
.qc h3{font-size:21px;color:var(--navy);margin-bottom:6px;letter-spacing:-.02em}.qc p.s{color:#4a5070;font-size:14.5px;margin-bottom:16px}
.qc input{width:100%;padding:13px 14px;border:1.5px solid var(--line);border-radius:10px;font:inherit;margin-bottom:10px;background:var(--bg)}.qc input:focus{outline:none;border-color:var(--navy3);background:#fff}
.qc .btn{width:100%;justify-content:center}
.qc .ln{display:flex;gap:12px;align-items:center;padding:13px 0;border-top:1px solid var(--line);color:var(--navy);font-weight:600;font-size:14.5px}.qc .ln:first-of-type{margin-top:18px}.qc .ln svg{width:18px;height:18px;stroke:var(--navy3);fill:none;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round;flex:none}.qc .ln:hover{color:#a87c00}
.qc .fine{font-size:12px;color:#7a80a0;margin-top:8px}
.tiles{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.tile{display:flex;gap:12px;align-items:center;background:#fff;border:1px solid var(--line);border-radius:10px;padding:15px 16px;font-weight:600;color:var(--navy);font-size:14.5px;transition:.4s var(--ease);line-height:1.35}.tile:hover{border-color:var(--gold);transform:translateY(-3px);box-shadow:0 12px 30px rgba(5,13,58,.08)}.tile:before{content:"";width:9px;height:9px;border-radius:50%;background:var(--gold);flex:none;box-shadow:0 0 0 4px rgba(255,196,0,.22)}
.cov24{background:#fff;border:1px solid var(--line);border-radius:12px;padding:26px}
.ctabs{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:22px}.ctabs button{border:1px solid var(--line);background:#fff;padding:10px 18px;border-radius:999px;font:600 14px Inter;cursor:pointer;color:var(--navy);transition:.3s}.ctabs button.on,.ctabs button:hover{background:var(--navy);color:#fff;border-color:var(--navy)}
.bar24{display:grid;grid-template-columns:repeat(24,1fr);gap:3px}.bar24 span{height:52px;border-radius:5px;background:#e7eaf5;transition:background .6s var(--ease),transform .6s var(--ease);position:relative}.bar24 span.on{background:linear-gradient(180deg,#ffd84d,#e0a800);transform:translateY(-4px)}
.lab24{display:grid;grid-template-columns:repeat(4,1fr);font-size:11.5px;font-weight:700;color:#6a7090;margin-top:10px}
#cap24{margin-top:16px;color:#4a5070;font-size:15.5px;min-height:3.2em}
.xp{background:var(--navy);color:#fff;position:relative;overflow:hidden}
.xp:before{content:"";position:absolute;inset:0;background:radial-gradient(700px 400px at 90% 0,rgba(255,196,0,.16),transparent 60%),linear-gradient(rgba(255,255,255,.04) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.04) 1px,transparent 1px);background-size:auto,56px 56px,56px 56px;mask-image:linear-gradient(#000,transparent 90%)}
.xp>.wrap{position:relative}.xp .h2{color:#fff}.xp .h2 em{color:var(--gold);background:none!important}.xp .sec-h p{color:#c9cef0}.xp .eyebrow.dk{color:var(--gold)}.xp .eyebrow .no{color:var(--gold)}
.xpg{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.14);border-radius:12px;overflow:hidden}
.xpc{background:#0a1470;padding:30px 26px;transition:.4s}.xpc:hover{background:#0e1d78}.xpc .k{font:800 44px/1 'Barlow Condensed';color:var(--gold);display:block;margin-bottom:12px}.xpc b{display:block;font-family:Manrope;font-size:18px;margin-bottom:8px;letter-spacing:-.01em}.xpc p{color:#c9cef0;font-size:14.5px}
.xpn{display:grid;grid-template-columns:repeat(4,1fr);margin-top:34px;gap:20px}.xpn div{text-align:center}.xpn b{display:block;font:700 56px/1 'Barlow Condensed'}.xpn b sup{color:var(--gold);font-size:.5em;top:-.7em}.xpn span{font-size:11.5px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#aab0d6}
.paths{display:grid;grid-template-columns:repeat(6,1fr);gap:14px}
.pth{display:flex;flex-direction:column;align-items:center;text-align:center;gap:10px;background:#fff;border:1px solid var(--line);border-radius:12px;padding:24px 10px 20px;transition:.5s var(--ease);font-weight:700;color:var(--navy);font-family:Manrope;font-size:15px;line-height:1.25}
.pth i{width:58px;height:58px;border-radius:14px;background:var(--navy);display:grid;place-items:center;color:var(--gold);transition:.5s var(--ease)}.pth svg{width:28px;height:28px;stroke:currentColor;fill:none;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}
.pth span{font:500 12.5px Inter;color:#6a7090}.pth:hover{transform:translateY(-6px);box-shadow:0 20px 44px rgba(5,13,58,.12);border-color:var(--gold)}.pth:hover i{background:var(--gold);color:var(--navy);transform:rotate(-6deg) scale(1.06)}
.mos{display:grid;grid-template-columns:2fr 1fr 1fr;grid-template-rows:210px 210px;gap:14px}.mos div{border-radius:12px;overflow:hidden;position:relative;background:var(--navy)}.mos img{width:100%;height:100%;object-fit:cover;transition:transform 1.2s var(--ease)}.mos div:hover img{transform:scale(1.06)}.mos .big{grid-row:1/3}.mos div:after{content:"";position:absolute;inset:0;background:linear-gradient(transparent 45%,rgba(5,13,58,.7))}.mos b{position:absolute;left:16px;bottom:14px;color:#fff;z-index:2;font-family:Manrope;font-size:15px}
.drop{border:2px dashed #c4cbe4;border-radius:12px;padding:22px;text-align:center;background:var(--bg);cursor:pointer;transition:.3s;position:relative}.drop:hover,.drop.dr{border-color:var(--gold);background:#fffbe8}
.drop input{position:absolute;inset:0;opacity:0;cursor:pointer;width:100%;height:100%}.drop svg{width:30px;height:30px;stroke:var(--navy3);fill:none;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round;margin-bottom:6px}.drop b{display:block;color:var(--navy);font-family:Manrope;font-size:15px}.drop span{font-size:12.5px;color:#6a7090}
.fileok{display:none;align-items:center;justify-content:space-between;gap:10px;background:#f0f9f2;border:1px solid #bfe3c8;border-radius:10px;padding:12px 14px;font-size:14px;font-weight:600;color:#1f6b35}.fileok.on{display:flex}.fileok button{background:none;border:0;color:#8a2a1c;font-weight:700;cursor:pointer;font-size:13px}
.cvst{display:none;padding:12px 14px;border-radius:10px;font-size:14px;line-height:1.5}.cvst a{color:var(--navy3);font-weight:700;text-decoration:underline}.cvst.err{display:block;background:#fff2f0;border:1px solid #f3c1ba;color:#8a2a1c}.cvst.ok{display:block;background:#f0f9f2;border:1px solid #bfe3c8;color:#1f6b35}.cvst.wait{display:block;background:var(--bg);color:var(--navy)}
.hp{position:absolute;left:-9999px;opacity:0;height:0;width:0}
@media(max-width:1100px){.glance{display:none}.svl{grid-template-columns:1fr;gap:0}.sva{position:static;padding:40px 0 0}.svm .steps{grid-template-columns:1fr}.paths{grid-template-columns:repeat(3,1fr)}.xpg{grid-template-columns:1fr 1fr}}
@media(max-width:980px){
.tbar .wrap{grid-template-columns:1fr 1fr}.tbi{padding:14px 12px;border-bottom:1px solid var(--line)}.tbi:nth-child(2n){border-right:0}.tbi:nth-child(-n+2){border-bottom:1px solid var(--line)}.tbi:last-child,.tbi:nth-last-child(2){border-bottom:0}.tbi:first-child{padding-left:12px}.tbi i{width:36px;height:36px}.tbi b{font-size:13px}.tbi span{display:none}
.svm>.blk{padding:40px 0 0}.svm>.blk:first-child{padding-top:34px}.svm .fc{grid-template-columns:1fr}.tiles{grid-template-columns:1fr 1fr;gap:8px}.tile{padding:12px;font-size:13px}
.cov24{padding:18px 14px}.bar24 span{height:38px}.ctabs button{padding:8px 13px;font-size:13px}#cap24{font-size:14px}
.xpg{grid-template-columns:1fr}.xpc{padding:20px 18px}.xpc .k{font-size:34px;margin-bottom:6px}.xpn{grid-template-columns:1fr 1fr;gap:18px}.xpn b{font-size:40px}
.paths{grid-template-columns:1fr 1fr;gap:10px}.pth{padding:16px 8px 14px;font-size:13.5px}.pth i{width:46px;height:46px}.pth svg{width:23px;height:23px}
.mos{grid-template-columns:1fr 1fr;grid-template-rows:150px 150px 150px;gap:10px}.mos .big{grid-column:1/3;grid-row:1}
.sva{padding-top:30px}.qc{padding:20px 16px}
}

/* ===== device matrix: small phones, tablets, large screens ===== */
@media(max-width:380px){
.wrap{padding:0 14px!important}
.brand small{display:none!important}.brand b{font-size:14.5px!important}.brand img{height:30px!important;width:30px!important}
.hx{min-height:520px!important}.hx h1,.hx .hh{font-size:25px!important}.hx .lead{font-size:13px!important}
.hx .cta{gap:8px}.hx .cta .btn{padding:9px 10px!important;font-size:11px!important;min-height:40px!important}
.h2{font-size:22px!important}.pbn h1{font-size:25px!important}.pbn .lead{font-size:14px!important}
body .stat b{font-size:28px!important}body .stat span{font-size:9.5px!important;letter-spacing:.06em!important}
.mbar a{font-size:10.5px!important;gap:5px!important}.mbar .mw svg{width:15px!important;height:15px!important}
.subnav .snv a{padding:6px 9px!important;font-size:12px!important}
.tbi b{font-size:12px!important}.paths{gap:8px}.pth{font-size:12.5px!important;padding:12px 6px!important}
.btn{padding:10px 16px!important;font-size:12.5px!important}
.cta2b h2{font-size:22px!important}.ls{font-size:16px!important}
}
@media(min-width:600px) and (max-width:980px){
.fc,.fc.c4{grid-template-columns:1fr 1fr!important}.svm .fc{grid-template-columns:1fr 1fr!important}
.tiles{grid-template-columns:repeat(3,1fr)!important}.paths{grid-template-columns:repeat(3,1fr)!important}
.rel{grid-template-columns:repeat(2,1fr)!important}.rcard span{display:block!important}
.xpg{grid-template-columns:1fr 1fr!important}.tbar .wrap{grid-template-columns:repeat(4,1fr)!important}.tbi span{display:none}.tbi{flex-direction:column;text-align:center;gap:8px;border-bottom:0!important;padding:14px 6px!important}.tbi:nth-child(2n){border-right:1px solid var(--line)!important}.tbi:last-child{border:0!important}
.nums{grid-template-columns:repeat(4,1fr)!important}.nums div{border-bottom:0!important}
.cc{grid-template-columns:repeat(3,1fr)!important}
.pbn h1{font-size:40px!important}.pbn .lead{font-size:17px!important}.h2{font-size:32px!important}
.hx{max-height:760px!important}.hx h1,.hx .hh{font-size:44px!important}.hx .lead{font-size:16px!important;max-width:520px}
.wrap{padding:0 28px!important}
body{font-size:16px!important}
.ind{grid-template-columns:repeat(4,1fr)!important}.ic{aspect-ratio:3/4!important}
.mos{grid-template-columns:2fr 1fr 1fr!important;grid-template-rows:170px 170px!important}.mos .big{grid-column:auto!important;grid-row:1/3!important}
}
@media(min-width:1600px){
.wrap{max-width:1440px}.hx{max-height:980px}.hx h1,.hx .hh{font-size:84px}.pbn h1{font-size:68px}.pbn .lead{font-size:21px}.h2{font-size:52px}
.sec-h{max-width:900px}.sva{top:160px}
}
@media(min-width:2200px){.wrap{max-width:1680px}html{font-size:110%}}

html{overflow-x:clip}body{overflow-x:clip}

/* ===== 3D and picture motion ===== */
[data-tilt]{transform-style:preserve-3d;will-change:transform;transition:transform .45s cubic-bezier(.22,.8,.24,1),box-shadow .45s}
[data-tilt].tilting{transition:transform .1s linear,box-shadow .45s}
.glare{position:absolute;inset:0;pointer-events:none;z-index:6;border-radius:inherit;background:radial-gradient(360px circle at var(--gx,50%) var(--gy,50%),rgba(255,255,255,.26),transparent 60%);opacity:0;transition:opacity .35s}
[data-tilt]:hover .glare{opacity:1}
.sp2i img,.mos img{scale:1.14;translate:0 var(--py,0px)}
.pbn .pbg{top:-32px;bottom:-32px;translate:0 var(--py,0px)}
.orbs{position:absolute;inset:0;pointer-events:none;z-index:1;overflow:hidden}
.orbs i{position:absolute;border-radius:50%;transition:translate .3s ease-out}
.orbs .o1{width:520px;height:520px;right:6%;top:6%;border:1px solid rgba(255,196,0,.26);translate:calc(var(--mx,0)*-46px) calc(var(--my,0)*-34px)}
.orbs .o1:after{content:"";position:absolute;inset:44px;border-radius:50%;border:1px dashed rgba(255,255,255,.14);animation:spin 40s linear infinite}
.orbs .o2{width:340px;height:340px;right:22%;bottom:-6%;background:radial-gradient(circle,rgba(255,196,0,.22),transparent 65%);translate:calc(var(--mx,0)*70px) calc(var(--my,0)*50px)}
.orbs .o3{width:14px;height:14px;right:30%;top:22%;background:var(--gold);box-shadow:0 0 0 8px rgba(255,196,0,.18),0 0 40px 10px rgba(255,196,0,.35);translate:calc(var(--mx,0)*-90px) calc(var(--my,0)*-70px)}
.floor,.pbn .floor{position:absolute;left:-25%;right:-25%;bottom:-2px;height:46%;perspective:420px;z-index:1;pointer-events:none;-webkit-mask-image:linear-gradient(transparent,#000 75%);mask-image:linear-gradient(transparent,#000 75%)}
.floor:before{content:"";position:absolute;inset:0;background-image:linear-gradient(rgba(255,196,0,.26) 1px,transparent 1px),linear-gradient(90deg,rgba(255,196,0,.26) 1px,transparent 1px);background-size:64px 64px;transform:rotateX(64deg);transform-origin:50% 100%;animation:floorm 4s linear infinite}
@keyframes floorm{to{background-position:0 64px}}
.hx .ph{translate:calc(var(--mx,0)*-14px) calc(var(--my,0)*-10px);transition:transform 8s linear,translate .4s ease-out}
.emb3d{display:none;width:170px;height:170px;perspective:900px;flex:none;margin:-18px 10px;filter:drop-shadow(0 22px 22px rgba(5,13,58,.38));animation:embf 5s ease-in-out infinite}
@keyframes embf{50%{transform:translateY(-8px)}}
.emb-in{position:relative;width:100%;height:100%;transform-style:preserve-3d;transform:rotateY(calc(var(--ex,0)*36deg)) rotateX(calc(var(--ey,0)*-24deg));transition:transform .25s ease-out}
.emb-sw{position:absolute;inset:0;transform-style:preserve-3d;animation:sway 9s ease-in-out infinite}
.emb-sw img{position:absolute;inset:0;width:100%;height:100%;object-fit:contain}
@keyframes sway{0%,100%{transform:rotateY(-32deg) rotateX(5deg)}50%{transform:rotateY(32deg) rotateX(-3deg)}}
.cta2b .emb3d{display:none}
@media(min-width:1000px){.emb3d{display:block}}
@media(max-width:980px){.orbs .o1{width:300px;height:300px;right:-80px;top:3%}.orbs .o2,.orbs .o3{display:none}.floor{height:30%}}
@media(prefers-reduced-motion:reduce){.floor:before,.emb3d,.emb-sw,.orbs .o1:after{animation:none!important}}

/* ===== art panels: distinct graphics instead of repeated photos ===== */
.art{position:relative;overflow:hidden;background:linear-gradient(145deg,#0a1660,#050d3a);isolation:isolate}
.art:before{content:"";position:absolute;inset:0;z-index:-1}
.art.m1:before{background:radial-gradient(circle at 72% 28%,rgba(255,196,0,.3),transparent 55%),repeating-linear-gradient(45deg,rgba(255,255,255,.055) 0 2px,transparent 2px 20px)}
.art.m2:before{background:radial-gradient(circle at 28% 72%,rgba(60,110,255,.55),transparent 58%),linear-gradient(rgba(255,255,255,.055) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.055) 1px,transparent 1px);background-size:auto,34px 34px,34px 34px}
.art.m3:before{background:conic-gradient(from 210deg at 62% 46%,rgba(255,196,0,.26),transparent 38%,rgba(90,130,255,.32),transparent 78%)}
.art.m4:before{background:radial-gradient(circle at 18% 22%,rgba(255,196,0,.28),transparent 52%),radial-gradient(rgba(255,255,255,.16) 1.4px,transparent 1.6px) 0 0/22px 22px}
.art.m5:before{background:repeating-radial-gradient(circle at 70% 42%,rgba(255,255,255,.075) 0 2px,transparent 2px 28px),radial-gradient(circle at 70% 42%,rgba(255,196,0,.22),transparent 45%)}
.art.m6:before{background:linear-gradient(125deg,rgba(255,196,0,.2),transparent 42%),repeating-linear-gradient(90deg,rgba(255,255,255,.055) 0 1px,transparent 1px 30px)}
.art.m7:before{background:radial-gradient(circle at 80% 80%,rgba(60,110,255,.5),transparent 55%),repeating-linear-gradient(135deg,rgba(255,196,0,.09) 0 2px,transparent 2px 22px)}
.art.m8:before{background:radial-gradient(circle at 30% 30%,rgba(255,196,0,.25),transparent 50%),linear-gradient(rgba(255,255,255,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.05) 1px,transparent 1px);background-size:auto,26px 26px,26px 26px}
.art .ai{position:absolute;left:50%;top:50%;width:44%;max-width:170px;aspect-ratio:1;translate:-50% -50%;display:grid;place-items:center;color:var(--gold);animation:aif 6s ease-in-out infinite}
.art .ai svg{width:100%;height:100%;stroke:currentColor;fill:none;stroke-width:1.15;stroke-linecap:round;stroke-linejoin:round;filter:drop-shadow(0 0 16px rgba(255,196,0,.5))}
@keyframes aif{50%{transform:translateY(-8px)}}
.art .rg{position:absolute;left:50%;top:50%;border:1px solid rgba(255,196,0,.3);border-radius:50%;translate:-50% -50%;pointer-events:none}
.art .rg.a{width:74%;aspect-ratio:1}.art .rg.b{width:104%;aspect-ratio:1;border-style:dashed;border-color:rgba(255,255,255,.16);animation:spin 60s linear infinite}
.pm.art:after{display:none}
.pm.art{min-height:260px}
.ic{background:var(--navy)}.ic:before{display:none}.ic>.art{position:absolute;inset:0;z-index:-2}.ic>.art .ai{top:38%;width:40%}.ic .art .rg{top:38%}
.rt.art{aspect-ratio:16/10}.rt.art .ai{width:34%}
.pbn .pbg.pbart{width:52%;opacity:1;-webkit-mask-image:linear-gradient(90deg,transparent,#000 40%);mask-image:linear-gradient(90deg,transparent,#000 40%);background:none}
.pbn .pbg.pbart .art{position:absolute;inset:0;background:none}.pbn .pbg.pbart .ai{left:56%;width:34%;max-width:280px}.pbn .pbg.pbart .rg{left:56%}
.empanel{aspect-ratio:4/3.4}.empanel .emb3d{display:block!important;width:min(240px,60%);height:auto;aspect-ratio:1;margin:0;position:absolute;left:50%;top:50%;translate:-50% -50%;animation:none}
.sp2i.art{aspect-ratio:4/3}.sp2i.art .ai{width:34%}
.tile2{position:relative;border-radius:12px;overflow:hidden;min-height:170px;display:flex;align-items:flex-end;padding:16px;color:#fff;font-family:Manrope;font-weight:700;background:var(--navy)}.tile2 .art{position:absolute;inset:0}.tile2 .ai{top:40%;width:38%}.tile2 .rg{top:40%}.tile2 b{position:relative;z-index:2}
@media(max-width:980px){.pm.art{min-height:190px}.pbn .pbg.pbart{width:100%;opacity:.35;-webkit-mask-image:linear-gradient(180deg,#000,transparent);mask-image:linear-gradient(180deg,#000,transparent)}.pbn .pbg.pbart .ai{left:74%;top:44%;width:38%}.pbn .pbg.pbart .rg{left:74%;top:44%}}
@media(prefers-reduced-motion:reduce){.art .ai,.art .rg.b{animation:none}}
.sp2i .emb3d{display:block!important;position:absolute;left:50%;top:50%;translate:-50% -50%;width:min(230px,56%);height:auto;aspect-ratio:1;margin:0;animation:none}.mos .art .ai{top:44%;width:34%}.mos>div>.art .rg{top:44%}.mos>div:after{z-index:1}.mos b{z-index:2}
.rt{position:relative}.rt>.art{position:absolute;inset:0}.rt .ai{width:32%;max-width:120px}.rcard:hover .art .ai{transform:scale(1.1)}.art .ai{transition:transform .6s var(--ease)}

.mg .allsv{grid-column:1/-1;font-weight:700;color:#a87c00;background:var(--bg)}.mg .allsv i{background:var(--gold)}.mg .allsv i svg{stroke:var(--navy)}
@media(max-width:980px){.tl{margin:0 -18px!important;padding:0 18px 4px!important;scroll-padding-left:18px!important}}

@media(max-width:600px){
.rel{grid-template-columns:1fr!important;gap:10px!important}
.rcard{display:grid!important;grid-template-columns:108px 1fr;align-items:stretch}
.rcard .rt{aspect-ratio:auto!important;height:100%;min-height:118px}
.rcard .rb{padding:14px 14px 14px 16px!important;display:flex;flex-direction:column;justify-content:center}
.rcard span{display:block!important;font-size:13px!important;margin-top:3px;line-height:1.45}
.rcard b{font-size:16px!important}.rcard em{margin-top:8px!important}
.rt .ai{width:50%!important}.rt .rg.a{width:120%}.rt .rg.b{width:170%}
}

.rvfix .rv,.rvfix .h2 .w>span{opacity:1!important;transform:none!important}
.rvfix .imgc .im{clip-path:none!important}
.rvfix2 .rv:not(.in){opacity:1!important;transform:none!important}
.rvfix2 .imgc .im{clip-path:none!important}
</style>
</head>
<body>
<div id="intro" aria-hidden="true"><div class="ip ipt"></div><div class="ip ipb"></div><div class="igrid"></div>
<div class="ic2"><svg class="shd" viewBox="0 0 100 120"><path d="M50 4 L94 19 V58 C94 89 73 109 50 117 C27 109 6 89 6 58 V19 Z"/></svg><img class="lg" src="logo.png" alt="" width="150" height="150"><div class="scan"></div></div>
<div class="it"><b>PARAKRAM</b><span>SECURITY INDIA PVT. LTD.</span><em>Your Safety Is Our Mission</em></div>
<div class="ibar"><i></i></div><button class="skip2" type="button">Skip</button></div>
<a class="skip" href="#main">Skip to content</a>
<div id="pg"></div>
<div id="toast" role="status" aria-live="polite"></div>
<div id="nudge" role="dialog" aria-label="Security plan"><button class="x" aria-label="Close">×</button><b>Need a security plan?</b><span>Tell us what you need. It takes about a minute.</span><a class="btn btn-g" href="#planner">Start now →</a></div>
<a class="sidetab" href="#contact">Get in Touch</a>
<nav class="rail" aria-label="Page sections"><a href="#about" data-l="About"></a><a href="#services" data-l="Services"></a><a href="#planner" data-l="Planner"></a><a href="#industries" data-l="Industries"></a><a href="#why" data-l="Why Us"></a><a href="#journey" data-l="Journey"></a><a href="#coverage" data-l="Coverage"></a><a href="#faq" data-l="FAQ"></a><a href="#contact" data-l="Contact"></a></nav>
<div class="util"><div class="wrap"><div class="l"><span class="pulse"></span>Control room online · 24/7 <span class="ist" id="ist"></span></div><div class="r"><a href="tel:+919105909006">+91 91059 09006</a><a href="mailto:info@parakramindia.org">info@parakramindia.org</a><a href="#careers">Careers</a></div></div></div>
<header id="hd"><div class="wrap nav">
<a class="brand" href="/"><img src="logo.png" alt="Parakram shield logo" width="56" height="56"><div><b>PARAKRAM</b><small>SECURITY INDIA PVT. LTD.</small></div></a>
<nav id="nav"><ul>
<li><a href="/about">About</a></li>
<li class="dd"><a href="/services">Services<span class="cv"> ▾</span></a><button class="ddt" aria-label="Show services" aria-expanded="false"></button><div class="menu"><div class="mg"><a class="allsv" href="/services"><i>@@ALLI@@</i>All Services</a>@@MEGA@@</div><div class="mp"><div class="art m4" style="position:absolute;inset:0"><div class="rg a"></div><div class="rg b"></div><span class="ai"><svg viewBox="0 0 24 24"><path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/></svg></span></div><b>Customized security solutions for every environment</b><a href="/services">All services →</a></div></div></li>
<li><a href="/industries">Industries</a></li><li><a href="/why">Why Us</a></li><li><a href="/coverage">Coverage</a></li><li><a href="/careers">Careers</a></li><li><a href="/faq">FAQ</a></li><li><a href="/contact">Contact</a></li><li class="mcta"><a class="btn btn-g" href="/planner">Plan Your Security →</a><a class="btn btn-n" href="tel:+919105909006">Call +91 91059 09006</a></li><li class="mfoot"><b>Parakram Security India Pvt. Ltd.</b><span>6A Sandesh Nagar, Kankhal, Haridwar 249408</span><a href="mailto:info@parakramindia.org">info@parakramindia.org</a></li></ul></nav>
<a class="btn btn-n" href="/planner" style="padding:13px 24px">Plan Your Security</a><button class="burger" id="bg" aria-label="Menu" aria-expanded="false"><i></i></button>
</div></header>

<main id="main">
<section class="hx" id="hero" style="padding:0" aria-roledescription="carousel">
<div class="orbs" aria-hidden="true"><i class="o1"></i><i class="o2"></i><i class="o3"></i></div><div class="floor" aria-hidden="true"></div>
<div class="slide on"><div class="bgc"></div><div class="ph phm" style="--bg:url(img/parakram-about.webp)"></div>
<div class="fig" id="fig"><div class="halo"></div><img src="img/parakram-hero-portrait.webp" alt="Parakram security officer" width="800" height="620" fetchpriority="high" decoding="async"></div>
<div class="wrap hxg"><div class="tx"><div class="eyebrow">Your Safety Is Our Mission</div>
<h1><span class="ln"><span>A life with</span></span><span class="ln"><span><em>full protection.</em></span></span></h1>
<p class="lead">Professionally managed private security since 2017, with disciplined manpower, rigorous training and deeply rooted Indian values to protect people, property and operations.</p>
<div class="cta"><a class="btn btn-g" href="#planner">Plan Your Security →</a><a class="btn btn-o" href="#services">Our Services</a></div></div></div></div>
<div class="slide"><div class="bgc"></div><div class="ph" style="--bg:url(img/parakram-operations.webp)"></div>
<div class="wrap hxg"><div class="tx"><div class="eyebrow">Corporate &amp; Commercial</div>
<h2 class="hh"><span class="ln"><span>Protection for</span></span><span class="ln"><span><em>every premises.</em></span></span></h2>
<p class="lead">Trained, verified guards with excellent site coordination, for offices, campuses and business environments.</p>
<div class="cta"><a class="btn btn-g" href="#contact">Get Started →</a><a class="btn btn-o" href="#industries">Industries We Protect</a></div></div></div></div>
<div class="slide"><div class="bgc"></div><div class="ph" style="--bg:url(img/parakram-training.webp)"></div>
<div class="wrap hxg"><div class="tx"><div class="eyebrow">Trained &amp; Verified Personnel</div>
<h2 class="hh"><span class="ln"><span>Trained. Verified.</span></span><span class="ln"><span><em>Ready to serve.</em></span></span></h2>
<p class="lead">Disciplined recruitment and rigorous training ensure professionalism, integrity and courtesy at every site.</p>
<div class="cta"><a class="btn btn-g" href="#why">Why Parakram →</a><a class="btn btn-o" href="#contact">Talk to Us</a></div></div></div></div>
<a class="cue" href="#statement" aria-label="Scroll down"><i></i></a>
<div class="hxc"><div class="wrap"><div class="dots"><button class="d on" aria-label="Slide 1"><i></i><span>01 · Protection</span></button><button class="d" aria-label="Slide 2"><i></i><span>02 · Corporate</span></button><button class="d" aria-label="Slide 3"><i></i><span>03 · Training</span></button></div>
<div class="arrows"><button id="pv" aria-label="Previous">←</button><button id="nx" aria-label="Next">→</button></div></div></div>
</section>

<div class="stats"><div class="wrap"><div class="grid">
<div class="stat"><b data-n="9" data-s="+">0</b><span>Years of Experience</span></div>
<div class="stat"><b data-n="1500" data-s="+">0</b><span>Trained Professionals</span></div>
<div class="stat"><b data-n="210" data-s="K">0</b><span>Partners</span></div>
<div class="stat"><b data-n="4.9" data-d="1">0</b><span>Client Rating</span></div>
<div class="stat"><b data-n="8">0</b><span>Security Services</span></div>
</div></div></div>

<section class="lead-s" id="statement"><div class="wrap"><p class="ls rv">Parakram Security India provides <b>manned, armed, industrial, commercial, residential, hospital, educational and bank &amp; ATM security</b>, professionally managed since 2017 and combining disciplined manpower, rigorous training and deeply rooted Indian values to protect people, property and operations.</p><a class="kn" href="#about">Know more</a></div></section>

<section class="blk" id="paths" style="padding-bottom:0"><div class="wrap"><div class="sec-h rv" style="margin-bottom:28px"><div class="eyebrow dk">Find your solution</div><h2 class="h2">What do you need to <em>protect?</em></h2></div>
<div class="paths">
<a class="pth rv" href="/industries#industrial"><i>@@I_ind@@</i>Factory or warehouse<span>Industrial security</span></a>
<a class="pth rv" href="/industries#corporate"><i>@@I_com@@</i>Office or business<span>Corporate security</span></a>
<a class="pth rv" href="/industries#healthcare"><i>@@I_hos@@</i>Hospital or clinic<span>Healthcare security</span></a>
<a class="pth rv" href="/services/banking"><i>@@I_bnk@@</i>Bank or ATM<span>Banking security</span></a>
<a class="pth rv" href="/services/residential"><i>@@I_res@@</i>Home or society<span>Residential security</span></a>
<a class="pth rv" href="/services/educational"><i>@@I_edu@@</i>School or college<span>Educational security</span></a>
</div></div></section>

<section id="about"><div class="wrap two">
<div class="abt rv"><div class="eyebrow dk">About Parakram</div><h2 class="h2">Protecting people, property &amp; <em>operations.</em></h2>
<p>Parakram Security India Private Limited was established in 2017 as a professionally managed private security company.</p>
<p>We combine disciplined manpower, rigorous training and deeply rooted Indian values to protect people, property and operations, with personnel known for professionalism, integrity and courtesy.</p>
<div class="vals"><div><b>Professionalism</b><span>Disciplined, trained personnel</span></div><div><b>Integrity</b><span>Verified, trustworthy teams</span></div><div><b>Courtesy</b><span>Respectful service, always</span></div></div>
<a class="btn btn-n" href="/about">Read Our Story →</a></div>
<div class="imgc rv"><div class="im art m3 empanel"><div class="rg a"></div><div class="rg b"></div><div class="emb3d" aria-hidden="true"></div></div><div class="bd"><b>2017</b><span>Established · Haridwar</span></div></div>
</div></section>

<section id="services" class="bg"><div class="wrap">
<div class="sec-h rv"><div class="eyebrow dk">Security Services</div><h2 class="h2">Eight services. One standard of <em>excellence.</em></h2><p>Customized security solutions for every environment.</p></div>
<div class="sx rv"><div class="tl" role="tablist">@@TABS@@</div><div class="pw">@@PANELS@@</div></div>
</div></section>

<section id="planner" class="plan"><div class="wrap">
<div class="rv"><div class="eyebrow">Security Planner</div><h2 class="h2">Tell us what you need. <em>We'll design the plan.</em></h2>
<p class="s">Answer four quick questions and our team will respond with a solution customized to your site, with no obligation.</p>
<ul><li>Customized security solutions</li><li>Trained &amp; verified personnel</li><li>Support for multiple sites</li><li>Available 24/7</li></ul></div>
<div class="wz rv" id="wz">
<div class="st"><i class="on"></i><i></i><i></i><i></i></div>
<div class="step on"><h3>Which services do you need?</h3><p class="sub">Select one or more.</p><div class="chips">@@CHIPS@@</div><div class="nav2"><span></span><button class="btn btn-n" data-nx>Continue →</button></div></div>
<div class="step"><h3>What type of site?</h3><p class="sub">Choose the closest match.</p><div class="chips" id="sites">
<label class="chp"><input type="radio" name="site" value="Industrial"><span>Industrial</span></label><label class="chp"><input type="radio" name="site" value="Corporate / Commercial"><span>Corporate / Commercial</span></label><label class="chp"><input type="radio" name="site" value="Healthcare"><span>Healthcare</span></label><label class="chp"><input type="radio" name="site" value="Banking / ATM"><span>Banking / ATM</span></label><label class="chp"><input type="radio" name="site" value="Residential"><span>Residential</span></label><label class="chp"><input type="radio" name="site" value="Educational"><span>Educational</span></label></div>
<div class="nav2"><button class="bk" data-bk>← Back</button><button class="btn btn-n" data-nx>Continue →</button></div></div>
<div class="step"><h3>Coverage &amp; team size</h3><p class="sub">Approximate is fine.</p><div class="chips">
<label class="chp"><input type="radio" name="g" value="1 to 5 personnel"><span>1 to 5 personnel</span></label><label class="chp"><input type="radio" name="g" value="6 to 20 personnel"><span>6 to 20 personnel</span></label><label class="chp"><input type="radio" name="g" value="21 to 50 personnel"><span>21 to 50 personnel</span></label><label class="chp"><input type="radio" name="g" value="50+ personnel"><span>50+ personnel</span></label><label class="chp"><input type="radio" name="sh" value="24/7 coverage"><span>24/7 coverage</span></label><label class="chp"><input type="radio" name="sh" value="Day shift"><span>Day shift</span></label><label class="chp"><input type="radio" name="sh" value="Night shift"><span>Night shift</span></label><label class="chp"><input type="radio" name="sh" value="Multiple sites"><span>Multiple sites</span></label></div>
<div class="nav2"><button class="bk" data-bk>← Back</button><button class="btn btn-n" data-nx>Continue →</button></div></div>
<div class="step"><h3>Where should we reach you?</h3><p class="sub">We'll open WhatsApp with your plan prefilled.</p><input class="t" id="pn" placeholder="Your name"><input class="t" id="pp" type="tel" placeholder="Phone number"><input class="t" id="pc" placeholder="City / site location"><p class="note">Your details are shared only with the Parakram team.</p>
<div class="nav2"><button class="bk" data-bk>← Back</button><button class="btn btn-g" id="send">Send on WhatsApp →</button></div></div>
</div></div></section>

<section id="industries"><div class="wrap">
<div class="sec-h rv"><div class="eyebrow dk">Industries We Protect</div><h2 class="h2">Trusted where safety <em>matters most.</em></h2></div>
<div class="ind">
<a class="ic rv" href="/industries#industrial"><div class="art m1"><div class="rg a"></div><div class="rg b"></div><span class="ai">@@IC_ind@@</span></div><span class="n">01</span><span class="go">→</span><h3>Industrial</h3><span>Plants · Warehouses</span></a>
<a class="ic rv" href="/industries#corporate"><div class="art m2"><div class="rg a"></div><div class="rg b"></div><span class="ai">@@IC_com@@</span></div><span class="n">02</span><span class="go">→</span><h3>Corporate</h3><span>Offices · Business premises</span></a>
<a class="ic rv" href="/industries#healthcare"><div class="art m3"><div class="rg a"></div><div class="rg b"></div><span class="ai">@@IC_hos@@</span></div><span class="n">03</span><span class="go">→</span><h3>Healthcare</h3><span>Hospitals · Clinics</span></a>
<a class="ic rv" href="/industries#banking"><div class="art m4"><div class="rg a"></div><div class="rg b"></div><span class="ai">@@IC_bnk@@</span></div><span class="n">04</span><span class="go">→</span><h3>Banking</h3><span>Branches · ATMs</span></a>
</div></div></section>

<section class="band" style="background-image:url(img/parakram-operations.webp)"><div class="wrap rv"><div class="eyebrow" style="justify-content:center">Trusted Protection</div><h2>Professionalism. Integrity. <em>Courtesy.</em></h2><p>Personnel who protect people, property and operations, 24/7.</p><a class="btn btn-g" href="#contact">Get Started →</a></div></section>

<section id="why" class="bg"><div class="wrap">
<div class="sec-h rv"><div class="eyebrow dk">Why Us</div><h2 class="h2">Why leaders choose <em>Parakram.</em></h2><a class="kn" href="/why">Why Parakram</a></div>
<div class="pil">
<div class="pl rv"><div class="big" data-n="9" data-s="+">0</div><h3>Years of Experience</h3><p>A professionally managed security company operating since 2017.</p></div>
<div class="pl rv"><div class="big" data-n="1500" data-s="+">0</div><h3>Trained &amp; Verified Personnel</h3><p>Disciplined recruitment and rigorous training for every guard.</p></div>
<div class="pl rv"><div class="big" data-n="100" data-s="%">0</div><h3>Customized Solutions</h3><p>Services designed around your site, your risk and your operations.</p></div></div>
<div class="proc"><h3 class="h2 rv">How we get you protected.</h3>
<div class="steps rv" id="steps"><i class="fl"></i><div class="sp"><i>1</i><div><b>Consult</b><span>Tell us your needs</span></div></div><div class="sp"><i>2</i><div><b>Assess</b><span>We study your site</span></div></div><div class="sp"><i>3</i><div><b>Customize</b><span>A tailored security plan</span></div></div><div class="sp"><i>4</i><div><b>Deploy</b><span>Trained, verified personnel</span></div></div><div class="sp"><i>5</i><div><b>Supervise</b><span>Ongoing quality checks</span></div></div></div></div>
</div></section>

<section id="journey"><div class="wrap">
<div class="sec-h rv"><div class="eyebrow dk">Our Journey</div><h2 class="h2">Growing steadily <em>since 2017.</em></h2><p>A professionally managed company built on training, discipline and trust.</p></div>
<div class="jr" id="jr"><div class="jl"><i id="jfill"></i></div><div class="jn">
<div class="jm"><span class="dot"></span><small>2017</small><b>Company established</b><p>Founded as a professionally managed private security company in Haridwar, Uttarakhand.</p></div>
<div class="jm"><span class="dot"></span><small>Services</small><b class="jv"><em data-n="8">0</em></b><p>Security services, from manned and armed to industrial, commercial, residential, hospital, educational, and bank and ATM security.</p></div>
<div class="jm"><span class="dot"></span><small>People</small><b class="jv"><em data-n="1500" data-s="+">0</em></b><p>Trained professionals, recruited with discipline and prepared with rigorous training.</p></div>
<div class="jm"><span class="dot"></span><small>Client rating</small><div class="ring"><svg viewBox="0 0 120 120"><circle class="rb" cx="60" cy="60" r="52"/><circle class="rf" cx="60" cy="60" r="52"/></svg><b><em data-n="4.9" data-d="1">0</em></b></div><p>Average rating, reviewed by more than 1,200 satisfied clients.</p></div>
<div class="jm"><span class="dot"></span><small>Partners</small><b class="jv"><em data-n="210" data-s="K">0</em></b><p>Partners who trust Parakram to protect people, property and operations.</p></div>
</div></div></div></section>

<section id="coverage"><div class="wrap cov">
<div class="map rv" id="map">@@MAP@@<div class="mtip" id="mtip"></div><div class="mc"><div><b id="mn">Uttarakhand</b><span id="ms">Headquarters · 6A Sandesh Nagar, Kankhal, Haridwar 249408</span></div><a class="btn btn-n" id="mb" style="padding:12px 20px" href="#contact">Contact Us</a></div><div class="mhint">Hover or tap a state</div></div>
<div class="covt rv"><div class="eyebrow dk">Coverage</div><h2 class="h2">Local roots. <em>Wider reach</em> across India.</h2><a class="kn" href="/coverage">Explore coverage</a>
<ul><li><i>◎</i><div><b>Headquartered in Haridwar</b><span>Registered office in Kankhal, Haridwar, Uttarakhand.</span></div></li><li><i>⇄</i><div><b>Support for multiple sites</b><span>One partner across all your locations.</span></div></li><li><i>24</i><div><b>Always available</b><span>Services available 24/7.</span></div></li></ul></div>
</div></section>

<section class="tm"><div class="wrap rv"><div class="rate"><b>4.9</b>★★★★★ Rated by 1,200+ clients</div><h2 class="h2">What our <em>clients say.</em></h2>
<div class="qs"><div class="q on"><div class="st">★★★★★</div><blockquote>Well trained guards and excellent site coordination.</blockquote><cite>Facility Manager</cite></div>
<div class="q"><div class="st">★★★★★</div><blockquote>Dependable security routines that keep our operations running smoothly.</blockquote><cite>Industrial Client</cite></div>
<div class="q"><div class="st">★★★★★</div><blockquote>Supervisors are accessible and responsive whenever we need them.</blockquote><cite>Institutional Client</cite></div></div>
<div class="qd"><button class="on" aria-label="Quote 1"></button><button aria-label="Quote 2"></button><button aria-label="Quote 3"></button></div></div></section>

<section id="faq"><div class="wrap"><div class="fq">
<div class="sec-h rv"><div class="eyebrow dk">FAQ</div><h2 class="h2">Answers <em>before you ask.</em></h2><a class="kn" href="/faq">See all questions</a><p>Still have questions? Call +91 91059 09006 or email info@parakramindia.org.</p></div>
<div class="rv"><details open><summary>What types of security services do you provide?</summary><p>Manned, Armed, Industrial, Commercial, Residential, Hospital, Educational, and Bank &amp; ATM security.</p></details>
<details><summary>How are your personnel trained and verified?</summary><p>Through disciplined recruitment and rigorous training, so every guard is trained and verified before deployment.</p></details>
<details><summary>Is your service available 24/7?</summary><p>Yes, our services are available 24/7.</p></details>
<details><summary>Can solutions be customized to my site?</summary><p>Yes. We design customized security solutions around your needs, including support for multiple sites.</p></details>
<details><summary>How do I get started?</summary><p>Use our Security Planner, call +91 91059 09006, or email info@parakramindia.org.</p></details></div></div>
<div class="careers rv" id="careers"><div><div class="eyebrow">Careers</div><h3>Serve with <em>Parakram.</em></h3><p>Join a disciplined, professionally managed team built on integrity and courtesy.</p><a class="btn btn-g" href="/careers">Explore Careers →</a></div>
<div class="req"><div class="row"><span>Culture</span><b>Professionalism, integrity, courtesy</b></div><div class="row"><span>Training</span><b>Rigorous &amp; structured</b></div><div class="row"><span>Team</span><b>1,500+ professionals</b></div><div class="row"><span>Apply</span><b>info@parakramindia.org</b></div></div></div>
</div></section>

<section id="contact" class="bg"><div class="wrap"><div class="contact rv">
<div class="l"><h3>Let's secure your world.</h3>
<p><b>Address</b>6A Sandesh Nagar, Kankhal, Haridwar 249408, Uttarakhand</p>
<p><b>Phone</b><a href="tel:+919105909006">+91 91059 09006</a> · <a href="tel:+918937000489">+91 89370 00489</a> · <a href="tel:+919105909000">+91 91059 09000</a></p>
<p><b>Email</b><a href="mailto:info@parakramindia.org">info@parakramindia.org</a></p><p><b>Availability</b>Open 24/7</p><a class="dir" href="https://www.google.com/maps/search/?api=1&amp;query=6A+Sandesh+Nagar+Kankhal+Haridwar+249408" target="_blank" rel="noopener">Get directions →</a></div>
<form id="cf"><input required id="cn" placeholder="Full name"><input required id="cp" type="tel" placeholder="Phone"><input class="full" id="ce" type="email" placeholder="Email">
<select class="full" id="cs"><option value="">Service required</option>@@OPTS@@</select>
<textarea class="full" id="cm" placeholder="Tell us about your site and requirements"></textarea>
<button class="btn btn-n full" style="justify-content:center">Get Started →</button></form></div></div></section>
</main>

<div class="ctab"><div class="wrap"><div><h2>Ready to secure your premises?</h2><p>Speak to our team. We are available 24/7.</p></div><div class="emb3d" aria-hidden="true"></div><div class="cta2"><a class="btn btn-g" href="#planner">Plan Your Security →</a><a class="btn btn-o" href="tel:+919105909006">+91 91059 09006</a></div></div></div>
<footer><div class="wrap"><div class="fg">
<div><div class="brand" style="margin-bottom:18px"><img src="logo.png" alt="" style="height:64px"><div><b style="color:#fff">PARAKRAM</b><small style="color:#aab0d6">SECURITY INDIA PVT. LTD.</small></div></div><p style="font-size:14.5px;max-width:320px">We aim to provide you with a life with full protection.</p></div>
<div><h4>Company</h4><ul><li><a href="/about">About Us</a></li><li><a href="/why">Why Parakram</a></li><li><a href="/industries">Industries</a></li><li><a href="/coverage">Coverage</a></li><li><a href="/careers">Careers</a></li><li><a href="/faq">FAQ</a></li><li><a href="/contact">Contact</a></li></ul></div>
<div><h4>Services</h4><ul><li><a href="/services/manned">Manned Security</a></li><li><a href="/services/armed">Armed Security</a></li><li><a href="/services/industrial">Industrial Security</a></li><li><a href="/services/commercial">Commercial Security</a></li><li><a href="/services/residential">Residential Security</a></li><li><a href="/services/hospital">Hospital Security</a></li><li><a href="/services/educational">Educational Security</a></li><li><a href="/services/banking">Bank &amp; ATM Security</a></li></ul></div>
<div><h4>Contact</h4><ul><li>Parakram Security India Pvt. Ltd.<br>6A Sandesh Nagar, Kankhal,<br>Haridwar 249408, Uttarakhand</li><li><a href="tel:+918937000489">+91 89370 00489</a></li><li><a href="tel:+919105909006">+91 91059 09006</a></li><li><a href="mailto:info@parakramindia.org">info@parakramindia.org</a></li><li><a href="https://wa.me/919105909006" target="_blank" rel="noopener">Chat on WhatsApp</a></li><li><a href="https://www.google.com/maps/search/?api=1&amp;query=6A+Sandesh+Nagar+Kankhal+Haridwar+249408" target="_blank" rel="noopener">Get directions</a></li></ul></div></div>
<div class="fb"><span>© 2026 Parakram Security India Pvt. Ltd. All rights reserved.</span><span class="fl"><a href="/privacy">Privacy Policy</a><a href="/terms">Terms of Use</a><span>Website by <a class="by" href="https://aibootstrapper.com" target="_blank" rel="noopener">AIBOOTSTRAPPER</a></span></span></div></div></footer>
<div class="mbar"><a href="tel:+919105909006">Call</a><a class="mw" href="https://wa.me/919105909006" aria-label="WhatsApp"><svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 0 0-8.6 15l-1.4 5 5.2-1.4A10 10 0 1 0 12 2zm5.4 14.2c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.2-.7-2.7-1.1-4.4-3.8-4.5-4-.1-.1-1.100-1.500-1.100-2.800s.7-2 1-2.300c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 2c.1.2.1.3 0 .5l-.3.4-.4.4c-.1.1-.3.3-.1.6.2.3.7 1.100 1.500 1.800 1 .9 1.900 1.200 2.200 1.300.3.1.4.1.6-.1l.8-1c.2-.3.4-.2.6-.1l1.900.9c.3.1.5.2.6.3.1.2.1.8-.1 1.400z"/></svg>WhatsApp</a><a href="#planner">Get Started</a></div>
<button class="top" id="top2" aria-label="Back to top">↑</button>
<a class="wa" href="https://wa.me/919105909006" aria-label="WhatsApp"><svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 0 0-8.6 15l-1.4 5 5.2-1.4A10 10 0 1 0 12 2zm5.4 14.2c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.2-.7-2.7-1.1-4.4-3.8-4.5-4-.1-.1-1.1-1.5-1.1-2.8s.7-2 1-2.3c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 2c.1.2.1.3 0 .5l-.3.4-.4.4c-.1.1-.3.3-.1.6.2.3.7 1.1 1.5 1.8 1 .9 1.900 1.200 2.200 1.300.3.1.4.1.6-.1l.8-1c.2-.3.4-.2.6-.1l1.900.9c.3.1.5.2.6.3.1.2.1.8-.1 1.400z"/></svg></a>
<script src="js/lenis.min.js"></script>
<script>
const $=s=>[...document.querySelectorAll(s)],mq=q=>matchMedia(q).matches,PH='919105909006';
/* smooth inertial scrolling (desktop, fine pointer only) */
const hd0=document.getElementById('hd');let lenis=null;const REDUCE=mq('(prefers-reduced-motion:reduce)');
if(!REDUCE&&!mq('(pointer:coarse)')&&window.Lenis){lenis=new Lenis({duration:1.15,easing:t=>Math.min(1,1.001-Math.pow(2,-10*t)),wheelMultiplier:.95});const raf=t=>{lenis.raf(t);requestAnimationFrame(raf)};requestAnimationFrame(raf);document.documentElement.classList.add('lenis')}
const goTo=el=>{window.__nj=Date.now();hd0.classList.remove('hide');const hh=document.getElementById('hd').offsetHeight;const sp=parseFloat(getComputedStyle(el).paddingTop)||0;const off=el.matches('.sx')?-(hh+16):(el.matches('section')?-(hh+24-sp):-(hh+16));if(lenis){lenis.scrollTo(el,{offset:off,duration:1.4});setTimeout(()=>{const d=el.getBoundingClientRect().top+off;if(Math.abs(d)>60){lenis.scrollTo(scrollY+d,{immediate:true})}},2000)}else el.scrollIntoView({behavior:'smooth'})};
/* clean URLs: smooth-scroll to anchors without leaving #hash in the address bar */
document.addEventListener('click',e=>{const a=e.target.closest('a[href^="#"]');if(!a)return;const id=a.getAttribute('href').slice(1);const t=a.dataset.go!==undefined?document.querySelector('.sx'):(id&&document.getElementById(id));if(!t&&id)return;e.preventDefault();setTimeout(()=>goTo(t||document.body),a.closest('nav')?60:0);if(location.hash)history.replaceState(null,'',location.pathname+location.search)});
document.querySelector('.brand').addEventListener('click',e=>{e.preventDefault();lenis?lenis.scrollTo(0,{duration:1.3}):scrollTo({top:0,behavior:'smooth'});if(location.hash)history.replaceState(null,'',location.pathname)});
if(location.hash){const t=document.getElementById(location.hash.slice(1));if(t)setTimeout(()=>{lenis?lenis.scrollTo(t,{immediate:true,offset:-(document.getElementById('hd').offsetHeight)}):t.scrollIntoView();history.replaceState(null,'',location.pathname)},60)}
/* header/progress/back-to-top */
const hd=document.getElementById('hd'),pg=document.getElementById('pg'),t2=document.getElementById('top2');
let lastY=0;addEventListener('scroll',()=>{const y=scrollY;hd.classList.toggle('sh',y>10);pg.style.width=(y/(document.documentElement.scrollHeight-innerHeight)*100)+'%';t2.classList.toggle('v',y>900);if(!document.body.classList.contains('no')){if(y>420&&y>lastY+6&&Date.now()-(window.__nj||0)>2600)hd.classList.add('hide');else if(y<lastY-6||y<420)hd.classList.remove('hide')}lastY=y},{passive:true});
t2.onclick=()=>lenis?lenis.scrollTo(0,{duration:1.3}):scrollTo({top:0,behavior:'smooth'});
/* mobile nav */
const nav=document.getElementById('nav'),bg=document.getElementById('bg');
bg.onclick=()=>{const o=nav.classList.toggle('open');document.body.classList.toggle('no',o);bg.classList.toggle('x',o);bg.setAttribute('aria-expanded',o);document.body.style.overflow=o?'hidden':''};
$('nav a').forEach(a=>a.addEventListener('click',e=>{if(a.parentNode.classList.contains('dd')&&mq('(max-width:1180px)')){e.preventDefault();const o=a.parentNode.classList.toggle('o');const b=a.parentNode.querySelector('.ddt');if(b)b.setAttribute('aria-expanded',o);return}nav.classList.remove('open');document.body.classList.remove('no');bg.classList.remove('x');bg.setAttribute('aria-expanded','false');document.body.style.overflow=''}));
$('.ddt').forEach(b=>b.addEventListener('click',()=>{const o=b.parentNode.classList.toggle('o');b.setAttribute('aria-expanded',o)}));
/* reveal */
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:0,rootMargin:'0px 0px -4% 0px'});
const io2=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io2.unobserve(e.target)}}),{threshold:.3});
$('.vals>div,.stats .stat,.fg>div,.covt li,.faq details,.fq details').forEach(e=>e.classList.add('rv'));
$('.rv').forEach(e=>{const sib=[...e.parentNode.children].filter(c=>c.classList.contains('rv'));e.style.setProperty('--d',Math.min(sib.indexOf(e),6)*90+'ms');io.observe(e)});

/* reveal failsafe: never leave content hidden */
var revealNow=()=>{const vh=innerHeight;$('.rv:not(.in)').forEach(e=>{const r=e.getBoundingClientRect();if(r.top<vh*.98&&r.bottom>-40)e.classList.add('in')});$('.h2:not(.in)').forEach(e=>{const r=e.getBoundingClientRect();if(r.top<vh*.98&&r.bottom>-40)e.classList.add('in')})};
addEventListener('scroll',revealNow,{passive:true});addEventListener('resize',revealNow);addEventListener('load',revealNow);addEventListener('pageshow',revealNow);addEventListener('orientationchange',revealNow);
var __rv=0;var __ti=setInterval(()=>{revealNow();if(++__rv>12)clearInterval(__ti)},700);revealNow();
/* counters */
const co=new IntersectionObserver(es=>es.forEach(e=>{if(!e.isIntersecting)return;const el=e.target,n=+el.dataset.n,d=+el.dataset.d||0,s=el.dataset.s||'';let t0=null;const f=t=>{t0=t0||t;const p=Math.min((t-t0)/1800,1),v=n*(1-Math.pow(1-p,4));el.innerHTML=(d?v.toFixed(d):Math.round(v).toLocaleString('en-IN'))+(s?'<sup>'+s+'</sup>':'');if(p<1)requestAnimationFrame(f)};requestAnimationFrame(f);co.unobserve(el)}),{threshold:.5});
$('[data-n]').forEach(e=>co.observe(e));
/* hero slider */
(()=>{const sl=$('.slide'),ds=$('.d');let i=0,t;const go=n=>{i=(n+sl.length)%sl.length;sl.forEach((e,k)=>e.classList.toggle('on',k==i));ds.forEach((e,k)=>{e.classList.remove('on');if(k==i){void e.offsetWidth;e.classList.add('on')}});clearTimeout(t);t=setTimeout(()=>go(i+1),6500)};
window.__heroReset=()=>go(0);ds.forEach((d,k)=>d.onclick=()=>go(k));document.getElementById('pv').onclick=()=>go(i-1);document.getElementById('nx').onclick=()=>go(i+1);t=setTimeout(()=>go(1),6500);
const fig=document.getElementById('fig'),hx=document.getElementById('hero');if(!mq('(pointer:coarse)'))hx.addEventListener('mousemove',e=>{const x=(e.clientX/innerWidth-.5)*16,y=(e.clientY/innerHeight-.5)*10;fig.style.transform=`translate(${x}px,${y}px)`})})();
/* services */
(()=>{const tb=$('.tb'),pn=$('.pn');const sel=k=>{tb.forEach((e,i)=>e.classList.toggle('on',i==k));pn.forEach((e,i)=>e.classList.toggle('on',i==k));if(mq('(max-width:980px)')){const tl=tb[k].parentNode;tl.scrollTo({left:tb[k].offsetLeft-(tl.clientWidth-tb[k].offsetWidth)/2,behavior:'smooth'})}};
tb.forEach((b,k)=>{b.onclick=()=>sel(k);b.onmouseenter=()=>{if(!mq('(max-width:980px)'))sel(k)}});$('[data-go]').forEach(a=>a.addEventListener('click',()=>sel(+a.dataset.go)))})();
/* spotlight cards */
$('.pl').forEach(c=>c.addEventListener('mousemove',e=>{const r=c.getBoundingClientRect();c.style.setProperty('--mx',(e.clientX-r.left)+'px');c.style.setProperty('--my',(e.clientY-r.top)+'px')}));
/* testimonials */
(()=>{const q=$('.q'),d=$('.qd button');let i=0,t;const go=n=>{i=n%q.length;q.forEach((e,k)=>e.classList.toggle('on',k==i));d.forEach((e,k)=>e.classList.toggle('on',k==i));clearTimeout(t);t=setTimeout(()=>go(i+1),5500)};d.forEach((b,k)=>b.onclick=()=>go(k));t=setTimeout(()=>go(1),5500)})();

/* --- enhancement JS --- */

const toast=m=>{const t=document.getElementById('toast');t.textContent=m;t.classList.add('on');clearTimeout(t._h);t._h=setTimeout(()=>t.classList.remove('on'),3200)};
/* split headings */
$('.h2').forEach(h=>{let i=0;const wrap=n=>{[...n.childNodes].forEach(c=>{if(c.nodeType===3){const f=document.createDocumentFragment();c.textContent.split(/(\s+)/).forEach(t=>{if(!t)return;if(/^\s+$/.test(t)){f.appendChild(document.createTextNode(' '));return}const w=document.createElement('span');w.className='w';const b=document.createElement('span');b.textContent=t;b.style.setProperty('--i',i++);w.appendChild(b);f.appendChild(w)});c.replaceWith(f)}else if(c.nodeType===1)wrap(c)})};wrap(h);h.setAttribute('aria-label',h.textContent);io2.observe(h)});
/* scrollspy */
const spy=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){$('nav>ul>li>a').forEach(a=>a.classList.toggle('act',a.getAttribute('href')==='#'+e.target.id))}}),{rootMargin:'-45% 0px -50% 0px'});
$('main section[id]').forEach(x=>spy.observe(x));
/* tilt cards (disabled for a calmer enterprise feel) */
if(false)$('.ic').forEach(c=>{c.addEventListener('mousemove',e=>{const r=c.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;c.style.transform=`perspective(1000px) translateY(-8px) rotateX(${-y*7}deg) rotateY(${x*9}deg)`});c.addEventListener('mouseleave',()=>c.style.transform='')});
/* magnetic buttons (disabled) */
if(false)$('.btn-g,.btn-n').forEach(b=>{b.addEventListener('mousemove',e=>{const r=b.getBoundingClientRect();b.style.transform=`translate(${(e.clientX-r.left-r.width/2)*.18}px,${(e.clientY-r.top-r.height/2)*.28}px)`});b.addEventListener('mouseleave',()=>b.style.transform='')});
/* hero glow + scroll fade */
(()=>{addEventListener('scroll',()=>{if(scrollY<900){const y=scrollY;$('.hxg .tx').forEach(t=>{t.style.transform=`translateY(${y*.12}px)`;t.style.opacity=Math.max(0,1-y/650)})}},{passive:true})})();
/* parallax on about image + band */
addEventListener('scroll',()=>{const im=document.querySelector('.imgc .im img');if(im){const r=im.getBoundingClientRect();if(r.top<innerHeight&&r.bottom>0)im.style.objectPosition=`50% ${50+(r.top/innerHeight-.5)*18}%`}},{passive:true});

/* ist clock */
(()=>{const e=document.getElementById('ist');const t=()=>{e.textContent=new Date().toLocaleTimeString('en-IN',{timeZone:'Asia/Kolkata',hour:'2-digit',minute:'2-digit',second:'2-digit',hour12:true})+' IST'};t();setInterval(t,1000)})();
/* india map */
(()=>{const m=document.getElementById('map'),tip=document.getElementById('mtip'),mn=document.getElementById('mn'),ms=document.getElementById('ms'),mb=document.getElementById('mb'),sts=$('.st');
const pick=p=>{const n=p.dataset.n;sts.forEach(x=>x.classList.toggle('sel',x===p));mn.textContent=n;
if(n==='Uttarakhand'){ms.textContent='Headquarters · 6A Sandesh Nagar, Kankhal, Haridwar 249408';mb.textContent='Contact Us';mb.href='#contact';mb.onclick=null}
else{ms.textContent='Support for multiple sites — tell us about your site in '+n+'.';mb.textContent='Enquire for '+n+' →';mb.href='#planner';mb.onclick=()=>{const f=document.getElementById('pc');if(f)f.value=n}}};
sts.forEach(p=>{p.addEventListener('mousemove',e=>{const r=m.getBoundingClientRect();tip.textContent=p.dataset.n+(p.classList.contains('hq')?' · HQ':'');tip.style.left=(e.clientX-r.left)+'px';tip.style.top=(e.clientY-r.top)+'px';tip.classList.add('on')});p.addEventListener('mouseleave',()=>tip.classList.remove('on'));p.addEventListener('click',()=>pick(p));p.setAttribute('tabindex','0');p.setAttribute('role','button');p.setAttribute('aria-label',p.dataset.n);p.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();pick(p)}})});
pick(document.querySelector('.st.hq'))})();

/* touch swipe: hero + services */
(()=>{const sw=(el,fn)=>{let x=0,y=0,t=0;el.addEventListener('touchstart',e=>{x=e.touches[0].clientX;y=e.touches[0].clientY;t=Date.now()},{passive:true});el.addEventListener('touchend',e=>{const dx=e.changedTouches[0].clientX-x,dy=e.changedTouches[0].clientY-y;if(Math.abs(dx)>50&&Math.abs(dx)>Math.abs(dy)*1.5&&Date.now()-t<700)fn(dx<0?1:-1)},{passive:true})};
const hero=document.getElementById('hero');if(hero)sw(hero,d=>document.getElementById(d>0?'nx':'pv').click());
const pw=document.querySelector('.pw');if(pw)sw(pw,d=>{const tb=$('.tb');const k=tb.findIndex(b=>b.classList.contains('on'));const n=k+d;if(n>=0&&n<tb.length)tb[n].click()})})();

/* section rail */
(()=>{const r=$('.rail a');if(!r.length)return;const io3=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){r.forEach(a=>a.classList.toggle('on',a.getAttribute('href')==='#'+e.target.id))}}),{rootMargin:'-45% 0px -50% 0px'});r.forEach(a=>{const t=document.querySelector(a.getAttribute('href'));if(t)io3.observe(t)})})();

/* scroll driven progress: journey timeline and process steps */
(()=>{const prog=(box,fill,items)=>{if(!box||!fill)return;const upd=()=>{const r=box.getBoundingClientRect();const p=Math.min(1,Math.max(0,(innerHeight*.72-r.top)/(r.height+innerHeight*.05)));const v=mq('(max-width:980px)');fill.style.transform=v?`scaleY(${p})`:`scaleX(${p})`;items.forEach((it,i)=>it.classList.toggle('on',REDUCE||p>=(i+.35)/items.length))};addEventListener('scroll',upd,{passive:true});addEventListener('resize',upd);upd()};
prog(document.getElementById('jr'),document.getElementById('jfill'),$('.jm'));
prog(document.getElementById('steps'),document.querySelector('#steps .fl'),$('#steps .sp'))})();
/* services autoplay (starts when visible, stops on any interaction) */
(()=>{const sx=document.querySelector('.sx');if(!sx||REDUCE||mq('(max-width:980px)')||mq('(pointer:coarse)'))return;const tb=$('.tb');let t=null,stopped=false,vis=false;
const idx=()=>tb.findIndex(b=>b.classList.contains('on'));
const step=()=>{if(stopped||!vis)return;tb[(idx()+1)%tb.length].click();sx.classList.remove('auto');void sx.offsetWidth;sx.classList.add('auto');t=setTimeout(step,5500)};
const start=()=>{clearTimeout(t);sx.classList.add('auto');t=setTimeout(step,5500)};
const stop=()=>{stopped=true;clearTimeout(t);sx.classList.remove('auto')};
['pointerdown','mouseenter','touchstart','keydown'].forEach(ev=>sx.addEventListener(ev,stop,{passive:true,once:true}));
new IntersectionObserver(es=>es.forEach(e=>{vis=e.isIntersecting&&e.intersectionRatio>.35;if(vis&&!stopped)start();else{clearTimeout(t);sx.classList.remove('auto')}}),{threshold:[0,.35,.6]}).observe(sx)})();
/* spotlight follow */
if(!mq('(pointer:coarse)'))$('.stat,.vals div,.covt li').forEach(c=>c.addEventListener('mousemove',e=>{const r=c.getBoundingClientRect();c.style.setProperty('--mx',(e.clientX-r.left)+'px');c.style.setProperty('--my',(e.clientY-r.top)+'px')}));

/* number the section labels 01, 02, 03 */
(()=>{let n=0;['about','services','planner','industries','why','journey','coverage','faq','contact'].forEach(id=>{const sec=document.getElementById(id);if(!sec)return;const e=sec.querySelector('.eyebrow');if(!e)return;n++;const sp=document.createElement('span');sp.className='no';sp.textContent=(n<10?'0':'')+n+' /';e.insertBefore(sp,e.firstChild)})})();

/* gentle planner prompt, once per visit */
(()=>{const n=document.getElementById('nudge');if(!n)return;let seen=false;try{seen=sessionStorage.getItem('nudge')==='1'}catch(e){}if(seen)return;
const hide=()=>{n.classList.remove('on');try{sessionStorage.setItem('nudge','1')}catch(e){}};
n.querySelector('.x').onclick=hide;n.querySelector('a').addEventListener('click',hide);
let ready=false,shown=false;const check=()=>{if(shown||!ready||scrollY<600)return;const pl=document.getElementById('planner').getBoundingClientRect();if(pl.top<innerHeight&&pl.bottom>0)return;shown=true;n.classList.add('on');setTimeout(()=>n.classList.remove('on'),16000)};setTimeout(()=>{ready=true;check()},10000);addEventListener('scroll',check,{passive:true})})();

/* security intro: short, skippable, once per visit */
(()=>{const I=document.getElementById('intro'),root=document.documentElement;if(!I||!root.classList.contains('intro'))return;let done=false;
const end=()=>{if(done)return;done=true;I.classList.add('open');setTimeout(()=>{root.classList.remove('intro');try{sessionStorage.setItem('intro','1')}catch(e){}window.__heroReset&&window.__heroReset()},900)};
setTimeout(end,2500);I.addEventListener('click',end);addEventListener('keydown',e=>{if(e.key==='Escape'||e.key==='Enter')end()});I.querySelector('.skip2').addEventListener('click',e=>{e.stopPropagation();end()})})();

/* faq filter and search */
(()=>{const box=document.getElementById('faqf');if(!box)return;const chips=$('#faqf .fchips button'),items=$('#faqf details'),inp=document.getElementById('faqs'),none=document.getElementById('fnone');let cat='all';
const run=()=>{const q=(inp.value||'').toLowerCase().trim();let n=0;items.forEach(d=>{const ok=(cat==='all'||d.dataset.c===cat)&&(!q||d.textContent.toLowerCase().includes(q));d.style.display=ok?'':'none';if(ok)n++});none.style.display=n?'none':'block'};
chips.forEach(b=>b.onclick=()=>{cat=b.dataset.c;chips.forEach(x=>x.classList.toggle('on',x===b));run()});inp.addEventListener('input',run)})();
/* subnav highlight */
(()=>{const links=$('.subnav .snv a');if(!links.length)return;const io4=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting)links.forEach(a=>a.classList.toggle('on',a.getAttribute('href')==='#'+e.target.id))}),{rootMargin:'-40% 0px -55% 0px'});links.forEach(a=>{const t=document.querySelector(a.getAttribute('href'));if(t)io4.observe(t)})})();
/* inner page banner entrance */
(()=>{const b=document.querySelector('.pbn');if(b)setTimeout(()=>b.classList.add('in'),80)})();

/* coverage options (24 hour bar) */
(()=>{const box=document.getElementById('cov24');if(!box)return;const bar=box.querySelector('.bar24'),spans=[...bar.children],cap=document.getElementById('cap24'),tabs=$('#cov24 .ctabs button');
const M={day:{h:h=>h>=6&&h<18,t:'Day shift: guards on duty from morning to evening. A good fit for offices, campuses and sites that are busiest during the day.'},night:{h:h=>h>=18||h<6,t:'Night shift: guards on duty through the night. A good fit for warehouses, residential societies and sites that need protection after hours.'},full:{h:()=>true,t:'24/7 coverage: guards on duty at every hour of every day, with planned handovers so there is never a gap.'}};
const set=k=>{tabs.forEach(b=>b.classList.toggle('on',b.dataset.m===k));spans.forEach((s,i)=>{setTimeout(()=>s.classList.toggle('on',M[k].h(i)),i*14)});cap.textContent=M[k].t};
tabs.forEach(b=>b.onclick=()=>set(b.dataset.m));set('full')})();
/* quick enquiry cards */
$('.qc form').forEach(f=>f.addEventListener('submit',e=>{e.preventDefault();const g=n=>f.querySelector('[name='+n+']').value.trim();if(!g('p')){toast('Please enter your phone number.');return}const m=`Hello Parakram Security, I am interested in ${f.dataset.s}.%0A*Name:* ${g('n')}%0A*Phone:* ${g('p')}`;open(`https://wa.me/${PH}?text=${m}`,'_blank');toast('Opening WhatsApp...')}));
/* resume upload */
(()=>{const f=document.getElementById('cvf');if(!f)return;f.onsubmit=null;const fi=document.getElementById('vf'),drop=document.getElementById('drop'),ok=document.getElementById('fileok'),st=document.getElementById('cvst'),btn=document.getElementById('cvb');let file=null;const MAX=3*1024*1024;
const say=(c,h)=>{st.className='cvst '+c;st.innerHTML=h};
const pick=fl=>{if(!fl)return;const okT=/\.(pdf|doc|docx)$/i.test(fl.name);if(!okT){say('err','Please choose a PDF or Word file (.pdf, .doc or .docx).');fi.value='';return}if(fl.size>MAX){say('err','That file is larger than 3 MB. Please choose a smaller file or email it to <a href="mailto:info@parakramindia.org">info@parakramindia.org</a>.');fi.value='';return}file=fl;st.className='cvst';ok.classList.add('on');ok.querySelector('span').textContent=fl.name+' ('+Math.max(1,Math.round(fl.size/1024))+' KB)'};
fi.addEventListener('change',()=>pick(fi.files[0]));
['dragenter','dragover'].forEach(ev=>drop.addEventListener(ev,e=>{e.preventDefault();drop.classList.add('dr')}));['dragleave','drop'].forEach(ev=>drop.addEventListener(ev,e=>{e.preventDefault();drop.classList.remove('dr')}));drop.addEventListener('drop',e=>{if(e.dataTransfer.files[0])pick(e.dataTransfer.files[0])});
ok.querySelector('button').onclick=()=>{file=null;fi.value='';ok.classList.remove('on')};
const g=i=>document.getElementById(i).value.trim();
const fallback=()=>{const sub=encodeURIComponent('Career application: '+g('vn'));const body=encodeURIComponent('Name: '+g('vn')+'\nPhone: '+g('vp')+'\nCity: '+g('vc')+'\nRole: '+g('vr')+'\n\n'+g('vm')+'\n\n(Please attach your resume to this email.)');const wa='https://wa.me/'+PH+'?text='+encodeURIComponent('Hello Parakram Security, I would like to apply. Name: '+g('vn')+', Phone: '+g('vp')+', City: '+g('vc')+', Role: '+g('vr'));say('err','We could not upload your resume online right now. Please <a href="mailto:info@parakramindia.org?subject='+sub+'&body='+body+'">email your application</a> or <a href="'+wa+'" target="_blank" rel="noopener">send it on WhatsApp</a>.')};
f.addEventListener('submit',async e=>{e.preventDefault();if(document.getElementById('vh').value)return;btn.disabled=true;btn.textContent='Sending...';say('wait','Sending your application...');
try{let b64='';if(file){b64=await new Promise((res,rej)=>{const r=new FileReader();r.onload=()=>res(String(r.result).split(',')[1]||'');r.onerror=rej;r.readAsDataURL(file)})}
const r=await fetch('/api/apply',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name:g('vn'),phone:g('vp'),email:g('ve'),city:g('vc'),role:g('vr'),message:g('vm'),fileName:file?file.name:'',fileType:file?file.type:'',fileBase64:b64})});
const j=await r.json().catch(()=>({}));if(r.ok&&j.ok){f.innerHTML='<div class="full" style="grid-column:1/-1;text-align:center;padding:30px 10px"><div style="width:64px;height:64px;border-radius:50%;background:var(--gold);display:grid;place-items:center;margin:0 auto 16px;font-size:30px">✓</div><h3 style="font-size:24px;color:var(--navy)">Application received</h3><p style="color:#4a5070;margin-top:8px">Thank you. Our team will review your details and contact you.</p></div>';return}
if(j.code==='too_large')say('err','That file is larger than 3 MB. Please choose a smaller file.');else if(j.code==='invalid')say('err','Please enter your name and a valid phone number.');else fallback()}catch(err){fallback()}
btn.disabled=false;btn.textContent='Submit application'})})();

/* 3D: tilt with glare, hero depth, emblem, image parallax */
(()=>{const fine=!mq('(pointer:coarse)')&&!REDUCE;
if(fine){$('.rcard,.sp2i,.imgc,.ic,.mos>div,.hx .fig').forEach(el=>{el.setAttribute('data-tilt','');if(getComputedStyle(el).position==='static')el.style.position='relative';const g=document.createElement('span');g.className='glare';el.appendChild(g);const lift=el.matches('.rcard,.ic')?-6:0,m=el.matches('.hx .fig')?4.5:6.5;
el.addEventListener('pointermove',e=>{const r=el.getBoundingClientRect(),x=(e.clientX-r.left)/r.width,y=(e.clientY-r.top)/r.height;el.classList.add('tilting');el.style.transform=`perspective(1000px) translateY(${lift}px) rotateX(${((.5-y)*m*2).toFixed(2)}deg) rotateY(${((x-.5)*m*2).toFixed(2)}deg) scale(1.015)`;el.style.setProperty('--gx',(x*100).toFixed(1)+'%');el.style.setProperty('--gy',(y*100).toFixed(1)+'%')});
el.addEventListener('pointerleave',()=>{el.classList.remove('tilting');el.style.transform=''})});
const hx=document.getElementById('hero');if(hx){let raf=0;hx.addEventListener('pointermove',e=>{if(raf)return;raf=requestAnimationFrame(()=>{raf=0;const r=hx.getBoundingClientRect();hx.style.setProperty('--mx',((e.clientX-r.left)/r.width-.5).toFixed(3));hx.style.setProperty('--my',((e.clientY-r.top)/r.height-.5).toFixed(3))})});hx.addEventListener('pointerleave',()=>{hx.style.setProperty('--mx',0);hx.style.setProperty('--my',0)})}}
$('.emb3d').forEach(b=>{const a=document.createElement('div');a.className='emb-in';const w=document.createElement('div');w.className='emb-sw';for(let i=0;i<16;i++){const im=new Image();im.src='/logo.png';im.alt='';im.width=170;im.height=170;im.decoding='async';im.style.transform='translateZ('+((i-8)*2.4)+'px)';im.style.filter=i<15?'brightness('+(0.4+i*0.038).toFixed(2)+')':'none';w.appendChild(im)}a.appendChild(w);b.appendChild(a);if(fine)b.addEventListener('pointermove',e=>{const r=b.getBoundingClientRect();b.style.setProperty('--ex',((e.clientX-r.left)/r.width-.5).toFixed(3));b.style.setProperty('--ey',((e.clientY-r.top)/r.height-.5).toFixed(3))})});
if(!REDUCE){const ps=$('.sp2i img,.mos img,.pbn .pbg');if(ps.length){let t=0;const upd=()=>{t=0;const vh=innerHeight;ps.forEach(el=>{const host=el.closest('.sp2i,.mos>div')||el;const r=host.getBoundingClientRect();if(r.bottom<-60||r.top>vh+60)return;const p=((r.top+r.height/2)-vh/2)/vh;el.style.setProperty('--py',(p*-28).toFixed(1)+'px')})};addEventListener('scroll',()=>{if(!t)t=requestAnimationFrame(upd)},{passive:true});upd()}}
})();
/* planner wizard */
(()=>{const w=document.getElementById('wz'),st=$('#wz .step'),bars=$('#wz .st i');let s=0;const show=n=>{s=n;st.forEach((e,k)=>e.classList.toggle('on',k==n));bars.forEach((e,k)=>e.classList.toggle('on',k<=n))};
$('#wz [data-nx]').forEach(b=>b.onclick=()=>show(Math.min(s+1,3)));$('#wz [data-bk]').forEach(b=>b.onclick=()=>show(Math.max(s-1,0)));
document.getElementById('send').onclick=()=>{const sv=$('#wz .step:first-of-type input:checked').map(i=>i.value).join(', ')||'Not specified';const v=n=>(document.querySelector(`#wz input[name=${n}]:checked`)||{}).value||'Not specified';
const m=`Hello Parakram Security, I'd like a security plan.%0A%0A*Services:* ${sv}%0A*Site type:* ${v('site')}%0A*Team size:* ${v('g')}%0A*Coverage:* ${v('sh')}%0A*Name:* ${pn.value}%0A*Phone:* ${pp.value}%0A*Location:* ${pc.value}`;if(!pp.value.trim()){toast('Please enter your phone number.');pp.focus();return}open(`https://wa.me/${PH}?text=${m}`,'_blank');toast('Opening WhatsApp with your plan…')}})();
/* contact form -> WhatsApp */
cf.onsubmit=e=>{e.preventDefault();const m=`Hello Parakram Security,%0A*Name:* ${cn.value}%0A*Phone:* ${cp.value}%0A*Email:* ${ce.value}%0A*Service:* ${cs.value||'Not specified'}%0A*Details:* ${cm.value}`;open(`https://wa.me/${PH}?text=${m}`,'_blank');toast('Opening WhatsApp…')};
</script>
</body></html>'''
mq=['Trained &amp; Verified Personnel','Customized Solutions','24/7 Availability','Support for Multiple Sites','Professionalism','Integrity','Courtesy','Your Safety Is Our Mission']
M=json.load(open(os.path.join(H,'india_paths.json')))
mapsvg=f'<svg id="imap" viewBox="0 0 {M["w"]} {M["h"]}" role="img" aria-label="Interactive map of India"><g>'+''.join(f'<path class="st{" hq" if x["n"]=="Uttarakhand" else ""}" data-n="{x["n"].replace("&","&amp;")}" d="{x["d"]}"/>' for x in M['states'])+f'</g><g class="pinG" transform="translate({M["pin"][0]} {M["pin"][1]})"><circle class="rd" r="14"/><circle class="rd r2" r="14"/><circle class="pd" r="9"/></g></svg>'
for _k in ['ind','com','hos','bnk','res','edu']:
    html=html.replace('@@IC_'+_k+'@@',IC[_k])
    html=html.replace('@@I_'+_k+'@@',IC[{'ind':'ind','com':'com','hos':'hos','bnk':'bnk','res':'res','edu':'edu'}[_k]])
html=html.replace('@@ALLI@@','<svg viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/></svg>')
html=(html.replace('@@MAP@@',mapsvg).replace('@@MEGA@@',mega).replace('@@TABS@@',tabs).replace('@@PANELS@@',panels).replace('@@CHIPS@@',chips)
 .replace('@@MARQUEE@@',''.join(f'<span>{x}</span>' for x in mq*2))
 .replace('@@OPTS@@',''.join(f'<option>{h}</option>' for _,h,*_ in SV)))
open(os.path.join(H,'..','index.html'),'w').write(html)
print(len(html))
