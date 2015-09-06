from matplotlib import pyplot as plt

test_1_grades = [99, 90, 85, 97, 89]
test_2_grades = [100, 85, 60, 90, 70]

plt.scatter(test_1_grades, test_2_grades)
plt.title('Axes aren\'t comparable')
plt.xlabel('test 1 grades')
plt.ylabel('test 2 grades')
plt.show()
