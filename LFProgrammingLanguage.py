from script.ScriptReader import ScriptReader
from interpreter.Interpreter import Interpreter
class LFProgrammingLanguage:
    def __init__(this):
        this.run()

    def findCode(this):
        sr = ScriptReader()
        #Percorre a lista de scripts
        for s in sr.getScripts():
            Interpreter(s.script)

    def run(this):
        this.findCode()