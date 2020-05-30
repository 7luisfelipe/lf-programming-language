import re
"""
    A classe Script armazena as informações do nosso código fonte,
    lendo elas do arquivo informado
"""
class Script:
    def __init__(this, scriptName):
        this.script = this.openFile(scriptName) #Código original
        #this.scriptLst = this.script.split(' ') #Separa o código em uma lista separada por um espaço
        this.scriptLst = re.split("\.| ", this.script)

    #Abre o arquivo com o nome do script
    def openFile(this, filename):
        code = open('lfScripts/'+filename, 'r').read()
        return code

    def __str__(this):
        return this.script