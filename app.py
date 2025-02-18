from agent.graph import run_graph

palabra = input("Ingrese una palabra:")
resultados = run_graph(palabra)
print(
    f"""
La palabra {resultados["word"]} {"si" if resultados.get("is_palindrome") else "no"} es palindroma.

"""
)
