import json,os,sys,random,urllib.request,urllib.error
U=os.environ["MAKEFUN_ENV_URL"]
def post(p,b):
 q=urllib.request.Request(U+p,data=json.dumps(b).encode(),headers={"content-type":"application/json"})
 try:
  with urllib.request.urlopen(q) as x:return json.load(x)
 except urllib.error.HTTPError as e:sys.exit("http "+str(e.code))
KN=[];KG=[];RAY=[];CPW=[];CPB=[]
D8=[(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
for s in range(64):
 r,f=divmod(s,8);kn=[];kg=[];ry=[];cw=[];cb=[]
 for dr,df in [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]:
  r2,f2=r+dr,f+df
  if 0<=r2<8 and 0<=f2<8:kn.append(r2*8+f2)
 for dr,df in D8:
  r2,f2=r+dr,f+df
  if 0<=r2<8 and 0<=f2<8:kg.append(r2*8+f2)
  t=[]
  while 0<=r2<8 and 0<=f2<8:t.append(r2*8+f2);r2+=dr;f2+=df
  ry.append(t)
 if r>0:
  for f2 in (f-1,f+1):
   if 0<=f2<8:cw.append((r-1)*8+f2)
 if r<7:
  for f2 in (f-1,f+1):
   if 0<=f2<8:cb.append((r+1)*8+f2)
 KN.append(kn);KG.append(kg);RAY.append(ry);CPW.append(cw);CPB.append(cb)
FM=[]
for f in range(8):
 m=0
 for r in range(8):m|=1<<(r*8+f)
 FM.append(m)
ADJ=[0]*8
for f in range(8):
 if f>0:ADJ[f]|=FM[f-1]
 if f<7:ADJ[f]|=FM[f+1]
V=[0,100,320,330,500,900,0,0,0,100,320,330,500,900,0]
RK=[[0]*8,[0,0,5,10,18,30,50,0],[-14,-6,-2,2,4,2,-6,-14],[-8,-3,0,1,1,0,-3,-8],[0,0,0,2,2,2,8,0],[-6,-3,-1,0,0,-1,-3,-6],[0,-4,-12,-20,-28,-36,-44,-52]]
FL=[[0]*8,[-3,-1,0,2,2,0,-1,-3],[-14,-6,-2,2,2,-2,-6,-14],[-8,-3,0,1,1,0,-3,-8],[-2,0,1,2,2,1,0,-2],[-6,-3,-1,0,0,-1,-3,-6],[6,8,-4,-10,-10,-4,8,6]]
RKE=[-18,-10,-4,2,2,-4,-10,-18];FLE=[-18,-10,-4,2,2,-4,-10,-18]
PB=[0,0,6,12,24,45,80,0]
_r=random.Random(424243)
ZB=[[ _r.getrandbits(64) for _ in range(64)] for _ in range(15)]
ZS=_r.getrandbits(64);ZC=[_r.getrandbits(64) for _ in range(16)];ZE=[_r.getrandbits(64) for _ in range(64)]
CM=[15]*64;CM[60]=12;CM[63]=14;CM[56]=13;CM[4]=3;CM[7]=11;CM[0]=7
MATE=100000;INF=200000;BUDGET=55000;HARD=85000
B=[0]*64;STM=0;CAST=0;EP=-1;HALF=0;Z=0;SMG=0;SEG=0;CNT=[0]*15;PWB=0;PBB=0;KS=[0,0]
RC={};UND=[];ND=0;PHT={}
TT=[None]*(1<<20);TM=(1<<20)-1
K1=[0]*512;K2=[0]*512;HIST=[0]*8192
BK={4260148928:'h2h4g2g4d4e5g4g5d1d4c4d5f2f4f4e5e5d6d4g7g7e5f1b5',2724279988:'b8d7e7e5a7a6d7c5d8a5b7b5b5b4f6d5f7f5f5f4e8f7a5b6g7g6e5f4f8g7a8b8g6h5c5a4a4b2g7c3',2173103723:'b2b4b4b5c4d3e1g1a2a4c3c4a4b5b1c3h2h4f3g5g2g3f2f3c3d5g5h3g3g4d1e1f3g4e1h4h3g5',3410528031:'e4d6c6e5f8e7e8g8c7c6a7a5f7f6f6f5d6f5e7c5f5d4d4f3f3e1e1d3b7b6d8f6c8a6',2133012567:'a2a4c1d2f3g5h2h3e2e4g5f3e4e5c3e2e2f4b2b3f3d4d4e6d1h5f1c4f4e6h5d5c4d5d2c3a1d1d5c4d1d4',1118361096:'f6g4f7f6c7c6e5d4d8b6g4e5e5f7g7g5f6g5f8e7e7h4b6f2f2f7d7e5e8g8b7b5a7a5a8a5b5b4c8a6a5a6f7g6g6e4h4g5e4g2f8f1g2f1g8g7f1h3g7g6',3470245272:'d4c6e4e5d1e2c2c4g2g4e5f6g4g5f1e2f2f3e1f1f1g2c1d2b2b3d2b4b1d2a2a3h2h4g2f2f2e2d2b3e2e3a1b1h1c1f3f4e3d4d4c5a3a4b1a1c5c6c6c7c7d6h4g5c1c7c7b7d6e5a1h1',178114669:'g8f6e7e5a7a5e8g8d7d6f6d5c6d4a5a4h7h5f7f5a4b3d4b3f5f4f4f3b7b6d8c7a8b8c8d7d7g4g7f6f6g5c7d8b8a8a8a4a4a5a5a1b6b5b5b4'}
BKM=[None];BKN=[0]
class Abort(Exception):pass
def pv(p,s):
 t=p&7;f=s&7;pr=7-(s>>3) if p<8 else s>>3
 if t==6:return V[p]+RK[6][pr]+FL[6][f],V[p]+RKE[pr]+FLE[f]
 v=V[p]+RK[t][pr]+FL[t][f]
 return v,v
PV=[[None]*64 for _ in range(15)]
for _p in range(1,15):
 if _p!=7 and _p!=8:
  for _s in range(64):PV[_p][_s]=pv(_p,_s)
def ap(p,s,k):
 global SMG,SEG,PWB,PBB
 c=CNT;c[p]+=k
 v=PV[p][s]
 if p<8:SMG+=k*v[0];SEG+=k*v[1]
 else:SMG-=k*v[0];SEG-=k*v[1]
 if p==1:PWB^=1<<s
 elif p==9:PBB^=1<<s
 if (p&7)==6:KS[p>8]=s
def hash_now():
 z=0
 for s in range(64):
  p=B[s]
  if p:z^=ZB[p][s]
 if STM:z^=ZS
 z^=ZC[CAST]
 if EP>=0:z^=ZE[EP]
 return z
def set_fen(fen):
 global B,STM,CAST,EP,HALF,Z,SMG,SEG,CNT,PWB,PBB,KS
 B=[0]*64;CNT=[0]*15;SMG=0;SEG=0;PWB=0;PBB=0;KS=[0,0]
 ps=fen.split();r=0;f=0
 for c in ps[0]:
  if c=='/':r+=1;f=0
  elif c.isdigit():f+=int(c)
  else:
   t="pnbrqk".index(c.lower())+1;p=t if c.isupper() else t+8
   B[r*8+f]=p;ap(p,r*8+f,1);f+=1
 STM=0 if ps[1]=='w' else 1
 CAST=0
 if 'K' in ps[2]:CAST|=1
 if 'Q' in ps[2]:CAST|=2
 if 'k' in ps[2]:CAST|=4
 if 'q' in ps[2]:CAST|=8
 EP=-1 if ps[3]=='-' else (8-int(ps[3][1]))*8+"abcdefgh".index(ps[3][0])
 HALF=int(ps[4]) if len(ps)>4 else 0
 Z=hash_now()
def att(s,by):
 bb=B
 if by==0:
  for t in CPB[s]:
   if bb[t]==1:return 1
  n,bp,rp,qp,kp=2,3,4,5,6
 else:
  for t in CPW[s]:
   if bb[t]==9:return 1
  n,bp,rp,qp,kp=10,11,12,13,14
 for t in KN[s]:
  if bb[t]==n:return 1
 for t in KG[s]:
  if bb[t]==kp:return 1
 R=RAY[s]
 for d in range(4):
  for t in R[d]:
   p=bb[t]
   if p:
    if p==rp or p==qp:return 1
    break
 for d in range(4,8):
  for t in R[d]:
   p=bb[t]
   if p:
    if p==bp or p==qp:return 1
    break
 return 0
def gen(caponly):
 ms=[];w=STM==0;lo,hi=(1,6) if w else (9,14);add=ms.append;bb=B;knl=KN;kgl=KG;ryl=RAY;vl=V
 for s in range(64):
  p=bb[s]
  if p<lo or p>hi:continue
  t=p&7
  if t==1:
   d=-8 if w else 8;pr7=0 if w else 7;one=s+d
   if not caponly and not bb[one]:
    if (one>>3)==pr7:
     for pr in (5,4,3,2):add(((1900000+vl[pr]*10)<<15)|(s|one<<6|pr<<12))
    else:
     add(s|one<<6)
     if (s>>3)==(6 if w else 1) and not bb[s+2*d]:add(s|(s+2*d)<<6)
   for t2 in (CPW[s] if w else CPB[s]):
    q=bb[t2]
    if q and (q>8)==w:
     if (t2>>3)==pr7:
      for pr in (5,4,3,2):add(((2000000+vl[q]*10+vl[pr]*10-vl[p]//10)<<15)|(s|t2<<6|pr<<12))
     else:add(((2000000+vl[q]*10-vl[p]//10)<<15)|(s|t2<<6))
    elif t2==EP:add(((2000000+1000-vl[p]//10)<<15)|(s|t2<<6))
  elif t==2 or t==6:
   for t2 in (knl[s] if t==2 else kgl[s]):
    q=bb[t2]
    if not q:
     if not caponly:add(s|t2<<6)
    elif (q>8)==w:add(((2000000+vl[q]*10-vl[p]//10)<<15)|(s|t2<<6))
   if t==6 and not caponly:
    if w:
     if CAST&1 and not B[61] and not B[62] and not att(60,1) and not att(61,1) and not att(62,1):add(60|62<<6)
     if CAST&2 and not B[59] and not B[58] and not B[57] and not att(60,1) and not att(59,1) and not att(58,1):add(60|58<<6)
    else:
     if CAST&4 and not B[5] and not B[6] and not att(4,0) and not att(5,0) and not att(6,0):add(4|6<<6)
     if CAST&8 and not B[3] and not B[2] and not B[1] and not att(4,0) and not att(3,0) and not att(2,0):add(4|2<<6)
  else:
   dirs=range(8) if t==5 else (range(4,8) if t==3 else range(4))
   for d in dirs:
    for t2 in ryl[s][d]:
     q=bb[t2]
     if not q:
      if not caponly:add(s|t2<<6)
     else:
      if (q>8)==w:add(((2000000+vl[q]*10-vl[p]//10)<<15)|(s|t2<<6))
      break
 return ms
def make(m):
 global STM,CAST,EP,HALF,Z
 f=m&63;t=(m>>6)&63;pr=(m>>12)&15
 p=B[f];cap=B[t]
 UND.append((cap,CAST,EP,HALF,Z))
 HALF=0 if cap or (p&7)==1 else HALF+1
 Z^=ZC[CAST]
 if EP>=0:Z^=ZE[EP]
 if cap:ap(cap,t,-1);Z^=ZB[cap][t]
 ap(p,f,-1);Z^=ZB[p][f];B[f]=0
 if (p&7)==1:
  if t==EP and not cap and (f&7)!=(t&7):
   cp=t+8 if p==1 else t-8;ep=B[cp];ap(ep,cp,-1);Z^=ZB[ep][cp];B[cp]=0
  EP=(f+t)//2 if abs(t-f)==16 else -1
 else:EP=-1
 np=p if not pr else (pr if p<8 else pr+8)
 B[t]=np;ap(np,t,1);Z^=ZB[np][t]
 if (p&7)==6 and abs(t-f)==2:
  if t>f:rf,rt=(63,61) if t==62 else (7,5)
  else:rf,rt=(56,59) if t==58 else (0,3)
  rp=B[rf];ap(rp,rf,-1);Z^=ZB[rp][rf];B[rf]=0;B[rt]=rp;ap(rp,rt,1);Z^=ZB[rp][rt]
 CAST&=CM[f]&CM[t];Z^=ZC[CAST]
 if EP>=0:Z^=ZE[EP]
 STM^=1;Z^=ZS
 RC[Z]=RC.get(Z,0)+1
def unmake(m):
 global STM,CAST,EP,HALF,Z
 RC[Z]-=1
 f=m&63;t=(m>>6)&63;pr=(m>>12)&15
 np=B[t];p=np if not pr else (1 if np<8 else 9)
 ap(np,t,-1);B[t]=0
 if (p&7)==6 and abs(t-f)==2:
  if t>f:rf,rt=(63,61) if t==62 else (7,5)
  else:rf,rt=(56,59) if t==58 else (0,3)
  rp=B[rt];ap(rp,rt,-1);B[rt]=0;B[rf]=rp;ap(rp,rf,1)
 B[f]=p;ap(p,f,1)
 cap,CAST,EP,HALF,Z=UND.pop()
 STM^=1
 if cap:B[t]=cap;ap(cap,t,1)
 elif (p&7)==1 and t==EP and (f&7)!=(t&7):
  cp=t+8 if p==1 else t-8;ep=9 if p==1 else 1;B[cp]=ep;ap(ep,cp,1)
def pt():
 s=0;bb=PWB
 while bb:
  l=bb&-bb;sq=l.bit_length()-1;bb^=l;r=sq>>3;f=sq&7
  if not PBB&(FM[f]|ADJ[f])&((1<<(r*8))-1):s+=PB[7-r]
 bb=PBB
 while bb:
  l=bb&-bb;sq=l.bit_length()-1;bb^=l;r=sq>>3;f=sq&7
  if not PWB&(FM[f]|ADJ[f])&(~((1<<((r+1)*8))-1)):s-=PB[r]
 for f in range(8):
  cw=(PWB&FM[f]).bit_count();cb=(PBB&FM[f]).bit_count()
  if cw>1:s-=9*(cw-1)
  if cb>1:s+=9*(cb-1)
  if cw and not PWB&ADJ[f]:s-=10
  if cb and not PBB&ADJ[f]:s+=10
 return s
def ev():
 if CNT[1]|CNT[9]|CNT[4]|CNT[12]|CNT[5]|CNT[13]==0 and CNT[2]+CNT[3]+CNT[10]+CNT[11]<2:return 0
 ph=CNT[2]+CNT[3]+CNT[10]+CNT[11]+2*(CNT[4]+CNT[12])+4*(CNT[5]+CNT[13])
 if ph>24:ph=24
 s=(SMG*ph+SEG*(24-ph))//24
 if CNT[3]>1:s+=28
 if CNT[11]>1:s-=28
 k=PWB<<64|PBB
 v=PHT.get(k)
 if v is None:v=pt();PHT[k]=v
 s+=v
 return s if STM==0 else -s
def qs(a,b,ply):
 global ND
 ND+=1
 if (ND&1023)==0 and ND>HARD:raise Abort()
 inch=att(KS[STM],STM^1)
 if inch and ply>14:return ev()
 if inch:best=-INF
 else:
  best=ev()
  if best>=b:return b
  if best>a:a=best
 ms=gen(1 if not inch else 0);ms.sort(reverse=True);any=0
 for x in ms:
  m=x&32767;t=(m>>6)&63
  if not inch and (m>>12)&15==0 and best+V[B[t] or 1]+150<=a:continue
  make(m)
  if att(KS[STM^1],STM):unmake(m);continue
  if not inch and not (m>>12)&15 and B[t] and V[B[t]]<V[B[m&63]] and att(t,STM) and not att(KS[STM],STM^1):unmake(m);continue
  any=1
  s=-qs(-b,-a,ply+1)
  unmake(m)
  if s>best:
   best=s
   if s>a:a=s
   if s>=b:break
 if inch and not any:return -MATE+ply
 return best
def srch(d,a,b,ply,cn):
 global ND,STM,EP,Z,HALF
 if d<=0:return qs(a,b,ply)
 ND+=1
 if (ND&1023)==0 and ND>HARD:raise Abort()
 if ply>0:
  if RC.get(Z,0)>1:return -35
  if HALF>=100:return 0
  a=max(a,-MATE+ply);b=min(b,MATE-ply-1)
  if a>=b:return a
 inch=att(KS[STM],STM^1)
 if inch:d+=1
 e=TT[Z&TM];ttm=0
 if e and e[0]==Z:
  ttm=e[4]
  if e[1]>=d and ply>0:
   s=e[3]
   if s>MATE-1000:s-=ply
   elif s<-MATE+1000:s+=ply
   if e[2]==0 or (e[2]==1 and s>=b) or (e[2]==2 and s<=a):return s
 npm=CNT[2]+CNT[3]+CNT[4]+CNT[5] if STM==0 else CNT[10]+CNT[11]+CNT[12]+CNT[13]
 se=None
 if not inch and ply>0 and npm:
  if d<=3:
   se=ev()
   if se>=b+200*d:return b
  if cn and d>=3 and b<MATE-1000:
   if se is None:se=ev()
   if se>=b:
    sv=EP;sh=HALF
    if EP>=0:Z^=ZE[EP];EP=-1
    STM^=1;Z^=ZS;HALF+=1;RC[Z]=RC.get(Z,0)+1
    s=-srch(d-3,-b,-b+1,ply+1,0)
    RC[Z]-=1;STM^=1;Z^=ZS;EP=sv;HALF=sh
    if sv>=0:Z^=ZE[sv]
    if s>=b:return b
 ms=gen(0);w=STM;best=-INF;bm=0;flag=2;n=0
 ad=[]
 for x in ms:
  m=x&32767
  if m==ttm:ad.append((1<<45)|m)
  elif (x>>15)==0:
   if m==K1[ply]:ad.append((1500000<<15)|m)
   elif m==K2[ply]:ad.append((1499000<<15)|m)
   else:ad.append((min(HIST[w*4096+(m&63)*64+((m>>6)&63)],1400000)<<15)|m)
  else:ad.append(x)
 ad.sort(reverse=True);ms=ad
 for x in ms:
  m=x&32767;quiet=(x>>15)<1900000
  make(m)
  if att(KS[STM^1],STM):unmake(m);continue
  if d<=2 and se is not None and quiet and best>-INF and se+160*d<=a and not att(KS[STM],STM^1):unmake(m);continue
  if n==0:s=-srch(d-1,-b,-a,ply+1,1)
  else:
   r=0
   if d>=3 and quiet and not inch:
    if not att(KS[STM],STM^1):
     r=1 if n>=2 else 0
     if n>=8:r=2
     if n>=20 and d>=6:r=3
   s=-srch(d-1-r,-a-1,-a,ply+1,1)
   if s>a and r>0:s=-srch(d-1,-a-1,-a,ply+1,1)
   if s>a and s<b:s=-srch(d-1,-b,-a,ply+1,1)
  unmake(m);n+=1
  if s>best:best=s;bm=m
  if s>a:
   a=s;flag=0
   if s>=b:
    flag=1
    if quiet:
     if K1[ply]!=m:K2[ply]=K1[ply];K1[ply]=m
     HIST[w*4096+(m&63)*64+((m>>6)&63)]+=d*d
    break
 if n==0:return -MATE+ply if inch else 0
 s2=best
 if s2>MATE-1000:s2+=ply
 elif s2<-MATE+1000:s2-=ply
 TT[Z&TM]=(Z,d,flag,s2,bm)
 return best
def root():
 global ND,HARD
 ND=0
 ph=CNT[2]+CNT[3]+CNT[10]+CNT[11]+2*(CNT[4]+CNT[12])+4*(CNT[5]+CNT[13])
 if ph>24:ph=24
 sc=45+55*ph//24
 bud=BUDGET*sc//100;HARD=85000*sc//100
 ms=gen(0)
 if BKM[0] and BKN[0]*4<len(BKM[0]):
  cand=u2m(BKM[0][BKN[0]*4:BKN[0]*4+4])
  if any((x&32767)==cand for x in ms):BKN[0]+=1;return cand
  BKM[0]=None
 if len(ms)==1:
  m=ms[0]&32767;make(m);ok=not att(KS[STM^1],STM);unmake(m)
  if ok:return m
 best=ms[0]&32767;d=1
 while d<80:
  try:s=srch(d,-INF,INF,0,1)
  except Abort:break
  e=TT[Z&TM]
  if e and e[0]==Z and e[4] and e[1]>=d:best=e[4]
  if ND>bud or s>=MATE-30:break
  d+=1
 return best
def u2m(u):
 f=(8-int(u[1]))*8+ord(u[0])-97;t=(8-int(u[3]))*8+ord(u[2])-97
 return f|t<<6|(0 if len(u)<5 else "nbrq".index(u[4])+2)<<12
def m2u(m):
 f=m&63;t=(m>>6)&63;s=chr(97+(f&7))+str(8-(f>>3))+chr(97+(t&7))+str(8-(t>>3))
 pr=(m>>12)&15
 return s+("nbrq"[pr-2] if pr else "")
#DRV
sf=None;cg=-1
while True:
 g=post("/game",{})
 if g["status"]=="done":break
 while g["status"]=="your_move":
  if g.get("start_fen"):sf=g["start_fen"]
  newg=g["game"]!=cg
  if newg:
   cg=g["game"];TT=[None]*(1<<20);K1=[0]*512;K2=[0]*512;HIST=[0]*8192;PHT={}
  set_fen(sf);UND.clear();RC={Z:1}
  for mv in g["moves"]:make(u2m(mv))
  UND.clear()
  if newg:BKM[0]=BK.get(Z&0xFFFFFFFF);BKN[0]=0
  g=post("/move",{"game":g["game"],"move":m2u(root())})
