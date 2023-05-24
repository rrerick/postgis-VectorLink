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

        #Create object and execute
        for tablename in file.get('tables'):
            arguments.table = tablename
            exampleTable = Table(host=arguments.host, port=arguments.port, database=arguments.database, user= arguments.user , password= arguments.password, tablename=arguments.table)
            print(exampleTable.__str__())
            execute.executeExportation(exampleTable.__connect__(),exampleTable)
            sleep(3)
    else:
        exampleTable = Table(host=arguments.host, port=arguments.port, database=arguments.database, user= arguments.user , password= arguments.password, tablename=arguments.table)
        print(exampleTable.__str__())
        execute.executeExportation(exampleTable.__connect__(),exampleTable)




if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
