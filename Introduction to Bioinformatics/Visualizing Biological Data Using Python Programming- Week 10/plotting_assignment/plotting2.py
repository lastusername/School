import matplotlib.pyplot as plt

fig, ax = plt.subplots()
fruits = ['bio1', 'bio2', 'bio3', 'bio4']
counts = [40, 100, 30, 55]
bar_labels = ['red', 'blue', '_red', 'orange']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
ax.set_ylabel('Bio supply')
ax.set_title('Bio supply by kind and color')
ax.legend(title='Bio color')

plt.show()
