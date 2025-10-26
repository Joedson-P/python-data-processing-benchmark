from datetime import datetime, timedelta

import numpy as np
import pandas as pd


def create_large_dataset(rows=100000, add_issues=True):
    """
    Cria um dataset realista para testes de performance e limpeza de dados

    Args:
        rows (int): Número de linhas do dataset
        add_issues (bool): Adiciona problemas comuns em dados reais
    Returns:
        pd.DataFrame: Dataset com dados para testes
    """

    np.random.seed(42)

    data = {
        "id": range(1, rows + 1),
        "nome": [f"Usuario_{i}" for i in range(1, rows + 1)],
        "idade": np.random.randint(18, 80, rows),
        "salario": np.random.normal(50000, 15000, rows),
        "departamento": np.random.choice(["TI", "RH", "Financeiro", "Marketing"], rows),
        "data_admissao": [
            datetime(2020, 1, 1) + timedelta(days=np.random.randint(0, 1460))
            for _ in range(rows)
        ],
        "ativo": np.random.choice([True, False], rows, p=[0.7, 0.3]),
    }

    df = pd.DataFrame(data)

    if add_issues:
        df = _add_data_issues(df)

    return df


def _add_data_issues(df):
    """Adiciona problemas comuns em dados reais"""
    rows_original = len(df)

    # Valores nulos
    null_mask = np.random.random(rows_original) < 0.05
    df.loc[null_mask, "salario"] = np.nan

    # Inconsistências de texto
    text_mask = np.random.random(rows_original) < 0.03
    df.loc[text_mask, "departamento"] = df.loc[text_mask, "departamento"].str.upper()

    # Valores extremos
    outlier_mask = np.random.random(rows_original) < 0.01
    df.loc[outlier_mask, "salario"] = df.loc[outlier_mask, "salario"] * 10

    # Datas inconsistentes
    date_mask = np.random.random(rows_original) < 0.02
    df.loc[date_mask, "data_admissao"] = datetime(1990, 1, 1)

    # Duplicatas
    if rows_original > 10:
        duplicate_indices = np.random.choice(
            df.index, size=min(100, rows_original // 100), replace=False
        )
        df = pd.concat([df, df.loc[duplicate_indices]], ignore_index=True)

    return df


def save_dataset(df, filename="dataset_teste.csv"):
    """Salva o dataset em CSV"""
    import os

    os.makedirs("data/raw", exist_ok=True)
    df.to_csv(f"data/raw/{filename}", index=False)
    print(f"Dataset salvo em: data/raw/{filename}")
    print(f"Shape do dataset: {df.shape}")


if __name__ == "__main__":
    df = create_large_dataset(rows=5000)
    print("Dataset criado com sucesso!")
    print(df.head())
    print(f"Total de linhas: {len(df)}")
    print(f"Colunas: {list(df.columns)}")
    print(f"Valores nulos: {df.isnull().sum().sum()}")
    print(f"Duplicatas: {df.duplicated().sum()}")
    save_dataset(df, "dataset_exemplo.csv")
