# Temporizador e cronómetro simples para o NVDA ${addon_version}

Fornece implementações de temporizador e cronómetro directamente para o NVDA

## Download

Baixe o [extra temporizador e cronómetro simples para NVDA ${addon_version}](${addon_url}/releases/download/${addon_version}/${addon_name}-${addon_version}.nvda-addon)

## Temporizadores e cronómetros

Um temporizador inicia uma contagem regressiva a partir de um tempo inicial determinado.

Um cronómetro inicia uma contagem a partir do 0 e continua até que seja instruído a parar. Quando isso acontece, o tempo total é mostrado.

## Recursos

### Diálogo simples de configurações

Um temporizador ou um cronómetro podem ser configurados a partir de um diálogo simples de configurações.

Neste diálogo, Também podem ser configuradas as diferentes indicações de progresso.

#### Como funciona

Use o submenu  "Configurações do temporizador para o NVDA" ou pressione  NVDA + Shift + t Para abrir o diálogo de configurações do extra.
O submenu pode ser encontrado no menu "ferramentas" do NVDA.

* Se existir um cronómetro ou um temporizador em andamento, pode:
    * Monitorizar o progresso lendo a barra de estado do diálogo.
    * Pausar, continuar ou parar o temporizador ou cronómetro.
* Se nenhum temporizador ou cronómetro estiver em amdanento, pode:
    * Configurar o tipo de operação (temporizador ou cronómetro)
    * Configurar a unidade de tempo usada para tempo inicial de temporizador e também para indicação de (segundos, minutos ou horas)
    * Iniciar o temporizador ou cronómetro
* A qualquer momento, pode:
    * Escolher se o progresso é indicado via áudio, voz, ambos ou nenhum.

### Executar a partir de comandos do NVDA

A qualquer momento, é possível iniciar, parar, pausar, continuar e obter indicações de progresso     de um temporizador ou cronómetro sem abrir o diálogo de configurações.

#### Como funciona

* Pressione ctrl + shift + NVDA + s para iniciar ou parar um temporizador ou cronómetro.
    * Se nenhum temporizador ou cronómetro estiver activo, um deles iniciará, respeitando o modo de operação configurado.
    * Se algum deles estiver activo, irá parar. O tempo decorrido será anunciado, caso um cronómetro tenha sido parado.
    * Caso um temporizador tente ser iniciado e não exista um valor de tempo inicial configurado, um aviso é emitido.
* Pressione ctrl + shift + NVDA + p para pausar ou continuar um temporizador ou cronómetro.
* Pressione ctrl + shift + NVDA + r para verificar o progresso de um temporizador ou cronómetro. Isto é especialmente útil se todas as indicações de progresso estiverem desligadas e for necessário consultar o progresso sob demanda.

### Escrever tempo

No diálogo de configurações, o tempo inicial para temporizador é escrito no formato HH:MM:SS, onde HH significa horas, MM minutos e SS segundos.

Não é necessário escrever o formato completo, o sistema irá deduzí-lo:

* Se um número simples for escrito, a unidade de tempo configurada será usada.
* Se alguma sub unidade for especificada, ela será considerada. Por exemplo, 01:05 significa um minuto  e cinco segundos, se a unidade de tempo seleccionada for "minutos".
Se for "horas", 01:05 significa uma hora, cinco minutos e zero segundos.
* sub unidades abaixo de "segundos" são inválidas. Se a unidade de tempo for "minutos", o valor 01:05:02 não será aceite.

### Executar timers e cronômetros

Apenas um temporizador ou cronómetro pode ser executado de cada vez.

O progresso pode ser monitorizado habilitando-se nenhuma, uma ou mais de uma das indicações, lendo-se a barra de estado do diálogo de configurações ou pressionando-se o comando do NVDA para indicação de progresso , ctrl+shift+NVDA+r.

Assim, é perfeitamente possível activar um temporizador ou um cronómetro mantendo todas as indicações desligadas e monitorizar o seu progresso através da barra de estado do diálogo de configurações.

Comandos para iniciar, parar, pausar, continuar e obter indicação de progresso sob demanda podem ser usados mesmo se o diálogo de configurações estiver activo.

Pode existir apenas um diálogo de configurações aberto. Se houver um temporizador ou cronómetro activo, quando o diálogo for fechado, a operação continuará normalmente.

