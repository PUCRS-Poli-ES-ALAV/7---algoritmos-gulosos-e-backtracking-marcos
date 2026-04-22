def calcular_moedas(moedas_disp: list, valor):
    sum = 0
    moedas = []
    moedas_disp.sort(reverse=True)
    curr_coin = 0;
    iteracoes = 0;
    while(sum < valor):
        iteracoes+=1
        it = moedas_disp[curr_coin]
        if(sum+it<=valor):
            sum+=it
            moedas.append(it)
        else:
            curr_coin+=1
        if curr_coin == len(moedas_disp) and moedas_disp[curr_coin] + sum > valor:
            return []

    return moedas, iteracoes

def main():
    print("moedas (100, 50, 25, 10, 5, 1, 0.50), valor 435")
    print(calcular_moedas([100, 50, 25, 10, 5, 1, 0.5], 435))

if __name__ == "__main__":
    main()