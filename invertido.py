n = 1
A = '54751212454521123'
B = '5648975474474648978124'

while(n > 0):
    Ainvertido = A[:: -1]
    Binvertido = B[:: -1]
    

    if Ainvertido[0] == Binvertido[0] and Ainvertido[1] == Binvertido[1]:
        print('encaixa')
    else:
        print('não encaixa')

    n = 0