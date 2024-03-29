def printLogo(color = 'white'):
    import shutil                       
    from colorama import Fore, Style
    import os

    supportedColors = ["BLACK", 
                       "RED", 
                       "GREEN", 
                       "YELLOW", 
                       "BLUE", 
                       "MAGENTA", 
                       "CYAN", 
                       "WHITE", 
                       "RESET", 
                       "LIGHTBLACK_EX", 
                       "LIGHTRED_EX", 
                       "LIGHTGREEN_EX", 
                       "LIGHTYELLOW_EX", 
                       "LIGHTBLUE_EX", 
                       "LIGHTMAGENTA_EX", 
                       "LIGHTCYAN_EX", 
                       "LIGHTWHITE_EX"]

    if color.upper() not in supportedColors:
        print(f"ERROR: unsupported color given, supported colors:\n{supportedColors}")
        return

    text_color = getattr(Fore, color.upper())

    logo = f"""         {text_color}▄▄ • ▄▄▄   ▄▄▄· • ▌ ▄ ·. .▄▄ · ▄▄▌  ▄▄▄ .▄• ▄▌▄▄▄▄▄ ▄ .▄{Style.RESET_ALL}
        {text_color}▐█ ▀ ▪▀▄ █·▐█ ▀█ ·██ ▐███▪▐█ ▀. ██•  ▀▄.▀·█▪██▌•██  ██▪▐█{Style.RESET_ALL}
        {text_color}▄█ ▀█▄▐▀▀▄ ▄█▀▀█ ▐█ ▌▐▌▐█·▄▀▀▀█▄██▪  ▐▀▀▪▄█▌▐█▌ ▐█.▪██▀▐█{Style.RESET_ALL}
        {text_color}▐█▄▪▐█▐█•█▌▐█ ▪▐▌██ ██▌▐█▌▐█▄▪▐█▐█▌▐▌▐█▄▄▌▐█▄█▌ ▐█▌·██▌▐▀{Style.RESET_ALL}
        {text_color}·▀▀▀▀ .▀  ▀ ▀  ▀ ▀▀  █▪▀▀▀ ▀▀▀▀ .▀▀▀  ▀▀▀  ▀▀▀  ▀▀▀ ▀▀▀ ·{Style.RESET_ALL}"""

    terminal_size = shutil.get_terminal_size()
    lines = logo.split('\n')
    max_length = max(len(line) for line in lines)
    centered_lines = [(line.center(terminal_size.columns, ' ') if len(line.strip()) > 0 else ' ' * terminal_size.columns) for line in lines]

    os.system("cls")
    print('\n'.join(centered_lines))

def helpPage():
    print(f"HELP MENU")
    print(f"\nAll help commands start with !")
    print(f"exit\t- Exit program.")
    print(f"help\t- bring up help menu.")

    