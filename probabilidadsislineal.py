import numpy as np
def print_hi(name):
    print(f'Hi, {name}')
def proba(v,p):
    t=v[p]
    r=np.real(t)
    i=np.imag(t)
    normanum=(r**2)+(i**2)
    l=0
    m=0
    while l<len(v):
        t=v[l]
        r=int(np.real(t))
        i=int(np.imag(t))
        m+=(r**2)+(i**2)
        l+=1
    normaden= m
    r=normanum/normaden
    return r

def transicion(v1, v2):
    x=np.array(v1)
    vn=x/np.linalg.norm(x)
    y=np.array(v2)
    vn2=y/np.linalg.norm(y)
    r=np.transpose(np.conjugate(vn2))
    o=np.dot(r,vn)
    return o
    
def probabilidadtrans(v1,v2):
    x=np.array(v1)
    vn=x/np.linalg.norm(x)
    y=np.array(v2)
    vn2=y/np.linalg.norm(y)
    r=np.transpose(np.conjugate(vn2))
    o=np.dot(r,vn)
    p=np.real(o)
    i=np.imag(o)
    normanum=(p**2)+(i**2)
    return normanum

def hervarmed(m,a):
    ma=len(m)
    na=(len(m[0]))
    c=[[0 for i in range (len(m))]for j in range (len(m))]
    for elemento in c:
        for i in range (ma):
            for j in range(na):
                c[i][j]=np.conjugate(m[j][i])
    if m==c:
        media = np.real(np.dot(np.conjugate(np.transpose(a)), np.dot(m, a)))
        varianza = np.real(np.dot(np.conjugate(np.transpose(a)), np.dot(np.dot(m,m), a)) - media**2)
        return media, varianza
    else:
        return("Matriz no hermitiana")
if __name__ == '__main__':
    
   print_hi('PyCharm')

