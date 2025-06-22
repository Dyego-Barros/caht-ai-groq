from langchain_core.runnables import Runnable, RunnableLambda, RunnablePassthrough, RunnableParallel


#Recebe a entrada e passa para frente

parte1_runnable = RunnablePassthrough()


#Conta caracteres da entrada
def conta_carateres(dic: dict) -> int:
    count = len(dic["input"])
    return count

convert_funcao = RunnableLambda(conta_carateres)

parte2_runnable = RunnablePassthrough.assign(conta_carateres= convert_funcao)

def transforma(entrada: dict)->str:    
    resultado = entrada["input"] + " conseguiu"
    return resultado

parte3_transforma_entrada = RunnableLambda(transforma)
parte_passa_frente = RunnablePassthrough()

parte3_runnable = RunnableParallel({
    "trasnforma_entrada": parte3_transforma_entrada,
    "parte3_passa_frente": parte_passa_frente
})

parte4_runnable = RunnablePassthrough()


chain = parte1_runnable| parte2_runnable| parte3_runnable|parte4_runnable

resposta = chain.invoke({"input":"Paranbéns você"})

print(resposta)