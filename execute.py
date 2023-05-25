from osgeo import gdal
import config.exceptions as err
import os
import re
from pathlib import Path

def executeExportation(coordenate:str,format:str,connection:str=None,tableClass:object=None):
    """_summary_
    """

    if connection is None:
        raise err.ExecutionFailed

    if coordenate is None:
        coordenate='EPSG:4674'
    tablename = str(tableClass.__getattribute__("tablename"))
    tablename = re.sub(r'[a-z]*\.',"",tablename)

    export_path = os.path.join(Path.home(),'script_ExportTables_Result/')

    try:
        os.mkdir(export_path)
    except FileExistsError:
        print("Pasta Já Criada")
    finally:
        export_path = os.path.join(export_path,tablename+f'.{format.lower()}')
        ogr2ogr_comand = f'ogr2ogr -f "{format}" "{export_path}" -nln "{tablename}" -t_srs "{coordenate}"-skipfailures PG:"{connection}" {tableClass.__getattribute__("tablename")}'
        os.system(ogr2ogr_comand)


def executeImportantion(format:str,connection:str=None,tableClass:object=None):
    """

    Args:
        connection (str, optional): _description_. Defaults to None.
        TableClass (object, optional): _description_. Defaults to None.
    """

    if connection is None:
        raise err.ExecutionFailed

    #Separando o nome da tabela do nome do esquema
    tablename = tableClass.__getattribute__("tablename")
    schema_name = re.sub(r'\..*',"",tablename)
    tablename = re.sub(r'[a-z]*\.',"",tablename)

    #O caminho do arquivo no objeto não pode ser nulo
    if tableClass.__getattribute__("path") is None:
        raise err.NoFileLocation

    #Importando arquivo para o banco de dados
    ogr2ogr_comand = f'PGCLIENTENCODING=UTF-8 ogr2ogr -f "PostgreSQL" PG:"{connection} schemas={schema_name}" \
    -progress \
    -append \
    -t_srs EPSG:4674 \
    -lco GEOMETRY_NAME=geom \
    -lco FID=fid \
    -lco PRECISION=no \
    -nlt PROMOTE_TO_MULTI \
    {tableClass.__getattribute__("path")} -nln {tablename} -append'

    #Executa o comando
    os.system(ogr2ogr_comand)