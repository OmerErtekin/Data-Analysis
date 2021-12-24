import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model

def ShowModMedianAndDistrubition(arrayName):
    selectedArray = pd.Series(readedData[arrayName])

    #Grafigin ve density egrisinin cizilmesi
    sns.histplot(selectedArray,kde=True,color = 'red',bins = 10)
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
    plt.title('Histogram of ' + arrayName+ ' / Season')
    plt.xlabel(arrayName)
    plt.ylabel('Team Count')

    plt.show()


def ShowCorrelationHeatMap():
   # print(readedData.corr())
    plt.figure(figsize = (8,8))
    sns.heatmap(readedData.corr(),annot = True,cmap = 'YlGnBu')
    plt.show()
    
def ShowPairPlot():
    sns.set()
    sns.pairplot(readedData,height = 1.5)
    plt.show()
    
def ShowLinearRegression(xColumn,yColumn):
    readedData.plot(kind = 'scatter' ,x = xColumn, y = yColumn,color='blue')
    plt.xlabel(xColumn)
    plt.ylabel(yColumn)
        
        
    xVariable = pd.DataFrame(readedData[xColumn])
    yVariable = pd.DataFrame(readedData[yColumn])
    
    
    plt.text(xVariable.mean(),yVariable.mean()+0.25,'Correlation : {:.2f}'.format(readedData[xColumn].corr(readedData[yColumn])))
    if(abs(readedData[xColumn].corr(readedData[yColumn])) > 0.5):
        linearRegression = linear_model.LinearRegression()
        model = linearRegression.fit(xVariable,yVariable)
    
        #Lineer regresyon dogrusunun cizimi
        plt.plot(xVariable,model.predict(xVariable),color ='red')
    
    plt.show()


    
readedData = pd.read_csv("foot.csv")


#ShowModMedianAndDistrubition('Shots pg')
#ShowCorrelationHeatMap()
ShowLinearRegression('yellow_cards','Rating')
#ShowPairPlot()