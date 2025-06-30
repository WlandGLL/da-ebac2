
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv')

plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='dia', y='preco', marker='o')
plt.title('Preço da Gasolina por Dia')
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')
plt.grid(True)

plt.savefig('gasolina.png')
