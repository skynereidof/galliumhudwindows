import subprocess

# Komenda do uruchomienia glxgears z Gallium HUD
glxgears_command = "GALLIUM_HUD=GPU-load+cpu+VRAM-usage+temperature+fps glxgears"

# Uruchomienie polecenia glxgears w terminalu
glxgears_process = subprocess.Popen(glxgears_command, shell=True)

# Poczekaj na chwilę, aby glxgears zdążył się uruchomić
# Możesz dostosować czas oczekiwania w razie potrzeby
import time
time.sleep(1)

# Ustawienie okna na wierzchu za pomocą wmctrl
wmctrl_command = "wmctrl -r glxgears -b add,above"

# Uruchomienie polecenia wmctrl w terminalu
wmctrl_process = subprocess.Popen(wmctrl_command, shell=True)

# Czekaj na zakończenie procesu wmctrl
wmctrl_process.wait()

# Ustaw przezroczystość okna glxgears na 50% przy użyciu xprop
xprop_command = "xprop -f _NET_WM_WINDOW_OPACITY 32c -set _NET_WM_WINDOW_OPACITY 0x7FFFFFFF"

# Uruchomienie polecenia xprop w terminalu
xprop_process = subprocess.Popen(xprop_command, shell=True)

# Czekaj na zakończenie procesu xprop
xprop_process.wait()

# Czekaj na zakończenie procesu glxgears
glxgears_process.wait()
