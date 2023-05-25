# postgis-VectorLink
Python Script to export Postgis tables using GDAL



## Requirements

GDAL/OGR: https://mothergeo-py.readthedocs.io/en/latest/development/how-to/gdal-ubuntu-pkg.html

## Configuration

1. Put this Repo in a good location in your computer and get the repo location
2. First configure the programm in ~/.bashrc
  * The repo location getting on step 1, switch in "/path/to/dir/"
```

echo export PATH=/path/to/dir/:PATH >> ~/.bashrc

```

3. Execute:

``` 
source ~/.bashrc
```

## Execution
```

VectorLink.py [-h/--help] [-u/--user] [-w/--password] [-H/--host] [-p/--port] [-d/--database] [-t/--table] 
              [-f/--file] [-F/--function] [-n/--new] [-y/--drive] [t_srs]

```

* -h/--help : Manual    
* -u/--user : Database username
*  -w/--password : Database username's password
*  -H/--host : Ip/ Host ( Default 'localhost' ) 
*  -p/--port : Database Port ( Default: 5432)
*  -d/--database : Database Name  -- -- **mandatory**
*  -t/--table : "schema.table" to Export 
*  -n/--new : "schema.table" name to Import
*  -f/--file : "example.json" If you want to export or import many tables, use this parameter with the path of .json file
* -F/--function : ['Export' / 'Import'] -- -- **mandatory** 
* -y/--drive : [ 'GPKG'/ 'GEOJSON' ] In Export Functions set the file data type  -- -- **mandatory**
* -t_srs : System Reference ( Default : 'EPSG:4674' ) 
  
## Important :triangular_flag_on_post:	
  
*1. Import/Export Many files in one execution:*
  
  
>The file is the same of example.json, but can be anywhere on your machine

  





