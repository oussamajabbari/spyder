

def porte(x):
    return 1 if abs(x) < 0.5 else 0

def echelon(x):
    return 0 if x < 0 else 1;

def fc(x):
    return (x-2)*echelon(x-3)
    
def fd(x):
    return (-x+3)*echelon(x-2)*echelon(-x+3)

def fe(x):
    return np.exp(-2*x)*echelon(x-1)

def ftp(x):
    return np.exp(-abs(x))

t = np.arange(-5,5,0.01)
f = np.vectorize(ftp, otypes=[np.float])
r = f(t)
plt.plot(t, r)
