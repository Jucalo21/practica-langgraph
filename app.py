from agent.graph import run_graph


def main():
    palabra = input("Ingrese una palabra: ")
    resultados = run_graph(palabra)
    print(
        f"""
    La palabra {resultados["info"]["word"]} {"si" if resultados["info"]["is_palindrome"] else "no"} es palindroma, tiene una longitud de {resultados["info"]['length']} letras y significa: 
    {resultados['definition']}.

    """
    )


if __name__ == "__main__":
    main()
