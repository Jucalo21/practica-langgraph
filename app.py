from agent.graph import run_graph


def main():
    palabra = input("Ingrese una palabra: ")
    resultados = run_graph(palabra)
    print(
        f"""
    La palabra {resultados["info"]["word"]} {"si" if resultados["info"]["is_palindrome"] else "no"} es palindroma, tiene una longitud de {resultados["info"]['length']} letras,
    sus {"sinonimos" if resultados['syn_ant']['is_synonym'] else "antonimos"} son {resultados['syn_ant']['words']} y significa: 
    {resultados['definition']['definition']}.

    """
    )


if __name__ == "__main__":
    main()
