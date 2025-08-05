

"""
Are some cities more windy than others? Does Chicago deserve to be nicknamed “The Windy
City”? Given below are the average wind speeds (in miles per hour) for 45 selected U.S. cities:

8.9 12.4 8.6 11.3 9.2 8.8 35.1 6.2 7.0
7.1 11.8 10.7 7.6 9.1 9.2 8.2 9.0 8.7
9.1 10.9 10.3 9.6 7.8 11.5 9.3 7.9 8.8
8.8 12.7 8.4 7.8 5.7 10.5 10.5 9.6 8.9
10.2 10.3 7.7 10.6 8.3 8.8 9.5 8.8 9.4

Source: The World Almanac and Book of Facts, 2004.

a Construct a relative frequency histogram for these data. (Choose the class boundaries
without including the value 35.1 in the range of values.)

b The value 35.1 was recorded at Mt. Washington, New Hampshire. Does the geography of
that city explain the magnitude of its average wind speed?

c The average wind speed for Chicago is 10.3 miles per hour. What percentage of the cities
have average wind speeds in excess of Chicago’s?

d Do you think that Chicago is unusually windy?

"""

# A)

# line skips contain \n, which shows in the array causing strings.
# Replacing \n with " " then split on " " to avoid strings
avg_list = """8.9 12.4 8.6 11.3 9.2 8.8 35.1 6.2 7.0
7.1 11.8 10.7 7.6 9.1 9.2 8.2 9.0 8.7
9.1 10.9 10.3 9.6 7.8 11.5 9.3 7.9 8.8
8.8 12.7 8.4 7.8 5.7 10.5 10.5 9.6 8.9
10.2 10.3 7.7 10.6 8.3 8.8 9.5 8.8 9.4""".replace("\n", " ").split(" ")

# convert list of strings to list of floats
wind_avgs = [ float(avg) for avg in avg_list ]
print(wind_avgs)

# Plot histogram with outlier
import matplotlib.pyplot as plt

plt.hist(wind_avgs, bins=10, color='blue')
plt.title("Hello World")
plt.xlabel("Average Wind Speed")
plt.ylabel("Frequency")
plt.show()

# Remove outlier, being direct for now
wind_avgs = [ float(avg) for avg in avg_list if float(avg) < 30]

plt.hist(wind_avgs, bins=10, color='blue')
plt.show()

# B) Mt. Washington, New Hampshire is a mountain know for high winds. Does not qualify as a city. 

# C)

'''What percentage of the cities have average wind speeds in excess of Chicago’s?'''

gte_chicago = [ avg for avg in wind_avgs if avg > 10.3]

ratio = len(gte_chicago) / len(wind_avgs)
print(f"{round(ratio, 4) * 100}% of cities have a higher wind average than Chicago")

# D) Given that Chicago is not in the top 20th percentile, Chicago does no deviate enough to declare it unusually wind. 


# Bonus Recommendations from chatGPT

import numpy as np
percentile = np.sum(np.array(wind_avgs) <= 10.3) / len(wind_avgs)
print(f"Chicago is windier than about {round(percentile * 100, 2)}% of the cities.")

plt.hist(wind_avgs, bins=10, color='skyblue', edgecolor='black')
plt.axvline(10.3, color='red', linestyle='dashed', linewidth=2, label='Chicago (10.3 mph)')
plt.title("Relative Frequency of Wind Speeds (Excluding Mt. Washington)")
plt.xlabel("Wind Speed (mph)")
plt.ylabel("Frequency")
plt.legend()
plt.show()
