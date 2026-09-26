
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
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.1});
const io2=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io2.unobserve(e.target)}}),{threshold:.3});
$('.vals>div,.stats .stat,.fg>div,.covt li,.faq details,.fq details').forEach(e=>e.classList.add('rv'));
$('.rv').forEach(e=>{const sib=[...e.parentNode.children].filter(c=>c.classList.contains('rv'));e.style.setProperty('--d',Math.min(sib.indexOf(e),6)*90+'ms');io.observe(e)});

/* counters */
const co=new IntersectionObserver(es=>es.forEach(e=>{if(!e.isIntersecting)return;const el=e.target,n=+el.dataset.n,d=+el.dataset.d||0,s=el.dataset.s||'';let t0=null;const f=t=>{t0=t0||t;const p=Math.min((t-t0)/1800,1),v=n*(1-Math.pow(1-p,4));el.innerHTML=(d?v.toFixed(d):Math.round(v).toLocaleString('en-IN'))+(s?'<sup>'+s+'</sup>':'');if(p<1)requestAnimationFrame(f)};requestAnimationFrame(f);co.unobserve(el)}),{threshold:.5});
$('[data-n]').forEach(e=>co.observe(e));

try{
/* hero slider */
(()=>{const sl=$('.slide'),ds=$('.d');let i=0,t;const go=n=>{i=(n+sl.length)%sl.length;sl.forEach((e,k)=>e.classList.toggle('on',k==i));ds.forEach((e,k)=>{e.classList.remove('on');if(k==i){void e.offsetWidth;e.classList.add('on')}});clearTimeout(t);t=setTimeout(()=>go(i+1),6500)};
window.__heroReset=()=>go(0);ds.forEach((d,k)=>d.onclick=()=>go(k));document.getElementById('pv').onclick=()=>go(i-1);document.getElementById('nx').onclick=()=>go(i+1);t=setTimeout(()=>go(1),6500);
const fig=document.getElementById('fig'),hx=document.getElementById('hero');if(!mq('(pointer:coarse)'))hx.addEventListener('mousemove',e=>{const x=(e.clientX/innerWidth-.5)*16,y=(e.clientY/innerHeight-.5)*10;fig.style.transform=`translate(${x}px,${y}px)`})})();

}catch(e){}
try{
/* services */
(()=>{const tb=$('.tb'),pn=$('.pn');const sel=k=>{tb.forEach((e,i)=>e.classList.toggle('on',i==k));pn.forEach((e,i)=>e.classList.toggle('on',i==k));if(mq('(max-width:980px)')){const tl=tb[k].parentNode;tl.scrollTo({left:tb[k].offsetLeft-(tl.clientWidth-tb[k].offsetWidth)/2,behavior:'smooth'})}};
tb.forEach((b,k)=>{b.onclick=()=>sel(k);b.onmouseenter=()=>{if(!mq('(max-width:980px)'))sel(k)}});$('[data-go]').forEach(a=>a.addEventListener('click',()=>sel(+a.dataset.go)))})();

}catch(e){}
try{
/* spotlight cards */
$('.pl').forEach(c=>c.addEventListener('mousemove',e=>{const r=c.getBoundingClientRect();c.style.setProperty('--mx',(e.clientX-r.left)+'px');c.style.setProperty('--my',(e.clientY-r.top)+'px')}));

}catch(e){}
try{
/* testimonials */
(()=>{const q=$('.q'),d=$('.qd button');let i=0,t;const go=n=>{i=n%q.length;q.forEach((e,k)=>e.classList.toggle('on',k==i));d.forEach((e,k)=>e.classList.toggle('on',k==i));clearTimeout(t);t=setTimeout(()=>go(i+1),5500)};d.forEach((b,k)=>b.onclick=()=>go(k));t=setTimeout(()=>go(1),5500)})();


}catch(e){}
try{
/* --- enhancement JS --- */

var toast=m=>{const t=document.getElementById('toast');t.textContent=m;t.classList.add('on');clearTimeout(t._h);t._h=setTimeout(()=>t.classList.remove('on'),3200)};

}catch(e){}
try{
/* split headings */
$('.h2').forEach(h=>{let i=0;const wrap=n=>{[...n.childNodes].forEach(c=>{if(c.nodeType===3){const f=document.createDocumentFragment();c.textContent.split(/(\s+)/).forEach(t=>{if(!t)return;if(/^\s+$/.test(t)){f.appendChild(document.createTextNode(' '));return}const w=document.createElement('span');w.className='w';const b=document.createElement('span');b.textContent=t;b.style.setProperty('--i',i++);w.appendChild(b);f.appendChild(w)});c.replaceWith(f)}else if(c.nodeType===1)wrap(c)})};wrap(h);h.setAttribute('aria-label',h.textContent);io2.observe(h)});

}catch(e){}
try{
/* scrollspy */
const spy=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){$('nav>ul>li>a').forEach(a=>a.classList.toggle('act',a.getAttribute('href')==='#'+e.target.id))}}),{rootMargin:'-45% 0px -50% 0px'});
$('main section[id]').forEach(x=>spy.observe(x));

}catch(e){}
try{
/* tilt cards (disabled for a calmer enterprise feel) */
if(false)$('.ic').forEach(c=>{c.addEventListener('mousemove',e=>{const r=c.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;c.style.transform=`perspective(1000px) translateY(-8px) rotateX(${-y*7}deg) rotateY(${x*9}deg)`});c.addEventListener('mouseleave',()=>c.style.transform='')});

}catch(e){}
try{
/* magnetic buttons (disabled) */
if(false)$('.btn-g,.btn-n').forEach(b=>{b.addEventListener('mousemove',e=>{const r=b.getBoundingClientRect();b.style.transform=`translate(${(e.clientX-r.left-r.width/2)*.18}px,${(e.clientY-r.top-r.height/2)*.28}px)`});b.addEventListener('mouseleave',()=>b.style.transform='')});

}catch(e){}
try{
/* hero glow + scroll fade */
(()=>{addEventListener('scroll',()=>{if(scrollY<900){const y=scrollY;$('.hxg .tx').forEach(t=>{t.style.transform=`translateY(${y*.12}px)`;t.style.opacity=Math.max(0,1-y/650)})}},{passive:true})})();

}catch(e){}
try{
/* parallax on about image + band */
addEventListener('scroll',()=>{const im=document.querySelector('.imgc .im img');if(im){const r=im.getBoundingClientRect();if(r.top<innerHeight&&r.bottom>0)im.style.objectPosition=`50% ${50+(r.top/innerHeight-.5)*18}%`}},{passive:true});


}catch(e){}
try{
/* ist clock */
(()=>{const e=document.getElementById('ist');const t=()=>{e.textContent=new Date().toLocaleTimeString('en-IN',{timeZone:'Asia/Kolkata',hour:'2-digit',minute:'2-digit',second:'2-digit',hour12:true})+' IST'};t();setInterval(t,1000)})();

}catch(e){}
try{
/* india map */
(()=>{const m=document.getElementById('map'),tip=document.getElementById('mtip'),mn=document.getElementById('mn'),ms=document.getElementById('ms'),mb=document.getElementById('mb'),sts=$('.st');
const pick=p=>{const n=p.dataset.n;sts.forEach(x=>x.classList.toggle('sel',x===p));mn.textContent=n;
if(n==='Uttarakhand'){ms.textContent='Headquarters · 6A Sandesh Nagar, Kankhal, Haridwar 249408';mb.textContent='Contact Us';mb.href='#contact';mb.onclick=null}
else{ms.textContent='Support for multiple sites — tell us about your site in '+n+'.';mb.textContent='Enquire for '+n+' →';mb.href='#planner';mb.onclick=()=>{const f=document.getElementById('pc');if(f)f.value=n}}};
sts.forEach(p=>{p.addEventListener('mousemove',e=>{const r=m.getBoundingClientRect();tip.textContent=p.dataset.n+(p.classList.contains('hq')?' · HQ':'');tip.style.left=(e.clientX-r.left)+'px';tip.style.top=(e.clientY-r.top)+'px';tip.classList.add('on')});p.addEventListener('mouseleave',()=>tip.classList.remove('on'));p.addEventListener('click',()=>pick(p));p.setAttribute('tabindex','0');p.setAttribute('role','button');p.setAttribute('aria-label',p.dataset.n);p.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();pick(p)}})});
pick(document.querySelector('.st.hq'))})();


}catch(e){}
try{
/* touch swipe: hero + services */
(()=>{const sw=(el,fn)=>{let x=0,y=0,t=0;el.addEventListener('touchstart',e=>{x=e.touches[0].clientX;y=e.touches[0].clientY;t=Date.now()},{passive:true});el.addEventListener('touchend',e=>{const dx=e.changedTouches[0].clientX-x,dy=e.changedTouches[0].clientY-y;if(Math.abs(dx)>50&&Math.abs(dx)>Math.abs(dy)*1.5&&Date.now()-t<700)fn(dx<0?1:-1)},{passive:true})};
const hero=document.getElementById('hero');if(hero)sw(hero,d=>document.getElementById(d>0?'nx':'pv').click());
const pw=document.querySelector('.pw');if(pw)sw(pw,d=>{const tb=$('.tb');const k=tb.findIndex(b=>b.classList.contains('on'));const n=k+d;if(n>=0&&n<tb.length)tb[n].click()})})();


}catch(e){}
try{
/* section rail */
(()=>{const r=$('.rail a');if(!r.length)return;const io3=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){r.forEach(a=>a.classList.toggle('on',a.getAttribute('href')==='#'+e.target.id))}}),{rootMargin:'-45% 0px -50% 0px'});r.forEach(a=>{const t=document.querySelector(a.getAttribute('href'));if(t)io3.observe(t)})})();


}catch(e){}
try{
/* scroll driven progress: journey timeline and process steps */
(()=>{const prog=(box,fill,items)=>{if(!box||!fill)return;const upd=()=>{const r=box.getBoundingClientRect();const p=Math.min(1,Math.max(0,(innerHeight*.72-r.top)/(r.height+innerHeight*.05)));const v=mq('(max-width:980px)');fill.style.transform=v?`scaleY(${p})`:`scaleX(${p})`;items.forEach((it,i)=>it.classList.toggle('on',REDUCE||p>=(i+.35)/items.length))};addEventListener('scroll',upd,{passive:true});addEventListener('resize',upd);upd()};
prog(document.getElementById('jr'),document.getElementById('jfill'),$('.jm'));
prog(document.getElementById('steps'),document.querySelector('#steps .fl'),$('#steps .sp'))})();

}catch(e){}
try{
/* services autoplay (starts when visible, stops on any interaction) */
(()=>{const sx=document.querySelector('.sx');if(!sx||REDUCE||mq('(max-width:980px)')||mq('(pointer:coarse)'))return;const tb=$('.tb');let t=null,stopped=false,vis=false;
const idx=()=>tb.findIndex(b=>b.classList.contains('on'));
const step=()=>{if(stopped||!vis)return;tb[(idx()+1)%tb.length].click();sx.classList.remove('auto');void sx.offsetWidth;sx.classList.add('auto');t=setTimeout(step,5500)};
const start=()=>{clearTimeout(t);sx.classList.add('auto');t=setTimeout(step,5500)};
const stop=()=>{stopped=true;clearTimeout(t);sx.classList.remove('auto')};
['pointerdown','mouseenter','touchstart','keydown'].forEach(ev=>sx.addEventListener(ev,stop,{passive:true,once:true}));
new IntersectionObserver(es=>es.forEach(e=>{vis=e.isIntersecting&&e.intersectionRatio>.35;if(vis&&!stopped)start();else{clearTimeout(t);sx.classList.remove('auto')}}),{threshold:[0,.35,.6]}).observe(sx)})();

}catch(e){}
try{
/* spotlight follow */
if(!mq('(pointer:coarse)'))$('.stat,.vals div,.covt li').forEach(c=>c.addEventListener('mousemove',e=>{const r=c.getBoundingClientRect();c.style.setProperty('--mx',(e.clientX-r.left)+'px');c.style.setProperty('--my',(e.clientY-r.top)+'px')}));


}catch(e){}
try{
/* number the section labels 01, 02, 03 */
(()=>{let n=0;['about','services','planner','industries','why','journey','coverage','faq','contact'].forEach(id=>{const sec=document.getElementById(id);if(!sec)return;const e=sec.querySelector('.eyebrow');if(!e)return;n++;const sp=document.createElement('span');sp.className='no';sp.textContent=(n<10?'0':'')+n+' /';e.insertBefore(sp,e.firstChild)})})();


}catch(e){}
try{
/* gentle planner prompt, once per visit */
(()=>{const n=document.getElementById('nudge');if(!n)return;let seen=false;try{seen=sessionStorage.getItem('nudge')==='1'}catch(e){}if(seen)return;
const hide=()=>{n.classList.remove('on');try{sessionStorage.setItem('nudge','1')}catch(e){}};
n.querySelector('.x').onclick=hide;n.querySelector('a').addEventListener('click',hide);
let ready=false,shown=false;const check=()=>{if(shown||!ready||scrollY<600)return;const pl=document.getElementById('planner').getBoundingClientRect();if(pl.top<innerHeight&&pl.bottom>0)return;shown=true;n.classList.add('on');setTimeout(()=>n.classList.remove('on'),16000)};setTimeout(()=>{ready=true;check()},10000);addEventListener('scroll',check,{passive:true})})();


}catch(e){}
try{
/* security intro: short, skippable, once per visit */
(()=>{const I=document.getElementById('intro'),root=document.documentElement;if(!I||!root.classList.contains('intro'))return;let done=false;
const end=()=>{if(done)return;done=true;I.classList.add('open');setTimeout(()=>{root.classList.remove('intro');try{sessionStorage.setItem('intro','1')}catch(e){}window.__heroReset&&window.__heroReset()},900)};
setTimeout(end,2500);I.addEventListener('click',end);addEventListener('keydown',e=>{if(e.key==='Escape'||e.key==='Enter')end()});I.querySelector('.skip2').addEventListener('click',e=>{e.stopPropagation();end()})})();


}catch(e){}
try{
/* faq filter and search */
(()=>{const box=document.getElementById('faqf');if(!box)return;const chips=$('#faqf .fchips button'),items=$('#faqf details'),inp=document.getElementById('faqs'),none=document.getElementById('fnone');let cat='all';
const run=()=>{const q=(inp.value||'').toLowerCase().trim();let n=0;items.forEach(d=>{const ok=(cat==='all'||d.dataset.c===cat)&&(!q||d.textContent.toLowerCase().includes(q));d.style.display=ok?'':'none';if(ok)n++});none.style.display=n?'none':'block'};
chips.forEach(b=>b.onclick=()=>{cat=b.dataset.c;chips.forEach(x=>x.classList.toggle('on',x===b));run()});inp.addEventListener('input',run)})();

}catch(e){}
try{
/* subnav highlight */
(()=>{const links=$('.subnav .snv a');if(!links.length)return;const io4=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting)links.forEach(a=>a.classList.toggle('on',a.getAttribute('href')==='#'+e.target.id))}),{rootMargin:'-40% 0px -55% 0px'});links.forEach(a=>{const t=document.querySelector(a.getAttribute('href'));if(t)io4.observe(t)})})();

}catch(e){}
try{
/* inner page banner entrance */
(()=>{const b=document.querySelector('.pbn');if(b)setTimeout(()=>b.classList.add('in'),80)})();


}catch(e){}
try{
/* coverage options (24 hour bar) */
(()=>{const box=document.getElementById('cov24');if(!box)return;const bar=box.querySelector('.bar24'),spans=[...bar.children],cap=document.getElementById('cap24'),tabs=$('#cov24 .ctabs button');
const M={day:{h:h=>h>=6&&h<18,t:'Day shift: guards on duty from morning to evening. A good fit for offices, campuses and sites that are busiest during the day.'},night:{h:h=>h>=18||h<6,t:'Night shift: guards on duty through the night. A good fit for warehouses, residential societies and sites that need protection after hours.'},full:{h:()=>true,t:'24/7 coverage: guards on duty at every hour of every day, with planned handovers so there is never a gap.'}};
const set=k=>{tabs.forEach(b=>b.classList.toggle('on',b.dataset.m===k));spans.forEach((s,i)=>{setTimeout(()=>s.classList.toggle('on',M[k].h(i)),i*14)});cap.textContent=M[k].t};
tabs.forEach(b=>b.onclick=()=>set(b.dataset.m));set('full')})();

}catch(e){}
try{
/* quick enquiry cards */
$('.qc form').forEach(f=>f.addEventListener('submit',e=>{e.preventDefault();const g=n=>f.querySelector('[name='+n+']').value.trim();if(!g('p')){toast('Please enter your phone number.');return}const m=`Hello Parakram Security, I am interested in ${f.dataset.s}.%0A*Name:* ${g('n')}%0A*Phone:* ${g('p')}`;open(`https://wa.me/${PH}?text=${m}`,'_blank');toast('Opening WhatsApp...')}));

}catch(e){}
try{
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


}catch(e){}
try{
/* 3D: tilt with glare, hero depth, emblem, image parallax */
(()=>{const fine=!mq('(pointer:coarse)')&&!REDUCE;
if(fine){$('.rcard,.sp2i,.imgc,.ic,.mos>div,.hx .fig').forEach(el=>{el.setAttribute('data-tilt','');if(getComputedStyle(el).position==='static')el.style.position='relative';const g=document.createElement('span');g.className='glare';el.appendChild(g);const lift=el.matches('.rcard,.ic')?-6:0,m=el.matches('.hx .fig')?4.5:6.5;
el.addEventListener('pointermove',e=>{const r=el.getBoundingClientRect(),x=(e.clientX-r.left)/r.width,y=(e.clientY-r.top)/r.height;el.classList.add('tilting');el.style.transform=`perspective(1000px) translateY(${lift}px) rotateX(${((.5-y)*m*2).toFixed(2)}deg) rotateY(${((x-.5)*m*2).toFixed(2)}deg) scale(1.015)`;el.style.setProperty('--gx',(x*100).toFixed(1)+'%');el.style.setProperty('--gy',(y*100).toFixed(1)+'%')});
el.addEventListener('pointerleave',()=>{el.classList.remove('tilting');el.style.transform=''})});
const hx=document.getElementById('hero');if(hx){let raf=0;hx.addEventListener('pointermove',e=>{if(raf)return;raf=requestAnimationFrame(()=>{raf=0;const r=hx.getBoundingClientRect();hx.style.setProperty('--mx',((e.clientX-r.left)/r.width-.5).toFixed(3));hx.style.setProperty('--my',((e.clientY-r.top)/r.height-.5).toFixed(3))})});hx.addEventListener('pointerleave',()=>{hx.style.setProperty('--mx',0);hx.style.setProperty('--my',0)})}}
$('.emb3d').forEach(b=>{const a=document.createElement('div');a.className='emb-in';const w=document.createElement('div');w.className='emb-sw';for(let i=0;i<16;i++){const im=new Image();im.src='/logo.png';im.alt='';im.width=170;im.height=170;im.decoding='async';im.style.transform='translateZ('+((i-8)*2.4)+'px)';im.style.filter=i<15?'brightness('+(0.4+i*0.038).toFixed(2)+')':'none';w.appendChild(im)}a.appendChild(w);b.appendChild(a);if(fine)b.addEventListener('pointermove',e=>{const r=b.getBoundingClientRect();b.style.setProperty('--ex',((e.clientX-r.left)/r.width-.5).toFixed(3));b.style.setProperty('--ey',((e.clientY-r.top)/r.height-.5).toFixed(3))})});
if(!REDUCE){const ps=$('.sp2i img,.mos img,.pbn .pbg');if(ps.length){let t=0;const upd=()=>{t=0;const vh=innerHeight;ps.forEach(el=>{const host=el.closest('.sp2i,.mos>div')||el;const r=host.getBoundingClientRect();if(r.bottom<-60||r.top>vh+60)return;const p=((r.top+r.height/2)-vh/2)/vh;el.style.setProperty('--py',(p*-28).toFixed(1)+'px')})};addEventListener('scroll',()=>{if(!t)t=requestAnimationFrame(upd)},{passive:true});upd()}}
})();

}catch(e){}
try{
/* planner wizard */
(()=>{const w=document.getElementById('wz'),st=$('#wz .step'),bars=$('#wz .st i');let s=0;const show=n=>{s=n;st.forEach((e,k)=>e.classList.toggle('on',k==n));bars.forEach((e,k)=>e.classList.toggle('on',k<=n))};
$('#wz [data-nx]').forEach(b=>b.onclick=()=>show(Math.min(s+1,3)));$('#wz [data-bk]').forEach(b=>b.onclick=()=>show(Math.max(s-1,0)));
document.getElementById('send').onclick=()=>{const sv=$('#wz .step:first-of-type input:checked').map(i=>i.value).join(', ')||'Not specified';const v=n=>(document.querySelector(`#wz input[name=${n}]:checked`)||{}).value||'Not specified';
const m=`Hello Parakram Security, I'd like a security plan.%0A%0A*Services:* ${sv}%0A*Site type:* ${v('site')}%0A*Team size:* ${v('g')}%0A*Coverage:* ${v('sh')}%0A*Name:* ${pn.value}%0A*Phone:* ${pp.value}%0A*Location:* ${pc.value}`;if(!pp.value.trim()){toast('Please enter your phone number.');pp.focus();return}open(`https://wa.me/${PH}?text=${m}`,'_blank');toast('Opening WhatsApp with your plan…')}})();

}catch(e){}
try{
/* contact form -> WhatsApp */
cf.onsubmit=e=>{e.preventDefault();const m=`Hello Parakram Security,%0A*Name:* ${cn.value}%0A*Phone:* ${cp.value}%0A*Email:* ${ce.value}%0A*Service:* ${cs.value||'Not specified'}%0A*Details:* ${cm.value}`;open(`https://wa.me/${PH}?text=${m}`,'_blank');toast('Opening WhatsApp…')};

}catch(e){}