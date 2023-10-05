import numpy as np

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

def main():
    a=[1+1j, 3-3j, 2+6j]
    b=[2+1j, 3-5j, 2+3j]
    print(probabilidadtrans(a,b))
    print(transicion(a,b))
main()
