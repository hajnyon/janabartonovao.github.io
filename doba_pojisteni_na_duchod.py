import matplotlib.pyplot as mat
x = [ 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
y = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 35, 35, 35, 35]

mat.plot(x,y)
mat.title("Potřebná doba pojištění pro nárok na starobní důchod")
mat.xlabel("V roce")
mat.ylabel("Počet let pojištění")
mat.show()


