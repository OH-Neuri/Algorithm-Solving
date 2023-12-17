import sys
input = sys.stdin.readline

N,M,K = map(int, input().split())
dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]
fireball=[]

def move(fireball):
    for i in range(len(fireball)):
        x,y,m,s,d=fireball[i]
        nx,ny = (x+dx[d]*s)%N,(y+dy[d]*s)%N
        fireball[i][0],fireball[i][1] = nx,ny
        board.setdefault((nx,ny), []).append([m,s,d])

def comdiv(board):
    temp=[]
    for (x,y), vals in board.items():
        num=len(vals)
        if num==1: temp.append([x,y,*vals[0]])
        else:
            m,s = 0,0
            even,odd = 0,0
            for k in range(num):
                m+=vals[k][0]
                s+=vals[k][1]
                if vals[k][2]%2: odd+=1
                else: even+=1
            m//=5
            s//=num
            if m==0: continue
            if even==num or odd==num:
                for d in range(0,8,2):
                    temp.append([x,y,m,s,d])
            else:
                for d in range(1,8,2):
                    temp.append([x,y,m,s,d])
    return temp

for _ in range(M):
    r,c,m,s,d=map(int, input().split())
    fireball.append([r-1,c-1,m,s,d])

for _ in range(K):
    board={}
    move(fireball)
    fireball=comdiv(board)

ans=0
for i in range(len(fireball)):
    ans+=fireball[i][2]
print(ans)
