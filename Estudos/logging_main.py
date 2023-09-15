import logging

logging.basicConfig(level=logging.INFO, filename='exec')

def resultado_operacional(faturamento, custo):
    return faturamento - custo

def lucro_liquido(faturamento, custo, percentual_imposto):
    if percentual_imposto == 0:
        logging.warning("Percentual de imposto é 0, tá certo isso?")
    return (faturamento - custo) * (1 - percentual_imposto)

def lucro_por_acoes(faturamento, custo, percentual_imposto, acoes):
    if acoes == 0:
        logging.error("Ações não pode ser igual a 0")
    return lucro_liquido(faturamento, custo, percentual_imposto) / acoes

faturamento = 1000
custo = 400
percentual_imposto = 0.3
acoes = 100

resultado = resultado_operacional(faturamento, custo)
logging.info(f"Resultado: {resultado}")

lucro = lucro_liquido(faturamento, custo, percentual_imposto)
logging.info(f"Lucro: {lucro}")

lucro_acao = lucro_por_acoes(faturamento, custo, percentual_imposto, acoes)
logging.info(f"Lucro por ação {lucro_acao}")