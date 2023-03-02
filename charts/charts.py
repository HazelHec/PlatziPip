import matplotlib.pyplot as plt


def genera_grafico_Pie():
    labels = ['A', 'B', 'C']
    values = [100, 200, 130]
    
    
    
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close()
