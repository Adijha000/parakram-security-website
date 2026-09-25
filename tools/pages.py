# Builds the multi page site. Run after build.py:  python3 tools/build.py && python3 tools/pages.py
import os,re,json,time
H=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')
def rd(f): return open(os.path.join(H,f)).read()
def wr(f,t):
    p=os.path.join(H,f); os.makedirs(os.path.dirname(p),exist_ok=True); open(p,'w').write(t)
U='https://parakram-website.vercel.app'
V=str(int(time.time()))

home=rd('index.html')

# ---------- 1. split shared CSS and JS out of the home page ----------
css=re.search(r'<style>(.*?)</style>',home,re.S).group(1)
wr('css/site.css',css)
home=home.replace('<style>'+css+'</style>','<link rel="stylesheet" href="/css/site.css?v='+V+'">')
scripts=re.findall(r'<script>(.*?)</script>',home,re.S)
main_js=scripts[-1]
chunks=re.split(r'(?m)^(?=/\*)',main_js)
out=[]
for i,c in enumerate(chunks):
    c=c.replace('const toast=','var toast=')
    out.append(c if i<7 else 'try{\n'+c+'\n}catch(e){}')
wr('js/app.js','\n'.join(out))
home=home.replace('<script>'+main_js+'</script>','<script src="/js/app.js?v='+V+'"></script>')
home=home.replace('<script src="js/lenis.min.js"></script>','<script src="/js/lenis.min.js"></script>')

def absolutize(t):
    t=re.sub(r'(src|href)="(?!https?:|/|#|mailto:|tel:|data:)([^"]+)"',lambda m:f'{m.group(1)}="/{m.group(2)}"',t)
    t=t.replace('url(img/','url(/img/')
    t=t.replace('href="/privacy.html"','href="/privacy"').replace('href="/terms.html"','href="/terms"')
    return t
home=absolutize(home)
wr('index.html',home)

# ---------- 2. shared shell pieces ----------
head=home[:home.index('<body>')]
header=re.search(r'<header id="hd">.*?</header>',home,re.S).group(0)
ctab=re.search(r'<div class="ctab">.*?</div></div></div>\n',home,re.S).group(0)
footer=re.search(r'<footer>.*?</footer>',home,re.S).group(0)
mbar=re.search(r'<div class="mbar">.*?</div>\n',home,re.S).group(0)
topbtn=re.search(r'<button class="top".*?</button>',home,re.S).group(0)
wabtn=re.search(r'<a class="wa".*?</a>',home,re.S).group(0)
util=re.search(r'<div class="util">.*?</div></div></div>',home,re.S).group(0)
wz=home[home.index('<div class="wz rv" id="wz">'):]
wz=wz[:wz.index('</div></div></section>')+6]
mapx=home[home.index('<div class="map rv" id="map">'):home.index('<div class="covt rv">')].strip()
jr=home[home.index('<div class="jr" id="jr">'):]
jr=jr[:jr.index('</div></div></section>')+6]
IC={
'man':'<svg viewBox="0 0 24 24"><circle cx="12" cy="7" r="4"/><path d="M4 21c0-4.5 3.6-7 8-7s8 2.5 8 7"/></svg>',
'arm':'<svg viewBox="0 0 24 24"><path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/></svg>',
'ind':'<svg viewBox="0 0 24 24"><path d="M3 21V9l6 4V9l6 4V5h6v16z"/></svg>',
'com':'<svg viewBox="0 0 24 24"><rect x="4" y="3" width="16" height="18"/><path d="M8 7h2M14 7h2M8 11h2M14 11h2M8 15h2M14 15h2"/></svg>',
'res':'<svg viewBox="0 0 24 24"><path d="M3 11l9-8 9 8"/><path d="M5 10v11h14V10"/></svg>',
'hos':'<svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M12 7v10M7 12h10"/></svg>',
'edu':'<svg viewBox="0 0 24 24"><path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c3 2 9 2 12 0v-5"/></svg>',
'bnk':'<svg viewBox="0 0 24 24"><rect x="3" y="6" width="18" height="12" rx="1"/><circle cx="12" cy="12" r="3"/></svg>',
'eye':'<svg viewBox="0 0 24 24"><path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/></svg>',
'clk':'<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
'usr':'<svg viewBox="0 0 24 24"><circle cx="9" cy="8" r="3.5"/><path d="M2 20c0-3.6 3-6 7-6s7 2.4 7 6"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18 14c2.4.6 4 2.4 4 5"/></svg>',
'chk':'<svg viewBox="0 0 24 24"><path d="M5 12l4 4 10-10"/></svg>',
'map':'<svg viewBox="0 0 24 24"><path d="M12 21s7-6.2 7-11.5A7 7 0 0 0 5 9.5C5 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg>',
'ph':'<svg viewBox="0 0 24 24"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A15 15 0 0 1 3 6a2 2 0 0 1 2-2z"/></svg>',
'ml':'<svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>',
'book':'<svg viewBox="0 0 24 24"><path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2z"/><path d="M4 19V5"/></svg>',
'star':'<svg viewBox="0 0 24 24"><path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/></svg>',
}

