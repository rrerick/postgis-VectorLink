from osgeo import gdal
import config.exceptions as err
import os
import re
from pathlib import Path

def executeExportation(connection:str=None,tableClass:object=None):
    """_summary_
    """

    if connection is None:
        raise err.ExecutionFailed

 
    tablename = str(tableClass.__getattribute__("tablename"))
    tablename = re.sub(r'[a-z]*\.',"",tablename)

    export_path = os.path.join(Path.home(),'script_ExportTables_Result/')

    try:
        os.mkdir(export_path)
    except FileExistsError:
        print("Pasta Já Criada")
    finally:
        export_path = os.path.join(export_path,tablename+'.gpkg')
        ogr2ogr_comand = f'ogr2ogr -f "GPKG" "{export_path}" -nln "{tablename}" -skipfailures PG:{connection} {tableClass.__getattribute__("tablename")}'
        os.system(ogr2ogr_comand)

