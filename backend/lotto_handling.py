import requests
import copy

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
            self.int_szamok = sorted(list(int(x) for x in line_split[11:16]))
            self.szamsorosszeg = 0
            for n in self.int_szamok:
                self.szamsorosszeg += n

            self.rendezett_szamsorhossz = 1
            ##bit faulty but works
            for i in range(0, len(self.int_szamok)-1):
                if self.int_szamok[i]+1 == self.int_szamok[i+1]:
                    self.rendezett_szamsorhossz += 1
                else:
                    self.rendezett_szamsorhossz = 1

            # if (self.rendezett_szamsorhossz > 2):
            #     print("nagyobb mint fasz")
        else:
            self.ev = ""
            self.het = ""

    def __str__(self):
        return f"év: {self.ev}, hét: {self.het}"
        

eredmenyek: list[Huzas] = []
     
def parse_official_link():
    otos_url = "https://bet.szerencsejatek.hu/cmsfiles/otos.csv"

    current_file = requests.get(otos_url)

    rawdata: str = current_file.content.decode()
    all_weeks = rawdata.split("\r\n")[:-1] #last line is empty
    for week in all_weeks:
        eredmenyek.append(Huzas(week))

def nyeroszamok_x_hete(hany_hete: int) -> list:
    return eredmenyek[hany_hete-1].szamok

def szamok_gyakorisag_szerint():
    szamok = {str(n):0 for n in range(1, 91)}
    for sorsolas in eredmenyek:
        for szam in sorsolas.szamok:
            szamok[szam] += 1


    gyakorisag_szerint = {k: v for k, v in sorted(szamok.items(), key=lambda item: item[1], reverse=True)}
    print(gyakorisag_szerint)
    return gyakorisag_szerint

szamok_gyakorisag_szerint()

def leghasonlobb_huzasok():
    top2_hasonlo = {'egyik':eredmenyek[0], 'masik':eredmenyek[1], "ugyanaz":0}


    for huzas in eredmenyek:
        for masikhuzas in eredmenyek:
            egyezo_szamok = 0
            if huzas.datum != masikhuzas.datum:
                for szam in huzas.szamok:
                    for masikszam in masikhuzas.szamok:
                        if szam == masikszam:
                            egyezo_szamok += 1
                if egyezo_szamok > top2_hasonlo["ugyanaz"]:
                    top2_hasonlo["egyik"] = copy.deepcopy(huzas)
                    top2_hasonlo["masik"] = copy.deepcopy(masikhuzas)
                    top2_hasonlo["ugyanaz"] = egyezo_szamok
    return top2_hasonlo

def a3_leghoszabb_sorozatot_tartalmazo_szamsor(): ###not working properly
    return sorted(eredmenyek, key=lambda x: x.rendezett_szamsorhossz, reverse=True)[:3]

def a3_legkisebb_osszegu_szamsor():
    return sorted(eredmenyek, key=lambda x: x.szamsorosszeg)[:3]



# parse_official_link()

# # print(list(str(eredmeny) for eredmeny in eredmenyek))
# print("Legutolsó nyerőszámok: ", nyeroszamok_x_hete(1))
# print(szamok_gyakorisag_szerint())

# leghasonlobb_h = leghasonlobb_huzasok()
# print("leghasonlóbb számsorok:", leghasonlobb_h["egyik"].szamok, 
#       f"húzás időpontja: {str(leghasonlobb_h['egyik'])}", 
#       leghasonlobb_h["masik"].szamok, 
#       f"húzás időpontja: {str(leghasonlobb_h['masik'])}")

# a3 = a3_leghoszabb_sorozatot_tartalmazo_szamsor()

# print("a 3 leghoszabb számsorozat:", a3[0].rendezett_szamsorhossz, a3[0].int_szamok, "\n", a3[1].rendezett_szamsorhossz, a3[1].int_szamok, "\n", a3[2].rendezett_szamsorhossz, a3[2].int_szamok)


# legkisebbek = a3_legkisebb_osszegu_szamsor()
# print(legkisebbek[0].szamsorosszeg, legkisebbek[1].szamsorosszeg, legkisebbek[2].szamsorosszeg)