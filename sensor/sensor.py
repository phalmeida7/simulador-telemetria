# Dicionário de leituras 
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
        return f"Sucesso {leitura['timestamp']} -> {temperatura_float}ºC"
    
    except (ValueError, TypeError) as e:
        return f"\033[31mAviso: falha ao processar da leitura {leitura.get('timestamp')}. Motivo: ({temperatura_bruta}\033[0m)."
    
    except Exception as e:
        return f"Erro inesperado em {leitura.get('timestamp')}: {e}"