from modulos_telemetria import leituras, processar_leitura, calcular_media_temperaturas

print("Processamento de telemetria: ")
print()
for leitura in leituras:
    mensagem = processar_leitura(leitura)
    print(mensagem)

    temp = leitura.get("temperatura")
    try:
        if temp is not None and float(temp) > 50.0:
            print (f"Anomalida detectada: temperatura crítica as {leitura['timestamp']}: {temp}°C!")
            print()

    except (ValueError, TypeError):
        pass

print()

result =  calcular_media_temperaturas(leituras)
print(f"A média das temperaturas válidas foi: {result:.2f}°C")