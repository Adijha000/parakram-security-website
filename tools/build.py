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
SV=[('man','Manned Security','Trained, verified guards for round-the-clock protection of your premises.','operations','30% 40%'),
('arm','Armed Security','Disciplined armed personnel for high-security requirements.','hero','' ),
('ind','Industrial Security','Protection for plants, warehouses and industrial campuses.','training','60% 50%'),
('com','Commercial Security','Professional guards for offices and business premises.','operations','80% 40%'),
('res','Residential Security','Courteous, reliable security for homes and societies.','about','40% 50%'),
('hos','Hospital Security','Calm, courteous security for hospitals and healthcare facilities.','about','70% 30%'),
('edu','Educational Security','Safe, well-supervised campuses for schools and institutions.','training','30% 60%'),
('bnk','Bank &amp; ATM Security','Vigilant, verified personnel for branches and ATMs.','operations','55% 35%')]
tabs=panels=mega=chips=''
for k,(ic,h,p,im,pos) in enumerate(SV):
    on=' on' if k==0 else ''
    alt=h.replace('&amp;','and')
    tabs+=f'<button class="tb{on}" data-k="{k}" role="tab"><span class="ti">{IC[ic]}</span><span class="tt">{h}</span><span class="ar">→</span></button>'
    media=(f'<div class="pm cut"><div class="bgc"></div><img src="img/parakram-hero-guard.webp" alt="{alt}" loading="lazy"></div>' if im=='hero'
      else f'<div class="pm"><img src="img/parakram-{im}.webp" alt="{alt}" style="object-position:{pos}" loading="lazy"></div>')
    panels+=f'<article class="pn{on}" data-k="{k}">{media}<div class="pb"><div class="num">0{k+1}<small>/ 08</small></div><h3>{h}</h3><p>{p}</p><ul><li>Trained &amp; verified personnel</li><li>Available 24/7</li><li>Customized to your site</li></ul><a class="btn btn-g" href="#planner">Plan this service →</a></div></article>'
    mega+=f'<a href="#services" data-go="{k}"><i>{IC[ic]}</i>{h}</a>'
    chips+=f'<label class="chp"><input type="checkbox" value="{alt}"><span>{IC[ic]}{h}</span></label>'

