

def ler_conjunto(nome):
    elementos = input(f"Digite os elementos do conjunto {nome} separados por espaço: ")
    return set(map(int, elementos.split()))


A = ler_conjunto("A")
B = ler_conjunto("B")

print(f"\nConjunto A = {A}")
print(f"Conjunto B = {B}")


print("\n=== Operações com conjuntos ===")
print(f"A ∪ B (união): {A | B}")
print(f"A ∩ B (interseção): {A & B}")
print(f"A - B (diferença): {A - B}")
print(f"B - A (diferença): {B - A}")
print(f"A == B (igualdade): {A == B}")
print(f"A ⊆ B (A é subconjunto de B): {A.issubset(B)}")
print(f"A ≠ B (desigualdade): {A != B}")

print("\n=== Produto cartesiano ===")
produto_cartesiano = {(a, b) for a in A for b in B}
print(f"A × B = {produto_cartesiano}")


print("\n=== Relações binárias ===")
R = {(a, b) for a in A for b in B if a < b}
print(f"R (a < b): {R}")

par = (int(input("\nDigite um valor para 'a': ")), int(input("Digite um valor para 'b': ")))
print(f"O par {par} pertence a R? {par in R}")
