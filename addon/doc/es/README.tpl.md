# Temporizador y cronómetro simples para NVDA ${addon_version}

Proporciona funcionalidades  de temporizador y de cronómetro directamente para NVDA

## Descargar

Descargar el complemento [Temporizador  y cronómetro simples para NVDA ${addon_version}](${addon_url}/releases/download/${addon_version}/${addon_name}-${addon_version}.nvda-addon)

## Temporizador y cronómetro

Un temporizador inicia un conteo regresivo desde un tiempo específico hasta 0. Cuando llega a 0, se termina y se emite una alarma.

Un cronómetro inicia un conteo de 0 y continúa hasta que se le indica que se detenga. Cuando esto sucede, se muestra el tiempo transcurrido.

## Características

### Diálogo de configuración simple

Un temporizador o un cronómetro puede configurarse desde un diálogo de configuración simple.

Las diferentes indicaciones de monitoreo de progreso también se pueden configurar desde el mismo diálogo.

#### ¿Como funciona?

Usa el submenú "Configuración del temporizador para NVDA" o pulsa NVDA + Shift + t para abrir el diálogo  de configuración del complemento.
El submenú se puede encontrar en el menú "Herramientas" de NVDA.

* Si hay un temporizador o un cronómetro en ejecución, puedes:
    * Monitorear el progreso al leer la barra de estado del diálogo de configuración.
    * Pausar, reanudar o detener el temporizador o cronómetro.
* Si se detiene el temporizador o el cronómetro, puedes:
    * Configurar el modo de ejecución (temporizador o cronómetro)
    * Configurar la unidad de tiempo utilizada para el tiempo inicial para el temporizador y también Para la indicación (segundos, minutos o horas)
    * Iniciar el temporizador o cronómetro.
* En cualquier momento, puedes:
    * Elegir si el progreso es indicado con voz, pitidos, ambos o ninguno.

### Ejecutar a partir de las órdenes de NVDA

En cualquier momento, es posible iniciar, detener, pausar, reanudar y obtener indicaciones de progreso desde un temporizador o cronómetro sin abrir el diálogo de configuración.

#### ¿Como funciona?

* Pulsar ctrl + shift + NVDA + s para iniciar o detener el temporizador o el cronómetro.
    * Si no hay temporizador ni cronómetro en ejecución, uno de ellos se iniciará según el modo de configuración actual.
    * Si uno  de ellos está en ejecución, se detendrá. Se anunciará el tiempo transcurrido si se ha detenido un temporizador.
    *     Si un temporizador intenta iniciarse y no hay un valor de tiempo inicial configurado, se emite una advertencia.
* Pulsar ctrl + shift + NVDA + p para pausar o reanudar un temporizador o cronómetro.
* Pulsar ctrl + shift + NVDA + r Para comprobar el progreso  del temporizador o del cronómetro. Esto es especialmente útil si todas las indicaciones de progreso están desactivados y es necesario consultar el progreso a la demanda.

### Escribiendo tiempo

En el diálogo de configuración, el tiempo inicial para el temporizador se ingresa en  formato HH:MM:SS, donde  HH significa horas, MM minutos y SS segundos.

No es necesario escribir el formato completo, el sistema lo deducirá:

* Si se escribe un número simple, se utilizará la unidad de tiempo configurada.
* Si se especifican sub unidades, se considerarán. Por ejemplo, 01:05 se convierte en un minuto y cinco segundos, si la unidad de tiempo seleccionada es  "minutos".
Si la unidad de tiempo seleccionada es "horas", 01:05 se convierte en una hora, cinco minutos y cero segundos.
* Las sub unidades debajo de "segundos" no son válidas. Si la unidad de tiempo es "minutos", el valor 01:05:02 no será aceptado.

### Ejecutando temporizadores y cronómetros

Solo se puede iniciar un temporizador o cronómetro a la vez.

El progreso puede ser monitoreado al habilitar ninguna, una o más indicaciones, leyendo la barra de estado  del diálogo de configuración o pulsando la órden de NVDA para la indicación de progreso, ctrl+shift+NVDA+r.

Por lo tanto, es perfectamente posible activar un temporizador o un cronómetro manteniendo todas las indicaciones desactivadas y monitorear el progreso leyendo la barra de estado cuando el diálogo  de configuración está abierto.

Las órdenes para iniciar, detener, pausar, reanudar y obtener una indicación de progreso a la demanda Se puede utilizar incluso cuando el  diálogo de configuración está activo.

