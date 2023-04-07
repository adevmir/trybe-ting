def txt_importer(path_file):
    import sys
    try:
        if not path_file.endswith('.txt'):
            print("Formato inválido", file=sys.stderr)
            return
        with open(path_file, 'r') as arquivo:
            return arquivo.read().splitlines()
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
