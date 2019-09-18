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
        self.st_especial = ["@","$","¨","~","#",'\\']
        self.caractere = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","ç","z","x","c","v","b","n","m",
                          "Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Ç","Z","X","C","V","B","N","M"]
    def separador(self):
        lnText = []
        for i in range(len(self.texto)):
            rec = False
            pt = False
            for x in self.texto[i].split(" "):
                x = x.replace("\n","")
                if x != "" or x != "\n":                         #remove o \s e add em um novo vetor. (Linha,tipo, palavra)
                    if x in self.token:
                        lnText.append((i+1,"TOKEN",x))
                        if x == "//":
                            rec = True
                        if x == "print":
                            pt = True
                    elif pt:
                        print("LINHA DO PRINT",i) #alguma logica para o print vai ser necessario
                        if x[0] == "&":
                            print("PRINT-Identificador")
                            lnText.append((i+1,"IDENTIFICADOR",x))
                    elif rec:
                        print("Comentario---")
                    elif self.is_number(x):
                        lnText.append((i+1,"TOKEN_NUMERICO",x))
                    else:
                        if len(x) >1:
                            if x[0] in self.caractere:
                                lnText.append((i+1,"IDENTIFICADOR",x))
                            else:
                                lnText.append((i+1,"NÃO ACEITO",x))
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