SERV=[
('manned','Manned Security','man','operations','60% 25%','Trained and verified guards who protect your premises around the clock, from the first entry of the day to the last patrol of the night.',
 'Uniformed guards for gates, reception, patrols and access control.',
 [('Gate and access control','Guards manage entry and exit, check identity and keep a clear record of who comes and goes.'),
  ('Visitor management','A courteous first point of contact who guides visitors and keeps reception areas orderly.'),
  ('Planned patrols','Regular patrols across buildings, parking areas and perimeters, with observations reported to supervisors.'),
  ('Incident reporting','Clear procedures for reporting incidents quickly and escalating them to the right people.'),
  ('Vehicle and material checks','Checks at gates keep the movement of vehicles, goods and property under control.'),
  ('Supervision at every post','Supervisors visit posts regularly so standards stay high through every shift.')],
 ['Offices and corporate parks','Factories and warehouses','Residential societies','Campuses and institutions','Hospitals and clinics','Retail and commercial sites'],
 [('How many guards will my site need?','It depends on the size of your site, the number of entry points, your working hours and your risk. We assess your site and recommend a plan that you can adjust as your needs change.'),
  ('Can you cover night shifts only?','Yes. We can cover day shifts, night shifts or the full 24 hours, based on what your site needs.'),
  ('Who supervises the guards?','Supervisors and managers visit posts regularly and are available to you whenever you need to raise a concern.')]),
('armed','Armed Security','arm','hero','50% 0%','Disciplined armed personnel for locations that need a higher level of protection, deployed with clear procedures and strict supervision.',
 'Trained armed personnel for high security requirements.',
 [('Armed guarding for sensitive sites','Trained armed personnel are deployed where the risk profile of your site calls for a stronger deterrent.'),
  ('Strict procedures','Clear rules for conduct, handling and reporting keep every deployment disciplined and accountable.'),
  ('Verified personnel','Every person is verified and trained before deployment, so you know who is protecting your site.'),
  ('Site specific planning','Deployment is planned around your premises, your assets and the specific risks you face.'),
  ('Coordination','We coordinate closely with your team and, where needed, with the relevant authorities.'),
  ('Supervision and reporting','Regular supervision and clear reporting keep you informed about how your site is being protected.')],
 ['High value assets and storage','Sensitive facilities','Financial premises','Industrial and infrastructure sites','Private and corporate properties','Locations needing a stronger deterrent'],
 [('Are armed guards licensed?','Armed deployments follow the rules and licence requirements that apply to your site and location. We explain what is needed during the site assessment.'),
  ('When is armed security needed?','It is usually chosen for high value assets, sensitive facilities or locations where a stronger deterrent is needed. We help you decide during the assessment.'),
  ('Can armed and unarmed guards work together?','Yes. Many sites combine both under one plan, with clear roles for each.')]),
('industrial','Industrial Security','ind','training','50% 20%','Protection for plants, warehouses and industrial campuses, built around shifts, material movement and the safety rules of your site.',
 'Protection for plants, warehouses and industrial campuses.',
 [('Perimeter and gate control','Guards control entry points, check vehicles and keep the boundary of your site secure.'),
  ('Material movement checks','Consistent checks on goods entering and leaving help you keep a reliable record.'),
  ('Shift wise deployment','Guards are planned around your shifts, so coverage is strong when your site is busiest and when it is quiet.'),
  ('Safety awareness','Personnel follow your site safety rules and raise hazards quickly so they can be addressed.'),
  ('Asset protection','Regular patrols protect equipment, stock and infrastructure across large areas.'),
  ('Emergency coordination','Clear procedures help guards support your team during emergencies.')],
 ['Manufacturing plants','Warehouses and logistics parks','Industrial estates and campuses','Construction and project sites','Storage yards','Utilities and infrastructure'],
 [('Can you secure a large campus with several gates?','Yes. We plan posts, patrols and supervision across the whole campus so every entry point is covered.'),
  ('Do guards follow our site safety rules?','Yes. Guards are briefed on your site rules and follow them as part of their duties.'),
  ('How do you handle shift changes?','Handovers are planned so that there is no gap in coverage and information passes clearly from one shift to the next.')]),
('commercial','Commercial Security','com','operations','70% 25%','Professional guards for offices and business premises, who protect your people and make a confident first impression on every visitor.',
 'Professional guards for offices and business premises.',
 [('Reception and lobby presence','Well presented guards welcome visitors, direct them and keep entrances orderly.'),
  ('Access control','Visitor passes, identity checks and clear entry rules keep your premises secure.'),
  ('Parking and vehicle management','Guards keep parking areas organised and make sure vehicles are directed safely.'),
  ('After hours security','Patrols and monitoring of entrances protect your premises when your team has gone home.'),
  ('Tenant coordination','In shared buildings we coordinate with tenants and building management so procedures stay consistent.'),
  ('Courteous service','Our people are known for professionalism, integrity and courtesy with your staff and guests.')],
 ['Corporate offices','Business parks and towers','Shopping and retail spaces','Co working spaces','Showrooms and service centres','Multi tenant buildings'],
 [('Can guards act as front desk support?','Guards are trained to be courteous and helpful to visitors. Their main role is security, and we agree the scope of front desk duties with you.'),
  ('Can you manage visitor passes?','Yes. We can follow your visitor process or help you set up a simple one.'),
  ('Do you support multi tenant buildings?','Yes. We coordinate with building management and tenants so procedures are clear and consistent.')]),
('residential','Residential Security','res','about','50% 30%','Courteous and reliable security for homes and residential societies, so that families feel safe and welcome at their own gate.',
 'Courteous, reliable security for homes and societies.',
 [('Gate and visitor control','Guards check visitors, keep entry records and follow the rules set by your society.'),
  ('Night patrols','Planned patrols through the night keep common areas and boundaries secure.'),
  ('Courteous resident service','Guards greet residents politely and support them with everyday needs at the gate.'),
  ('Delivery and vehicle management','Deliveries and vehicles are handled in an orderly way without blocking entrances.'),
  ('Emergency support','Guards know how to raise the alarm and support residents when something goes wrong.'),
  ('Coordination with committees','We work with resident committees and managers so that rules and reports are clear.')],
 ['Gated communities','Apartment societies','Townships','Villas and private homes','Senior living communities','Housing complexes'],
 [('Can guards follow our society rules?','Yes. We brief guards on your rules for visitors, deliveries and vehicles and update them when rules change.'),
  ('Do you provide night patrols?','Yes. Patrol routes and timings are planned with your committee.'),
  ('How do residents raise a concern?','Concerns can be raised with the supervisor or through the contact channel we agree with your committee, and we act on feedback quickly.')]),
('hospital','Hospital Security','hos','about','60% 20%','Calm and courteous security for hospitals and healthcare facilities, where patients, families and staff need to feel safe at difficult moments.',
 'Calm, courteous security for hospitals and healthcare facilities.',
 [('Visitor and crowd management','Guards manage busy entrances and visiting hours calmly and politely.'),
  ('Emergency entrance access','Clear routes keep emergency access open and support smooth arrival for patients.'),
  ('Patient and staff safety','Visible, approachable guards help staff and patients feel safe throughout the building.'),
  ('Respectful conduct','Our people are trained to treat anxious families with patience and respect.'),
  ('Parking and traffic control','Guards keep ambulance routes and parking areas organised.'),
  ('Assistance for visitors','Guards help visitors find their way and support those who need assistance.')],
 ['Hospitals','Clinics and diagnostic centres','Nursing homes','Medical colleges','Pharmacies and health campuses','Rehabilitation centres'],
 [('Are guards trained to handle emotional situations?','Our people are trained in courtesy and calm communication, which matters most in a healthcare setting.'),
  ('Can you keep emergency routes clear?','Yes. Keeping emergency access open is a priority in every healthcare deployment.'),
  ('Do you cover night shifts in hospitals?','Yes. Hospitals never close, so we plan round the clock coverage when needed.')]),
('educational','Educational Security','edu','training','40% 25%','Safe and well supervised campuses for schools, colleges and institutions, with guards who are approachable and alert.',
 'Safe, closely supervised campuses for schools and institutions.',
 [('Campus gate control','Guards check entry and exit points and keep unauthorised people out.'),
  ('Visitor and vehicle checks','Simple, consistent checks keep your campus secure without slowing the day.'),
  ('Arrival and dispersal support','Guards help manage the busiest times of day so that students move safely.'),
  ('Patrols','Regular patrols cover classrooms, grounds and boundaries.'),
  ('Event support','Guards support events, admissions and examinations with clear crowd management.'),
  ('Courteous conduct','Our people are trained to be polite, patient and professional around students and parents.')],
 ['Schools','Colleges and universities','Coaching institutes','Hostels and residential campuses','Training centres','Sports and event grounds'],
 [('Can you support school arrival and dispersal?','Yes. We plan extra support around the busiest times so that students move safely.'),
  ('Do guards receive special training for campuses?','Guards are briefed on your campus rules and trained to be courteous and alert around students.'),
  ('Can you support events and examinations?','Yes. We can add personnel and plan crowd management for specific events.')]),
('banking','Bank & ATM Security','bnk','operations','50% 30%','Vigilant and verified personnel for bank branches and ATMs, where trust and alertness matter every hour of the day.',
 'Vigilant, verified personnel for branches and ATMs.',
 [('Branch entrance security','Guards welcome customers, watch entrances and keep branch premises orderly.'),
  ('ATM vigilance','Alert personnel keep ATM locations safe for customers at all hours.'),
  ('Verified personnel','Every guard is verified and trained before deployment to a financial site.'),
  ('Clear alert procedures','Simple, rehearsed procedures help guards respond quickly if something looks wrong.'),
  ('Customer courtesy','Guards treat customers with respect and help maintain a calm branch environment.'),
  ('Supervision and reporting','Regular supervision and reporting keep standards high across branches.')],
 ['Bank branches','ATM locations','Cooperative banks and societies','Financial service offices','Currency and payment outlets','Head offices and back offices'],
 [('Can you cover many branches under one plan?','Yes. We can plan several branches together so standards stay consistent.'),
  ('Do you provide guards for ATMs only?','Yes. We can cover ATMs on their own or together with the branch.'),
  ('How are guards for financial sites selected?','Personnel for financial sites are verified and trained before deployment, and supervised regularly.')]),
]
SL={s[0]:s for s in SERV}
def img(name,pos=''): return f'/img/parakram-{name}.webp'

