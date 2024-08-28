import matplotlib.pyplot as mat
categories = ["Jihočeský", "Jihomoravský", "Liberecký", "Moravskoslezský", "Olomoucký", "Pardubický", "Středočeský", "Ústecký", "Vysočina", "Praha", "Zlínský", "Plzeňský", "Královehradský", "Karlovarský"]
values = [29922, 31370, 29881, 30717, 28105, 30724, 40281, 29946, 30363, 29922, 24991, 34742, 32666, 32691]

mat.bar(categories,values)

for i, value in enumerate(values):
    mat.text(i, value, str(value), ha="center", va="bottom")

mat.title("Medián Hrubé měsíční mzdy účetních specialistů", fontweight="bold")
mat.xlabel("Kraj", fontweight="bold")
mat.ylabel("Hrubá mzda v Kč", fontweight="bold")
mat.xticks(rotation=90)
mat.show()