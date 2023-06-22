# Trabajo Práctico 2 - Algoritmo Genético

En este TP se explora la implementacion de un algoritmo genético, con el uso de diversos metodos
de cruza, mutación y seleccion.

## Dependencias

- Python **>= 3.11**
- Pipenv

## Set up

Primero se deben descargar las dependencias a usar en el programa. Para ello podemos hacer uso de los archivos _Pipfile_ y _Pipfile.lock_ provistos, que ya las tienen detalladas. Para usarlos se debe correr en la carpeta del TP1:

```bash
$> pipenv shell
$> pipenv install
```

Esto creará un nuevo entorno virtual, en el que se instalarán las dependencias a usar, que luego se borrarán una vez se cierre el entorno.

**NOTA:** Previo a la instalación se debe tener descargado **python** y **pipenv**, pero se omite dicho paso en esta instalación.

## Cómo Correr

Utilizando python se debera ejecutar el main.py con el siguiente flag que indica el nombre del archivo de salida:
**i**: para especificar la implementacion
**c**: para especificar el metodo de cruza
**m**: para especificar el metodo de mutacion
**s**: para especificar el metodo de seleccion
default(sin flag): sin especificación en el nombre del archivo de salida

```bash
python main.py i|c|m|s
```

## Archivo de Configuración:

### Configuraciones Basicas

**Nota: opción_a | opción_b | opción_c representa un parámetro que puede tomar únicamente esas opciones**

```json5
{
  palette: [
    [200, 200, 200],
    [25, 100, 233],
    [155, 155, 0],
    [45, 90, 150],
    [200, 45, 200],
  ],
  color_objective: [225, 23, 232],
  selections: {
    parents: {
      name: "elite|roulette|universal|deterministic_tournament",
      amount: 250,
    },
    new_gen: {
      name: "elite|roulette|universal|deterministic_tournament",
      amount: 250,
    },
  },
  max_population_size: 500,
  max_generations: 200,
  cross_over: { name: "one_point|uniform", probability: 0.95 },
  mutation: { name: "limited|complete", probability: 0.25 , "amount": 2},
  implementation: "use_all|new_over_actual",
  runs: 10,
}
```

### Archivos de salida

Los archivos de salida son estadísticas en formato `.csv`, que se encuentran en la carpeta `results` donde, segun el flag que le pasemos al main.py, se generara un directorio con el nombre del archivo especificado. En caso de no especificar un flag, se generara un archivo con el nombre `other.csv`.

##### Ejemplos de archivos de salida

Estas corresponden con los archivos de salida de los siguientes comandos:

```bash
1. python main.py
2. python main.py i
3. python main.py c
4. python main.py m
5. python main.py s
```

```bash
1. results/other.csv
2. resultus/implementations/use_all.csv
3. results/crosses/one_point-0.5.csv
4. results/mutations/limited-0.5.csv
5. results/selections/elite-50_roulette-50.csv
```

Estas estadísticas pueden ser luego visualizadas corriendo el script **graphs.py**, que genera gráficos sobre

- use_all vs new_over_actual
- deterministico vs probabilistico
- variacion en la cantidad de hijos
