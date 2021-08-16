import math
angulo = float(input("Digite o ângulo desejado: ".strip()))
#É preciso converter para radianos com math.radians
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print("Ângulo {}: seno {:.2f}, cosseno {:.2f}, tangente {:.2f}.VAMO PORRA!".format(angulo, sen, cos, tan))
