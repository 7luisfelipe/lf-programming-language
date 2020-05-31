import re
from message.Console import Console
from mathematics.Math import Math

class Interpreter:
    def __init__(this, script):
        this.script = script
        this.interpreter()

    def interpreter(this):
        # Percorre cada linha do script
        try:
            while True:
                scriptLst = re.split("\n", this.script)
                # filter(lambda i: i != '', scriptLst)
                while '' in scriptLst:
                    scriptLst.remove('')

                #Se acabou de ler o Script
                if len(scriptLst) <= 0:
                    break

                for l in scriptLst:
                    # Split na linha
                    lst = re.split('\.| |\(', l)
                    for it in lst:
                        if it == 'console':
                            # Encontra o tipo da mensagem
                            typee = ''
                            idx_start_console = l.index(it)
                            idx_end_console = idx_start_console + (len(it) - 1)
                            if l[idx_end_console + 1] == '.':  # Significa que depois do console tem um .
                                # Busca o primeiro ESPAÇO depois da palavra reservada CONSOLE
                                idx_type_console_end = l.index(' ', idx_end_console)
                                typee = l[idx_end_console + 2:idx_type_console_end]  # idx_end_console+2 = pis não queremos a ultima letra da palavra CONSOLE nem o .(ponto)

                            # O que estiver entre '' é a MSG
                            idx_start = l.index("'", l.index(
                                it))  # Primeira ' da linha que está sendo analisada a partir da palavra reservada CONSOLE
                            idx_end = l.index("'", idx_start + 1)  # Primeira ' após a ' que marca o inicio do texto
                            msg = l[(idx_start + 1):idx_end]  # idx_Start + 1 para pegar só o texto e não a '
                            Console(typee, msg)
                            break
                        elif it == 'loop':
                            quantity_str = l[
                                           (l.index('(', l.index(it))) + 1
                                           :
                                           l.index(')', l.index('('))
                                           ]

                            # Busca o comando a ser executado dentro do loop - abre { do loop no script
                            idx_start_loop_script = this.script.index('{', this.script.index(l))
                            idx_end_loop_script = this.script.index('}', this.script.index(l))
                            #Loop(int(quantity_str), (this.script[idx_start_loop_script + 1:idx_end_loop_script]))


                            for i in range(int(quantity_str)):
                                Interpreter((this.script[idx_start_loop_script + 1:idx_end_loop_script]))

                            break
                        elif it == '+':
                            #Busca os valores para somar
                            idx_start_script = this.script.index('{', this.script.index(l))
                            idx_end_script = this.script.index('}', this.script.index(l))

                            numbers = this.script[idx_start_script+1:idx_end_script]
                            numbers = numbers.split(',')
                            r = Math(numbers).addition()
                            Console('', '+Result: '+str(r))
                            break
                        elif it == '*':
                            #Busca os valores para somar
                            idx_start_script = this.script.index('{', this.script.index(l))
                            idx_end_script = this.script.index('}', this.script.index(l))

                            numbers = this.script[idx_start_script+1:idx_end_script]
                            numbers = numbers.split(',')
                            r = Math(numbers).multiplication()
                            Console('', '*Result: '+str(r))
                            break
                        elif it == '/':
                            #Busca os valores para somar
                            idx_start_script = this.script.index('{', this.script.index(l))
                            idx_end_script = this.script.index('}', this.script.index(l))

                            numbers = this.script[idx_start_script+1:idx_end_script]
                            numbers = numbers.split(',')
                            r = Math(numbers).division()
                            Console('', '/Result: '+str(r))
                            break
                        elif it == '-':
                            #Busca os valores para somar
                            idx_start_script = this.script.index('{', this.script.index(l))
                            idx_end_script = this.script.index('}', this.script.index(l))

                            numbers = this.script[idx_start_script+1:idx_end_script]
                            numbers = numbers.split(',')
                            r = Math(numbers).subtraction()
                            Console('', '-Result: '+str(r))
                            break
                    # s.script = s.script.replace(l,'')
                    # ultimo caractere da linha
                    last_str = l[len(l) - 1]
                    if last_str == '{':
                        idx_start_loop_script = this.script.index('{', this.script.index(l))
                        idx_end_loop_script = this.script.index('}', this.script.index(l))

                        for line in re.split("\n", this.script):
                            if this.script.index(line) >= idx_start_loop_script and this.script.index(
                                    line) <= idx_end_loop_script:
                                this.script = this.script.replace(line, '', 1)
                            if line == '}':
                                break
                    this.script = this.script.replace(l, '', 1)
                    break
        except:
            print('fim da execução')