Se o diálogo de configurações for aberto enquanto um temporizador ou cronómetro estiver activo, as informações actualizadas serão mostradas.

### Precisão do tempo

Este extra não é capaz de contar o tempo de maneira extremamente precisa.

Isto acontece porque o Python, a linguagem de programação na qual o NVDA é escrito, não é capaz de executar mais de uma instrução ao mesmo tempo, mesmo quando existe mais de um processador ou núcleo de processador disponível no computador.

Assim, toda vez que o NVDA fala, calcula ou processa algo, um pequeno atrazo é inserido na contagem do tempo.

A precisão, entretanto, deve ser suficientemente aceitável para a vasta maioria das situações, excepto se uma precisão a nível de milissegundos for necessária ou se qualquer imprecisão causar um impacto severo em algum processo.

Para melhores resultados, as indicações de progresso devem ser manmtidas desligadas e o progresso deve ser solicitado sob demanda usando-se o comando do NVDA para indicação de progresso , ctrl+shift+NVDA+r, ou lendo-se a barra de estado do diálogo de configuração.

### Indicações de progresso

#### Indicação por áudio

Quando activa, esta indicação emite um bipe toda vez que a contagem de tempo do temporizador ou cronómetro atinge um valor cheio, de acordo com a cunidade de tempo especificada através do diálogo de configurações. 

Se, por exemplo, configurar um temporizador para iniciar em 02:30 minutos, um bipe irá tocar quando a contagem estiver em 02:00 minutos e um outro quando a contagem estiver em 01:00 minuto.

Pode consultar a contagem exacta de tempo a qualquer momento, lendo a barra de estado do diálogo de configurações ou usando o comando do NVDA para indicação de progresso , ctrl+shift+NVDA+r

#### Indicação por voz

Quando activa, esta indicação  informa a contagem de tempo toda vez que esta atinge um valor cheio, de acordo com a unidade de tempo especificada através do diálogo de configurações. 

Se, por exemplo, configurar um temporizador para iniciar em 02:30 minutos, "2" será falado quando a contagem estiver em 02:00 minutos e "1" será falado quando a contagem estiver em 01:00 minuto.

Pode consultar a contagem exacta de tempo a qualquer momento, lendo a barra de estado do diálogo de configurações ou usando o comando do NVDA para indicação de progresso , ctrl+shift+NVDA+r

### Indicação de completude do temporizador

Quando a contagem de tempo para um temporizador atinge 0, o temporizador está completo. Este evento é sinalizado, independentemente de o diálogo de configuração estar aberto, com um discreto som de alarme de relógio. Este som não depende de nenhuma indicação estar activa.

### Indicação de completude do cronómetro

Quando o cronómetro é parado, o tempo decorrido é anunciado, independentemente do diálogo de configuração estar aberto.

O tempo decorrido relativo ao último cronómetro executado pode ser consultado a qualquer momento revendo-se a barra de status do diálogo de configurações ou pressionando-se ctrl+shift+NVDA+R. Esta informação fica disponível até que um novo temporizador ou cronómetro seja iniciado.

### modificar os comandos

Você pode modificar todos os comandos de teclado atribuídos a funções deste extra acessando a secção "Temporizador para o NVDA" do diálogo de definição de comandos, disponível através do menu NVDA / configurações / definir comandos.

Se for modificar algum comando, lembre-se de escolher combinações que não estejam em uso por comandos atuais do NVDA ou de outros extras, para que conflitos não ocorram.

# ajudar a traduzir ou desenvolver o extra

Se quiser ajudar a traduzir ou a desenvolver o extra, aceda o [repositório do projecto](${addon_url}) e procure pelo arquivo contributing.md no diretório de documentação equivalente ao seu idioma ou no diretório do idioma Inglês.

## Colaboradores

Agradecimentos a:

* Marlon Brandão de Sousa - tradução para Português do Brasil
* Ângelo Miguel Abrantes - Tradução para Português
* Tarik Hadžirović - Tradução para Croata
* Rémy Ruiz - Tradução para Francês
* Rémy Ruiz - Tradução para Espanhol
* Umut KORKMAZ - tradução para Turco
* Danil Kostenkov - tradução para Russo
* Heorhii - tradução para Ucraniano
* Brian Missao da Vera - Compatibilidade com NVDA 2022.1
* Edilberto Fonseca - Compatibilidade com NVDA 2024.1
