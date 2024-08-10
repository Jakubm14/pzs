tab = {}

tab["Warszawa"] = ["1793579", "517.24", 5392, "mazowieckie"]
tab["Kraków"] = ["779115", "326.85", 5600, "małopolskie"]
tab["Łódź"] = ["679941", "293.25", 4300, "łódzkie"]
tab["Wrocław"] = ["641607", "292.92", 4925, "dolnośląskie"]
tab["Poznań"] = ["539843", "261.91", 4800, "wielkopolskie"]
tab["Gdańsk"] = ["470907", "262.46", 4900, "pomorskie"]
tab["Szczecin"] = ["98274", "301.55", 4500, "zachodniopomorskie"]
tab["Bydgoszcz"] = ["352876", "174.98", 4300, "kujawsko-pomorskie"]
tab["Lublin"] = ["339682", "147.46", 4100, "lubelskie"]
tab["Białystok"] = ["294738", "102.12", 4200, "podlaskie"]
tab["Katowice"] = ["290610", "164.67", 5200, "śląskie"]
tab["Gdynia"] = ["246309", "135.98", 4700, "pomorskie"]
tab["Częstochowa"] = ["218568", "160.45", 4000, "śląskie"]
tab["Radom"] = ["214080", "111.71",4100, "mazowieckie"]
tab["Sosnowiec"] = ["202708", "91.36", 4300, "śląskie"]

print (tab)

sz_16 = sum(int(miasto[0]) for miasto in tab.values())

print("Suma zaludnienia:", sz_16)
