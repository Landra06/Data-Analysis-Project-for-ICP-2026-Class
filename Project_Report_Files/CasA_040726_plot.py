import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("casA_040726_fixed.txt", skiprows=2)

#Trace 1
freq1 = data[:,0]
amp1 = data[:,1]

#Trace2
freq2 = data[:,2]
amp2 = data[:,3]


#Plot Trace 1 and Trace 2

plt.plot(freq1, amp1, label="Trace 1")
plt.plot(freq2, amp2, label="Trace 2")

plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude (dBm)")
plt.legend()
plt.show()
