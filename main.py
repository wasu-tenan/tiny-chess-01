import json,os;from urllib.request import*
W=[0,100,320,330,500,900,0,100,320,330,500,900,0];M=100000;KD=[-17,-16,-15,-1,1,15,16,17];ND=[-33,-31,-18,-14,14,18,31,33]
TP=["k"*8+"uuuuuuuummoqqommllmppmllkkkookkkljikkijllmmggmml"+"k"*8,"eccaacce"*4+"geecceegiggggggiookkkkoooqmkkmqo"]
PS=[None]+[[(ord(c)-107)*5 for c in t]for t in TP];PS[2:2]=[[0]*64]*4
MV=[None]*128
for s in range(128):
 if s&0x88:continue
 sl=[]
 for d in KD:
  r=[];t=s+d
  while not t&0x88:r.append(t);t+=d
  sl.append(r)
 MV[s]=[0,0,[[s+d]for d in ND if not(s+d)&0x88],[sl[i]for i in(0,2,5,7)],[sl[i]for i in(1,3,4,6)],sl,[r[:1]for r in sl if r]]
B=[0]*128;S=0;C=0;E=-1;KS=[0,0];NDS=0;LIM=85000;BM=0;T={};HH=[0]*16384;SQ=[s for s in range(128)if s&119==s]
CM=[15]*128;CM[119]=14;CM[112]=13;CM[7]=11;CM[0]=7
def fen(f):
 global B,S,C,E
 B=[0]*128;w=f.split();s=0
 for c in w[0]:
  if c=="/":s+=8
  elif c.isdigit():s+=int(c)
  else:
   p="pnbrqk".index(c.lower())+1;B[s]=p+6*(c>"Z")
   if p==6:KS[c>"Z"]=s
   s+=1
 S=w[1]!="w";C=sum((c in w[2])<<i for i,c in enumerate("KQkq"));E=-1 if w[3]=="-"else(8-int(w[3][1]))*16+ord(w[3][0])-97
def atk(s,by):
 b=6*by;d=32*by-16
 for t in(s-d-1,s-d+1):
  if not t&0x88 and B[t]==1+b:return 1
 for pt in range(2,7):
  for ray in MV[s][pt]:
   for t in ray:
    q=B[t]
    if q:
     if q==pt+b:return 1
     break
 return 0
def gen(cap):
 ms=[];bl=S;b=6*bl;fw=32*bl-16;sr=6-5*bl;pr=1+5*bl;ap=ms.append
 def pm(s,t):
  if(s>>4)==pr:
   for x in(5,4,3,2):ap(s|t<<7|x<<14)
  else:ap(s|t<<7)
 for s in SQ:
  p=B[s]
  if not p or(p>6)!=bl:continue
  pt=p-b
  if pt==1:
   for d in(fw-1,fw+1):
    t=s+d
    if not t&0x88 and((B[t]and(B[t]>6)!=bl)or t==E):pm(s,t)
   t=s+fw
   if not B[t]and(not cap or(s>>4)==pr):
    pm(s,t)
    if not cap and(s>>4)==sr and not B[s+2*fw]:ap(s|s+2*fw<<7)
  else:
   for ray in MV[s][pt]:
    for t in ray:
     q=B[t]
     if q:
      if(q>6)!=bl:ap(s|t<<7)
      break
     if not cap:ap(s|t<<7)
   if pt==6 and not cap:
    for sg,bit in((1,1),(-1,2)):
     if C&(bit<<2*bl)and B[s+[3,-4][sg<0]]==4+b and all(not B[s+d]for d in[(1,2),(-1,-2,-3)][sg<0])and all(not atk(s+d,1-bl)for d in(0,sg,2*sg)):ap(s|s+2*sg<<7)
 return ms
def mk(m):
 global S,C,E
 f=m&127;t=(m>>7)&127;pr=(m>>14)&7;p=B[f];b=(p>6)*6;pt=p-b;cp=B[t]
 if pt==1 and t==E and not cp and(f&7)!=(t&7):B[t+16-32*(p>6)]=0
 B[f]=0;B[t]=pr+b if pr else p
 if pt==6:
  KS[p>6]=t;C&=~(3+9*(p>6))
  if abs(t-f)==2:
   rf,rt=(f+3,f+1)if t>f else(f-4,f-1);B[rf],B[rt]=B[rt],B[rf]
 C&=CM[f]&CM[t];E=-1
 if pt==1 and abs(t-f)==32:E=(f+t)//2
 S=1-S
def ev():
 s=0
 for q in SQ:
  p=B[q]
  if not p:continue
  bl=p>6;pt=p-6*bl;i=q-(q>>4)*8;v=W[pt]+PS[pt][i^(56*bl)]
  s+=-v if bl else v
 return s
def ordm(ms,tm):
 def sc(m):cp=B[(m>>7)&127];return(7**9)if m==tm else W[cp]*16-W[B[m&127]]if cp else HH[m&16383]//16
 return sorted(ms,key=sc,reverse=True)
def sr(d,a,be,ply):
 global NDS,BM,C,E,S
 NDS+=1
 if NDS>LIM:exit()
 tm=d>0 and T.get(bytes(B))or 0
 chk=atk(KS[S],1-S)
 if d<=0 and not chk:
  st=-ev()if S else ev()
  if st>=be:return be
  if st>a:a=st
 bst=-2*M
 for m in ordm(gen(d<=0 and not chk),tm):
  sv=(B[:],C,E,KS[:],S);mk(m)
  if atk(KS[1-S],S):
   B[:],C,E,KS[:],S=sv;continue
  v=-sr(d-1+chk,-be,-a,ply+1);B[:],C,E,KS[:],S=sv
  if v>bst:
   bst=v
   if ply==0:BM=m
   if d>0:T[bytes(B)]=m
  if v>a:a=v
  if a>=be:
   if d>0 and not B[m>>7&127]:HH[m&16383]+=d
   break
 if bst==-2*M:return-M+ply if chk else a if d<=0 else 0
 return a if d<=0 else bst
def best(f):
 global NDS,BM
 fen(f);NDS=0;BM=0;T.clear()
 for d in range(99):
  try:sr(d,-M-1,M+1,0)
  except SystemExit:break
 return BM
def post(p,b):
 q=Request(ENV+p,data=json.dumps(b).encode(),headers={"content-type":"application/json"})
 with urlopen(q)as x:return json.load(x)
if __name__=="__main__":
 ENV=os.environ["MAKEFUN_ENV_URL"]
 while 1:
  g=post("/game",{})
  if g["status"]=="done":break
  while g["status"]=="your_move":
   m=best(g["fen"]);u=g["legal_moves"][0]
   if m:
    u=""
    for x in(m&127,m>>7&127):u+=chr(97+(x&7))+str(8-(x>>4))
    if m>>14:u+="__nbrq"[m>>14]
   g=post("/move",{"game":g["game"],"move":u})
