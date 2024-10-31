#Creamos un entorno virtual e instalamos FastAPI

Siguiendo la documentación de Python (que previamente debemos tener instalado), creamos un entorno virtual desde un terminal con las siguientes instroducciones:

```
mkdir proyecto
cd proyecto
python3 -m venv .venv
#Para Windows bash:
source .venv/Scripts/activate
#Para linux/MacOS:
source .venv/bin/activate
pip install fastapi
```

#Iniciamos y probamos el endpoint

Junto a la carpeta que hemos creado en el punto anterior, añadimos el main.py antes de escribir el siguiente código en el terminal:

```
cd ../
fastapi dev main.py
```

Tras haces esto, nos mostrará dos direcciones IPs. Si abrimos en nuestro navegador con la IP de la documentación, podemos ver los valores requeridos para el endpoint. Si pulsamos en el botón de "Try it out", se pueden modificar los parámetros. Al pegar el contenido del json que hay subido, se puede ver el resultado tras ejecutarlo. 






