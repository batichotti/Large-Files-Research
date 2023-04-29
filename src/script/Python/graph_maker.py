import pandas as pd
import matplotlib.pyplot as plt

tabela2 = pd.read_csv('Large_Files\\python_count.csv')

tabela2 = tabela2[tabela2['Count'] > 5]

plt.bar(tabela2['Project'], tabela2['Count'])
plt.xlabel('Project')
plt.xticks(rotation=75)
plt.tight_layout()
plt.ylabel('Large Files')
plt.title('TOP Projects with Python Large Files')
plt.show()
