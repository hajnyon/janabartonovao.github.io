

import matplotlib.pyplot as mat
categories = ["Zemní plyn", "Tepelné čerpadlo", "Elektřina - přímotop", "Dřevní pelety", "Palivové dřevo"]
values = [38198, 31668, 79176, 31180, 17858]

mat.bar(categories,values)

for i, value in enumerate(values):
    mat.text(i, value, str(value), ha="center", va="bottom")

mat.title("Roční náklady na energie v domě bez zahrnutí ostatní spotřeby elektřiny v Kč", fontweight="bold")
mat.xlabel("Zdroj energií")
mat.ylabel("Náklady v Kč")
mat.show()
