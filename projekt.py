import tkinter as tk
from tkinter import ttk, messagebox

class Teisendaja:
    def __init__(self, root):
        self.root = root
        self.root.title("Yhik - SI/USCS")  # prog tabi tekst

        self.notebook = ttk.Notebook(root)  # notebook kuhu lähevad vaheleheküljed
        self.tab1 = ttk.Frame(self.notebook)  # Frame (tab) notebooki
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)

        self.notebook.add(self.tab1, text="Pikkused")  # notebooki tabide lisamine, tekst tabi peal
        self.notebook.add(self.tab2, text="Mass")
        self.notebook.add(self.tab3, text="Vedeliku maht")
        
        about_button = tk.Button(root, text="?", command=self.about)
        about_button.pack(side=tk.TOP, anchor=tk.NE)

        self.notebook.pack(expand=True, fill='both')  # packib kokku ja väljastab

        self.pikkused()  # alumised funktsioonid, loob tabid
        self.mass()
        self.vedelik()
        
    def about(self):
        text = "Yhik on converter programm, mis suudab teha teisendusi SI ja USCS süsteemi ühikute vahel.\n\nVersion 1.0\n\nLoojad:\n Noel Lünekünd\nGregor Artur Mäe"
        messagebox.showinfo("Yhik", text)
                
    def pikkused(self):  # siin tabi sisu
        self.pikkus_entry = tk.Entry(self.tab1, width=15)
        pikkus_label = tk.Label(self.tab1, text="Pikkus:")
        self.tulemus = tk.StringVar()
        tulemus_label = tk.Label(self.tab1, textvariable=self.tulemus)

        # dropdown lahtrid
        self.ühikust = tk.StringVar()
        self.ühikust.set("mm")
        self.ühikuks = tk.StringVar()
        self.ühikuks.set("in (tolli)")

        ühikust_label = tk.Label(self.tab1, text="SI:")
        ühikust_dropdown = ttk.Combobox(self.tab1, values=["mm", "cm", "dm", "m", "km"], textvariable=self.ühikust)

        ühikuks_label = tk.Label(self.tab1, text="USCS:")
        ühikuks_dropdown = ttk.Combobox(self.tab1, values=["in (tolli)", "ft (jalga)", "yd (jardi)", "mi (miili)"], textvariable=self.ühikuks)

        # teisenduse nupp
        teisenda_button = tk.Button(self.tab1, text="Teisenda", command=self.teisendap)

        # paigutus
        pikkus_label.grid(row=0, column=0, padx=5, pady=5)
        self.pikkus_entry.grid(row=0, column=1, padx=5, pady=5)

        ühikust_label.grid(row=1, column=0, padx=5, pady=5)
        ühikust_dropdown.grid(row=1, column=1, padx=5, pady=5)

        ühikuks_label.grid(row=2, column=0, padx=5, pady=5)
        ühikuks_dropdown.grid(row=2, column=1, padx=5, pady=5)

        teisenda_button.grid(row=3, column=0, columnspan=2, pady=10)
        tulemus_label.grid(row=4, column=0, columnspan=2, pady=5)

    def teisendap(self): # pikkuste teisendaja
        try:
            väärtus_str = self.pikkus_entry.get().replace(",", ".")
            väärtus = float(väärtus_str)
            valitud_ühikust = self.ühikust.get()
            mis_ühikuks = self.ühikuks.get()
            
            # teisenduse faktorid
            teisendused = { 
                ("mm", "in (tolli)"): 0.0393701,
                ("mm", "ft (jalga)"): 0.00328084,
                ("mm", "yd (jardi)"): 0.00109361,
                ("mm", "mi (miili)"): 6.2137e-7,
                ("cm", "in (tolli)"): 0.393701,
                ("cm", "ft (jalga)"): 0.0328084,
                ("cm", "yd (jardi)"): 0.0109361,
                ("cm", "mi (miili)"): 6.2137e-6,
                ("dm", "in (tolli)"): 3.93701,
                ("dm", "ft (jalga)"): 0.328084,
                ("dm", "yd (jardi)"): 0.109361,
                ("dm", "mi (miili)"): 6.2137e-5,
                ("m", "in (tolli)"): 39.3701,
                ("m", "ft (jalga)"): 3.28084,
                ("m", "yd (jardi)"): 1.09361,
                ("m", "mi (miili)"): 6.2137e-4,
                ("km", "in (tolli)"): 39370.1,
                ("km", "ft (jalga)"): 3280.84,
                ("km", "yd (jardi)"): 1093.61,
                ("km", "mi (miili)"): 0.621371,
            }

            teisendus = väärtus * teisendused[(valitud_ühikust, mis_ühikuks)] #põhivalem
            self.tulemus.set(f"{väärtus:.2f} {valitud_ühikust} on {teisendus:.2f} {mis_ühikuks}.")
        except ValueError:
            self.tulemus.set("Vigane sisend. Sisestage kehtiv arv.")

    def mass(self):
        self.mass_entry = tk.Entry(self.tab2, width=15)
        mass_label = tk.Label(self.tab2, text="Mass:")
        self.mass_tulemus = tk.StringVar()
        tulemus_label = tk.Label(self.tab2, textvariable=self.mass_tulemus)

        # dropdown lahtrid
        self.mass_ühikust = tk.StringVar()
        self.mass_ühikust.set("mg")
        self.mass_ühikuks = tk.StringVar()
        self.mass_ühikuks.set("oz (untsi)")

        ühikust_label = tk.Label(self.tab2, text="SI:")
        ühikust_dropdown = ttk.Combobox(self.tab2, values=["mg", "g", "kg"], textvariable=self.mass_ühikust)

        ühikuks_label = tk.Label(self.tab2, text="USCS:")
        ühikuks_dropdown = ttk.Combobox(self.tab2, values=["oz (untsi)", "lb (naela)", "ton (tonni)"], textvariable=self.mass_ühikuks)
        
        # teisenduse nupp
        teisenda_button = tk.Button(self.tab2, text="Teisenda", command=self.teisendam)

        # paigutus
        mass_label.grid(row=0, column=0, padx=5, pady=5)
        self.mass_entry.grid(row=0, column=1, padx=5, pady=5)

        ühikust_label.grid(row=1, column=0, padx=5, pady=5)
        ühikust_dropdown.grid(row=1, column=1, padx=5, pady=5)

        ühikuks_label.grid(row=2, column=0, padx=5, pady=5)
        ühikuks_dropdown.grid(row=2, column=1, padx=5, pady=5)

        teisenda_button.grid(row=3, column=0, columnspan=2, pady=10)
        tulemus_label.grid(row=4, column=0, columnspan=2, pady=5)
        
    def teisendam(self): # massi teisendaja
        try:
            väärtus_str = self.mass_entry.get().replace(",", ".")
            väärtus = float(väärtus_str)
            valitud_ühikust = self.mass_ühikust.get()
            mis_ühikuks = self.mass_ühikuks.get()
            
            # teisenduste faktorid
            teisendused = {
                ("mg", "oz (untsi)"): 3.5274e-5,
                ("mg", "lb (naela)"): 2.20462e-6,
                ("mg", "ton (tonni)"): 1.10231e-9,
                ("g", "oz (untsi)"): 0.035274,
                ("g", "lb (naela)"): 0.00220462,
                ("g", "ton (tonni)"): 1.10231e-6,
                ("kg", "oz (untsi)"): 35.274,
                ("kg", "lb (naela)"): 2.20462,
                ("kg", "ton (tonni)"): 0.00110231,
            }
            teisendus = väärtus * teisendused[(valitud_ühikust, mis_ühikuks)]
            self.mass_tulemus.set(f"{väärtus:.2f} {valitud_ühikust} on {teisendus:.2f} {mis_ühikuks}.")
        except ValueError:
            self.mass_tulemus.set("Vigane sisend. Sisestage kehtiv arv.")

    def vedelik(self):
        self.vedelik_entry = tk.Entry(self.tab3, width=15)
        vedelik_label = tk.Label(self.tab3, text="Vedelik:")
        self.vedelik_tulemus = tk.StringVar()
        tulemus_label = tk.Label(self.tab3, textvariable=self.vedelik_tulemus)

        # dropdown lahtrid
        self.vedelik_ühikust = tk.StringVar()
        self.vedelik_ühikust.set("ml")
        self.vedelik_ühikuks = tk.StringVar()
        self.vedelik_ühikuks.set("fl oz (untsi)")

        ühikust_label = tk.Label(self.tab3, text="SI:")
        ühikust_dropdown = ttk.Combobox(self.tab3, values=["ml", "dl", "l"], textvariable=self.vedelik_ühikust)

        ühikuks_label = tk.Label(self.tab3, text="USCS:")
        ühikuks_dropdown = ttk.Combobox(self.tab3, values=["fl oz (untsi)", "c (tassi)", "pt (pinti)", "qt (kvarti)", "gal (gallonit)"], textvariable=self.vedelik_ühikuks)

        # teisenduse nupp
        teisenda_button = tk.Button(self.tab3, text="Teisenda", command=self.teisendav)

        # paigutus
        vedelik_label.grid(row=0, column=0, padx=5, pady=5)
        self.vedelik_entry.grid(row=0, column=1, padx=5, pady=5)

        ühikust_label.grid(row=1, column=0, padx=5, pady=5)
        ühikust_dropdown.grid(row=1, column=1, padx=5, pady=5)

        ühikuks_label.grid(row=2, column=0, padx=5, pady=5)
        ühikuks_dropdown.grid(row=2, column=1, padx=5, pady=5)

        teisenda_button.grid(row=3, column=0, columnspan=2, pady=10)
        tulemus_label.grid(row=4, column=0, columnspan=2, pady=5)
        
    def teisendav(self): # vedelike teisendaja
        try:
            väärtus_str = self.vedelik_entry.get().replace(",", ".")
            väärtus = float(väärtus_str)
            valitud_ühikust = self.vedelik_ühikust.get()
            mis_ühikuks = self.vedelik_ühikuks.get()
            
            # teisenduste faktorid
            teisendused = {
                ("ml", "fl oz (untsi)"): 0.033814,
                ("ml", "c (tassi)"): 0.00422675,
                ("ml", "pt (pinti)"): 0.00211338,
                ("ml", "qt (kvarti)"): 0.00105669,
                ("ml", "gal (gallonit)"): 2.64172e-6,
                ("dl", "fl oz (untsi)"): 3.3814,
                ("dl", "c (tassi)"): 0.422675,
                ("dl", "pt (pinti)"): 0.211338,
                ("dl", "qt (kvarti)"): 0.105669,
                ("dl", "gal (gallonit)"): 0.000264172,
                ("l", "fl oz (untsi)"): 33.814,
                ("l", "c (tassi)"): 4.22675,
                ("l", "pt (pinti)"): 2.11338,
                ("l", "qt (kvarti)"): 1.05669,
                ("l", "gal (gallonit)"): 0.264172,
                }
            teisendus = väärtus * teisendused[(valitud_ühikust, mis_ühikuks)]
            self.vedelik_tulemus.set(f"{väärtus:.2f} {valitud_ühikust} on {teisendus:.2f} {mis_ühikuks}.")
        except ValueError:
            self.vedelik_tulemus.set("Vigane sisend. Sisestage kehtiv arv.")

def main():
    root = tk.Tk()
    app = Teisendaja(root)
    root.geometry("350x280")
    root.mainloop()

if __name__ == "__main__":
    main()
