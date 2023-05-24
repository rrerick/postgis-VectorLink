import sys
import argparse
import config.exceptions as err


def argumentParser(args):
    """

    Args:
        args (_type_): _description_
    """

    desc = 'Programa para Exportar tables com geometrias em arquivos .GPKG'
    parser = argparse.ArgumentParser(description=desc)

    hlp = 'Usuário com Acesso ao banco de dados'
    parser.add_argument('-u', '--user', type=str, help=hlp)

    hlp = 'Senha do Banco de Dados'
    parser.add_argument('-w', '--password', type=str, help=hlp)

    hlp = 'ip do banco de dados'
    parser.add_argument('-H', '--host', type=str, help=hlp)
    
    hlp = 'Porta do banco de dados'
    parser.add_argument('-p', '--port', type=str, help=hlp)

    hlp = 'Nome do Banco de Dados'
    parser.add_argument('-d', '--database', type=str, help=hlp)

    hlp = 'Tabela que será exportada <esquema>.<nome tabela>'
    parser.add_argument('-t', '--table', type=str, help=hlp)

    hlp = 'Caminho do Arquivo com o JSON para realização de Tarefas'
    parser.add_argument('-f', '--file', type=str, help=hlp)

    if args.__len__() == 0:
        raise err.NoParameters
    else:
        args = parser.parse_args()
        return args
