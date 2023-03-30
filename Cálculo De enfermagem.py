import tkinter as tk
from tkinter import ttk

def pega_valor(input_box):
    try:
        x = float(input_box.get())
        return x
    except:
        print("Digite um entrada válida: (Número) ")
        return None
    
def constante_marinho_window():
    def calculate_cm():
        DS = pega_valor(ds_input)
        JST = pega_valor(jst_input)
        IST = pega_valor(ist_input)
        if DS is None or JST is None or IST is None:
            return
        km = (DS/JST)*IST
        km_output.configure(text=f"KM: {km}")
    
    cm_window = tk.Toplevel()
    cm_window.title("Constante de Marinho")

    ds_label = ttk.Label(cm_window, text="Dias da semana")
    ds_input = ttk.Entry(cm_window)

    jst_label = ttk.Label(cm_window, text="Jornada semanal de trabalho (20,30,36,40..)")
    jst_input = ttk.Entry(cm_window)

    ist_label = ttk.Label(cm_window, text="Índice de segurança técnica")
    ist_input = ttk.Entry(cm_window)

    calculate_button = ttk.Button(cm_window, text="Calcular", command=calculate_cm)
    km_output = ttk.Label(cm_window, text="KM: ")

    ds_label.pack()
    ds_input.pack()
    jst_label.pack()
    jst_input.pack()
    ist_label.pack()
    ist_input.pack()
    calculate_button.pack()
    km_output.pack()

def the_window():
    def calculate_the():
        PCM = pega_valor(pcm_input)
        PCI = pega_valor(pci_input)
        PCAD = pega_valor(pcad_input)
        PCSI = pega_valor(pcsi_input)
        PCIt = pega_valor(pcit_input)
        if PCM is None or PCI is None or PCAD is None or PCSI is None or PCIt is None:
            return
        the = ((PCM*4)+(PCI*6)+(PCAD*10)+(PCSI*10)+(PCIt*18))
        the_output.configure(text=f"THE: {the}")
    
    the_window = tk.Toplevel()
    the_window.title("Tempo de horas de enfermagem")

    pcm_label = ttk.Label(the_window, text="PCM")
    pcm_input = ttk.Entry(the_window)

    pci_label = ttk.Label(the_window, text="PCI")
    pci_input = ttk.Entry(the_window)

    pcad_label = ttk.Label(the_window, text="PCAD")
    pcad_input = ttk.Entry(the_window)

    pcsi_label = ttk.Label(the_window, text="PCSI")
    pcsi_input = ttk.Entry(the_window)

    pcit_label = ttk.Label(the_window, text="PCIt (Caso não tenha, envie 0)")
    pcit_input = ttk.Entry(the_window)

    calculate_button = ttk.Button(the_window, text="Calcular", command=calculate_the)
    the_output = ttk.Label(the_window, text="THE: ")

    pcm_label.pack()
    pcm_input.pack()
    pci_label.pack()
    pci_input.pack()
    pcad_label.pack()
    pcad_input.pack()
    pcsi_label.pack()
    pcsi_input.pack()
    pcit_label.pack()
    pcit_input.pack()
    calculate_button.pack()
    the_output.pack()

def qp_window():
    def calculate_qp():
        the = pega_valor(the_input)
        ds = pega_valor(ds_input)
        jst = pega_valor(jst_input)
       
import tkinter as tk

def open_janela_constante():
    janela_constante = tk.Toplevel()
    janela_constante.title("Constante Marinho")

    def calcular_constante():
        try:
            DS = float(ds_entry.get())
            JST = float(jst_entry.get())
            IST = float(ist_entry.get())
            Km = (DS/JST)*IST
            resultado_label["text"] = f"O valor da constante é: {Km:.2f}"
        except ValueError:
            resultado_label["text"] = "Digite valores válidos!"

    ds_label = tk.Label(janela_constante, text="Dias da semana:")
    ds_label.pack()
    ds_entry = tk.Entry(janela_constante)
    ds_entry.pack()

    jst_label = tk.Label(janela_constante, text="Jornada semanal de trabalho:")
    jst_label.pack()
    jst_entry = tk.Entry(janela_constante)
    jst_entry.pack()

    ist_label = tk.Label(janela_constante, text="Índice de segurança técnica:")
    ist_label.pack()
    ist_entry = tk.Entry(janela_constante)
    ist_entry.pack()

    calcular_button = tk.Button(janela_constante, text="Calcular", command=calcular_constante)
    calcular_button.pack()

    resultado_label = tk.Label(janela_constante, text="")
    resultado_label.pack()

