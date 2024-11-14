import matplotlib.pyplot as plt

valores = [5,4,3,2,1,0,2,4,4,5]
valores2 = [1,1,1,1,1,1,1,1,1,1]

plt.plot(valores,label="plot1")
plt.plot(valores2, label="plot2")
plt.legend()
plt.style.use("ggplot")
plt.title("Grafico")

x = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
y = 1
fx = [] #lista vacía

#por cada elemento en la lista x
for elemento in x:

    fx.append(elemento**3 + y)
    # Hacemos la cuenta, y lo agregamos a la lista fx

print(f"F(x) = {fx}")