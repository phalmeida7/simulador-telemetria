# Dicionário de leituras  {chave:; valor}

leituras = [
    {"timestamp": "20:00", "temperatura": 25.0},
    {"timestamp": "20:01", "temperatura": 25.2},
    {"timestamp": "20:05", "temperatura": 26.0},
    {"timestamp": "20:08", "temperatura": 25.7},
    {"timestamp": "20:12", "temperatura": 25.4},
    {"timestamp": "20:24", "temperatura": 97.9},
    {"timestamp": "20:26", "temperatura": "Erro"},
    {"timestamp": "20:30", "temperatura": None},
    {"timestamp": "20:32", "temperatura": 67.0},
    {"timestamp": "20:33", "temperatura": 39.2},
    {"timestamp": "20:34", "temperatura": 25.5}
]

# Função de validação

def processar_leitura(leitura):
    try:
        temperatura_bruta = leitura.get("temperatura")

        if temperatura_bruta is None:
            raise ValueError ("Dado ausente")
        
        temperatura_float = float(temperatura_bruta)
        return f"Sucesso {leitura['timestamp']} -> {temperatura_float}ºC"  # f antes = f string
    
    except (ValueError, TypeError) as e:
        return f"\033[31mFalha ao processar leitura das {leitura.get('timestamp')}. Motivo: ({temperatura_bruta})\033[0m."
    
    except Exception as e:
        return f"Erro inesperado em {leitura.get('timestamp')}: {e}"
    
def calcular_media_temperaturas(lista_de_leituras):
    soma_total = 0.0 
    qntd = 0
    for leitura in lista_de_leituras:

        try:
            temp_bruta = leitura.get("temperatura")

            temp_float  = float(temp_bruta)

            soma_total += temp_float
            qntd += 1 
        
        except (TypeError, ValueError):
            continue

    if qntd > 0:
            media = soma_total/qntd
            return media
    
    else: 
        return 0, 0
    
