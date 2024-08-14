import tkinter as tk
import subprocess
import time

def start_glxgears():
    # Komenda do uruchomienia glxgears z Gallium HUD
    glxgears_command = 'GALLIUM_HUD="simple,fps,frametime,cpu,GPU-load,VRAM-usage,sensors_temp_cu-amdgpu-pci-0600.edge,temperature,sensors_temp_cu-k10temp-pci-00c3.Tdie,shader-clock" glxgears'

    # Uruchomienie polecenia glxgears w terminalu
    glxgears_process = subprocess.Popen(glxgears_command, shell=True)

    # Poczekaj na chwilę, aby glxgears zdążył się uruchomić
    time.sleep(1)

    # Ustawienie okna na wierzchu za pomocą wmctrl
    wmctrl_command = "wmctrl -r glxgears -b add,above"
    subprocess.Popen(wmctrl_command, shell=True).wait()

    # Ustaw przezroczystość okna glxgears na 50% przy użyciu xprop
    xprop_command = "xprop -f _NET_WM_WINDOW_OPACITY 32c -set _NET_WM_WINDOW_OPACITY 0x7F7F7F7F"
    subprocess.Popen(xprop_command, shell=True).wait()

    # Usuń dekoracje okna za pomocą wmctrl
    wmctrl_command_undecorate = "wmctrl -r glxgears -b add,undecorated"
    subprocess.Popen(wmctrl_command_undecorate, shell=True).wait()

    # Czekaj na zakończenie procesu glxgears
    glxgears_process.wait()

def create_window():
    # Tworzenie głównego okna tkinter
    root = tk.Tk()

    # Ustawienie rozmiaru okna
    root.geometry("300x300")

    # Ustawienie koloru tła na przezroczysty
    root.configure(bg='')

    # Uruchomienie pętli głównej programu tkinter
    root.mainloop()

# Wywołanie funkcji do uruchomienia glxgears z HUD i manipulacji oknem
start_glxgears()

# Po zakończeniu glxgears, utwórz okno tkinter
create_window()
