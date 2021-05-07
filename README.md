Pruebas con tabula y pdftotext para la extracción de 
datos del pdf seleccionable.

### Dataset
#
https://data.controlciudadanopy.org/policianacional/

### Formato: documentos a ser analizados
#
downloadDate(%y-%MM-%dd)_hashDocument_salarios_*.pdf

### Dependencias
#
- https://pypi.org/project/tabula-py/
- https://pypi.org/project/pdftotext/
- pdfseparate

### TODO
#
- Evaluar resultados sobre el pdf seleccionable con:
    - https://github.com/pdfminer/pdfminer.six
    - https://github.com/camelot-dev/camelot
- Probar con AWS Textract
- Parsear resultados por página
