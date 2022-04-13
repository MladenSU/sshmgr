import subprocess
import re
import pyinputplus as pyin
from modules.menus import managerMenu
from pathlib import Path


class sshManager(managerMenu):

    def __init__(self, configFile: str) -> None:
        self.configFile = configFile

    @property
    def verifyConfig(self) -> None:
        if not Path(self.configFile).exists():
            self.warning('No config file detected!')
            self.okmsg(f"Created a config file: {self.configFile}")
            Path(self.configFile).touch(exist_ok=True)

    def writeData(self, msg) -> None:
        with open(self.configFile, 'w') as cnfg:
            self.parser.write(cnfg)
        self.okmsg(msg)

    @property
    def addLabel(self) -> str:
        while True:
            label = pyin.inputStr("Give a label: ")
            self.parser.read(self.configFile)
            if label not in self.parser.sections():
                return f"{label} (SSH)"
            else:
                self.warning("Label already exists, give another one!")
                continue

    @property
    def recordData(self) -> None:
        label = self.addLabel
        username = pyin.inputStr("Username: ")
        server = pyin.inputStr("Server/Host: ")
        port = pyin.inputInt("Port number: ")
        key = self.keysMenu
        self.parser[label] = {
            "command": f"ssh -p {port} {username}@{server} {key}"}
        self.writeData(f"Successfully added - \"{label}\"!")

    @property
    def removeData(self) -> None:
        toRemove = self.removeMenu(self.configFile)
        exitExists = True if "Exit" in toRemove else False
        if exitExists:
            self.info(
                "Exit was selected while removing entries, hence nothing will be removed!")
            self.info("Bye Bye!")
            exit()
        for label in toRemove:
            self.parser.remove_section(label)
        self.writeData(f"Successfully removed - {', '.join(toRemove)}!")

    @property
    def menuActions(self) -> None:
        choice = self.mainMenu(self.configFile)
        if choice[1] == (choice[0] - 2):
            self.recordData
        elif choice[1] == (choice[0] - 3):
            self.removeData
        elif choice[1] == (choice[0] - 1):
            exit("Bye Bye!")
        else:
            self.sshConnect(self.parser.get(
                re.sub(r'^\[\d{1,10}\]\s+', '', choice[2]), 'command'))

    @staticmethod
    def sshConnect(cmd) -> None:
        subprocess.run(cmd, shell=True)

    @property
    def main(self) -> None:
        while True:
            try:
                self.verifyConfig
                self.menuActions
            except (KeyboardInterrupt, TypeError):
                self.warning("Caught interruption! Bye Bye!")
                exit(1)
