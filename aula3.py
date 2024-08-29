
Esse código vai analisar todos os números até o numero escolhido menos 1
num = int(input("Digite um número: "))
i = 2
while i < num:
    print(f"{num}%{i}={num%i}")
    if num % i == 0:
        print(f"{num} não é primo") #se o resto da divisão número analisado do i for 0 vai printar que ele é um número primo
        break # se o resto da divisão de algum número analisado do i ja for 0 ele vai parar e não vai fazer o resto
    elif i == num-1:
        print(f"{num} é primo")
    i+=1 # esse i+=1 ele pertence ao while, então depois do numero que está sendo analisado do i passar pelo if ou elif ele vai adicionar mais um

num=48
qtd_divs = 0
i=2
while i < num:
    print(f"{num}%{i} = {num%i}")
    if num%i==0:
        qtd_divs+=1 # toda vez que o resto da divisão de algum número analisado pelo i for 0 será adicionado nessa variavel
        print(f"{num} não é primo")
        break # é muito importante pois ele economiza precesso e espaço
    elif i > num/2: # para ver se um número é primo basta fazer a divisão de todos os números até a metade pois nenhum número maior que sua metade é divisível por ele
        print(f"{num} é primo")
        break
    i+=1

num=3
while num < 100: # 3 ao 100
    num+=1
    i=2
    while i < num: # 2 até o número que está no num
        if num % i == 0: # se o resto da divisão do num por algum número de i for 0, o num não é primo
            print(f"{num} não é primo")
            break # se não tiver o break aqui todos vai printar que num não é primo todas as vezes que o resto da divisão de num por i for 0 
        elif i>num/2: # se o i for maior que a metade de num, pois depois da metade com certeza nenhum número vai ser divisível, portanto não precisa ser analisado
            print(f"{num} é primo")
            break # se não tiver o break vai printar que num é primo a metade de num vezes
        i+=1
# o primeiro while vai analisar os numeros de 3 a 100 e dentro dessa while tem outro while que vai analisar todos os números menos que o número que está sendo analisado no primeiro
# while. Ou seja, supondo que o num esteja no número 10 e o segundo while vai pegar todos o numeros de 2 a 10 (2,3,4,5,6,7,8,9,10) e todos eles vão entrar ou dentro do if ou dentro
# do elif. Caso o resto da divisão de alguns desses números (3,4,5,6,7,8,9,10) for igual a 0, o número que está sendo analisado em num não é primo, e se, o número analisado em i
# for maior que a metade de num sem o resto da divisão dar 0 ele é primo

a = 1
b = 0
qtd = 0
while a+b < 100:
    c = a + b
    a = b
    b = c
    qtd+=1
    print(c)
# forma de printar os números de fibonacci até um um número 

num=int(input("Digite até qual sequência você quer saber da sequência de fibonacci: "))
a=1
b=0
i=1
while i<num:
    c=a+b
    a=b
    b=c
    i+=1
    print(c)
# forma de printar os números de fibonacci até um sequência determinada

num=100
a=1
b=0
while a+b<num:
    c=a+b
    a=b
    b=c
    i=2
    while i<c:
        if c%i==0:
            print(f"{c} não é primo e faz parte da sequência de fibonacci")
            break
        elif i>c/2:# pode ser esse ou pode ser i==c-1, se usar um else não da certo
            print(f"{c} é primo mas faz parte da sequência de fibonacci")
            break
        i+=1