def rvs(cls_html): return cls_html

def pbn(crumbs,h1,lead,bg,pos,ctas,meta=None):
    bc='<a href="/">Home</a>'
    for i,(t,u) in enumerate(crumbs):
        bc+='<span>/</span>'+(f'<a href="{u}">{t}</a>' if u else f'<b>{t}</b>')
    ms=''.join(f'<span>{m}</span>' for m in (meta or []))
    return f'''<section class="pbn"><div class="pbg" style="--bg:url({bg});--pos:{pos}"></div><div class="wrap pbi"><div class="bc" role="navigation" aria-label="Breadcrumb">{bc}</div><h1>{h1}</h1><p class="lead">{lead}</p><div class="cta">{ctas}</div>{('<div class="pm2">'+ms+'</div>') if ms else ''}</div></section>'''
BTN=lambda t,u,c='btn-g':f'<a class="btn {c}" href="{u}">{t}</a>'
def sech(eyebrow,h2,p=''):
    return f'<div class="sec-h rv"><div class="eyebrow dk">{eyebrow}</div><h2 class="h2">{h2}</h2>{("<p>"+p+"</p>") if p else ""}</div>'
def cards(items,cls='',num=False):
    o=''
    for i,it in enumerate(items):
        ic,t,p=it
        head=(f'<span class="no2">0{i+1}</span>' if num else f'<div class="ico">{IC[ic]}</div>')
        o+=f'<div class="fcard rv">{head}<h3>{t}</h3><p>{p}</p></div>'
    return f'<div class="fc {cls}">{o}</div>'
def ticks(items,two=False): return f'<ul class="ticks{" two" if two else ""}">'+''.join(f'<li>{i}</li>' for i in items)+'</ul>'
def faq(items,cat=False,openfirst=True):
    o=''
    for i,it in enumerate(items):
        q,a=it[0],it[1]; c=it[2] if len(it)>2 else ''
        o+=f'<details{" open" if (i==0 and openfirst) else ""}{(" data-c=\""+c+"\"") if c else ""}><summary>{q}</summary><p>{a}</p></details>'
    return o
def faq_ld(items):
    return '<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":i[0],"acceptedAnswer":{"@type":"Answer","text":i[1]}} for i in items]},ensure_ascii=False)+'</script>'
def cta2(h,p,primary=('Plan Your Security →','/planner'),secondary=('Call +91 91059 09006','tel:+919105909006')):
    return f'<section class="blk"><div class="wrap"><div class="cta2b rv"><div><h2>{h}</h2><p>{p}</p></div><div class="cta">{BTN(primary[0],primary[1])}{BTN(secondary[0],secondary[1],"btn-o")}</div></div></div></section>'
