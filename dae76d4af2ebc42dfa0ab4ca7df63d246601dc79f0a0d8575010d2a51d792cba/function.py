
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

fig, ax = plt.subplots()

circle = Circle((0, 0), radius=1, color='red')

ax.add_patch(circle)

ax.set_aspect('equal')

plt.show()
