import os
import configparser
import tkinter.filedialog

class ConfigIni:
    def __init__(self, Percorso='', nFile=''):

        PercorsoIni = Percorso
        self.fileIni = nFile
        #self.Percorso = Percorso
        if not os.path.exists(PercorsoIni) and len(PercorsoIni):
            os.makedirs(PercorsoIni)

        self.fileIni = PercorsoIni +"/"+ self.fileIni
        if not os.path.exists(self.fileIni) and len(nFile):
            File = open(self.fileIni, 'w')
            File.close()

        if nFile == "":
            reso = tkinter.filedialog.askopenfile(initialdir=gPercorsoIni, title="Scegli il File", filetypes=(("Files di impostazione", "*.*"), ("", "")))
            PercorsoIni = reso.name
            PercorsoIni = gPercorsoIni[:reso.name.rfind('/')]
            NomeIni = reso.name[reso.name.rfind('/')+1:]
            #gNomeIni = gNome[:gNomeIni.index('.')]
            self.fileIni = PercorsoIni +"/"+ NomeIni

        self.Config = configparser.ConfigParser()
        self.Config.read(self.fileIni)

    def nomeIni(self):
        return self.fileIni

    def leggiIni(self, primoVuoto=0):
        #self.Config.read(self.fileIni)
        idx = 0
        iniDati = []
        if primoVuoto:
            iniDati.append([])
            for idx in range(primoVuoto):              
                iniDati[0].append(' ')
            idx = 1
            
        for sez in self.Config.sections():
            iniDati.append([]) #-
            iniDati[idx].append(sez)
            optioni = self.Config.options(sez)
            for opt in optioni:
                valOpz = self.Config.get(sez,opt)
                iniDati[idx].append(valOpz)
            idx += 1
        return iniDati

    def sezione(self, sez, param='', valore=''):
        if sez in self.Config.sections():
            if param:
                if param in self.Config[sez]:
                    self.Config.remove_option(sez, param)
        else:
            self.Config.add_section(sez)

        if param:
            self.Config.set(sez, param, valore)

    def salva(self):
        with open(self.fileIni, 'w') as configfile:
            self.Config.write(configfile)
            configfile.close()

    def sezioni(self):
        return self.Config.sections()

    def opzioni(self, sez):
        return self.Config.options(sez)

    def prendi(self, sez, opz):
        try:
            r = self.Config.get(sez, opz)
        except:
            r = ''

        return r

    def cancella(self, sez, opz=''):
        pass

'''
sez = 'http.Vodafone.it'
uti = 'arturo.Canaglia'
pwd = 'Qksmxui11Zd<>'
arr = []
Configura = ConfigIni('/home/rosa/bin/Py', 'prova.ini')
arr = Configura.leggiIni(3)
print (arr[2][2])

Configura.sezione('ww.tim.com','Utente', uti)
Configura.sezione('ww.tim.com','Password', pwd)
Configura.salva()
'''
