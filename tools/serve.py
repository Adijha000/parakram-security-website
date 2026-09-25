import http.server,socketserver,os,sys
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
class H(http.server.SimpleHTTPRequestHandler):
    def translate_path(self,path):
        p=super().translate_path(path.split('?')[0].split('#')[0])
        q=p.rstrip('/')
        if (not os.path.exists(p) or (os.path.isdir(p) and not os.path.exists(os.path.join(p,'index.html')))) and os.path.exists(q+'.html'): return q+'.html'
        return p
    def end_headers(self):
        self.send_header('Cache-Control','no-store'); super().end_headers()
    def log_message(self,*a): pass
socketserver.TCPServer.allow_reuse_address=True
with socketserver.TCPServer(('',int(sys.argv[1])),H) as s: s.serve_forever()
