def maior_primo(nr):

    primos = []
    for i in range(nr):
        c = 0
        for j in range(nr):
            if i%(j+1) == 0: 
                c = c + 1
        if c == 2:
            primos.append(i)

    return(max(primos))

print(maior_primo(100))