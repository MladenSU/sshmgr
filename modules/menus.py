from simple_term_menu import TerminalMenu
from os.path import join, isfile
import os
from pathlib import Path
from modules.coloring import Colors
import re
import configparser


class managerMenu(Colors):
    parser = configparser.ConfigParser()

    menuCursor = "> "
    menuCursorstyle = ("fg_red", "bold")
    menuStyle = ("bg_green", "fg_black")

    def enumerateMenus(self, menuList: list) -> list:
        result = []
        indicator = re.compile(r"^\[.\]")
        for num, item in list(enumerate(menuList)):
            if re.match(indicator, item):
                result.append(item)
            else:
                result.append(f"[{num + 1}] {item}")
        return result

    @property
    def keysMenu(self) -> str:
        ssh_folder = f"{Path.home()}/.ssh"
        skipping = re.compile(r'(^.*\.pub$|known_hosts|config)')
        keys = [file for file in os.listdir(ssh_folder) if isfile(
            join(ssh_folder, file)) and not re.match(skipping, file)]
        keys.extend(["[+]Custom path", "[x] No key (Skip)"])
        keys_menu_title = "  SSH Keys\n"
        keys_menu_items = self.enumerateMenus(keys)

        terminal_menu = TerminalMenu(
            menu_entries=keys_menu_items,
            title=keys_menu_title,
            menu_cursor=self.menuCursor,
            menu_cursor_style=self.menuCursorstyle,
            menu_highlight_style=self.menuStyle,
            cycle_cursor=True,
            clear_screen=True,
        )

        menu_entry_index = terminal_menu.show()

        if keys_menu_items[menu_entry_index].startswith("[x]"):
            return ""
        elif keys_menu_items[menu_entry_index].startswith("[+]"):
            keyPath = "-"
            while not Path(keyPath).exists():
                self.info("Make sure that the path is correct!")
                keyPath = pyin.inputStr("Full path: ").replace(
                    '~/', f"{str(Path.home())}/")
            self.okmsg(f"The path - \"{keyPath}\" exists!")
            return f"-i {keyPath}"
        else:
            return f"-i {ssh_folder}/{keys[menu_entry_index]}"

    def removeMenu(self, configFile: str) -> list:
        self.parser.read(configFile)
        options = self.parser.sections()
        options.append("Exit")
        terminal_menu = TerminalMenu(
            menu_entries=options,
            title="Remove:",
            multi_select=True,
            show_multi_select_hint=True,
        )
        terminal_menu.show()
        return terminal_menu.chosen_menu_entries

    def mainMenu(self, configFile):
        self.parser.read(configFile)
        menu_options = self.enumerateMenus(self.parser.sections())
        if len(menu_options) > 0:
            menu_options.extend(
                ("[-] Remove Connections", "[+] Add New", "[x] Exit"))
        else:
            menu_options.extend(("[+] Add New", "[x] Exit"))
        terminal_menu = TerminalMenu(
            menu_options, title="\nPlease select an action:")
        menu_entry_index = terminal_menu.show()
        return [len(menu_options), menu_entry_index, menu_options[menu_entry_index]]
