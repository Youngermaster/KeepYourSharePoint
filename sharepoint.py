import json
import os
from shareplum import Site, Office365
from shareplum.site import Version

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
config_path = '\\'.join([ROOT_DIR, 'config.json'])

with open(config_path) as config_file:
    config = json.load(config_file)
    config = config['share_point']

USERNAME = config['username']
PASSWORD = config['password']
SHAREPOINT_URL = config['url']
SHAREPOINT_SITE = config['site']
SHAREPOINT_DOC = config['doc_library']


class SharePoint:
    def auth(self):
        self.authcookie = Office365(
            share_point_site=SHAREPOINT_URL, username=USERNAME, password=PASSWORD).GetCookies()
        self.site = Site(SHAREPOINT_SITE, version=Version.v365,
                         authcookie=self.authcookie)

        return self.site

    def connect_folder(self, folder_name):
        self.auth_site = self.auth()

        self.sharepoint_dir = '\\'.join([SHAREPOINT_DOC, folder_name])
        self.folder = self.auth_site.Folder(self.sharepoint_dir)

        return self.folder