#!/usr/bin/env python

from cleo import option
from poetry.console.commands.installer_command import InstallerCommand
from poetry.console.application import Application

class CheckLockCommand(InstallerCommand):

    name = "check-lock"
    description = "Checks the pyproject.toml against poetry.lock ."

    loggers = ["poetry.repositories.pypi_repository"]

    def handle(self):
        if not (self.poetry.locker.is_locked() and self.poetry.locker.is_fresh()):
            self.line(
                "<error>"
                "Error: The lock file is not up to date with "
                "the latest changes in pyproject.toml. "
                "</error>"
            )
            return 1

        self.line(
            "<info>"
            "Lock and pyproject are in-sync."
            "</info>"
        )
        return 0


application = Application()
application.add(CheckLockCommand())

if __name__ == '__main__':
    application.run()