html=r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Parakram Security India | Your Safety Is Our Mission</title>
<meta name="description" content="Parakram Security India Pvt. Ltd. — manned, armed, industrial, commercial, residential, hospital, educational and bank &amp; ATM security. 9+ years, 1,500+ trained professionals, 24/7. Haridwar, Uttarakhand.">
<meta name="theme-color" content="#050d3a">
<meta property="og:title" content="Parakram Security India | Your Safety Is Our Mission"><meta property="og:description" content="Professionally managed private security — trained, verified personnel, customized solutions, 24/7."><meta property="og:type" content="website"><meta property="og:image" content="img/parakram-operations.webp">
<link rel="icon" href="favicon.png" type="image/png"><link rel="apple-touch-icon" href="logo.png"><link rel="preload" as="image" href="img/parakram-hero-guard.webp" type="image/webp" fetchpriority="high">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Inter:wght@400;500;600;700&family=Manrope:wght@600;700;800&display=swap" rel="stylesheet">
<script type="application/ld+json">{"@context":"https://schema.org","@type":"SecurityService","name":"Parakram Security India Pvt. Ltd.","url":"https://parakram-website.vercel.app","logo":"logo.png","email":"info@parakramindia.org","telephone":"+919105909006","foundingDate":"2017","address":{"@type":"PostalAddress","streetAddress":"6-A Sandesh Nagar, Kankhal","addressLocality":"Haridwar","addressRegion":"Uttarakhand","postalCode":"249408","addressCountry":"IN"},"aggregateRating":{"@type":"AggregateRating","ratingValue":"4.9","reviewCount":"1200"}}</script>
<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"What types of security services do you provide?","acceptedAnswer":{"@type":"Answer","text":"Manned, Armed, Industrial, Commercial, Residential, Hospital, Educational, and Bank & ATM security."}},{"@type":"Question","name":"Is your service available 24/7?","acceptedAnswer":{"@type":"Answer","text":"Yes, our services are available 24/7."}},{"@type":"Question","name":"Can solutions be customized to my site?","acceptedAnswer":{"@type":"Answer","text":"Yes — we design customized security solutions around your needs, including multi-site support."}}]}</script>
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
header{position:sticky;top:0;z-index:60;background:rgba(255,255,255,.94);backdrop-filter:saturate(1.6) blur(14px);border-bottom:1px solid var(--line);transition:box-shadow .3s}
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
.fb{border-top:1px solid rgba(255,255,255,.1);padding:26px 0;display:flex;justify-content:space-between;font-size:13px;flex-wrap:wrap;gap:10px}
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
/* ===== responsive ===== */
@media(max-width:1180px){
.util{display:none}.nav{height:68px}.brand img{height:44px}.brand b{font-size:19px}
nav{position:fixed;top:68px;left:0;right:0;bottom:0;background:#fff;transform:translateX(100%);transition:transform .35s var(--ease);overflow:auto;padding:10px 22px 120px;z-index:59}nav.open{transform:none}
nav>ul{flex-direction:column}nav>ul>li>a{padding:18px 2px;font-size:19px;border-bottom:1px solid var(--line);font-family:Manrope;font-weight:700}nav>ul>li>a:after{display:none}
.dd .menu{position:static;transform:none;width:auto;opacity:1;visibility:visible;box-shadow:none;border:0;display:none;grid-template-columns:1fr;background:var(--bg);border-radius:12px;margin:8px 0}.dd.o .menu{display:block}.mp{display:none}.mg{grid-template-columns:1fr;padding:8px}
.nav>.btn{display:none}.burger{display:block}
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
</style>
</head>
<body>
<a class="skip" href="#top">Skip to content</a>
<div id="pre" aria-hidden="true"><img src="logo.png" alt=""><i></i></div>
<div id="pg"></div>
<div id="toast" role="status" aria-live="polite"></div>
<a class="sidetab" href="#contact">Get in Touch</a>
<div class="util"><div class="wrap"><div class="l"><span class="pulse"></span>Control room online · 24/7 <span class="ist" id="ist"></span></div><div class="r"><a href="tel:+919105909006">+91 91059 09006</a><a href="mailto:info@parakramindia.org">info@parakramindia.org</a><a href="#careers">Careers</a></div></div></div>
<header id="hd"><div class="wrap nav">
<a class="brand" href="#top"><img src="logo.png" alt="Parakram shield logo" width="56" height="56"><div><b>PARAKRAM</b><small>SECURITY INDIA PVT. LTD.</small></div></a>
<nav id="nav"><ul>
<li><a href="#about">About</a></li>
<li class="dd"><a href="#services">Services ▾</a><div class="menu"><div class="mg">@@MEGA@@</div><div class="mp"><img src="img/parakram-operations.webp" alt="" loading="lazy"><b>Customized security solutions for every environment</b><a href="#planner">Plan your security →</a></div></div></li>
<li><a href="#industries">Industries</a></li><li><a href="#planner">Security Planner</a></li><li><a href="#why">Why Parakram</a></li><li><a href="#careers">Careers</a></li><li><a href="#faq">FAQ</a></li></ul></nav>
<a class="btn btn-n" href="#contact" style="padding:13px 24px">Get Started</a><button class="burger" id="bg" aria-label="Menu" aria-expanded="false"><i></i></button>
</div></header>

<main id="top">
<section class="hx" id="hero" style="padding:0" aria-roledescription="carousel">
<div class="hglow" id="hglow"></div><div class="slide on"><div class="bgc"></div>
<div class="fig" id="fig"><div class="halo"></div><img src="img/parakram-hero-guard.webp" alt="Parakram security officer" width="800" height="1000" fetchpriority="high" decoding="async"></div>
<div class="wrap hxg"><div class="tx"><div class="eyebrow">Your Safety Is Our Mission</div>
<h1><span class="ln"><span>A life with</span></span><span class="ln"><span><em>full protection.</em></span></span></h1>
<p class="lead">Professionally managed private security since 2017 — disciplined manpower, rigorous training and deep-rooted Indian values to protect people, property and operations.</p>
<div class="cta"><a class="btn btn-g" href="#planner">Plan Your Security →</a><a class="btn btn-o" href="#services">Our Services</a></div></div></div></div>
<div class="slide"><div class="bgc"></div><div class="ph" style="--bg:url(img/parakram-operations.webp)"></div>
<div class="wrap hxg"><div class="tx"><div class="eyebrow">Corporate &amp; Commercial</div>
<h2 class="hh"><span class="ln"><span>Protection for</span></span><span class="ln"><span><em>every premises.</em></span></span></h2>
<p class="lead">Trained, verified guards with excellent site coordination — for offices, campuses and business environments.</p>
<div class="cta"><a class="btn btn-g" href="#contact">Get Started →</a><a class="btn btn-o" href="#industries">Industries We Protect</a></div></div></div></div>
<div class="slide"><div class="bgc"></div><div class="ph" style="--bg:url(img/parakram-training.webp)"></div>
<div class="wrap hxg"><div class="tx"><div class="eyebrow">Trained &amp; Verified Personnel</div>
<h2 class="hh"><span class="ln"><span>Trained. Verified.</span></span><span class="ln"><span><em>Ready to serve.</em></span></span></h2>
<p class="lead">Disciplined recruitment and rigorous training ensure professionalism, integrity and courtesy at every site.</p>
<div class="cta"><a class="btn btn-g" href="#why">Why Parakram →</a><a class="btn btn-o" href="#contact">Talk to Us</a></div></div></div></div>
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

<div class="mq" aria-hidden="true"><div class="mt">@@MARQUEE@@</div></div>

<section id="about"><div class="wrap two">
<div class="abt rv"><div class="eyebrow dk">About Parakram</div><h2 class="h2">Protecting people, property &amp; <em>operations.</em></h2>
<p>Parakram Security India Private Limited was established in 2017 as a professionally managed private security company.</p>
<p>We combine disciplined manpower, rigorous training and deep-rooted Indian values to protect people, property and operations — with personnel known for professionalism, integrity and courtesy.</p>
<div class="vals"><div><b>Professionalism</b><span>Disciplined, trained personnel</span></div><div><b>Integrity</b><span>Verified, trustworthy teams</span></div><div><b>Courtesy</b><span>Respectful service, always</span></div></div>
<a class="btn btn-n" href="#contact">Get Started →</a></div>
<div class="imgc rv"><div class="im"><img src="img/parakram-about.webp" alt="Parakram security team" width="1200" height="896" loading="lazy" decoding="async"></div><div class="bd"><b>2017</b><span>Established · Haridwar</span></div></div>
</div></section>

<section id="services" class="bg"><div class="wrap">
<div class="sec-h rv"><div class="eyebrow dk">Security Services</div><h2 class="h2">Eight services. One standard of <em>excellence.</em></h2><p>Customized security solutions for every environment.</p></div>
<div class="sx rv"><div class="tl" role="tablist">@@TABS@@</div><div class="pw">@@PANELS@@</div></div>
</div></section>

<section id="planner" class="plan"><div class="wrap">
<div class="rv"><div class="eyebrow">Security Planner</div><h2 class="h2">Tell us what you need. <em>We'll design the plan.</em></h2>
<p class="s">Answer four quick questions and our team will respond with a solution customized to your site — no obligation.</p>
<ul><li>Customized security solutions</li><li>Trained &amp; verified personnel</li><li>Multi-site support</li><li>Available 24/7</li></ul></div>
<div class="wz rv" id="wz">
<div class="st"><i class="on"></i><i></i><i></i><i></i></div>
<div class="step on"><h3>Which services do you need?</h3><p class="sub">Select one or more.</p><div class="chips">@@CHIPS@@</div><div class="nav2"><span></span><button class="btn btn-n" data-nx>Continue →</button></div></div>
<div class="step"><h3>What type of site?</h3><p class="sub">Choose the closest match.</p><div class="chips" id="sites">
<label class="chp"><input type="radio" name="site" value="Industrial"><span>Industrial</span></label><label class="chp"><input type="radio" name="site" value="Corporate / Commercial"><span>Corporate / Commercial</span></label><label class="chp"><input type="radio" name="site" value="Healthcare"><span>Healthcare</span></label><label class="chp"><input type="radio" name="site" value="Banking / ATM"><span>Banking / ATM</span></label><label class="chp"><input type="radio" name="site" value="Residential"><span>Residential</span></label><label class="chp"><input type="radio" name="site" value="Educational"><span>Educational</span></label></div>
<div class="nav2"><button class="bk" data-bk>← Back</button><button class="btn btn-n" data-nx>Continue →</button></div></div>
<div class="step"><h3>Coverage &amp; team size</h3><p class="sub">Approximate is fine.</p><div class="chips">
<label class="chp"><input type="radio" name="g" value="1–5 personnel"><span>1–5 personnel</span></label><label class="chp"><input type="radio" name="g" value="6–20 personnel"><span>6–20 personnel</span></label><label class="chp"><input type="radio" name="g" value="21–50 personnel"><span>21–50 personnel</span></label><label class="chp"><input type="radio" name="g" value="50+ personnel"><span>50+ personnel</span></label><label class="chp"><input type="radio" name="sh" value="24/7 coverage"><span>24/7 coverage</span></label><label class="chp"><input type="radio" name="sh" value="Day shift"><span>Day shift</span></label><label class="chp"><input type="radio" name="sh" value="Night shift"><span>Night shift</span></label><label class="chp"><input type="radio" name="sh" value="Multiple sites"><span>Multiple sites</span></label></div>
<div class="nav2"><button class="bk" data-bk>← Back</button><button class="btn btn-n" data-nx>Continue →</button></div></div>
<div class="step"><h3>Where should we reach you?</h3><p class="sub">We'll open WhatsApp with your plan pre-filled.</p><input class="t" id="pn" placeholder="Your name"><input class="t" id="pp" type="tel" placeholder="Phone number"><input class="t" id="pc" placeholder="City / site location"><p class="note">Your details are shared only with the Parakram team.</p>
<div class="nav2"><button class="bk" data-bk>← Back</button><button class="btn btn-g" id="send">Send on WhatsApp →</button></div></div>
</div></div></section>

<section id="industries"><div class="wrap">
<div class="sec-h rv"><div class="eyebrow dk">Industries We Protect</div><h2 class="h2">Trusted where safety <em>matters most.</em></h2></div>
<div class="ind">
<a class="ic rv" style="--bg2:url(img/parakram-training.webp)" href="#planner"><span class="n">01</span><span class="go">→</span><h3>Industrial</h3><span>Plants · Warehouses</span></a>
<a class="ic rv" style="--bg2:url(img/parakram-operations.webp)" href="#planner"><span class="n">02</span><span class="go">→</span><h3>Corporate</h3><span>Offices · Business premises</span></a>
<a class="ic rv" style="--bg2:url(img/parakram-about.webp)" href="#planner"><span class="n">03</span><span class="go">→</span><h3>Healthcare</h3><span>Hospitals · Clinics</span></a>
<a class="ic rv" style="--bg2:url(img/parakram-operations.webp);--pos:85% 50%" href="#planner"><span class="n">04</span><span class="go">→</span><h3>Banking</h3><span>Branches · ATMs</span></a>
</div></div></section>

<section class="band" style="background-image:url(img/parakram-operations.webp)"><div class="wrap rv"><div class="eyebrow" style="justify-content:center">Trusted Protection</div><h2>Professionalism. Integrity. <em>Courtesy.</em></h2><p>Personnel who protect people, property and operations — 24/7.</p><a class="btn btn-g" href="#contact">Get Started →</a></div></section>

<section id="why" class="bg"><div class="wrap">
<div class="sec-h rv"><div class="eyebrow dk">Why Us</div><h2 class="h2">Why leaders choose <em>Parakram.</em></h2></div>
<div class="pil">
<div class="pl rv"><div class="big" data-n="9" data-s="+">0</div><h3>Years of Experience</h3><p>A professionally managed security company operating since 2017.</p></div>
<div class="pl rv"><div class="big" data-n="1500" data-s="+">0</div><h3>Trained &amp; Verified Personnel</h3><p>Disciplined recruitment and rigorous training for every guard.</p></div>
<div class="pl rv"><div class="big" data-n="100" data-s="%">0</div><h3>Customized Solutions</h3><p>Services designed around your site, your risk and your operations.</p></div></div>
<div class="proc"><h3 class="h2 rv">How we get you protected.</h3>
<div class="steps rv"><div class="sp"><i>1</i><div><b>Consult</b><span>Tell us your needs</span></div></div><div class="sp"><i>2</i><div><b>Assess</b><span>We study your site</span></div></div><div class="sp"><i>3</i><div><b>Customize</b><span>A tailored security plan</span></div></div><div class="sp"><i>4</i><div><b>Deploy</b><span>Trained, verified personnel</span></div></div><div class="sp"><i>5</i><div><b>Supervise</b><span>Ongoing quality checks</span></div></div></div></div>
</div></section>

<section id="coverage"><div class="wrap cov">
<div class="map rv" id="map">@@MAP@@<div class="mtip" id="mtip"></div><div class="mc"><div><b id="mn">Uttarakhand</b><span id="ms">Headquarters · 6-A Sandesh Nagar, Kankhal, Haridwar – 249408</span></div><a class="btn btn-n" id="mb" style="padding:12px 20px" href="#contact">Contact Us</a></div><div class="mhint">Hover or tap a state</div></div>
<div class="covt rv"><div class="eyebrow dk">Coverage</div><h2 class="h2">Local roots. <em>Multi-site</em> reach across India.</h2>
<ul><li><i>◎</i><div><b>Headquartered in Haridwar</b><span>Registered office in Kankhal, Haridwar, Uttarakhand.</span></div></li><li><i>⇄</i><div><b>Multi-site support</b><span>One partner across all your locations.</span></div></li><li><i>24</i><div><b>Always available</b><span>Services available 24/7.</span></div></li></ul></div>
</div></section>

<section class="tm"><div class="wrap rv"><div class="rate"><b>4.9</b>★★★★★ Rated by 1,200+ clients</div><h2 class="h2">What our <em>clients say.</em></h2>
<div class="qs"><div class="q on"><div class="st">★★★★★</div><blockquote>Well-trained guards and excellent site coordination.</blockquote><cite>Facility Manager</cite></div>
<div class="q"><div class="st">★★★★★</div><blockquote>Dependable security routines that keep our operations running smoothly.</blockquote><cite>Industrial Client</cite></div>
<div class="q"><div class="st">★★★★★</div><blockquote>Supervisors are accessible and responsive whenever we need them.</blockquote><cite>Institutional Client</cite></div></div>
<div class="qd"><button class="on" aria-label="Quote 1"></button><button aria-label="Quote 2"></button><button aria-label="Quote 3"></button></div></div></section>

<section id="faq"><div class="wrap"><div class="fq">
<div class="sec-h rv"><div class="eyebrow dk">FAQ</div><h2 class="h2">Answers <em>before you ask.</em></h2><p>Still have questions? Call +91 91059 09006 or email info@parakramindia.org.</p></div>
<div class="rv"><details open><summary>What types of security services do you provide?</summary><p>Manned, Armed, Industrial, Commercial, Residential, Hospital, Educational, and Bank &amp; ATM security.</p></details>
<details><summary>How are your personnel trained and verified?</summary><p>Through disciplined recruitment and rigorous training, so every guard is trained and verified before deployment.</p></details>
<details><summary>Is your service available 24/7?</summary><p>Yes, our services are available 24/7.</p></details>
<details><summary>Can solutions be customized to my site?</summary><p>Yes — we design customized security solutions around your needs, including multi-site support.</p></details>
<details><summary>How do I get started?</summary><p>Use our Security Planner, call +91 91059 09006, or email info@parakramindia.org.</p></details></div></div>
<div class="careers rv" id="careers"><div><div class="eyebrow">Careers</div><h3>Serve with <em>Parakram.</em></h3><p>Join a disciplined, professionally managed team built on integrity and courtesy.</p><a class="btn btn-g" href="mailto:info@parakramindia.org?subject=Career%20enquiry">Apply Now →</a></div>
<div class="req"><div class="row"><span>Culture</span><b>Professionalism, integrity, courtesy</b></div><div class="row"><span>Training</span><b>Rigorous &amp; structured</b></div><div class="row"><span>Team</span><b>1,500+ professionals</b></div><div class="row"><span>Apply</span><b>info@parakramindia.org</b></div></div></div>
</div></section>

<section id="contact" class="bg"><div class="wrap"><div class="contact rv">
<div class="l"><h3>Let's secure your world.</h3>
<p><b>Address</b>6-A Sandesh Nagar, Kankhal, Haridwar – 249408, Uttarakhand</p>
<p><b>Phone</b><a href="tel:+919105909006">+91 91059 09006</a> · <a href="tel:+918937000489">+91 89370 00489</a> · <a href="tel:+919105909000">+91 91059 09000</a></p>
<p><b>Email</b><a href="mailto:info@parakramindia.org">info@parakramindia.org</a></p></div>
<form id="cf"><input required id="cn" placeholder="Full name"><input required id="cp" type="tel" placeholder="Phone"><input class="full" id="ce" type="email" placeholder="Email">
<select class="full" id="cs"><option value="">Service required</option>@@OPTS@@</select>
<textarea class="full" id="cm" placeholder="Tell us about your site and requirements"></textarea>
<button class="btn btn-n full" style="justify-content:center">Get Started →</button></form></div></div></section>
</main>

<div class="ctab"><div class="wrap"><div><h2>Ready to secure your premises?</h2><p>Speak to our team — available 24/7.</p></div><div class="cta2"><a class="btn btn-g" href="#planner">Plan Your Security →</a><a class="btn btn-o" href="tel:+919105909006">+91 91059 09006</a></div></div></div>
<footer><div class="wrap"><div class="fg">
<div><div class="brand" style="margin-bottom:18px"><img src="logo.png" alt="" style="height:64px"><div><b style="color:#fff">PARAKRAM</b><small style="color:#aab0d6">SECURITY INDIA PVT. LTD.</small></div></div><p style="font-size:14.5px;max-width:320px">We aim to provide you with a life with full protection.</p></div>
<div><h4>Company</h4><ul><li><a href="#about">About</a></li><li><a href="#why">Why Parakram</a></li><li><a href="#coverage">Coverage</a></li><li><a href="#careers">Careers</a></li><li><a href="#faq">FAQ</a></li></ul></div>
<div><h4>Services</h4><ul><li><a href="#services">Manned</a></li><li><a href="#services">Armed</a></li><li><a href="#services">Industrial</a></li><li><a href="#services">Commercial</a></li><li><a href="#services">Bank &amp; ATM</a></li></ul></div>
<div><h4>Contact</h4><ul><li>6-A Sandesh Nagar, Kankhal, Haridwar 249408</li><li><a href="tel:+919105909006">+91 91059 09006</a></li><li><a href="mailto:info@parakramindia.org">info@parakramindia.org</a></li></ul></div></div>
<div class="fb"><span>© 2026 Parakram Security India Pvt. Ltd. All rights reserved.</span><span>Website by AIBOOTSTRAPPER</span></div></div></footer>
<div class="mbar"><a href="tel:+919105909006">Call Now</a><a href="#planner">Get Started</a></div>
<button class="top" id="top2" aria-label="Back to top">↑</button>
<a class="wa" href="https://wa.me/919105909006" aria-label="WhatsApp"><svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 0 0-8.6 15l-1.4 5 5.2-1.4A10 10 0 1 0 12 2zm5.4 14.2c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.2-.7-2.7-1.1-4.4-3.8-4.5-4-.1-.1-1.1-1.5-1.1-2.8s.7-2 1-2.3c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 2c.1.2.1.3 0 .5l-.3.4-.4.4c-.1.1-.3.3-.1.6.2.3.7 1.1 1.5 1.8 1 .9 1.900 1.200 2.200 1.300.3.1.4.1.6-.1l.8-1c.2-.3.4-.2.6-.1l1.900.9c.3.1.5.2.6.3.1.2.1.8-.1 1.400z"/></svg></a>
<script>
const $=s=>[...document.querySelectorAll(s)],mq=q=>matchMedia(q).matches,PH='919105909006';
/* header/progress/back-to-top */
const hd=document.getElementById('hd'),pg=document.getElementById('pg'),t2=document.getElementById('top2');
addEventListener('scroll',()=>{hd.classList.toggle('sh',scrollY>10);pg.style.width=(scrollY/(document.documentElement.scrollHeight-innerHeight)*100)+'%';t2.classList.toggle('v',scrollY>900)},{passive:true});
t2.onclick=()=>scrollTo({top:0,behavior:'smooth'});
/* mobile nav */
const nav=document.getElementById('nav'),bg=document.getElementById('bg');
bg.onclick=()=>{const o=nav.classList.toggle('open');bg.classList.toggle('x',o);bg.setAttribute('aria-expanded',o);document.body.style.overflow=o?'hidden':''};
$('nav a').forEach(a=>a.addEventListener('click',e=>{if(a.parentNode.classList.contains('dd')&&mq('(max-width:1180px)')&&e.target===a){e.preventDefault();a.parentNode.classList.toggle('o');return}nav.classList.remove('open');bg.classList.remove('x');document.body.style.overflow=''}));
/* reveal */
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.1});
const io2=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io2.unobserve(e.target)}}),{threshold:.3});
$('.rv').forEach((e,i)=>{e.style.transitionDelay=(i%4)*80+'ms';io.observe(e)});
/* counters */
const co=new IntersectionObserver(es=>es.forEach(e=>{if(!e.isIntersecting)return;const el=e.target,n=+el.dataset.n,d=+el.dataset.d||0,s=el.dataset.s||'';let t0=null;const f=t=>{t0=t0||t;const p=Math.min((t-t0)/1800,1),v=n*(1-Math.pow(1-p,4));el.innerHTML=(d?v.toFixed(d):Math.round(v).toLocaleString('en-IN'))+(s?'<sup>'+s+'</sup>':'');if(p<1)requestAnimationFrame(f)};requestAnimationFrame(f);co.unobserve(el)}),{threshold:.5});
$('[data-n]').forEach(e=>co.observe(e));
/* hero slider */
(()=>{const sl=$('.slide'),ds=$('.d');let i=0,t;const go=n=>{i=(n+sl.length)%sl.length;sl.forEach((e,k)=>e.classList.toggle('on',k==i));ds.forEach((e,k)=>{e.classList.remove('on');if(k==i){void e.offsetWidth;e.classList.add('on')}});clearTimeout(t);t=setTimeout(()=>go(i+1),6500)};
ds.forEach((d,k)=>d.onclick=()=>go(k));document.getElementById('pv').onclick=()=>go(i-1);document.getElementById('nx').onclick=()=>go(i+1);t=setTimeout(()=>go(1),6500);
const fig=document.getElementById('fig'),hx=document.getElementById('hero');if(!mq('(pointer:coarse)'))hx.addEventListener('mousemove',e=>{const x=(e.clientX/innerWidth-.5)*16,y=(e.clientY/innerHeight-.5)*10;fig.style.transform=`translate(${x}px,${y}px)`})})();
/* services */
(()=>{const tb=$('.tb'),pn=$('.pn');const sel=k=>{tb.forEach((e,i)=>e.classList.toggle('on',i==k));pn.forEach((e,i)=>e.classList.toggle('on',i==k));if(mq('(max-width:980px)'))tb[k].scrollIntoView({inline:'center',block:'nearest',behavior:'smooth'})};
tb.forEach((b,k)=>{b.onclick=()=>sel(k);b.onmouseenter=()=>{if(!mq('(max-width:980px)'))sel(k)}});$('[data-go]').forEach(a=>a.addEventListener('click',()=>sel(+a.dataset.go)))})();
/* spotlight cards */
$('.pl').forEach(c=>c.addEventListener('mousemove',e=>{const r=c.getBoundingClientRect();c.style.setProperty('--mx',(e.clientX-r.left)+'px');c.style.setProperty('--my',(e.clientY-r.top)+'px')}));
/* testimonials */
(()=>{const q=$('.q'),d=$('.qd button');let i=0,t;const go=n=>{i=n%q.length;q.forEach((e,k)=>e.classList.toggle('on',k==i));d.forEach((e,k)=>e.classList.toggle('on',k==i));clearTimeout(t);t=setTimeout(()=>go(i+1),5500)};d.forEach((b,k)=>b.onclick=()=>go(k));t=setTimeout(()=>go(1),5500)})();

