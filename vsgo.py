from urllib.parse import unquote, urlparse
from sys import argv
from os.path import expandvars, join, exists
from os import walk, system, chdir
import json

def get_workspaces():
    path = expandvars('%APPDATA%\\Code\\User\\workspaceStorage')
    (_, dirs, _) = next(walk(path))
    workspaces = []
    for dir in dirs:
        subpath = join(path, dir)
        filepath = join(subpath, 'workspace.json')
        if exists(filepath):
            with open(filepath) as f:
                data = json.load(f)
                try:
                    workspace_uri = data['folder']
                    workspaces.append(unquote(urlparse(workspace_uri).path)[1:])
                except:
                    pass
    return workspaces

if __name__=='__main__':
    if argv.__len__() != 2:
        print(
            'vsgo: Incorrect usage, please give a workspace name as argument\n \
            \n \
            vsgo <WORKSPACE-NAME>\n'
        )
        exit()
    for workspace in get_workspaces():
        if workspace.find(argv[1]) != -1:
            print(f"cd {workspace}")
