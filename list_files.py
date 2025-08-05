import os
import sys
import datetime

"""
Script para listar recursivamente todos os arquivos de um diretório
e salvar o resultado em um arquivo .txt, incluindo caminho, data de modificação e tamanho.

Uso:
    python list_files_to_txt.py <diretorio> <arquivo_saida>

Exemplo:
    python list_files_to_txt.py C:\industria C:\industria\lista_arquivos.txt
"""
def list_files(directory: str, output_file: str) -> None:
    with open(output_file, "w", encoding="utf-8") as outfile:
        for root, _, files in os.walk(directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                try:
                    stat = os.stat(filepath)
                except OSError as e:
                    outfile.write(f"Erro ao acessar {filepath}: {e}\n")
                    continue
                size = stat.st_size
                mtime = datetime.datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
                outfile.write(f"{filepath}\t{mtime}\t{size}\n")

def main() -> None:
    if len(sys.argv) < 3:
        print("Uso: python list_files_to_txt.py <diretorio> <arquivo_saida>")
        sys.exit(1)
    directory = sys.argv[1]
    output_file = sys.argv[2]
    if not os.path.isdir(directory):
        print(f"Erro: {directory} não é um diretório ou não existe")
        sys.exit(1)
    list_files(directory, output_file)
    print(f"Listagem salva em {output_file}")

if __name__ == "__main__":
    main()
