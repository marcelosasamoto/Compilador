class AnalisadorLexico:

    def __init__(self, nome, texto):
        self.nome = nome
        self.texto = texto
        self.lnTexto = []
        f = open(nome+".code", "r")
        self.texto = f.readlines()
        f.close()
        self.token = ["int","float","String","boolean","True","False","return","if","for", "in","or","and", "==","!=",
                      "<=",">=","!","+","-","*","^","/","%",'"',"=","//","{","}","(",")","[","]","print","input"]
        self.st_especial = ["@","$","¨","~"]

    def separador(self):
        lnText = []
        for i in range(len(self.texto)):
            for x in self.texto[i].split(" "):
                if x != "":                         #remove o \s e add em um novo vetor. (Linha,tipo, palavra)
                    if x in self.token:
                        lnText.append((i+1,"TOKEN",x))
                    elif self.is_number(x):
                        lnText.append((i+1,"TOKEN_NUMERICO",x))
                    elif x in range(len(lnText))
                    else:
                        lnText.append((i+1,"IDENTIFICADOR",x))
        return lnText

    def is_number(self,num):
        try:
            float(num)
            return True
        except:
            pass
        return False

    def salvar_codigo(nome,texto):
        f = open(nome+".code", "w")
        f.write(texto)
        f.close()
