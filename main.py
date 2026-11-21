import os,json,urllib.request as u
V=(0,100,320,330,500,900,0);D=(15,17,-15,-17,1,-1,16,-16);J=(33,31,18,14,-14,-18,-31,-33)
B=[0]*128;t=1;c=15;ep=-1;NM=6400;N=0;L=80000
TT={};KL=0;Pt=[];Ud=[]
Mc={0:13,7:14,4:12,112:7,119:11,116:3};X=Exception
def hk():return hash((tuple(B),t,c,ep))
def A(q,w):
 for d in(15,17):
  x=q-w*d
  if not x&136 and B[x]==w:return 1
 for d in J+D:
  x=q+d
  if not x&136 and B[x]==w*(6-4*(d in J)):return 1
 for j,d in enumerate(D):
  x=q
  while 1:
   x+=d
   if x&136:break
   p=B[x]
   if p:
    if p in(w*5,w*(3+(j>3))):return 1
    break
 return 0
def G(cp):
 m=[];ad=lambda x:m.append(f|(x<<7));am=lambda to:[m.append(f|(to<<7)|(q<<14))for q in(5,4,3,2)]if(to>>4)==7*(t>0)else ad(to)
 for f,p in enumerate(B):
  if p*t<=0:continue
  a=abs(p)
  if a==1:
   d=16*t;to=f+d
   if B[to]==0 and(not cp or(to>>4)==7*(t>0)):
    am(to)
    if(f>>4)==1+5*(t<0) and B[f+2*d]==0:ad(f+2*d)
   for dd in(d-1,d+1):
    to=f+dd
    if not to&136 and(B[to]*t<0 or to==ep):am(to)
  else:
   os=J if a==2 else D[:4] if a==3 else D[4:] if a==4 else D;sl=2<a<6
   for st in os:
    to=f
    while 1:
     to+=st
     if to&136:break
     if B[to]*t<0 or(not cp and B[to]==0):ad(to)
     if B[to] or not sl:break
   if a==6 and not cp:
    for sgn,bt in((1,1<<2*(t<0)),(-1,2<<2*(t<0))):
     if c&bt and all(B[f+j*sgn]==0 and not A(f+j*sgn,-t)for j in(1,2))and(sgn>0 or B[f-3]==0)and not A(f,-t):ad(f+2*sgn)
 return m
def M(m):
 global t,c,ep,NM
 f=m&127;to=(m>>7)&127;pr=m>>14
 p=B[f];v=B[to];cs=-1
 if p==t and to==ep and v==0:cs=to-16*t;v=B[cs]
 Ud.append((B[:],t,c,ep,NM))
 if cs>=0:B[cs]=0
 B[f]=0
 if pr:B[to]=pr*t;NM+=V[pr]-100
 else:B[to]=p
 if abs(v)>1:NM-=V[abs(v)]
 if p==6*t and abs(to-f)==2:rf,rt=(to+1,to-1)if to>f else(to-2,to+1);B[rt]=B[rf];B[rf]=0
 c&=Mc.get(f,15)&Mc.get(to,15)
 ep=(f+to)//2 if p==t and abs(to-f)==32 else -1;t=-t
def W():
 global t,c,ep,NM
 B[:],t,c,ep,NM=Ud.pop()
def O(m):
 if m==TM:return -99999
 v=B[(m>>7)&127]
 return -V[abs(v)]*10 if v else -9000 if m>>14 else -8000 if KL==m else 0
def S(d,a,b,pl):
 global N,BM,TM,KL,t,ep
 if(N:=N+1)>L:raise X
 k=hk()
 if Pt.count(k)>1:return 0
 d0,sc0,fl0,tm=TT.get(k,(-999,0,0,0))
 if d0>=d and(fl0==0 or sc0>=b if fl0<2 else sc0<=a):
  if pl==0:BM=tm
  return sc0
 chk=A(B.index(6*t),-t)
 if chk:d+=1
 if d<=0 and not chk:
  st=0
  for i,p in enumerate(B):
   if p:
    u=abs(p);q=9*(i>>4 if p>0 else 7-(i>>4))if u==1 else 0
    st+=V[u]+q if p*t>0 else -V[u]-q
  if d<-5:return st
  if st>=b:return b
  a=max(a,st)
 if d>=3 and not chk and NM>0:
  oe=ep;ep,t=-1,-t;sc=-S(d-3,-b,-b+1,pl+1);t,ep=-t,oe
  if sc>=b:return b
 ms=G(not chk and d<=0);TM=tm;ms.sort(key=O);a0=a;bs=-99999;bm=0
 for i,m in enumerate(ms):
  to=(m>>7)&127;v=B[to];cp=v or to==ep or m>>14
  if d<=0 and not chk and st+(V[abs(v)]or(to==ep)*100)+V[m>>14]+200<a:continue
  M(m)
  if A(B.index(-6*t),t):W();continue
  Pt.append(hk())
  r=i>2 and d>=3 and not chk and not cp
  sc=-S(d-1-r,-a-1 if r else -b,-a,pl+1)
  if r and sc>a:sc=-S(d-1,-b,-a,pl+1)
  Pt.pop();W()
  if sc>bs:bs=sc;bm=m
  if sc>a:a=sc
  if a>=b:KL=m;break
 if bs==-99999:return -99999+pl if chk else a*(d<=0)
 TT[k]=(d,bs,(bs>=b)or 2*(bs<=a0),bm)
 if pl==0:BM=bm
 return bs
def CH():
 global N,BM
 Pt[:]=[hk()];BM=0
 for d in range(8):
  N=0
  try:S(d+1,-99999,99999,0)
  except X:
   while Ud:W()
  if N>4e4:break
 return BM
def UC(m):
 f=m&127;to=(m>>7)&127
 s='abcdefgh'[f&7]+str(1+(f>>4))+'abcdefgh'[to&7]+str(1+(to>>4))
 return s+('nbrq'[(m>>14)-2] if m>>14 else '')
def post(p,d):
 try:return json.load(u.urlopen(os.environ['MAKEFUN_ENV_URL']+p,json.dumps(d).encode()))
 except Exception as h:return json.load(h)
lg=-1;sn=0
while 1:
 g=post('/game',{})
 if g['status']=='done':break
 if g['game']!=lg:
  lg=gm=g['game'];sn=0;B=[0]*128;NM=6400;t=1;c=15;ep=-1
  for i,p in enumerate((4,2,3,5,6,3,2,4)):B[i]=p;B[i+112]=-p;B[i+16]=1;B[i+96]=-1
 while g['status']=='your_move':
  for s in g['moves'][sn:]:[M(m)for m in G(0)if UC(m)==s]
  sn=len(g['moves']);Ud=[];mv=CH()
  s=UC(mv) if mv else g['legal_moves'][0]
  r=post('/move',{'game':gm,'move':s})
  g=r
