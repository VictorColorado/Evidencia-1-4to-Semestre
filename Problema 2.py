import matplotlib.pyplot as plt 

def diagrama_barras_notas(notas, color):
        fig, ax = plt.subplots()
        ax.bar(notas.keys(), notas.values(), color = color)
        return ax

notas = {'Programación':9, 'Mates':6.5, 'Economía':4, 'Historia': 8}
diagrama_barras_notas(notas, 'orange')
plt.show()