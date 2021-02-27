# Удаляем лишние пробелы и переносы строк:
def del_space(x: str) -> str:
    return ' '.join(x.split())