/* --- enhancement JS --- */
const pre=document.getElementById('pre');addEventListener('DOMContentLoaded',()=>setTimeout(()=>pre.classList.add('off'),250));setTimeout(()=>pre.classList.add('off'),1200);
const toast=m=>{const t=document.getElementById('toast');t.textContent=m;t.classList.add('on');clearTimeout(t._h);t._h=setTimeout(()=>t.classList.remove('on'),3200)};
/* split headings */
$('.h2').forEach(h=>{let i=0;const wrap=n=>{[...n.childNodes].forEach(c=>{if(c.nodeType===3){const f=document.createDocumentFragment();c.textContent.split(/(\s+)/).forEach(t=>{if(!t)return;if(/^\s+$/.test(t)){f.appendChild(document.createTextNode(' '));return}const w=document.createElement('span');w.className='w';const b=document.createElement('span');b.textContent=t;b.style.setProperty('--i',i++);w.appendChild(b);f.appendChild(w)});c.replaceWith(f)}else if(c.nodeType===1)wrap(c)})};wrap(h);h.setAttribute('aria-label',h.textContent);io2.observe(h)});
/* scrollspy */
const spy=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){$('nav>ul>li>a').forEach(a=>a.classList.toggle('act',a.getAttribute('href')==='#'+e.target.id))}}),{rootMargin:'-45% 0px -50% 0px'});
$('main section[id]').forEach(x=>spy.observe(x));
/* tilt cards */
if(!mq('(pointer:coarse)'))$('.ic').forEach(c=>{c.addEventListener('mousemove',e=>{const r=c.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;c.style.transform=`perspective(1000px) translateY(-8px) rotateX(${-y*7}deg) rotateY(${x*9}deg)`});c.addEventListener('mouseleave',()=>c.style.transform='')});
/* magnetic buttons */
if(!mq('(pointer:coarse)'))$('.btn-g,.btn-n').forEach(b=>{b.addEventListener('mousemove',e=>{const r=b.getBoundingClientRect();b.style.transform=`translate(${(e.clientX-r.left-r.width/2)*.18}px,${(e.clientY-r.top-r.height/2)*.28}px)`});b.addEventListener('mouseleave',()=>b.style.transform='')});
/* hero glow + scroll fade */
(()=>{const hx=document.getElementById('hero'),g=document.getElementById('hglow');if(!mq('(pointer:coarse)'))hx.addEventListener('mousemove',e=>{const r=hx.getBoundingClientRect();g.style.left=(e.clientX-r.left)+'px';g.style.top=(e.clientY-r.top)+'px'});
addEventListener('scroll',()=>{if(scrollY<900){const y=scrollY;$('.hxg .tx').forEach(t=>{t.style.transform=`translateY(${y*.12}px)`;t.style.opacity=Math.max(0,1-y/650)})}},{passive:true})})();
/* parallax on about image + band */
addEventListener('scroll',()=>{const im=document.querySelector('.imgc .im img');if(im){const r=im.getBoundingClientRect();if(r.top<innerHeight&&r.bottom>0)im.style.objectPosition=`50% ${50+(r.top/innerHeight-.5)*18}%`}},{passive:true});

