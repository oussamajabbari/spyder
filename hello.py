

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
    
def decalage(x):
    return ftp(x) * (np.exp(2*np.pi*5*x*1j))

Fe=20
Te=1.0/Fe
Tstart=-5
Tend=5
N=int((Tend - Tstart) / Te)
t = np.arange(Tstart,Tend, Te)
#f = np.vectorize(ftp, otypes=[np.float])
y = ftp(t)
y_decal = decalage(t)
f = np.fft.fftfreq(N, Te)
f = np.fft.fftshift(f)
fft_y = np.fft.fft(y, N)
fft_y = np.fft.fftshift(fft_y)

fft_y_decal = np.fft.fft(y_decal, N)
fft_y_decal = np.fft.fftshift(fft_y_decal)

xt = np.abs(np.fft.ifft(fft_y))

#plt.plot(t, y)
#plt.plot(t, xt)
#plt.plot(f[458:541], 1.0/N * np.abs(fft_y[458:541]))
#plt.plot(f, Te * np.abs(fft_y))
plt.plot(f, Te * np.angle(fft_y_decal))
#plt.plot(t, fourier_ftp(t))
#plt.plot(f[458:541], fourier_ftp(f[458:541]))