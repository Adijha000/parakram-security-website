// Career application endpoint. Sends an email (with the resume attached) through Resend.
// Configure in Vercel: RESEND_API_KEY (required), APPLY_TO_EMAIL (default info@parakramindia.org), APPLY_FROM_EMAIL (a verified sender).
const esc=s=>String(s==null?'':s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const OK=['application/pdf','application/msword','application/vnd.openxmlformats-officedocument.wordprocessingml.document'];
module.exports=async(req,res)=>{
  res.setHeader('Cache-Control','no-store');
  if(req.method!=='POST'){res.status(405).json({ok:false,code:'method'});return}
  let b=req.body;
  try{if(typeof b==='string')b=JSON.parse(b)}catch(e){res.status(400).json({ok:false,code:'bad_json'});return}
  b=b||{};
  if(b.website){res.status(200).json({ok:true});return} // honeypot
  const name=String(b.name||'').trim().slice(0,120),phone=String(b.phone||'').trim().slice(0,30);
  if(name.length<2||phone.replace(/\D/g,'').length<7){res.status(400).json({ok:false,code:'invalid'});return}
  let att;
  if(b.fileBase64){
    const size=Math.floor(String(b.fileBase64).length*0.75);
    if(size>3.2*1024*1024){res.status(413).json({ok:false,code:'too_large'});return}
    const fn=String(b.fileName||'resume').replace(/[^\w.\- ]+/g,'_').slice(0,120);
    const okExt=/\.(pdf|doc|docx)$/i.test(fn);
    if(!okExt&&!OK.includes(b.fileType)){res.status(415).json({ok:false,code:'type'});return}
    att=[{filename:fn,content:String(b.fileBase64)}];
  }
  const key=process.env.RESEND_API_KEY;
  if(!key){res.status(503).json({ok:false,code:'not_configured'});return}
  const to=process.env.APPLY_TO_EMAIL||'info@parakramindia.org';
  const from=process.env.APPLY_FROM_EMAIL||'Parakram Careers <onboarding@resend.dev>';
  const html=`<h2>New career application</h2><table cellpadding="6" style="font-family:Arial,sans-serif;font-size:14px"><tr><td><b>Name</b></td><td>${esc(name)}</td></tr><tr><td><b>Phone</b></td><td>${esc(phone)}</td></tr><tr><td><b>Email</b></td><td>${esc(b.email)}</td></tr><tr><td><b>City</b></td><td>${esc(b.city)}</td></tr><tr><td><b>Role of interest</b></td><td>${esc(b.role)}</td></tr><tr><td valign="top"><b>About</b></td><td>${esc(b.message).replace(/\n/g,'<br>')}</td></tr><tr><td><b>Resume</b></td><td>${att?esc(att[0].filename)+' (attached)':'Not attached'}</td></tr></table>`;
  try{
    const r=await fetch('https://api.resend.com/emails',{method:'POST',headers:{Authorization:'Bearer '+key,'Content-Type':'application/json'},body:JSON.stringify({from,to:[to],subject:'New career application: '+name,html,reply_to:b.email||undefined,attachments:att})});
    if(!r.ok){const t=await r.text();console.error('resend',r.status,t);res.status(502).json({ok:false,code:'send_failed'});return}
    res.status(200).json({ok:true});
  }catch(e){console.error(e);res.status(502).json({ok:false,code:'send_failed'})}
};
