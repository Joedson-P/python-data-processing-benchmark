import importlib.util
import os
import sys


def import_project_module(module_name, file_path):
    """
    Importa módulos do projeto de forma segura usando importlib

    Args:
        module_name (str): Nome do módulo
        file_path (str): Caminho para o arquivo .py

    Returns:
        module: Módulo importado
    """
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def setup_project_path():
    """
    Configura o path do projeto para imports

    Returns:
        str: Caminho para a raiz do projeto
    """
    project_root = os.path.abspath(os.path.join(os.getcwd(), ".."))
    sys.path.insert(0, project_root)
    return project_root


# Teste automático ao importar
if __name__ == "__main__":
    print("Módulo utils carregado com sucesso!")
    print("Funções disponíveis: import_project_module, setup_project_path")
