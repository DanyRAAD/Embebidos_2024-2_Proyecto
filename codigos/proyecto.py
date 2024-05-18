import curses
import subprocess

def mostrar_menu(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Bienvenido al Centro de Entretenimiento:", curses.A_BOLD)
    stdscr.addstr(2, 0, "1. Servicios en línea para video")
    stdscr.addstr(3, 0, "2. Servicios en línea para música")
    stdscr.addstr(4, 0, "3. Reproducir desde medio extraíble")
    stdscr.addstr(5, 0, "Seleccione una opción: ")
    stdscr.refresh()
    opcion = stdscr.getch()
    return opcion

def mostrar_submenu_video(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Seleccione un servicio en línea para video:", curses.A_BOLD)
    stdscr.addstr(2, 0, "1. Netflix")
    stdscr.addstr(3, 0, "2. Prime Video")
    stdscr.addstr(4, 0, "3. VIX")
    stdscr.refresh()
    opcion = stdscr.getch()
    return opcion

def mostrar_submenu_musica(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Seleccione un servicio en línea para música:", curses.A_BOLD)
    stdscr.addstr(2, 0, "1. Spotify")
    stdscr.addstr(3, 0, "2. Deezer")
    stdscr.addstr(4, 0, "3. Amazon Music")
    stdscr.refresh()
    opcion = stdscr.getch()
    return opcion

def abrir_netflix(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Abriendo Netflix en el navegador...", curses.A_BOLD)
    stdscr.refresh()
    stdscr.getch()  # Espera a que el usuario presione una tecla antes de continuar
    subprocess.run([“startx”,"chromium-browser", "https://www.netflix.com"])

def abrir_prime_video(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Abriendo Prime Video en el navegador...", curses.A_BOLD)
    stdscr.refresh()
    stdscr.getch()  # Espera a que el usuario presione una tecla antes de continuar
    subprocess.run([“startx”,"chromium-browser", "https://www.primevideo.com"])

def abrir_vix(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Abriendo VIX en el navegador...", curses.A_BOLD)
    stdscr.refresh()
    stdscr.getch()  # Espera a que el usuario presione una tecla antes de continuar
    subprocess.run([“startx”,"chromium-browser", "https://www.vix.com/es"])

def abrir_spotify(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Abriendo Spotify en el navegador...", curses.A_BOLD)
    stdscr.refresh()
    stdscr.getch()  # Espera a que el usuario presione una tecla antes de continuar
    subprocess.run([“startx”,"chromium-browser", "https://www.spotify.com"])

def abrir_deezer(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Abriendo Deezer en el navegador...", curses.A_BOLD)
    stdscr.refresh()
    stdscr.getch()  # Espera a que el usuario presione una tecla antes de continuar
    subprocess.run([“startx”,"chromium-browser", "https://www.deezer.com"])

def abrir_amazon_music(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Abriendo Amazon Music en el navegador...", curses.A_BOLD)
    stdscr.refresh()
    stdscr.getch()  # Espera a que el usuario presione una tecla antes de continuar
    subprocess.run([“startx”,"chromium-browser", "https://music.amazon.com"])

def mostrar_mensaje(stdscr, opcion_elegida):
    if opcion_elegida == ord('1'):
        subopcion_elegida = None
        while subopcion_elegida not in [ord('1'), ord('2'), ord('3'), ord('8')]:
            subopcion_elegida = mostrar_submenu_video(stdscr)
            if subopcion_elegida == ord('1'):
                abrir_netflix(stdscr)
            elif subopcion_elegida == ord('2'):
                abrir_prime_video(stdscr)
            elif subopcion_elegida == ord('3'):
                abrir_vix(stdscr)
    elif opcion_elegida == ord('2'):
        subopcion_elegida = None
        while subopcion_elegida not in [ord('1'), ord('2'), ord('3'), ord('8')]:
            subopcion_elegida = mostrar_submenu_musica(stdscr)
            if subopcion_elegida == ord('1'):
                abrir_spotify(stdscr)
            elif subopcion_elegida == ord('2'):
                abrir_deezer(stdscr)
            elif subopcion_elegida == ord('3'):
                abrir_amazon_music(stdscr)
    elif opcion_elegida == ord('8'):
        return False
    else:
        stdscr.clear()
        stdscr.addstr(0, 0, f"Ha seleccionado la opción: {chr(opcion_elegida)}")
        stdscr.refresh()
        stdscr.getch()
    return True

def main(stdscr):
    curses.curs_set(0)  # Ocultar el cursor
    opcion_elegida = None
    while opcion_elegida != ord('8'):
        opcion_elegida = mostrar_menu(stdscr)
        if not mostrar_mensaje(stdscr, opcion_elegida):
            break

if __name__ == "__main__":
    curses.wrapper(main)
