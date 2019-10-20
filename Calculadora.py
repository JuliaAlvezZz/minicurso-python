n1=int(input("Digite um número: "))
n2=int(input("Digite outro número: "))
op=input("Digite a operação que você deseja realizar (+, -, *, /): ")

if op=="+":
    resultado=n1+n2
elif op=="-":
    resultado=n1-n2
elif op=="*":
    resultado=n1*n2
elif op=="/":
    resultado=n1/n2
else:
    resultado="ERRO!"

print(n1,op,n2,"=",resultado)