STEPS='''<div class="steps rv" id="steps"><i class="fl"></i><div class="sp"><i>1</i><div><b>Consult</b><span>Tell us your needs</span></div></div><div class="sp"><i>2</i><div><b>Assess</b><span>We study your site</span></div></div><div class="sp"><i>3</i><div><b>Customize</b><span>A tailored security plan</span></div></div><div class="sp"><i>4</i><div><b>Deploy</b><span>Trained, verified personnel</span></div></div><div class="sp"><i>5</i><div><b>Supervise</b><span>Ongoing quality checks</span></div></div></div>'''
def related(exclude=None):
    o=''
    for s in SERV:
        if s[0]==exclude: continue
        o+=f'<a class="rcard rv" href="/services/{s[0]}"><div class="rt"><img src="{img(s[3] if s[3]!="hero" else "hero-portrait")}" alt="{s[1].replace("&","and")}" loading="lazy"></div><div class="rb"><b>{s[1].replace("&","&amp;")}</b><span>{s[6]}</span><em>Learn more →</em></div></a>'
    return f'<div class="rel">{o}</div>'
TESTI='''<section class="tm"><div class="wrap rv"><div class="rate"><b>4.9</b>★★★★★ Rated by 1,200+ clients</div><h2 class="h2">What our <em>clients say.</em></h2>
<div class="qs"><div class="q on"><div class="st">★★★★★</div><blockquote>Well trained guards and excellent site coordination.</blockquote><cite>Facility Manager</cite></div>
<div class="q"><div class="st">★★★★★</div><blockquote>Dependable security routines that keep our operations running smoothly.</blockquote><cite>Industrial Client</cite></div>
<div class="q"><div class="st">★★★★★</div><blockquote>Supervisors are accessible and responsive whenever we need them.</blockquote><cite>Institutional Client</cite></div></div>
<div class="qd"><button class="on" aria-label="Quote 1"></button><button aria-label="Quote 2"></button><button aria-label="Quote 3"></button></div></div></section>'''

PAGES={}   # path -> (title, description, body, nav_href, extra_head)

# ---------- Services overview ----------
def services_page():
    o=pbn([('Services',None)],'Eight services. <em>One standard.</em>','Customized security solutions for every environment, delivered by trained and verified personnel who are available 24/7.',img('operations'),'60% 25%',BTN('Plan Your Security →','/planner')+BTN('Talk to Us','/contact','btn-o'),['Trained and verified','Available 24/7','Customized to your site'])
    cs=''
    for s in SERV:
        cs+=f'<a class="rcard rv" href="/services/{s[0]}"><div class="rt"><img src="{img(s[3] if s[3]!="hero" else "hero-portrait")}" alt="{s[1].replace("&","and")}" loading="lazy"></div><div class="rb"><b>{s[1].replace("&","&amp;")}</b><span>{s[6]}</span><em>View details →</em></div></a>'
    o+=f'<section class="blk"><div class="wrap">{sech("Our Services","Choose the protection your site needs.","Every service is planned around your premises, your people and your risk. Open a service to see what it covers and how we deploy.")}<div class="rel r2">{cs}</div></div></section>'
    o+=f'<section class="blk alt"><div class="wrap">{sech("How we work","From first call to daily supervision.")}{STEPS}</div></section>'
    o+=f'<section class="blk"><div class="wrap">{sech("Not sure where to start?","Tell us about your site.","Use the Security Planner to describe what you need. We will come back with a plan customized to your site, with no obligation.")}<div class="cta"><a class="btn btn-n" href="/planner">Open the Security Planner →</a></div></div></section>'
    o+=cta2('Ready to secure your premises?','Speak to our team. We are available 24/7.')
    return o
PAGES['services']=('Security Services | Parakram Security India','Manned, armed, industrial, commercial, residential, hospital, educational and bank and ATM security from Parakram Security India. Trained, verified personnel, available 24/7.',services_page(),'/services','')

# ---------- Service detail pages ----------
for slug,name,ic,im,pos,lead,short,what,where,faqs in SERV:
    nm=name.replace('&','&amp;')
    banner=pbn([('Services','/services'),(nm,None)],nm.replace(' Security',' <em>Security</em>'),lead,img(im if im!='hero' else 'hero-portrait'),pos,BTN('Plan This Service →','/planner')+BTN('Talk to Us','/contact','btn-o'),['Trained and verified','Available 24/7','Customized to your site'])
    sub=f'<div class="subnav"><div class="wrap"><div class="snv"><a href="#overview">Overview</a><a href="#covers">What it covers</a><a href="#where">Where it is used</a><a href="#deploy">How we deploy</a><a href="#faqs">FAQ</a></div><a class="btn btn-g sm" href="/planner">Get a plan</a></div></div>'
    body=banner+sub
    body+=f'''<section class="blk" id="overview"><div class="wrap sp2"><div class="sp2t rv"><div class="eyebrow dk">Overview</div><h2 class="h2">{nm} you can rely on.</h2><p>{lead}</p><p>We combine disciplined manpower, rigorous training and deeply rooted Indian values, so that our people are known for professionalism, integrity and courtesy at every post.</p>{ticks(["Trained and verified personnel","Available 24/7","Customized to your site"])}<div class="cta" style="margin-top:26px">{BTN("Plan This Service →","/planner","btn-n")}</div></div><div class="sp2i rv"><img src="{img(im if im!='hero' else 'hero-tall')}" alt="{nm}" loading="lazy" style="object-position:{pos}"><span class="badge">{nm}</span></div></div></section>'''
    body+=f'<section class="blk alt" id="covers"><div class="wrap">{sech("What it covers",f"What our {nm.lower().replace(chr(38)+"amp;","and")} team does.","The exact scope is confirmed with you after a site assessment and can be adjusted as your needs change.")}{cards([(ic,a,b) for a,b in what])}</div></section>'
    body+=f'<section class="blk" id="where"><div class="wrap sp2"><div class="sp2t rv"><div class="eyebrow dk">Where it is used</div><h2 class="h2">Built for real environments.</h2><p>This service is used across a range of sites. Whatever the size, we plan the deployment around how your site actually works.</p></div><div class="rv">{ticks(where,True)}</div></div></section>'
    body+=f'<section class="blk alt" id="deploy"><div class="wrap">{sech("How we deploy","From first call to daily supervision.")}{STEPS}</div></section>'
    body+=f'<section class="blk" id="faqs"><div class="wrap"><div class="sp2" style="align-items:start"><div class="sp2t rv"><div class="eyebrow dk">FAQ</div><h2 class="h2">Questions about {nm.lower().replace(chr(38)+"amp;","and")}.</h2><p>Cannot find your answer? Call +91 91059 09006 or email info@parakramindia.org.</p></div><div class="rv">{faq(faqs)}</div></div></div></section>'
    body+=f'<section class="blk alt"><div class="wrap">{sech("Related services","Explore other services.")}{related(slug)}</div></section>'
    body+=cta2(f'Need {nm.lower().replace(chr(38)+"amp;","and")} for your site?','Tell us about your premises and we will design a plan around it.')
    PAGES['services/'+slug]=(f'{name} | Parakram Security India',f'{short} Trained, verified personnel, available 24/7. Customized to your site.',body,'/services',faq_ld(faqs))

