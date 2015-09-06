from matplotlib import pyplot as plt
from collections import Counter

num_friends = [100, 49, 41, 40, 25, 38, 23, 97, 56, 12, 87, 43, 12, 12, 6, 6, 6]
friend_counts = Counter(num_friends)
xs = range(101)
ys = [friend_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title('Histogram of Friend Counts')
plt.xlabel('# of friends')
plt.ylabel('# of people')
plt.show()
