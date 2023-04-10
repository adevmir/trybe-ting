from ting_file_management.file_management import txt_importer


def exists_word(word, instance):
    ocorrencias = list()
    line_number = 0
    for line in instance.search(0)["linhas_do_arquivo"]:
        line_number += 1
        if word.lower() in line.lower():
            ocorrencias.append({"linha": line_number})
    result = [{
        "palavra": word,
        "arquivo": instance.search(0)["nome_do_arquivo"],
        "ocorrencias": ocorrencias
    }]
    if (ocorrencias == []):
        return ocorrencias
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
