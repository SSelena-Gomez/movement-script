import time
import os
import sys
import ctypes
import threading
from pynput.keyboard import Key, Controller, Listener

# --- ELEVARE ADMIN ---
def is_admin():
    try: return ctypes.windll.shell32.IsUserAnAdmin()
    except: return False

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

# --- INSTALARE AUTOMATA DEPENDINTE ---
try:
    import psutil
    import pygetwindow as gw
except ImportError:
    os.system("pip install psutil pygetwindow pynput")
    os.execl(sys.executable, sys.executable, *sys.argv)

keyboard = Controller()
enabled = False
active_keys = set()
last_dir = None

# Locatie precisa pentru null.txt
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
NULL_FILE_PATH = os.path.join(SCRIPT_DIR, "null.txt")

class Colors:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    END = '\033[0m'
    BOLD = '\033[1m'

def check_steam_license():
    """Verifica daca hl.exe ruleaza din folderul Steam."""
    for proc in psutil.process_iter(['name', 'exe']):
        try:
            if proc.info['name'] == 'hl.exe':
                if "steamapps" in proc.info['exe'].lower(): return True
        except: continue
    return False

def is_cs_focused():
    """Verifica daca fereastra de joc este activa."""
    try:
        win = gw.getActiveWindow()
        return win and ("Counter-Strike" in win.title or "hl" in win.title.lower())
    except: return False

def on_press(key):
    global enabled, last_dir
    if key == Key.insert:
        enabled = not enabled
        draw_ui()
        return

    if not enabled or not is_cs_focused():
        return

    try:
        k = key.char.lower() if hasattr(key, 'char') else key
        if k in active_keys: return
        active_keys.add(k)

        # TRIGGER ACTIV: Logica de Null se aplica doar pe SPACE sau CTRL (Duck)
        trigger_on = any(x in active_keys for x in [Key.space, Key.ctrl_l, Key.ctrl_r])

        if trigger_on:
            if k == 'a':
                keyboard.release('d')
                last_dir = 'a'
            elif k == 'd':
                keyboard.release('a')
                last_dir = 'd'
    except: pass

def on_release(key):
    global last_dir
    try:
        k = key.char.lower() if hasattr(key, 'char') else key
        if k in active_keys: active_keys.remove(k)
        if k == last_dir: last_dir = None
    except: pass

def draw_ui():
    os.system('cls')
    status = f"{Colors.GREEN}READY (WAITING FOR TRIGGERS){Colors.END}" if enabled else f"{Colors.YELLOW}OFF (PRESS INSERT){Colors.END}"
    print(f"{Colors.CYAN}{Colors.BOLD}==========================================")
    print("      ENHANCED MOVEMENT ENGINE V7        ")
    print(f"=========================================={Colors.END}")
    print(f" [License] : {Colors.GREEN}Steam Verified{Colors.END}")
    print(f" [Logic]   : {Colors.BOLD}New Null-Canceling (A/D){Colors.END}")
    print(f" [Status]  : {status}")
    print("------------------------------------------")
    print(f" {Colors.BOLD}TRIGGERS ACTIVE:{Colors.END}")
    print(f" -> Hold {Colors.CYAN}[SPACE]{Colors.END} for Snap-Jump")
    print(f" -> Hold {Colors.CYAN}[CTRL]{Colors.END}  for Snap-Crouch")
    print("------------------------------------------")
    print(" [INSERT] - Toggle Engine ON/OFF")
    print("------------------------------------------")

if __name__ == "__main__":
    # Creare automata null.txt daca lipseste
    if not os.path.exists(NULL_FILE_PATH):
        with open(NULL_FILE_PATH, "w") as f:
            f.write("Ly8gRW5jcnlwdGVkIEtleSBmb3IgVjcgLSBEbyBOb3QgTW9kaWZ5")

    print(f"{Colors.CYAN}[>] Waiting for Steam CS 1.6...{Colors.END}")
    
    def monitor():
        while True:
            if not any(p.info['name'] == 'hl.exe' for p in psutil.process_iter(['name'])):
                os._exit(0)
            time.sleep(5)
    
    threading.Thread(target=monitor, daemon=True).start()
    draw_ui()

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
