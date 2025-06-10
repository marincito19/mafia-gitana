print("Bienvenido al registro de invitados.")
print("Debes ingresar la cantidad exacta de nombres que indiques.\n")

# Pedir la cantidad de nombres a ingresar
cantidad = int(input("¿Cuántos nombres deseas ingresar?: "))

# Lista para guardar los nombres en mayúsculas
invitados = []

# Ciclo para ingresar los nombres uno por uno
for i in range(cantidad):
    nombre = input("Escribe un nombre: ")
    invitados(nombre)

# Mostrar la lista completa
print("\nLista de invitados:")
for invitado in invitados:
    print(f"- {invitado}")

# Encontrar el nombre más largo y el más corto
nombre_mas_largo = max(invitados, key=len)
nombre_mas_corto = min(invitados, key=len)

print(f"\nInvitado con el nombre más largo: {nombre_mas_largo}")
print(f"Invitado con el nombre más corto: {nombre_mas_corto}")