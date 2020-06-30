from tkinter import * #importando a biblioteca de interface gráfica
from estilo import * #importando o arquivo contendo a formatação
from calculo import * #importando o arquivo para fazer o cálculo par ou impar
import random #importando a função random para gerar a escolha do pc
import tkinter.messagebox as mbox #importando um método de confirmação do reset e chamando pelo nome de 'mbox'
import win32gui, win32con

try:
    ocultar_janela = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(ocultar_janela, win32con.SW_HIDE)

except:
    pass

raiz = Tk() #Toda a parte gráfica será feita dentro de 'raiz'

class Janela:
    def __init__(self, raiz):
        self.fr1 = Frame(raiz, bg=preto)#Frame do campo de batalha e do reset
        self.fr1.pack()

        self.fr_resul = Frame(raiz, bg=preto)#Frame do deu par ou deu impar
        self.fr_resul.pack()

        self.fr2 = Frame(raiz, bg=preto)#Frame dos nomes e do placar
        self.fr2.pack()

        self.fr3 = Frame(raiz, bg=preto)#Frame da Imagem do player e do goku
        self.fr3.pack()

        self.fr4 = Frame(raiz, bg=preto)#Frame da escolha par ou impar
        self.fr4.pack()

        self.fr5 = Frame(raiz, bg=preto)#Frame do informe um número e a caxinha de digito
        self.fr5.pack()

        self.fr6 = Frame(raiz, bg=preto)#Frame do start e do erro
        self.fr6.pack()

        #Carregando todas as imagens
        self.img_player = PhotoImage(file="imagens/gamer.png")
        self.img_pc = PhotoImage(file="imagens/goku.png")
        self.img_0 = PhotoImage(file="imagens/numero_0.png")
        self.img_1 = PhotoImage(file="imagens/numero_1.png")
        self.img_2 = PhotoImage(file="imagens/numero_2.png")
        self.img_3 = PhotoImage(file="imagens/numero_3.png")
        self.img_4 = PhotoImage(file="imagens/numero_4.png")
        self.img_5 = PhotoImage(file="imagens/numero_5.png")
        self.img_6 = PhotoImage(file="imagens/numero_6.png")
        self.img_7 = PhotoImage(file="imagens/numero_7.png")
        self.img_8 = PhotoImage(file="imagens/numero_8.png")
        self.img_9 = PhotoImage(file="imagens/numero_9.png")
        self.img_10 = PhotoImage(file="imagens/numero_10.png")

        #Label do campo de batalha
        self.lb1 = Label(self.fr1, text="Campo de Batalha", bg=preto, font=fonte1, fg=laranja, pady=10, padx=25)
        self.lb1.pack(side=LEFT)

        #Botão do reset
        self.bt_reinicia = Button(self.fr1, bg=laranja, text="RESET", font=fonte4, fg=preto, relief=RAISED, border=5, command=self.reiniciar)
        self.bt_reinicia.bind("<Return>", self.reiniciar2)
        self.bt_reinicia.pack(side=LEFT)

        #Label do deu par ou deu impar
        self.lb_resul = Label(self.fr_resul, text="", font=fonte1, fg=verde,bg=preto)
        self.lb_resul.pack(side=LEFT)

        #Iniciando os placares e  o Label dos nomes e do placar
        self.placar1 = 0
        self.placar2 = 0
        self.lb2 = Label(self.fr2, text="PLAYER          " + str(self.placar1) + "  X  " + str(self.placar2) + "          GOKU ", bg=preto, font=fonte3, fg=laranja, pady=10)
        self.lb2.pack()

        #Imagem do player carregada no Label
        self.lb_img1 = Label(self.fr3, image=self.img_player,bg=preto)
        self.lb_img1.pack(side=LEFT)

        #Esse Label separa a imagem do player da do goku
        self.lb_separa = Label(self.fr3, bg=preto, text="   ")
        self.lb_separa.pack(side=LEFT)

        #Imagem do goku carregada no Label
        self.lb_img2 = Label(self.fr3, image=self.img_pc, bg=preto)
        self.lb_img2.pack(side=LEFT)

        #Criação da variável que armazena a escolha par ou impar do Radiobutton
        self.escolha = StringVar()
        self.rb_par = Radiobutton(self.fr4, text="Par", value="par", variable=self.escolha, bg=preto, fg=azul, font=fonte2, pady=20)
        self.rb_par.pack(side=LEFT)
        self.rb_impar = Radiobutton(self.fr4, text="Ímpar", value="impar", variable=self.escolha, bg=preto, fg=azul, font=fonte2, pady=20)
        self.rb_impar.pack(side=LEFT)

        #Label do informe um número
        self.lb3 = Label(self.fr5, text="Informe um número de 0 à 10: ", bg=preto, fg=azul, font=fonte3, pady=20, width=25)
        self.lb3.pack(side=LEFT)

        #Caixinha para informar o número
        self.num = Entry(self.fr5, width=2, font=fonte2, bg=azul)
        self.num.pack(side=LEFT)

        #Botão start. Funcina no click ou no enter. Tem foco forçado. Está empacotado
        self.bt_jogar = Button(self.fr6, bg=laranja, text="START", font=fonte1, fg=preto, relief=RAISED, border=10, command=self.jogar)
        self.bt_jogar.bind("<Return>", self.jogar2)
        #self.bt_jogar.focus_force()
        self.bt_jogar.pack()

        #Label do erro
        self.lb_erro = Label(self.fr6, text="", font=fonte4, bg=preto, fg=vermelho)
        self.lb_erro.pack()

    #Método jogar
    def jogar(self):
        #Tratamento caso a entrada não seja a esperada
        try:
            #Recebe a escolha par ou impar do usuário
            escolha = self.escolha.get()
            #Recebe o número escolhido e já tranforma em inteiro
            num = int(self.num.get())
            #Gera o número aleatório do pc
            num_comp = random.randrange(0, 11)

            #Se o número digitado estiver no intervalo correto e se a escolha for par ou impar
            if (num >= 0 and num <= 10) and (escolha == "par" or escolha == "impar"):

                    #Cada um compara o número do player e mostra a imagem que o representa e logo depois zera o Label do erro
                    if num == 0:
                        self.lb_img1["image"] = self.img_0
                        self.lb_erro["text"] = ""
                    elif num == 1:
                        self.lb_img1["image"] = self.img_1
                        self.lb_erro["text"] = ""
                    elif num == 2:
                        self.lb_img1["image"] = self.img_2
                        self.lb_erro["text"] = ""
                    elif num == 3:
                        self.lb_img1["image"] = self.img_3
                        self.lb_erro["text"] = ""
                    elif num == 4:
                        self.lb_img1["image"] = self.img_4
                        self.lb_erro["text"] = ""
                    elif num == 5:
                        self.lb_img1["image"] = self.img_5
                        self.lb_erro["text"] = ""
                    elif num == 6:
                        self.lb_img1["image"] = self.img_6
                        self.lb_erro["text"] = ""
                    elif num == 7:
                        self.lb_img1["image"] = self.img_7
                        self.lb_erro["text"] = ""
                    elif num == 8:
                        self.lb_img1["image"] = self.img_8
                        self.lb_erro["text"] = ""
                    elif num == 9:
                        self.lb_img1["image"] = self.img_9
                        self.lb_erro["text"] = ""
                    elif num == 10:
                        self.lb_img1["image"] = self.img_10
                        self.lb_erro["text"] = ""

                    #Cada um compara o número do goku e mostra a imagem que o representa
                    if num_comp == 0:
                        self.lb_img2["image"] = self.img_0
                    elif num_comp == 1:
                        self.lb_img2["image"] = self.img_1
                    elif num_comp == 2:
                        self.lb_img2["image"] = self.img_2
                    elif num_comp == 3:
                        self.lb_img2["image"] = self.img_3
                    elif num_comp == 4:
                        self.lb_img2["image"] = self.img_4
                    elif num_comp == 5:
                        self.lb_img2["image"] = self.img_5
                    elif num_comp == 6:
                        self.lb_img2["image"] = self.img_6
                    elif num_comp == 7:
                        self.lb_img2["image"] = self.img_7
                    elif num_comp == 8:
                        self.lb_img2["image"] = self.img_8
                    elif num_comp == 9:
                        self.lb_img2["image"] = self.img_9
                    elif num_comp == 10:
                        self.lb_img2["image"] = self.img_10

                    #Variável recebe o retorno da função, importada do arquivo calculo.py
                    par_impar = calcula_par_impar(num, num_comp)
                    if par_impar == "par":
                        self.lb_resul["text"] = "DEU PAR"
                    elif par_impar == "impar":
                        self.lb_resul["text"] = "DEU ÍMPAR"

                    #Se o player tiver acertado o placar dele é alterado
                    if (par_impar == "par" and escolha == "par") or (par_impar == "impar" and escolha == "impar"):
                        self.placar1 += 1
                        self.lb2["text"] = "PLAYER          " + str(self.placar1) + "  X  " + str(self.placar2) + "          GOKU "
                    #Se não, o placar do goku é alterado
                    else:
                        self.placar2 += 1
                        self.lb2["text"] = "PLAYER          " + str(self.placar1) + "  X  " + str(self.placar2) + "          GOKU "

            #Tratamento caso o usuário digite um número fora do intervalo
            else:
                self.lb_erro["text"] = "ERRO, ESCOLHA (PAR OU ÍMPAR) E DIGITE UM NÚMERO (ENTRE 0 E 10)"
        #Tratamento caso o usuário não digite um número
        except:
            self.lb_erro["text"] = "ERRO, ESCOLHA (PAR OU ÍMPAR) E DIGITE UM NÚMERO (ENTRE 0 E 10)"

    #Mesma coisa, a única diferença é o parâmetro event, que indica um evento do teclado, no caso o enter
    def jogar2(self, event):

        try:
            escolha = self.escolha.get()
            num = int(self.num.get())
            num_comp = random.randrange(0, 11)

            if (num >= 0 and num <= 10) and (escolha == "par" or escolha == "impar"):
                    if num == 0:
                        self.lb_img1["image"] = self.img_0
                        self.lb_erro["text"] = ""
                    elif num == 1:
                        self.lb_img1["image"] = self.img_1
                        self.lb_erro["text"] = ""
                    elif num == 2:
                        self.lb_img1["image"] = self.img_2
                        self.lb_erro["text"] = ""
                    elif num == 3:
                        self.lb_img1["image"] = self.img_3
                        self.lb_erro["text"] = ""
                    elif num == 4:
                        self.lb_img1["image"] = self.img_4
                        self.lb_erro["text"] = ""
                    elif num == 5:
                        self.lb_img1["image"] = self.img_5
                        self.lb_erro["text"] = ""
                    elif num == 6:
                        self.lb_img1["image"] = self.img_6
                        self.lb_erro["text"] = ""
                    elif num == 7:
                        self.lb_img1["image"] = self.img_7
                        self.lb_erro["text"] = ""
                    elif num == 8:
                        self.lb_img1["image"] = self.img_8
                        self.lb_erro["text"] = ""
                    elif num == 9:
                        self.lb_img1["image"] = self.img_9
                        self.lb_erro["text"] = ""
                    elif num == 10:
                        self.lb_img1["image"] = self.img_10
                        self.lb_erro["text"] = ""

                    if num_comp == 0:
                        self.lb_img2["image"] = self.img_0
                    elif num_comp == 1:
                        self.lb_img2["image"] = self.img_1
                    elif num_comp == 2:
                        self.lb_img2["image"] = self.img_2
                    elif num_comp == 3:
                        self.lb_img2["image"] = self.img_3
                    elif num_comp == 4:
                        self.lb_img2["image"] = self.img_4
                    elif num_comp == 5:
                        self.lb_img2["image"] = self.img_5
                    elif num_comp == 6:
                        self.lb_img2["image"] = self.img_6
                    elif num_comp == 7:
                        self.lb_img2["image"] = self.img_7
                    elif num_comp == 8:
                        self.lb_img2["image"] = self.img_8
                    elif num_comp == 9:
                        self.lb_img2["image"] = self.img_9
                    elif num_comp == 10:
                        self.lb_img2["image"] = self.img_10

                    par_impar = calcula_par_impar(num, num_comp)
                    if par_impar == "par":
                        self.lb_resul["text"] = "DEU PAR"
                    elif par_impar == "impar":
                        self.lb_resul["text"] = "DEU ÍMPAR"

                    if (par_impar == "par" and escolha == "par") or (par_impar == "impar" and escolha == "impar"):
                        self.placar1 += 1
                        self.lb2["text"] = "PLAYER          " + str(self.placar1) + "  X  " + str(self.placar2) + "          GOKU "
                    else:
                        self.placar2 += 1
                        self.lb2["text"] = "PLAYER          " + str(self.placar1) + "  X  " + str(self.placar2) + "          GOKU "

            else:
                self.lb_erro["text"] = "ERRO, ESCOLHA (PAR OU ÍMPAR) E DIGITE UM NÚMERO (ENTRE 0 E 10)"

        except:
            self.lb_erro["text"] = "ERRO, ESCOLHA (PAR OU ÍMPAR) E DIGITE UM NÚMERO (ENTRE 0 E 10)"

    #Método reiniciar
    def reiniciar(self):
        #Variável recebe o retorno da caixinha de reset, yes ou no
        resposta = mbox.askquestion("RESET", "Deseja Resetar?")

        #Zera todos os Labels para o início
        if resposta == "yes":
            self.lb_resul["text"] = ""
            self.lb_img1["image"] = self.img_player
            self.lb_img2["image"] = self.img_pc
            self.placar1 = 0
            self.placar2 = 0
            self.lb2["text"] = "PLAYER          " + str(self.placar1) + "  X  " + str(self.placar2) + "          GOKU "
            self.lb_erro["text"] = ""

    #Mesma coisa, só que com o event como parâmetro
    def reiniciar2(self, event):
        resposta = mbox.askquestion("RESET", "Deseja Resetar?")
        if resposta == "yes":
            self.lb_resul["text"] = ""
            self.lb_img1["image"] = self.img_player
            self.lb_img2["image"] = self.img_pc
            self.placar1 = 0
            self.placar2 = 0
            self.lb2["text"] = "PLAYER          " + str(self.placar1) + "  X  " + str(self.placar2) + "          GOKU "
            self.lb_erro["text"] = ""

#Indica a tamanho inicial da janela de execução
raiz.geometry("840x650+300+30")
#Adiciona o ícone à janela
raiz.iconbitmap("imagens/goku_icone.ico")
#Adiciona o título à janela
raiz.title("Par ou Impar do Moab")
#Define a cor de fundo da janela
raiz["bg"] = preto

#Estância da Janela raiz
janela = Janela(raiz)
#Deixa o programa aberto, até que o usuário feche
raiz.mainloop()