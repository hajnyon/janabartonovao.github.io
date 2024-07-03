import matplotlib.pyplot as mat

labels = ["Řemeslníci a kvalifikovaní pracovníci stavební výroby", "Malíři a příbuzní pracovníci, pracovníci povrchového čištění budov", "Montážní dělníci výrobků a zařízení", "Obsluha pojízdných zařízení", "Kuchaři (kromě šéfkuchařů), pomocní kuchaři", "Číšníci, servírky, barmani a příbuzní pracovníci", "Analytici a vývojáři softwaru a PC aplikací", "Mistři a příbuzní pracovníci v oblasti těžby, výroby a stavebnictví", "Technici ve fyzikálních a průmyslových oborech", "Specialisté ve výrobě, stavebnictví a příbuzných oborech"]
sizes = [52800, 32600, 32100, 30500, 28800, 24400, 23600, 22200, 19500, 19300]

def absolute_values(val):
    a = int(round(val / 100.0 * sum(sizes)))
    return f"{a:}"

mat.pie(sizes, labels=labels, autopct=absolute_values)
mat.title("Počet chybějící pracovní síly pro rok 2030 u nejvíce nedostatkových profesí v ČR", fontweight="bold")
mat.show()