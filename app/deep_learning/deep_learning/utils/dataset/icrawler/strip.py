# -*-coding:Latin-1 -*

from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

print("Lancement du script")

filename = 'liste.txt'
nouveau_csv = open("liste_nouveau.txt", 'w')

lines = open(filename).read().splitlines()
for line in lines:
	string = strip_tags(line)
	string = string.replace(' ', '%20')
	string = string.replace("'", "%27")
	string = string.replace('à', '%E0')
	string = string.replace('á', '%E1')
	string = string.replace('â', '%E2')
	string = string.replace('ã', '%E3')
	string = string.replace('ä', '%E4')
	string = string.replace('å', '%E5')
	string = string.replace('æ', '%E6')
	string = string.replace('ç', '%E7')
	string = string.replace('è', '%E8')
	string = string.replace('é', '%E9')
	string = string.replace('ê', '%EA')
	string = string.replace('ë', '%EB')
	string = string.replace('ì', '%EC')
	string = string.replace('í', '%ED')
	string = string.replace('î', '%EE')
	string = string.replace('ï', '%EF')
	string = string.replace('ð', '%F0')
	string = string.replace('ñ', '%F1')
	string = string.replace('ò', '%F2')
	string = string.replace('ó', '%F3')
	string = string.replace('ô', '%F4')
	string = string.replace('õ', '%F5')
	string = string.replace('ö', '%F6')
	string = string.replace('÷', '%F7')
	string = string.replace('ø', '%F8')
	string = string.replace('ù', '%F9')
	string = string.replace('ú', '%FA')
	string = string.replace('û', '%FB')
	string = string.replace('ü', '%FC')
	string = string.replace('ý', '%FD')
	string = string.replace('þ', '%FE')
	string = string.replace('ÿ', '%FF')
	nouveau_csv.write(string+ '\n')

print("Fin du script")
