def bruteForce(W,berat,nilai,deep,n,kondisi):
    #greedy
    if deep == n:
        cost = 0
        val = 0
        x = ''
        for i in range(n):
            if kondisi[i] :
                cost = cost + berat[i]
                val = val + nilai[i]
                x = x + str(i+1) + ' '
        if cost <= W and cost != 0:
            print(x, ' cost : ', 'value : ', val)
    else:
        kondisi[deep] = True
        bruteForce(W,berat,nilai,deep+1,n,kondisi)
        kondisi[deep] = False
        bruteForce(W,berat,nilai,deep+1,n,kondisi)

    

def Knapsack(Wmax,berat,nilai,n):
    #dengan Dynamic programming tanpa rekursif
    #Wmax untuk max, berat dan nilai array dengan panjang n
    #K adalah tabel hasil setiap iterasi yang berisi nilai dari setiap tahap
    #K array 2 dimensi K[i][w] menyimpan nilai tahap ke-i dengan nilai w
    # +1 karena mulai dari nilai basis f0(y)=0
    #function mengembalikan max nilai
    K = [[0 for x in range(Wmax + 1)] for x in range(n + 1)]
    
    for i in range(n+1):
        print()
        print("Tahap ke-",i)
        for w in range(Wmax+1):
            if i==0 or w == 0:
                #basis
                K[i][w] = 0
            elif berat[i-1] <= w:
                #rekurens
                K[i][w] = max(K[i-1][w],nilai[i-1] + K[i-1][w-berat[i-1]])
            else:
                K[i][w] = K[i-1][w]

            #Output pertahap
            print("y=",w," | F",i-1,"(y)=",K[i-1][w]," | max(F",i,"(y))= ",K[i][w])
    return K[n][Wmax]


def inputBeratNilai():
    #init
    #W kapasitas, nilai dan berat dengan panjang n
    nilai = [45,10,25,30,16,12]
    berat = [10,5,2,5,8,8]
    W = 18
    n = len(nilai)

    kondisi=[False]*n
    
    print("Knapsack Dynamic Programming")
    print(Knapsack(W,berat,nilai,n))
    print()
    print("Knapsack bruteforce greedy")
    bruteForce(W,berat,nilai,0,n,kondisi)
    

inputBeratNilai()