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


data = np.loadtxt("VirgoA_040726_fixed.txt", skiprows=7)

#Trace1
freq1 = data[:,0]
amp1 = data[:,1]

#Trace2
freq2 = data[:,2]
amp2 = data[:,3]

#Plot Trace 1 and Trace 2

plt.plot(freq1, amp1, label="Trace1")
plt.plot(freq2, amp2, label="Trace2")

plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude (dBm)")
plt.legend()
plt.tight_layout()
plt.savefig("VirgoA_040726_Data.png", dpi=300, bbox_inches="tight")

plt.close()
