import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

readedData = pd.read_csv("foot.csv")

selectedArray = pd.Series(readedData['Goals'])

## variance mod medyan hesaplayip grafige koy
standartDev = selectedArray.values.std()

#Grafigin ve density egrisinin cizilmesi
sns.histplot(selectedArray,kde=True,color = 'red',bins = 20)
#Ortalama cizgisinin cizilmesi ve 0.1 birim yanina 3 birim yüksekligine ortalama textin yazdirilmasi
plt.axvline(selectedArray.mean(),linestyle = 'dashed', linewidth = 2,color = 'black')
plt.text(selectedArray.mean(),3,'Mean : {:.2f}'.format(selectedArray.mean()))

#Medyan icin ayni islem - medyan birden fazla eleman oldugunda ortalamasi alinir
plt.axvline(selectedArray.median().mean(), linewidth = 2,color = 'blue')
plt.text(selectedArray.median().mean(),5,'Median : {:.2f}'.format(selectedArray.median().mean()))

#Mod icin ayni islem - mod birden fazla eleman oldugunda ortalamasi alinir

plt.axvline(selectedArray.mode().mean().astype(float),linestyle = 'dashed', linewidth = 2,color = 'yellow')
plt.text(selectedArray.mode().mean(),10,'Mode : {:.2f}'.format(selectedArray.mode().mean()))

#Histogram bilgileri
plt.title('Histogram of Rating / Season')
plt.xlabel('Rating')
plt.ylabel('Team Count')

plt.show()