Solo puede haber un diálogo de configuración abierto. Si hay un temporizador o un cronómetro en ejecución cuando el diálogo está cerrado, la ejecución continuará normalmente.

Si se abre el diálogo de configuración mientras un temporizador o un cronómetro está en ejecución, se mostrará la información actualizada en consecuencia.

### Precisión del tiempo

Este complemento no es capaz de contar el tiempo de manera extremadamente precisa.

Esto sucede porque Python, el lenguaje de programación en el que se escribe NVDA, no puede ejecutar más de una instrucción al mismo tiempo, incluso cuando hay más de un procesador o núcleo de procesador disponible en la computadora.

Entonces, cada vez que NVDA verbaliza, calcula o procesa algo, se inserta un pequeño retraso en el recuento de tiempo.

Sin embargo, la precisión debe ser lo suficientemente aceptable para la gran mayoría de las situaciones, excepto si se requiere precisión a nivel de milisegundos o si alguna imprecisión causa un impacto severo en algún proceso.

Para obtener los mejores resultados, las indicaciones de progreso deben mantenerse desactivadas y se debe solicitar un progreso a la demanda utilizando la órden de NVDA para la indicación de progreso, ctrl+shift+NVDA+r o leyendo la barra de estado del diálogo de configuración.

### Indicaciones de progreso

#### Indicación por sonido

Cuando está activo, esta indicación  emite un pitido cada vez que el conteo de tiempo del temporizador o del cronómetro alcanza un valor redondo, de acuerdo con la unidad de tiempo configurado en el diálogo de configuración.

Si por ejemplo, has configurado un temporizador para que se inicie  en 02:30 minutos, se reproducirá un pitido cuando el conteo se encuentra en 02:00 minutos y otro cuando el conteo se encuentra en 01:00 minuto.

Puedes consultar el conteo de tiempo exacto en cualquier momento leyendo la barra de estado del diálogo de configuración utilizando la órden de NVDA para la indicación de progreso, ctrl+shift+NVDA+r.

#### Indicación por voz

Cuando está activo, esta indicación verbaliza el conteo de tiempo  actual cada vez que alcanza un valor redondo, de acuerdo con la unidad de tiempo configurado en el diálogo de configuración.

Si por ejemplo, has configurado un temporizador para que se inicie  en 02:30 minutos, 2" se verbalizará cuando el conteo se encuentra en 02:00 minutos y "1" se verbalizará cuando el conteo se encuentra en 01:00 minuto.

Puedes consultar el conteo de tiempo exacto en cualquier momento leyendo la barra de estado del diálogo de configuración utilizando la órden de NVDA para la indicación de progreso, ctrl+shift+NVDA+r.

### Indicación de finalización del temporizador

Cuando el conteo de tiempo para un temporizador alcanza 0, el temporizador está completo. Este evento se señala, independientemente del diálogo de configuración  activo, con un sonido de alarma de reloj discreto. Este sonido no depende de ninguna indicación de progreso que está activo.

### Indicación de finalización del cronómetro

Cuando se detiene el cronómetro, se anuncia el tiempo transcurrido independientemente del diálogo de configuración activo.

El tiempo transcurrido de la última ejecución del cronómetro puede ser consultado en cualquier momento revisando la barra de estado del diálogo de configuración o pulsando NVDA+ctrl+shift+r. Esta información se restablece cuando se inicia un nuevo temporizador o cronómetro.

### Modificar los gestos de entrada

En el menú de NVDA / Preferencias / Gestos de entrada / Temporizador para NVDA podremos modificar un gesto de entrada es decir combinaciones de teclas a las órdenes existentes asignadas por defecto.

Acordaros que la combinación de teclas no este asignada para otra función o no se solape con alguna de las aplicaciones que usamos.

# ayudando a traducir o desarrollar el complemento

Si deseas ayudar a traducir o desarrollar el complemento, por favor  acceda al [repositório del proyecto](${addon_url}) y buscar el archivo contributing.md en el directorio de documentación equivalente a tu idioma.

## Contribuidores

Agradecimientos especiales a

*  Marlon Brandão de Sousa - Traducción Portugués del Brasil
* Ângelo Miguel Abrantes - Traducción Portugués
* Tarik Hadžirović - Traducción Croata
* Rémy Ruiz - Traducción Francés
* Rémy Ruiz - Traducción Español
* Umut KORKMAZ - Traducción turco
* Danil Kostenkov - Traducción Rusa
* Heorhii - Traducción ucraniano
* Brian Missao da Vera - Compatibilidad con NVDA 2022.1
* Edilberto Fonseca - Compatibilidad con NVDA 2024.1
