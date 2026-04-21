import numpy as np
import matplotlib.pyplot as plt

#Load the data from the first CasA Observation Data

data = np.loadtxt("CasA_data1_fixed.txt", skiprows=2)


#Trace 1
freq1 = data[:,0]
amp1 = data[:,1]

#Trace2
freq2 = data[:,2]
amp2 = data[:,3]


plt.plot(freq1, amp1, label="Trace 1")
plt.plot(freq2, amp2, label="Trace 2")

plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude (dBm)")
plt.legend()
plt.show()