def open_janela_tempo_enfermagem():
    janela_tempo = tk.Toplevel()
    janela_tempo.title("Tempo de horas de enfermagem")

    def calcular_tempo():
        try:
            PCM = float(pcm_entry.get())
            PCI = float(pci_entry.get())
            PCAD = float(pcad_entry.get())
            PCSI = float(pcsi_entry.get())
            PCIt = float(pcit_entry.get())
            THE = ((PCM*4)+(PCI*6)+(PCAD*10)+(PCSI*10)+(PCIt*18))
            resultado_label["text"] = f"O valor do tempo de horas é: {THE:.2f}"
        except ValueError:
            resultado_label["text"] = "Digite valores válidos!"

    pcm_label = tk.Label(janela_tempo, text="PCM:")
    pcm_label.pack()
    pcm_entry = tk.Entry(janela_tempo)
    pcm_entry.pack()

    pci_label = tk.Label(janela_tempo, text="PCI:")
    pci_label.pack()
    pci_entry = tk.Entry(janela_tempo)
    pci_entry.pack()

    pcad_label = tk.Label(janela_tempo, text="PCAD:")
    pcad_label.pack()
    pcad_entry = tk.Entry(janela_tempo)
    pcad_entry.pack()

    pcsi_label = tk.Label(janela_tempo, text="PCSI:")
    pcsi_label.pack()
    pcsi_entry = tk.Entry(janela_tempo)
    pcsi_entry.pack()

    pcit_label = tk.Label(janela_tempo, text="PCIt:")
    pcit_label.pack()
    pcit_entry = tk.Entry(janela_tempo)
    pcit_entry.pack()

    calcular_button = tk.Button(janela_tempo, text="Calcular", command=calcular_tempo)
    calcular_button.pack()

    resultado_label = tk.Label(janela_tempo, text="")
    resultado_label.pack()


def open_janela_constante():
    janela_constante = tk.Toplevel()
    janela_constante.title("Constante Marinho")

    def calcular_constante():
        try:
            DS = float(ds_entry.get())
            JST = float(jst_entry.get())
            IST = float(ist_entry.get())
            Km = (DS/JST)*IST
            resultado_label["text"] = f"O valor da constante é: {Km:.2f}"
        except ValueError:
            resultado_label["text"] = "Digite valores válidos!"

    ds_label = tk.Label(janela_constante, text="Dias da semana:")
    ds_label.pack()
    ds_entry = tk.Entry(janela_constante)
    ds_entry.pack()

    jst_label = tk.Label(janela_constante, text="Jornada semanal de trabalho:")
    jst_label.pack()
    jst_entry = tk.Entry(janela_constante)
    jst_entry.pack()

    ist_label = tk.Label(janela_constante, text="Índice de segurança técnica:")
    ist_label.pack()
    ist_entry = tk.Entry(janela_constante)
    ist_entry.pack()

    calcular_button = tk.Button(janela_constante, text="Calcular", command=calcular_constante)
    calcular_button.pack()

    resultado_label = tk.Label(janela_constante, text="")
    resultado_label.pack()

