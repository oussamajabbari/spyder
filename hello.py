

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

def fourier_ftp(f):
    return (2/(1+4*(pi**2)*(f**2)))

N=1000
t = np.arange(-5,5,0.01)
#f = np.vectorize(ftp, otypes=[np.float])
y = ftp(t)
f = np.fft.fftfreq(N, 0.01)
f = np.fft.fftshift(f)
fft_y = np.fft.fft(y, N)
fft_y = np.fft.fftshift(fft_y)

#plt.plot(t, y)
#plt.plot(f[458:541], 1.0/N * np.abs(fft_y[458:541]))
plt.plot(f, 1.0/N * np.abs(fft_y))
#plt.plot(f[458:541], fourier_ftp(f[458:541]))