import nessrest
import os
import re
import sys
import time
import datetime


class Settings(object):
    '''
    Settings interface
    '''

    def __init__(self, scanner=None,
                      url="",
                      login="",
                      password="",
                      insecure="",
                      template=""):
        if scanner:
            self.scanner = scanner
        else:
            self.scanner = nessrest.Scanner(url=url,
                                            login=login,
                                            password=password,
                                            insecure=insecure)
        self.scan_id = ""
        self.scanner_id = "1"
        self.folder_id = ""
        self.uuid = ""
        self.category = ""
        self.settings = {"launch":"ONETIME",
                         "enabled":False,
                         "launch_now":True,
                         "text_targets":"",
                         "file_targets":""}
        self.audits = {}
        self.creds = {}
        self.uploads = []
        self.categories = {}

        self._cache = {}

        if template:
            self.set_scan_template(template)

    def update_software(self):
        self.scanner.action(
            action="settings/software-update",
            method="POST"
        )
