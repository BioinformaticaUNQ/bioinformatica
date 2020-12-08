# for MAC
#clustalw = 'Users/fabrizio/Downloads/clustalw-2.1-macosx.dmg'

# For Windows
#clustalw = 'C:\Program Files (x86)\ClustalW2\clustalw2.exe'

import os

clustalw = os.path.join(os.path.join(os.getcwd(), 'clustal'), 'clustalw2.exe')


dssp_route = os.path.join(os.path.join(os.getcwd(), 'dssp'), 'dssp-2.0.4-win32.exe')
