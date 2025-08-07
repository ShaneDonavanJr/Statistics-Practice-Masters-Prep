

"""

1.3 Of great importance to residents of central Florida is the amount of radioactive material present
in the soil of reclaimed phosphate mining areas. Measurements of the amount of 238U in 25 soil
samples were as follows (measurements in picocuries per gram):
.74 6.47 1.90 2.69 .75
.32 9.99 1.77 2.41 1.96
1.66 .70 2.42 .54 3.36
3.59 .37 1.09 8.32 4.06
4.55 .76 2.03 5.70 12.48
Construct a relative frequency histogram for these data.

"""

soil_samples = """.74 6.47 1.90 2.69 .75
.32 9.99 1.77 2.41 1.96
1.66 .70 2.42 .54 3.36
3.59 .37 1.09 8.32 4.06
4.55 .76 2.03 5.70 12.48""".replace("\n", " ").split(" ")
# print(soil_samples)

soil_samples = [ float(sample) for sample in soil_samples ]
print(soil_samples)

import matplotlib.pyplot as plt
import numpy as np

print(f"Mean:   {np.mean(soil_samples)}")
print(f"Median: {np.median(soil_samples)}")
print(f"Min:    {np.array(soil_samples).min()}")
print(f"Max:    {np.array(soil_samples).max()}")

plt.hist(soil_samples, bins=5, color="skyblue", edgecolor="black")
# line(np.mean(soil_samples), color= "red", linestyle="dotted", linewidth=2,  label="Mean")
plt.axvline(np.mean(soil_samples), color="red", linestyle="dotted", linewidth=2, label="Mean")
plt.title("Frequency of 238U levels in soil samples")
plt.ylabel("Frequency")
plt.xlabel("238U levels")
plt.show()