# ---------- About ----------
def about_page():
    o=pbn([('About',None)],'A company built on <em>discipline and trust.</em>','Parakram Security India Private Limited was established in 2017 as a professionally managed private security company.',img('about'),'55% 15%',BTN('Plan Your Security →','/planner')+BTN('Contact Us','/contact','btn-o'))
    o+=f'''<section class="blk"><div class="wrap sp2"><div class="sp2t rv"><div class="eyebrow dk">Who we are</div><h2 class="h2">Protecting people, property and operations.</h2><p>We combine disciplined manpower, rigorous training and deeply rooted Indian values to protect people, property and operations. Our personnel are known for professionalism, integrity and courtesy.</p><p>Your safety is our mission. That mission shapes how we recruit, how we train and how we supervise every post we manage.</p><div class="cta" style="margin-top:26px">{BTN("Meet Our Services →","/services","btn-n")}</div></div><div class="sp2i rv"><img src="{img("about")}" alt="Parakram security personnel" loading="lazy"><span class="badge">Established 2017</span></div></div></section>'''
    o+=f'''<section class="blk alt"><div class="wrap"><div class="nums rv"><div><b data-n="9" data-s="+">0</b><span>Years of experience</span></div><div><b data-n="1500" data-s="+">0</b><span>Trained professionals</span></div><div><b data-n="210" data-s="K">0</b><span>Partners</span></div><div><b data-n="4.9" data-d="1">0</b><span>Client rating</span></div></div></div></section>'''
    o+=f'<section class="blk"><div class="wrap">{sech("What we stand for","Three values in everything we do.")}{cards([("star","Professionalism","Disciplined, trained personnel who present themselves and their work with pride."),("chk","Integrity","Verified, trustworthy teams who act ethically and honestly, every day."),("usr","Courtesy","Respectful, polite service to every visitor, resident, patient and customer.")])}</div></section>'
    o+=f'<section class="blk alt" id="journey"><div class="wrap">{sech("Our journey","Growing steadily since 2017.","A professionally managed company built on training, discipline and trust.")}{jr}</div></section>'
    o+=f'<section class="blk"><div class="wrap">{sech("What sets us apart","Why clients stay with Parakram.")}{cards([("usr","Trained and verified personnel","Disciplined recruitment and rigorous training for every guard before deployment."),("eye","Customized security solutions","Services designed around your site, your risk and your operations."),("clk","Available 24/7","Around the clock service, with supervisors who are accessible when you need them.")])}</div></section>'
    o+=f'''<section class="blk alt"><div class="wrap sp2"><div class="sp2t rv"><div class="eyebrow dk">Headquarters</div><h2 class="h2">Rooted in Haridwar.</h2><p>Our registered office is at 6A Sandesh Nagar, Kankhal, Haridwar 249408, Uttarakhand. From here we plan and support deployments and stay close to our people.</p><div class="cta" style="margin-top:22px">{BTN("Visit Our Coverage Page →","/coverage","btn-n")}</div></div><div class="rv">{ticks(["Registered office in Kankhal, Haridwar","Support for multiple sites","Available 24/7 for our clients"])}</div></div></section>'''
    o+=cta2('Let us protect what matters to you.','Speak to our team about a plan customized to your site.')
    return o
PAGES['about']=('About Us | Parakram Security India','Parakram Security India Private Limited, established in 2017, is a professionally managed private security company built on discipline, training and integrity.',about_page(),'/about','')

# ---------- Why ----------
def why_page():
    o=pbn([('Why Parakram',None)],'Why leaders choose <em>Parakram.</em>','Experience, trained and verified personnel, and solutions customized to your site.',img('training'),'50% 25%',BTN('Plan Your Security →','/planner')+BTN('Contact Us','/contact','btn-o'))
    o+=f'''<section class="blk"><div class="wrap">{sech("Why us","Three reasons clients choose us.")}<div class="fc">
<div class="fcard rv"><span class="no2" data-n="9" data-s="+">0</span><h3>Years of experience</h3><p>A professionally managed security company operating since 2017.</p></div>
<div class="fcard rv"><span class="no2" data-n="1500" data-s="+">0</span><h3>Trained and verified personnel</h3><p>Disciplined recruitment and rigorous training for every guard.</p></div>
<div class="fcard rv"><span class="no2">100%</span><h3>Customized solutions</h3><p>Services designed around your site, your risk and your operations.</p></div></div></div></section>'''
    o+=f'<section class="blk alt"><div class="wrap">{sech("Our standards","How we keep quality high.","Good security is a habit. These six practices shape how we work.")}{cards([("usr","Disciplined recruitment","We recruit with care, looking for people who are disciplined, honest and ready to learn."),("book","Rigorous training","Every guard is trained before deployment and receives guidance as your site needs change."),("chk","Verification","Personnel are verified before they are placed at your site."),("eye","Regular supervision","Supervisors and managers visit posts and act quickly on feedback."),("star","Courtesy","We expect respect and politeness towards every visitor, resident and customer."),("map","Customization","We design each deployment around your premises rather than using a fixed template.")])}</div></section>'
    o+=f'<section class="blk"><div class="wrap">{sech("How we work","From first call to daily supervision.")}{STEPS}</div></section>'
    o+=TESTI
    o+=f'<section class="blk"><div class="wrap">{sech("Explore","See what we can protect for you.")}{related()}</div></section>'
    o+=cta2('Experience the Parakram difference.','Speak to our team about a plan customized to your site.')
    return o
PAGES['why']=('Why Parakram | Parakram Security India','Nine years of experience, 1,500+ trained and verified professionals and security solutions customized to your site. See why clients choose Parakram.',why_page(),'/why','')

