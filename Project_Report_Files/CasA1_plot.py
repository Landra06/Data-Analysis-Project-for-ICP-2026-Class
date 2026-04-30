import numpy as np
import matplotlib.pyplot as plt



plt.rcParams.update({
    "font.size":12,
    "axes.labelsize":12,
    "axes.titlesize":12,
    "xtick.labelsize":12,
    "ytick.labelsize":12,
    "legend.fontsize":12
})



#Load the data from the first CasA Observation Data

data = np.loadtxt("CasA_data1_fixed.txt", skiprows=7)


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
plt.tight_layout()
plt.savefig("CasA1_Data.png", dpi=300, bbox_inches="tight")

plt.close()

