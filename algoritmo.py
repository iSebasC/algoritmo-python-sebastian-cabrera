def process_urls(file_path):
    valid_urls = set()  # Usamos un conjunto para evitar duplicados
    
    with open(file_path, 'r') as file:
        for line in file:
            url = line.strip()  # Quitamos los espacios en blanco y saltos de línea
            # Verificamos que la URL contenga 'shop' y termine en '.html'
            if 'shop' in url and url.endswith('.html'):
                valid_urls.add(url)  # Añadimos al conjunto, lo que evita duplicados
    
    # Contamos las URLs válidas
    total_urls = len(valid_urls)
    
    # Mostramos las URLs válidas
    print(f"Total de URLs que cumplen con los criterios: {total_urls}")
    for url in valid_urls:
        print(url)

# Se crea el archivo url.txt para haga el funcionamiento
process_urls('urls.txt')