# ---------- Industries ----------
IND=[('industrial','Industrial','ind','training','50% 25%','Plants, warehouses and industrial campuses need security that works around shifts, material movement and site safety rules.',['Gate and perimeter control','Vehicle and material checks','Shift wise deployment','Patrols across large areas'],[('industrial','Industrial Security'),('armed','Armed Security'),('manned','Manned Security')]),
('corporate','Corporate','com','operations','65% 25%','Offices and business premises need welcoming, professional security that protects people and leaves a confident first impression.',['Reception and lobby presence','Visitor and access management','Parking and vehicle control','After hours protection'],[('commercial','Commercial Security'),('manned','Manned Security')]),
('healthcare','Healthcare','hos','about','60% 20%','Hospitals and clinics need calm, courteous security that keeps entrances open, families reassured and staff safe.',['Visitor and crowd management','Emergency entrance access','Respectful, patient conduct','Round the clock coverage'],[('hospital','Hospital Security'),('manned','Manned Security')]),
('banking','Banking','bnk','operations','50% 30%','Bank branches and ATMs need vigilant, verified personnel who keep customers comfortable and premises secure.',['Branch entrance security','ATM vigilance','Verified personnel','Clear alert procedures'],[('banking','Bank and ATM Security'),('armed','Armed Security')])]
def industries_page():
    o=pbn([('Industries',None)],'Trusted where safety <em>matters most.</em>','Industrial, corporate, healthcare and banking clients rely on Parakram for trained and verified personnel.',img('operations'),'60% 25%',BTN('Plan Your Security →','/planner')+BTN('Talk to Us','/contact','btn-o'))
    o+=f'<div class="subnav"><div class="wrap"><div class="snv">'+''.join(f'<a href="#{i[0]}">{i[1]}</a>' for i in IND)+'</div><a class="btn btn-g sm" href="/planner">Get a plan</a></div></div>'
    for k,(sl,nm,ic,im,pos,txt,pts,links) in enumerate(IND):
        alt=' alt' if k%2==0 else ''
        rev=' rev' if k%2==1 else ''
        ls=''.join(f'<a class="lk" style="margin-right:18px" href="/services/{a}">{b} →</a>' for a,b in links)
        o+=f'''<section class="blk{alt}" id="{sl}"><div class="wrap sp2{rev}"><div class="sp2t rv"><div class="eyebrow dk">0{k+1} / {nm}</div><h2 class="h2">Security for {nm.lower()} sites.</h2><p>{txt}</p>{ticks(pts)}<div style="margin-top:22px">{ls}</div></div><div class="sp2i rv"><img src="{img(im)}" alt="{nm} security" loading="lazy" style="object-position:{pos}"><span class="badge">{nm}</span></div></div></section>'''
    o+=f'<section class="blk"><div class="wrap">{sech("Also protected","Homes and campuses too.","We also provide residential and educational security for societies, schools and institutions.")}<div class="fc c2">'
    for sl,nm,ic,d in [('residential','Residential Security','res','Courteous, reliable security for homes and societies.'),('educational','Educational Security','edu','Safe, closely supervised campuses for schools and institutions.')]:
        o+=f'<a class="fcard rv" href="/services/{sl}" style="display:block"><div class="ico">{IC[ic]}</div><h3>{nm}</h3><p>{d}</p></a>'
    o+='</div></div></section>'
    o+=cta2('Tell us about your industry.','We will design a plan around how your site works.')
    return o
PAGES['industries']=('Industries | Parakram Security India','Security for industrial, corporate, healthcare and banking sites, plus residential and educational premises. Trained, verified personnel, available 24/7.',industries_page(),'/industries','')

# ---------- Coverage ----------
def coverage_page():
    o=pbn([('Coverage',None)],'Local roots. <em>Wider reach.</em>','Headquartered in Haridwar, Uttarakhand, with support for multiple sites.',img('about'),'50% 20%',BTN('Tell Us Your Locations →','/contact')+BTN('Plan Your Security','/planner','btn-o'))
    o+=f'''<section class="blk"><div class="wrap sp2" style="align-items:start"><div class="rv">{mapx}</div><div class="sp2t rv"><div class="eyebrow dk">Coverage</div><h2 class="h2">Explore the map.</h2><p>Select a state to see how to reach us. Our headquarters is in Haridwar, Uttarakhand, and we support clients with multiple sites.</p>{ticks(["Registered office in Kankhal, Haridwar","Support for multiple sites under one plan","Available 24/7"])}<div class="cta" style="margin-top:24px">{BTN("Contact Us →","/contact","btn-n")}</div></div></div></section>'''
    o+=f'<section class="blk alt"><div class="wrap">{sech("Multiple sites","One partner across your locations.","When you have more than one site, we plan them together so standards stay consistent everywhere.")}{cards([("map","Plan together","We study each location and build one plan that respects the needs of every site."),("eye","Consistent standards","The same training, supervision and courtesy at every post."),("clk","Always reachable","Supervisors who are accessible, and service available 24/7.")])}</div></section>'
    o+=cta2('Have sites in more than one place?','Tell us where and we will confirm how we can support you.')
    return o
PAGES['coverage']=('Coverage | Parakram Security India','Parakram Security India is headquartered in Haridwar, Uttarakhand, with support for multiple sites. Explore our interactive coverage map.',coverage_page(),'/coverage','')