def open_janela_tempo_enfermagem():
    janela_tempo = tk.Toplevel()
    janela_tempo.title("Tempo de horas de enfermagem")

    def calcular_tempo():
        try:
            PCM = float(pcm_entry.get())
            PCI = float(pci_entry.get())
            PCAD = float(pcad_entry.get())
            PCSI = float(pcsi_entry.get())
            PCIt = float(pcit_entry.get())
            THE = ((PCM*4)+(PCI*6)+(PCAD*10)+(PCSI*10)+(PCIt*18))
            resultado_label["text"] = f"O valor do tempo de horas é: {THE:.2f}"
        except ValueError:
            resultado_label["text"] = "Digite valores válidos!"

    pcm_label = tk.Label(janela_tempo, text="PCM:")
    pcm_label.pack()
    pcm_entry = tk.Entry(janela_tempo)
    pcm_entry.pack()

    pci_label = tk.Label(janela_tempo, text="PCI:")
    pci_label.pack()
    pci_entry = tk.Entry(janela_tempo)
    pci_entry.pack()

    pcad_label = tk.Label(janela_tempo, text="PCAD:")
    pcad_label.pack()
    pcad_entry = tk.Entry(janela_tempo)
    pcad_entry.pack()

    pcsi_label = tk.Label(janela_tempo, text="PCSI:")
    pcsi_label.pack()
    pcsi_entry = tk.Entry(janela_tempo)
    pcsi_entry.pack()

    pcit_label = tk.Label(janela_tempo, text="PCIt:")
    pcit_label.pack()
    pcit_entry = tk.Entry(janela_tempo)
    pcit_entry.pack()

    calcular_button = tk.Button(janela_tempo, text="Calcular", command=calcular_tempo)
    calcular_button.pack()

    resultado_label = tk.Label(janela_tempo, text="")
    resultado_label.pack()

def open_janela_qp():
    janela_qp = tk.Toplevel()
    janela_qp.title("Quociente Parteiro")

    def calcular_qp():
        try:
            the = float(the_entry.get())
            ds = float(ds_entry.get())
            qp = the/(ds*24)
            resultado_label["text"] = f"O valor do Quociente Parteiro é: {qp:.2f}"
        except ValueError:
            resultado_label["text"] = "Digite valores válidos!"

    the_label = tk.Label(janela_qp, text="Tempo de horas de enfermagem:")
    the_label.pack()
    the_entry = tk.Entry(janela_qp)
    the_entry.pack()

    ds_label = tk.Label(janela_qp, text="Dias da semana:")
    ds_label.pack()
    ds_entry = tk.Entry(janela_qp)
    ds_entry.pack()

    calcular_button = tk.Button(janela_qp, text="Calcular", command=calcular_qp)
    calcular_button.pack()

    resultado_label = tk.Label(janela_qp, text="")
    resultado_label.pack()

def calculate_qp():
    the = pega_valor(the_input)
    ds = pega_valor(ds_input)
    jst = pega_valor(jst_input)
    if the is None or ds is None or jst is None:
        return
    qp = ((the/8)*ds)/jst
    qp_output.configure(text=f"QP: {qp}")

qp_window = tk.Toplevel()
qp_window.title("Quociente paciente-enfermeiro")

the_label = ttk.Label(qp_window, text="Tempo de horas de enfermagem (THE)")
the_input = ttk.Entry(qp_window)

ds_label = ttk.Label(qp_window, text="Dias da semana")
ds_input = ttk.Entry(qp_window)

jst_label = ttk.Label(qp_window, text="Jornada semanal de trabalho (20,30,36,40..)")
jst_input = ttk.Entry(qp_window)

calculate_button = ttk.Button(qp_window, text="Calcular", command=calculate_qp)
qp_output = ttk.Label(qp_window, text="QP: ")

the_label.pack()
the_input.pack()
ds_label.pack()
ds_input.pack()
jst_label.pack()
jst_input.pack()
calculate_button.pack()
qp_output.pack()

root = tk.Tk()
root.title("Calculadora de Enfermagem")

constante_marinho_button = ttk.Button(root, text="Constante de Marinho", command=constante_marinho_window)
constante_marinho_button.pack()

the_button = ttk.Button(root, text="Tempo de horas de enfermagem", command=the_window)
the_button.pack()

qp_button = ttk.Button(root, text="Quociente paciente-enfermeiro", command=qp_window)
qp_button.pack()

root.mainloop()