import tkinter as tk
from tkinter import ttk

class Teisendaja:
    def __init__(self, root):
        self.root = root
        self.root.title("SI -> USCS") #programmi tabi tekst
        
        self.notebook = ttk.Notebook(root) #notebook kuhu lähevad vaheleheküljed
        self.tab1 = ttk.Frame(self.notebook) #Frame (tab) notebooki
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)
        
        self.notebook.add(self.tab1, text = "Pikkused") #notebooki tabide lisamine, tekst tabi peal
        self.notebook.add(self.tab2, text = "Mass")
        self.notebook.add(self.tab3, text = "Vedeliku maht")
        
        self.pikkused() #alumised funktsioonid, loob tabid
        self.mass()
        self.vedelik()
        
        self.notebook.pack(expand = True, fill = 'both') #packib kokku ja väljastab 

    def pikkused(self): #siin tabi sisu
        tekst_tab1 = ttk.Label(self.tab1, text = "Pikkuste teisendus")
        tekst_tab1.pack(padx = 75, pady = 50)
        
        #siia peaks lisama rohkem widgeteid (kastid ja nupp, kastidest peaks saama väärtuseid, nupp tagastab kastide väärtustest saadud arvutused) 
    def mass(self):
        tekst_tab2 = ttk.Label(self.tab2, text = "Masside teisendus")
        tekst_tab2.pack(padx = 75, pady = 50)
        
    def vedelik(self):
        tekst_tab3 = ttk.Label(self.tab3, text = "Vedelike teisendus")
        tekst_tab3.pack(padx = 75, pady = 50)
        
def main():
    root = tk.Tk()
    app = Teisendaja(root)
    root.mainloop()

if __name__ == "__main__":
    main()
