import math

a=float(input("Digite o valor de a: "))
b=float(input("Digite o valor de b: "))
c=float(input("Digite o valor de c: "))

if a==0:
   print("Impossível de calcular, pois a não pode ser zero.")
else:

   d=(b**2)-(4*a*c)

   if d<0:
      print("A equação não tem solução real")
   else:

      if d==0:
         x=-b/(2*a)
         print("Existe uma única raiz real com valor",x)
      else:
         x1=(-(b) + math.sqrt(d))/(2*a)
         x2=(-(b) - math.sqrt(d))/(2*a)
         print("Existem duas raízes reais com valores",x1,"e",x2)
