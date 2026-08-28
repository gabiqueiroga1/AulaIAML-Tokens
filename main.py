def tokens_custo(texto:str, custo_por_token: float=0.0015)->dict:
    """estimativa na media de 3.2 caracteres por token em portugues"""
    total_caracteres = len(texto)
    tokens_estimados=max(int(total_caracteres / 3.2),1)
    custo_estimado =(tokens_estimados /1000) * custo_por_token

    return{
        "caracteres":total_caracteres,
        "tokens_estimados": tokens_estimados,
        "custo": f"{custo_estimado:6f}"
    }

especificacao = "antes de brasileira, sou corinthians...seja corinthians, vai corinhians"
print("Resultado", tokens_custo(especificacao))



