#!/usr/bin/env python3
import sys
from config.arguments import argumentParser
from config.table import Table
import getpass
from time import sleep
import json
import config.exceptions as err
import execute





def main(args:list):
    """Script to export table into gpkg file
    """
    arguments = argumentParser(args)

    #If dont have a path to a txt file or a tablename
    if arguments.table is None and arguments.file is None:
       raise err.MissingParam('-t/--table')

    #database name can not be null
    if arguments.database is None:
        raise err.MissingParam('-d/--database')

    #Important To know what to do
    if arguments.function is None:
        raise err.MissingParam('-F/--Function')


    #User or password is none
    if arguments.password is None:
        if arguments.user is None:
            arguments.user = input(f'Digite o nome do usuario: ')
        arguments.password = getpass.getpass(f'Digite a senha para o Usuario {arguments.user}:  ')

    #if port is none
    if arguments.port is None:
        arguments.port = '5432'

    #if host is none
    if arguments.host is None:
        arguments.host = 'localhost'


    #In case the the parameters -f/--file is passed, is necessary to use the file
    if arguments.table is None and arguments.file is not None:
        #Open file location
        with open(arguments.file, 'r') as f:
            file = json.loads(f.read())

        #Verificar se a tarefa é Import ou Export
        if arguments.function == 'Import':
            path_file = [x for x in file.get('path') if x != None]
            tablenames = [x for x in file.get('tables') if x != None]


            tablePath_dir = {}
            # Verifica se as listas têm o mesmo tamanho
            if len(path_file) == len(tablenames):
                #Criar um dicionario com o caminho e o nome da tabela
                for i in range(len(path_file)):
                    tablePath_dir[path_file[i]] = tablenames[i]
            else:
                raise err.FormationError


            #Create object and execute
            for path in tablePath_dir:
                print(f'Creating Table: {tablePath_dir[path]}')

                #Setting table name
                arguments.table = tablePath_dir[path]

                #Creating Object
                tableObj = Table(host=arguments.host, port=arguments.port, database=arguments.database, user= arguments.user , password= arguments.password, tablename=arguments.table, path=path)
                print(tableObj.__str__())
                execute.executeImportantion(tableObj.__connect__(),tableObj,format=arguments.drive)
                sleep(3)

        else:
            tablenames = [x for x in file.get('tables') if x != None]

            #Create object and execute
            for table in tablenames:
                print(table)
                #Setting
                arguments.table = table

                #Creating Object
                tableObj = Table(host=arguments.host, port=arguments.port, database=arguments.database, user= arguments.user , password= arguments.password, tablename=arguments.table)
                print(tableObj.__str__())
                #Execute
                execute.executeExportation(coordenate=arguments.t_srs,connection=tableObj.__connect__(),tableClass=tableObj,format=arguments.drive)
                sleep(3)


    else:
        if arguments.function == 'Import':
            pass
        else:
            pass
        tableObj = Table(host=arguments.host, port=arguments.port, database=arguments.database, user= arguments.user , password= arguments.password, tablename=arguments.table)
        print(tableObj.__str__())
        execute.executeExportation(coordenate=arguments.t_srs,connection=tableObj.__connect__(),tableClass=tableObj,format=arguments.drive)




if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
