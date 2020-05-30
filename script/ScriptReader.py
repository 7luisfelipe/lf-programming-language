import os
from script.Script import Script

"""
    -> Essa classe tem como objetivo ler todos os arquivos escritos em lf
"""

class ScriptReader:
    def __init__(this):
        this.scripts = [] #Lista de Scripts

    #Busca todos os Scripts(escritos em LF) que estão na pasta scripts
    def getScripts(this):
        for f in os.listdir('lfScripts'):
            if f.endswith('.lf'):
                this.scripts.append(Script(f))
        return this.scripts
