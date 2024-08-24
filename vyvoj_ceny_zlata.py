import matplotlib.pyplot as mat
import matplotlib.ticker as ticker

x = [ 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
y = [10066, 13673, 15794, 19664, 21981, 27705, 35474, 37640, 31765, 28546, 26130, 28201, 28413, 28672, 31495, 39964, 40550, 40632, 43810, 50372]

fig, ax = mat.subplots()
ax.plot(x,y)
ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))


mat.title("Graf vývoje ceny 1 OZ zlata v Kč", fontweight="bold")
mat.xlabel("V roce", fontweight="bold")
mat.ylabel("Kč", fontweight="bold")


mat.show()



