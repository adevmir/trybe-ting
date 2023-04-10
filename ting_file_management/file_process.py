import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    content = txt_importer(path_file)
    dict_content = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(content),
        "linhas_do_arquivo": content
    }
    for e in range(0, len(instance)):
        name_file = dict_content["nome_do_arquivo"]
        if (instance.search(e)["nome_do_arquivo"] == name_file):
            return
    instance.enqueue(dict_content)
    print(dict_content, file=sys.stdout)


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos", file=sys.stdout)
        return
    path_file = instance.dequeue()["nome_do_arquivo"]
    print(f"Arquivo {path_file} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
