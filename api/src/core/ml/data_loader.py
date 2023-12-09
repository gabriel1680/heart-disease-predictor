import pandas as pd


class DataLoader:
    """Carregador de dados que serão utilizados para o treinamento e teste do modelo.
    """

    def __init__(self, url: str):
        self.__url = url

    def load(self, attributes: list):
        """ Carrega e retorna um DataFrame. Há diversos parâmetros
        no read_csv que poderiam ser utilizados para dar opções
        adicionais.
        """
        return pd.read_csv(self.__url, skiprows=0, delimiter=',', usecols=attributes)
