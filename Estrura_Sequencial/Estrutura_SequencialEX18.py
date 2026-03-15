tamanho_arquivo_mb = float(input("Digite o tamanho do arquivo para download (em MB): "))
velocidade_internet_mbps = float(input("Digite a velocidade do link de Internet (em Mbps): "))

tamanho_arquivo_mbit = tamanho_arquivo_mb * 8
tempo_download_segundos = tamanho_arquivo_mbit / velocidade_internet_mbps
tempo_download_minutos = tempo_download_segundos / 60

print(f"O tempo aproximado de download é de {tempo_download_segundos:.2f} segundos.")
print(f"Isso equivale a aproximadamente {tempo_download_minutos:.2f} minutos.")