from math import floor, ceil
from random import uniform
from time import time
import matplotlib.pyplot as plt

start = time()


def main(): # y'=xy^2; y(0) = 2; y(1/2) = ?
        x = 1/2
        #f = func(1/2) # f(x) = 2/(1-x^2), solucao analitica da EDO
        yn = 2 #y0 = 2
        h = -1.0 # so pra inicializar h

        dydx = x*yn**2 # edo y' = x*y**2 = f(x,y)

        d2xdy2 = yn**2 + 2*x*yn*dydx # segunda derivada implicita a partir da EDO

        arr_yn = []
        arr_bigO = []
        arr_h = []
        arr_time = []
        arr_xne = []
        x0 = x

        h = float(input("h0 = ")) # primeiro "passo" que vamos dar
        lower_bound = float(input("potencia de 2 pra dividir o intervalo:  "))

        while(h >= (2**(-1*lower_bound))): #10^-n, da so pra dividir, nao sei pq eu escrevi assim
                yn = 2

                for i in range(ceil((x/h))):
                        yn = yn + h*(h*(i)*yn**2) # y_n+1 = y_n + h*F(x_n,y_n)

                c = uniform(x - h, x + h) # sorteando algum numero nesse intervalo, como no erro de taylor

                arr_yn.append(yn)
                arr_bigO.append(abs((h**2)*d2xdy2/2)) # analise de erro usando serie de taylor
                arr_h.append(h)
                x0 += h
                arr_xne.append(x0)
                h = h/2
                end = time()
                arr_time.append(abs(start - end))



        Fi = 2
        lbd = int(input("lambda = "))
        arr_Fn = [] # inicializacao das listas
        arr_bigOr = []
        arr_ordem = []
        cont_x0hR = []
        cont_fxyR = []
        arr_ynR = []
        x0 = 1/2
        y0 = 2

        print(arr_yn)

        for i in range(len(arr_yn) - 1): # esse loop "varre" a extensao do vetor das aproximacoes de euler, mas tira o ultimo valor, que nao vai ser usado (lembra que fica uma escadinha?)
          Fi = 2*(lbd**(i+1) * arr_yn[i+1]/lbd - arr_yn[i])/(lbd**(i+1) - 1) # aqui o h/lbd vai ser o proximo passo, ja que estamos dividindo simetricamente os intervalos
          arr_bigOr.append(arr_h[i]**(i+1)) # erro = O(h^n+1)
          arr_ordem.append(i) # aqui eu adiciono a "ordem", pra poder acompanhar em qual "n" acontece cada coisa
          arr_Fn.append(Fi) # aqui eu adiciono a um vetor os valores das aproximacoes
          cont_x0hR.append(x0 + arr_h[i])
          cont_fxyR.append((cont_x0hR[i])*(Fi + arr_h[i])**2) # coef linear
          arr_ynR.append(Fi)


        arr_h.pop()
        plt.scatter(arr_h, arr_Fn, color="black")
        plt.plot(arr_h, arr_Fn, color="red")
        plt.title('Relação entre valores de h e as aproximações fornecidas (menor divisão 2^-26)')
        plt.xlabel("Valores de h")
        plt.ylabel("Aproximações pela extrapolação de Richardson")
        plt.annotate('y(1/2) ~ 2.666667', xy=(0, 2.6666667), xytext=(0.4, 2.6), arrowprops=dict(facecolor = 'black'))
        plt.show()

        plt.scatter(arr_ordem, arr_bigOr, color="black")
        plt.plot(arr_ordem, arr_bigOr, color="red")
        plt.title('bigO x n')
        plt.xlabel("Ordem (n)")
        plt.ylabel("bigO")
        plt.show()

        #print(list(zip(arr_Fn, arr_h, arr_bigOr)))

        arr_bigO.pop() # removendo um ultimo elemento so de sacanagem; plot dos erros
        plt.plot(arr_h, arr_bigOr, color="blue", label="bigO richardson")
        plt.plot(arr_h, arr_bigO, color="red", label='bigO euler')
        plt.scatter(arr_h, arr_bigOr, color="black")
        plt.scatter(arr_h, arr_bigO, color="black")
        plt.title('comparacao dos erros')
        plt.legend(loc='upper left')
        plt.xlabel("h")
        plt.ylabel("bigO")
        plt.show()


        plt.scatter(arr_xne, arr_yn, color="black") # aproximacao do formato da funcao
        plt.plot(arr_xne, arr_yn, color="red", label='euler')
        plt.scatter(cont_x0hR, arr_ynR, color="black") # aproximacao do formato da funcao
        plt.plot(cont_x0hR, arr_ynR, color="blue", label='richardson')
        plt.title('Aproximação da função')
        plt.xlabel("x0 + h")
        plt.legend(loc='upper right')
        plt.ylabel("y_n")
        plt.annotate('y(1/2) ~ 2.666667', xy=(0, 2.6666667), xytext=(0.4, 2.6), arrowprops=dict(facecolor = 'black'))
        plt.show()

        arr_yn.pop() # removendo o ultimo pra poder plottar
        plt.scatter(arr_h, arr_Fn, color="black") # comparacao das aproximacoes
        plt.scatter(arr_h, arr_yn, color="black")
        plt.plot(arr_h, arr_Fn, color="red", label='richardson')
        plt.plot(arr_h, arr_yn, color='blue', label='euler')
        plt.title('Relação entre valores de h e as aproximações fornecidas (menor divisão 2^-26)')
        plt.xlabel("Valores de h")
        plt.legend(loc='upper right')
        plt.ylabel("Aproximações pela extrapolação de Richardson")
        plt.annotate('y(1/2) ~ 2.666667', xy=(0, 2.6666667), xytext=(0.4, 2.6), arrowprops=dict(facecolor = 'black'))
        plt.show()

main()