# ---------- Careers ----------
def careers_page():
    o=pbn([('Careers',None)],'Serve with <em>Parakram.</em>','Join a disciplined, professionally managed team built on integrity and courtesy.',img('training'),'50% 20%',BTN('Apply Now →','#apply')+BTN('Email Us','mailto:info@parakramindia.org?subject=Career%20enquiry','btn-o'))
    o+=f'<section class="blk"><div class="wrap">{sech("Why join us","A team that values discipline.","We are a team of more than 1,500 trained professionals, and we keep growing.")}{cards([("star","Professionalism","We expect high standards and we help you meet them with structured training."),("chk","Integrity","We value honesty and trust, and we build teams that clients can rely on."),("usr","Courtesy","Respectful service to every visitor and client is part of the job.")])}</div></section>'
    o+=f'<section class="blk alt"><div class="wrap sp2"><div class="sp2t rv"><div class="eyebrow dk">Who we look for</div><h2 class="h2">People ready to learn and serve.</h2><p>Parakram recruits with care. If you are disciplined, honest and want to build a career in security, we would like to hear from you.</p>{ticks(["Discipline and a sense of responsibility","Honesty and integrity","Courtesy towards everyone you serve","Willingness to complete rigorous training","Readiness to work in shifts"])}</div><div class="sp2i rv"><img src="{img("training")}" alt="Parakram personnel in training" loading="lazy"><span class="badge">Join our team</span></div></div></section>'
    o+=f'''<section class="blk"><div class="wrap">{sech("How hiring works","Four simple steps.")}<div class="fc c4">{"".join(f'<div class="fcard rv"><span class="no2">0{i+1}</span><h3>{t}</h3><p>{d}</p></div>' for i,(t,d) in enumerate([("Apply","Send us your details using the form or by email."),("Verification","We verify your details before moving ahead."),("Training","Selected candidates complete rigorous training."),("Deployment","You join a site with supervision and support.")]))}</div></div></section>'''
    o+=f'''<section class="blk alt" id="apply"><div class="wrap sp2" style="align-items:start"><div class="sp2t rv"><div class="eyebrow dk">Apply</div><h2 class="h2">Start your application.</h2><p>Fill in a few details and we will open WhatsApp with your message ready to send to our team. You can also email info@parakramindia.org.</p></div><form class="frm rv" id="cvf"><div><label for="vn">Full name</label><input id="vn" required autocomplete="name"></div><div><label for="vp">Phone</label><input id="vp" type="tel" required autocomplete="tel"></div><div><label for="vc">City</label><input id="vc" autocomplete="address-level2"></div><div><label for="vr">Role of interest</label><select id="vr"><option>Security guard</option><option>Supervisor</option><option>Armed guard</option><option>Other</option></select></div><div class="full"><label for="vm">A little about you</label><textarea id="vm" placeholder="Your experience, if any"></textarea></div><button class="btn btn-n full" style="justify-content:center">Apply on WhatsApp →</button></form></div></section>'''
    o+=cta2('Questions about working with us?','Email info@parakramindia.org and we will be happy to help.',('Email Us','mailto:info@parakramindia.org'),('Call +91 91059 09006','tel:+919105909006'))
    return o
PAGES['careers']=('Careers | Parakram Security India','Build a career with Parakram Security India. Join a disciplined, professionally managed team built on integrity and courtesy.',careers_page(),'/careers','')

# ---------- FAQ ----------
FAQS=[('What types of security services do you provide?','Manned, Armed, Industrial, Commercial, Residential, Hospital, Educational, and Bank and ATM security.','services'),
('Do you provide armed security?','Yes. Armed security is one of our eight services and is planned around the rules and licence requirements that apply to your site.','services'),
('Which industries do you serve?','Industrial, corporate, healthcare and banking clients, along with residential societies and educational institutions.','services'),
('How are your personnel trained and verified?','Through disciplined recruitment and rigorous training, so every guard is trained and verified before deployment.','personnel'),
('How do you keep guards professional?','Supervisors and managers visit posts regularly and are available to you. We act on feedback quickly.','personnel'),
('Is your service available 24/7?','Yes, our services are available 24/7.','deployment'),
('How is the number of guards decided?','We assess your site, entry points, working hours and risk, then recommend a plan. You can adjust it as your needs change.','deployment'),
('Where do you operate?','We are headquartered in Haridwar, Uttarakhand. Tell us your location and we will confirm how we can support you.','deployment'),
('Can you support more than one site?','Yes. We can support multiple sites, and we plan them together so that standards stay consistent.','deployment'),
('Can solutions be customized to my site?','Yes. We design customized security solutions around your needs, including support for multiple sites.','deployment'),
('How do I get started?','Use our Security Planner, call +91 91059 09006, or email info@parakramindia.org. We will respond with a plan customized to your site.','deployment')]
def faq_page():
    o=pbn([('FAQ',None)],'Answers <em>before you ask.</em>','Everything you need to know about our services, our people and how we work.',img('operations'),'60% 25%',BTN('Ask Us Directly →','/contact')+BTN('Plan Your Security','/planner','btn-o'))
    o+=f'''<section class="blk"><div class="wrap"><div class="narrow" id="faqf"><div class="fsearch rv"><input id="faqs" type="search" placeholder="Search questions" aria-label="Search questions"></div><div class="fchips rv"><button class="on" data-c="all">All</button><button data-c="services">Services</button><button data-c="personnel">Personnel</button><button data-c="deployment">Deployment</button></div><div class="rv">{faq(FAQS)}</div><div class="fnone" id="fnone">No questions match your search. Please call +91 91059 09006 and we will help.</div></div></div></section>'''
    o+=cta2('Still have a question?','Our team is available 24/7.')
    return o
PAGES['faq']=('FAQ | Parakram Security India','Answers about Parakram Security India services, personnel training and verification, 24/7 availability, coverage and how to get started.',faq_page(),'/faq',faq_ld(FAQS))

# ---------- Contact ----------
MAPQ='https://www.google.com/maps?q=6A+Sandesh+Nagar+Kankhal+Haridwar+249408&output=embed'
def contact_page():
    o=pbn([('Contact',None)],'Let us secure <em>your world.</em>','Speak to our team about a security plan customized to your site. We are available 24/7.',img('about'),'50% 20%',BTN('Plan Your Security →','/planner')+BTN('Call Now','tel:+919105909006','btn-o'))
    o+=f'''<section class="blk"><div class="wrap"><div class="cc rv"><div class="ccd"><div class="ico">{IC["ph"]}</div><h3>Call us</h3><a href="tel:+919105909006">+91 91059 09006</a><a href="tel:+918937000489">+91 89370 00489</a><a href="tel:+919105909000">+91 91059 09000</a></div><div class="ccd"><div class="ico">{IC["ml"]}</div><h3>Email us</h3><a href="mailto:info@parakramindia.org">info@parakramindia.org</a><p>We reply as quickly as we can.</p></div><div class="ccd"><div class="ico">{IC["map"]}</div><h3>Visit us</h3><p>6A Sandesh Nagar, Kankhal, Haridwar 249408, Uttarakhand</p><a href="https://www.google.com/maps/search/?api=1&amp;query=6A+Sandesh+Nagar+Kankhal+Haridwar+249408" target="_blank" rel="noopener">Get directions →</a></div></div></div></section>'''
    o+=f'''<section class="blk alt"><div class="wrap sp2" style="align-items:stretch"><form class="frm rv" id="cf"><div class="full"><h2 class="h2" style="font-size:28px!important">Send us a message</h2><p style="color:#4a5070;margin-top:6px">We will open WhatsApp with your message ready to send.</p></div><div><label for="cn">Full name</label><input id="cn" required autocomplete="name"></div><div><label for="cp">Phone</label><input id="cp" type="tel" required autocomplete="tel"></div><div class="full"><label for="ce">Email</label><input id="ce" type="email" autocomplete="email"></div><div class="full"><label for="cs">Service required</label><select id="cs"><option value="">Select a service</option>{"".join(f"<option>{s[1]}</option>" for s in SERV)}</select></div><div class="full"><label for="cm">Your requirement</label><textarea id="cm" placeholder="Tell us about your site and requirements"></textarea></div><button class="btn btn-n full" style="justify-content:center">Send on WhatsApp →</button></form><div class="rv"><iframe class="mapf" title="Parakram Security India on Google Maps" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="{MAPQ}"></iframe></div></div></section>'''
    o+=cta2('Prefer a guided plan?','Answer four quick questions with our Security Planner.',('Open the Security Planner →','/planner'),('Chat on WhatsApp','https://wa.me/919105909006'))
    return o
