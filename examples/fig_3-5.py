from matplotlib import pyplot as plt

mentions = [500, 505]
years = [2013, 2014]

plt.bar([2012.6, 2013.6], mentions, 0.8)
plt.xticks(years)
plt.ylabel('# of times I heard someone say data science')

plt.ticklabel_format(useOffset=False)

plt.axis([2012.5, 2014.5, 0, 550])
plt.title('Look at the "Huge" increase!')
plt.show()
