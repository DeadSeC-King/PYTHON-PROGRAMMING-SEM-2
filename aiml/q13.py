import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("students.csv")
df.plot(kind='line', x='Name', y='cgpa', title='Student CGPA Line Plot')
plt.show()