PAGES['contact']=('Contact Us | Parakram Security India','Contact Parakram Security India. Call +91 91059 09006, email info@parakramindia.org or visit our office in Kankhal, Haridwar. Available 24/7.',contact_page(),'/contact','')

# ---------- Planner ----------
def planner_page():
    o=pbn([('Security Planner',None)],'Tell us what you need. <em>We will design the plan.</em>','Answer four quick questions and our team will respond with a solution customized to your site, with no obligation.',img('training'),'50% 20%','',['Takes about a minute','Opens on WhatsApp','No obligation'])
    o+=f'<section class="blk"><div class="wrap"><div class="plan-wrap">{wz.replace("wz rv","wz rv")}</div></div></section>'
    o+=f'<section class="blk alt"><div class="wrap">{sech("What happens next","We take it from here.")}{cards([("ph","We review","Our team reads your answers and studies your requirement."),("eye","We assess","We may ask a few questions or visit your site to understand it properly."),("chk","We propose","You receive a plan customized to your site, with no obligation.")],num=False)}</div></section>'
    return o
PAGES['planner']=('Security Planner | Parakram Security India','Tell us what you need with the Parakram Security Planner. Answer four quick questions and receive a plan customized to your site.',planner_page(),'/planner','')

# ---------- assemble ----------
def hyphen_check(name,t):
    body=re.sub(r'<script.*?</script>|<style.*?</style>|<svg.*?</svg>','',t,flags=re.S)
    import html as H2
    txt=H2.unescape(re.sub(r'<[^>]+>','\n',body))
    bad=sorted(set(l.strip() for l in txt.split('\n') if re.search(r'[–—]|\w-\w',l)))
    if bad: print('HYPHEN',name,bad[:4])

def shell(path,title,desc,body,nav,extra):
    title=title.replace(' & ',' and ')
    h=head
    h=re.sub(r'<title>.*?</title>',f'<title>{title}</title>',h,flags=re.S)
    h=re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{desc}">',h)
    h=re.sub(r'<link rel="canonical" href="[^"]*">',f'<link rel="canonical" href="{U}/{path}">',h)
    h=re.sub(r'<meta property="og:title" content="[^"]*">',f'<meta property="og:title" content="{title}">',h)
    h=re.sub(r'<meta property="og:description" content="[^"]*">',f'<meta property="og:description" content="{desc}">',h)
    h=re.sub(r'<meta property="og:url" content="[^"]*">',f'<meta property="og:url" content="{U}/{path}">',h)
    h=re.sub(r'<meta name="twitter:title" content="[^"]*">',f'<meta name="twitter:title" content="{title}">',h)
    h=re.sub(r'<meta name="twitter:description" content="[^"]*">',f'<meta name="twitter:description" content="{desc}">',h)
    h=re.sub(r'<script>try\{if\(!sessionStorage.*?</script>\n','',h,flags=re.S)
    h=re.sub(r'<script type="application/ld\+json">\{"@context":"https://schema.org","@type":"FAQPage".*?</script>\n','',h,flags=re.S)
    bl=[{"@type":"ListItem","position":1,"name":"Home","item":U+"/"}]
    segs=path.split('/')
    for i,sg in enumerate(segs):
        bl.append({"@type":"ListItem","position":i+2,"name":(PAGES.get('/'.join(segs[:i+1]),(sg.title(),))[0].split(' | ')[0]),"item":U+'/'+'/'.join(segs[:i+1])})
    h=h.replace('</head>','<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":bl})+'</script>\n'+extra+'\n</head>')
    hd=header.replace(f'<a href="{nav}">',f'<a class="act" href="{nav}">',1) if nav else header
    return (h+'<body>\n<a class="skip" href="#main">Skip to content</a>\n<div id="pg"></div>\n<div id="toast" role="status" aria-live="polite"></div>\n'+util+'\n'+hd+'\n<main id="main">'+body+'</main>\n'+ctab+footer+'\n'+mbar+topbtn+'\n'+wabtn+'\n<script src="/js/lenis.min.js"></script>\n<script src="/js/app.js?v='+V+'"></script>\n</body></html>')

sitemap=['']
for path,(title,desc,body,nav,extra) in PAGES.items():
    html_=absolutize(shell(path,title,desc,body,nav,extra))
    wr(path+'.html',html_)
    hyphen_check(path,html_)
    sitemap.append(path)
for f in ('privacy','terms'): sitemap.append(f)
wr('sitemap.xml','<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{U}/{p}</loc></url>' for p in sitemap)+'</urlset>')
wr('vercel.json',json.dumps({"cleanUrls":True,"trailingSlash":False,"headers":[{"source":"/(css|js)/(.*)","headers":[{"key":"Cache-Control","value":"public, max-age=31536000, immutable"}]},{"source":"/img/(.*)","headers":[{"key":"Cache-Control","value":"public, max-age=86400"}]}]}))
hyphen_check('index',home)
print('pages',len(PAGES))
