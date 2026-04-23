import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("CasA_data1_fixed.txt", skiprows=2)

freq = data[:,0]
amp1 = data[:,1]
amp2 = data[:,3]

#Average the amplitudes
avg = (amp1 + amp2) / 2

#Boxcar Smoothing
r = 3
window = 2 * r + 1
kernel = np.ones(window) / window
smooth = np.convolve(avg, kernel, mode="same")

peak = np.max(smooth)


#Fix background noise
noise_mean = np.mean(smooth)
standard_deviation = np.std(smooth)


#Signal to noise ratio
snr = (peak - noise_mean) / standard_deviation


#Plot
plt.figure(figsize=(10, 6))
plt.plot(freq, avg, label="Average of Trace 1 and Trace 2")
plt.plot(freq, smooth, label="Boxcar Smoothed")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude (dBm)")
plt.title("Analysis of Cas A Trial 1")
plt.legend()
plt.show()
