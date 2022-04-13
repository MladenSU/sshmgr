#!/usr/bin/env python3
from pathlib import Path
from modules.manager import sshManager


if __name__ == '__main__':
    configFile = f"{Path(__file__).parent.resolve()}/ssh_data.ini"
    manageConn = sshManager(configFile)
    manageConn.main