/* ist clock */
(()=>{const e=document.getElementById('ist');const t=()=>{e.textContent=new Date().toLocaleTimeString('en-IN',{timeZone:'Asia/Kolkata',hour:'2-digit',minute:'2-digit',second:'2-digit',hour12:true})+' IST'};t();setInterval(t,1000)})();
/* india map */
(()=>{const m=document.getElementById('map'),tip=document.getElementById('mtip'),mn=document.getElementById('mn'),ms=document.getElementById('ms'),mb=document.getElementById('mb'),sts=$('.st');
const pick=p=>{const n=p.dataset.n;sts.forEach(x=>x.classList.toggle('sel',x===p));mn.textContent=n;
if(n==='Uttarakhand'){ms.textContent='Headquarters · 6-A Sandesh Nagar, Kankhal, Haridwar – 249408';mb.textContent='Contact Us';mb.href='#contact';mb.onclick=null}
else{ms.textContent='Multi-site support — tell us about your site in '+n+'.';mb.textContent='Enquire for '+n+' →';mb.href='#planner';mb.onclick=()=>{const f=document.getElementById('pc');if(f)f.value=n}}};
sts.forEach(p=>{p.addEventListener('mousemove',e=>{const r=m.getBoundingClientRect();tip.textContent=p.dataset.n+(p.classList.contains('hq')?' · HQ':'');tip.style.left=(e.clientX-r.left)+'px';tip.style.top=(e.clientY-r.top)+'px';tip.classList.add('on')});p.addEventListener('mouseleave',()=>tip.classList.remove('on'));p.addEventListener('click',()=>pick(p));p.setAttribute('tabindex','0');p.setAttribute('role','button');p.setAttribute('aria-label',p.dataset.n);p.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();pick(p)}})});
pick(document.querySelector('.st.hq'))})();
/* planner wizard */
(()=>{const w=document.getElementById('wz'),st=$('#wz .step'),bars=$('#wz .st i');let s=0;const show=n=>{s=n;st.forEach((e,k)=>e.classList.toggle('on',k==n));bars.forEach((e,k)=>e.classList.toggle('on',k<=n))};
$('#wz [data-nx]').forEach(b=>b.onclick=()=>show(Math.min(s+1,3)));$('#wz [data-bk]').forEach(b=>b.onclick=()=>show(Math.max(s-1,0)));
document.getElementById('send').onclick=()=>{const sv=$('#wz .step:first-of-type input:checked').map(i=>i.value).join(', ')||'Not specified';const v=n=>(document.querySelector(`#wz input[name=${n}]:checked`)||{}).value||'Not specified';
const m=`Hello Parakram Security, I'd like a security plan.%0A%0A*Services:* ${sv}%0A*Site type:* ${v('site')}%0A*Team size:* ${v('g')}%0A*Coverage:* ${v('sh')}%0A*Name:* ${pn.value}%0A*Phone:* ${pp.value}%0A*Location:* ${pc.value}`;if(!pp.value.trim()){toast('Please enter your phone number.');pp.focus();return}open(`https://wa.me/${PH}?text=${m}`,'_blank');toast('Opening WhatsApp with your plan…')}})();
/* contact form -> WhatsApp */
cf.onsubmit=e=>{e.preventDefault();const m=`Hello Parakram Security,%0A*Name:* ${cn.value}%0A*Phone:* ${cp.value}%0A*Email:* ${ce.value}%0A*Service:* ${cs.value||'Not specified'}%0A*Details:* ${cm.value}`;open(`https://wa.me/${PH}?text=${m}`,'_blank');toast('Opening WhatsApp…')};
</script>
</body></html>'''
mq=['Trained &amp; Verified Personnel','Customized Solutions','24/7 Availability','Multi-Site Support','Professionalism','Integrity','Courtesy','Your Safety Is Our Mission']
M=json.load(open(os.path.join(H,'india_paths.json')))
mapsvg=f'<svg id="imap" viewBox="0 0 {M["w"]} {M["h"]}" role="img" aria-label="Interactive map of India"><g>'+''.join(f'<path class="st{" hq" if x["n"]=="Uttarakhand" else ""}" data-n="{x["n"].replace("&","&amp;")}" d="{x["d"]}"/>' for x in M['states'])+f'</g><g class="pinG" transform="translate({M["pin"][0]} {M["pin"][1]})"><circle class="rd" r="14"/><circle class="rd r2" r="14"/><circle class="pd" r="9"/></g></svg>'
html=(html.replace('@@MAP@@',mapsvg).replace('@@MEGA@@',mega).replace('@@TABS@@',tabs).replace('@@PANELS@@',panels).replace('@@CHIPS@@',chips)
 .replace('@@MARQUEE@@',''.join(f'<span>{x}</span>' for x in mq*2))
 .replace('@@OPTS@@',''.join(f'<option>{h}</option>' for _,h,*_ in SV)))
open(os.path.join(H,'..','index.html'),'w').write(html)
print(len(html))
