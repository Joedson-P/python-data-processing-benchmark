import sys

import matplotlib
import numpy as np
import pandas as pd
import pytest
import seaborn as sns


def main():
    print("🔧 VERIFICAÇÃO DO AMBIENTE DE DESENVOLVIMENTO")
    print("=" * 50)

    # Verificar versão do Python
    print(f"✅ Python version: {sys.version}")

    # Verificar pacotes principais
    print(f"✅ Pandas version: {pd.__version__}")
    print(f"✅ NumPy version: {np.__version__}")
    print(f"✅ Matplotlib version: {matplotlib.__version__}")
    print(f"✅ Seaborn version: {sns.__version__}")
    print(f"✅ Pytest version: {pytest.__version__}")

    # Testar imports dos módulos locais
    try:
        from src.data_generator import create_large_dataset

        print("✅ Módulo data_generator importado com sucesso")
    except ImportError as e:
        print(f"⚠️  data_generator ainda não implementado: {e}")

    try:
        from src.data_cleaner import DataCleaner

        print("✅ Módulo data_cleaner importado com sucesso")
    except ImportError as e:
        print(f"⚠️  data_cleaner ainda não implementado: {e}")

    # Testar funcionalidades básicas
    try:
        df = pd.DataFrame({"test": [1, 2, 3]})
        print("✅ DataFrame do Pandas funcionando")
    except Exception as e:
        print(f"❌ Erro com Pandas: {e}")

    print("=" * 50)
    print("🎉 Ambiente configurado com sucesso!")
    print("📁 Estrutura do projeto pronta para desenvolvimento")


if __name__ == "__main__":
    main()
