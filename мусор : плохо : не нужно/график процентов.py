import matplotlib.pyplot as plt
a = 38
b = 66
c = 78
d = 88
podpis = ('5-6', '7-8', '9-10', '11-12')
znach = (a, b, c, d)
plt.bar(podpis, znach, align='center', alpha=0.7)
plt.title('Процент угаданных слов определённой группы', fontsize = 16, pad = 15) # Добавим заголовок
plt.style.use(style = '_mpl-gallery')
plt.grid(True)
plt.ylim(0, 100)
plt.savefig('/Users/alexmedvedev/Desktop/Visual Studio Code/графики/plot_bukvi.png', dpi = 300)
plt.show 