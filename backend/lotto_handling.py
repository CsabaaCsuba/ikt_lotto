import requests

class Huzas:
    def __init__(self, line: str):
        line_split = line.split(";")
        if len(line_split) == 16:

            self.ev = line_split[0]
            self.het = line_split[1]
            self.datum = line_split[2]
            self.fonyertes = line_split[3]
            self.fonyeremeny = line_split[4]
            self.negytalalat = line_split[5]
            self.negyes_nyeremeny = line_split[6]
            self.haromtalalat = line_split[7]
            self.harmas_nyeremeny = line_split[8]
            self.kettalalat = line_split[9]
            self.kettes_nyeremeny = line_split[10]
            self.szamok = line_split[11:16]
        else:
            self.ev = ""
            self.het = ""

    def __str__(self):
        return f"év: {self.ev}, hét: {self.het}"
        

eredmenyek = []
     
def parse_official_link():
    otos_url = "https://bet.szerencsejatek.hu/cmsfiles/otos.csv"

    current_file = requests.get(otos_url)

    rawdata: str = current_file.content.decode()
    all_weeks = rawdata.split("\r\n")
    for week in all_weeks:
        eredmenyek.append(Huzas(week))

def nyeroszamok_x_hete(hany_hete: int) -> list:
    return eredmenyek[hany_hete-1].szamok

def leggyakoribb_szamok():
    szamok = {str(n):0 for n in range(1, 91)}
    for sorsolas in eredmenyek:
        print()


parse_official_link()

print(list(str(eredmeny) for eredmeny in eredmenyek))
print(nyeroszamok_x_hete(1))