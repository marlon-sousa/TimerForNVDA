# Timer e cronômetro simples para NVDA ${addon_version}

Provê implementações de timer e cronômetro diretamente para o NVDA

## Download

Baixe o [complemento Timer e cronômetro simples para NVDA ${addon_version}](${addon_url}/releases/download/${addon_version}/${addon_name}-${addon_version}.nvda-addon)

## Timers e cronômetros

Um timer inicia uma contagem regressiva a partir de um tempo inicial determinado.

Um cronômetro inicia uma contagem a partir do 0 e continua até que seja instruído a parar. Quando isso acontece, o tempo total é exibido.

## Recursos

### Diálogo simples de configurações

Um timer ou um cronômetro podem ser configurados a partir de um diálogo simples de configurações.

Neste mesmo diálogo, Também podem ser configurados diferentes relatórios de progresso.

#### Como funciona

Use o submenu  "Configurações do complemento Timer para NVDA" ou pressione  NVDA + Shift + t Para abrir o diálogo de configurações do complemento.
O submenu pode ser encontrado no menu "ferramentas" do NVDA.

* Se existir um cronômetro ou um timer em andamento, você pode:
    * Monitorar o progresso lendo a barra de status do diálogo.
    * Pausar, continuar ou parar o timer ou cronômetro.
* Se nenhum timer ou cronômetro estiver em amdanento, você pode:
    * Configurar o tipo de operação (timer ou cronômetro)
    * Configurar a unidade de tempo usada para tempo inicial de timer e também para relatório (segundos, minutos ou horas)
    * Iniciar o timer ou cronômetro
* A qualquer momento, você pode:
    * Escolher se o progresso é relatado via áudio, fala, ambos ou nenhum.

### Executar a partir de comandos do NVDA

A qualquer momento, é possível iniciar, parar, pausar, continuar e obter relatórios de progresso     de um timer ou cronômetro sem abrir o diálogo de configurações.

#### Como funciona

* Pressione ctrl + shift + NVDA + s para iniciar ou parar um timer ou cronômetro.
    * Se nenhum timer ou cronômetro estiverem em operação, um deles iniciará, respeitando o modo de operação configurado.
    * Se algum deles estiver em operação, ele irá parar. O tempo decorrido será anunciado, caso um cronômetro tenha sido parado.
    * Caso um timer tente ser iniciado e não exista um valor de tempo inicial configurado, um aviso é emitido.
* Pressione ctrl + shift + NVDA + p para pausar ou continuar um timer ou cronômetro.
* Pressione ctrl + shift + NVDA + r para checar o progresso de um timer ou cronômetro. Isso é especialmente útil se todos os relatórios de progresso estiverem desligados e for necessário consultar o progresso sob demanda.

### Escrevendo tempo

No diálogo de configurações, o tempo inicial para timer é escrito no formato HH:MM:SS, onde HH significa horas, MM minutos e SS segundos.

Não é necessário escrever o formato completo, o sistema irá deduzí-lo:

* Se um número simples for escrito, a unidade de tempo configurada será usada.
* Se alguma sub unidade for especificada, ela será considerada. Por exemplo, 01:05 significa um minuto  e cinco seconds, se a unidade de tempo selecionada for "minutos".
Se for "horas", 01:05 significa uma hora, cinco minutos e zero segundos.
* sub unidades abaixo de "segundos" são inválidas. Se a unidade de tempo for "minuts", o valor 01:05:02 não será aceito.

### Executando timers e cronômetros

Apenas um timer ou cronômetro pode ser executado por vez.

O progresso pode ser monitorado habilitando-se nenhum, um ou mais de um dos relatórios, lendo-se a barra de status do diálogo de configurações ou pressionando-se o comando do NVDA para relatório de progresso , ctrl+shift+NVDA+r.

Assim, é perfeitamente possível ativar um timer ou um cronômetro mantendo todos os relatórios desligados e monitorar seu progresso através da barra de status do diálogo de configurações.

Comandos para iniciar, parar, pausar, continuar e obter relatório de progresso sob demanda podem ser usados mesmo se o diálogo de configurações estiver ativo.

Pode existir apenas um diálogo de configurações aberto. Se houver um timer ou cronômetro em operação quando o diálogo for fechado, a operação continuará normalmente.

Se o diálogo de configurações for aberto enquanto um timer ou cronômetro estiver em operação, as informações atualizadas serão exibidas.

### Precisão do tempo

Este complemento não é capaz de contar o tempo de maneira extremamente precisa.

Isso acontece porquê Python, a linguagem de programação na qual o NVDA é escrito, não é capaz de executar mais de uma instrução ao mesmo tempo, mesmo quando existe mais de um processador ou núcleo de processador disponível no computador.

Assim, toda vez que o NVDA fala, calcula ou processa algo, um pequeno atrazo é inserido na contagem do tempo.

A precisão, entretanto, deve ser suficientemente aceitável para a vasta maioria das situações, exceto se uma precisão a nível de milissegundos for necessária ou se qualquer imprecisão causar um impacto severo em algum processo.

Para melhores resultados, relatórios de progresso devem ser manmtidos desligados e o progresso deve ser solicitado sob demanda usando-se o o comando do NVDA para relatório de progresso , ctrl+shift+NVDA+r, ou lendo-se a barra de status do diálogo de configuração.

### relatórios de progresso

#### Relatório por áudio

Quando ativo, este relatório emite um bipe toda vez que a contagem de tempo do timer ou cronômetro atinge um valor cheio, de acordo com a cunidade de tempo especificada através do diálogo de configurações. 

Se você, por exemplo, configurar um timer para iniciar em 02:30 minutos, um bipe irá tocar quando a contagem estiver em 02:00 minutos e um outro quando a contagem estiver em 01:00 minuto.

Você pode consultar a contagem exata de tempo a qualquer momento lendo a barra de status do diálogo de configurações ou usando o comando do NVDA para relatório de progresso , ctrl+shift+NVDA+r

#### Relatório por fala

Quando ativo, este relatório  informa a contagem de tempo toda vez que esta atinge um valor cheio, de acordo com a unidade de tempo especificada através do diálogo de configurações. 

Se você, por exemplo, configurar um timer para iniciar em 02:30 minutos, "2" será falado quando a contagem estiver em 02:00 minutos e "1" será falado quando a contagem estiver em 01:00 minuto.

Você pode consultar a contagem exata de tempo a qualquer momento lendo a barra de status do diálogo de configurações ou usando o comando do NVDA para relatório de progresso , ctrl+shift+NVDA+r

### relatório de completude do timer

Quando a contagem de tempo para um timer atinge 0, o timer está completo. Este evento é sinalizado, independentemente de o diálogo de configuração estar aberto, com um discreto som de alarme de relógio. Este som não depende de nenhumrelatório estar ativo.

### relatório de completude do cronômetro

Quando o cronômetro é parado, o tempo decorrido é anunciado, independentemente de o diálogo de configuração estar aberto.

O tempo decorrido relativo ao último cronômetro executado pode ser consultado a qualquer momento revendo-se a barra de status do diálogo de configurações ou pressionando-se ctrl+shift+NVDA+R. Esta informação fica disponível até que um novo timer ou cronômetro seja iniciado.

### modificar os comandos

Você pode modificar todos os comandos de teclado atribuídos a funções deste complemento acessando a seção "Timer para NVDA" do diálogo de definição de comandos, disponível através do menu NVDA / configurações / definir comandos.

Se for modificar algum comando, lembre-se de escolher combinações que não estejam em uso por comandos atuais do NVDA ou de outros complementos, para que conflitos não ocorram.

# ajudando a traduzir ou desenvolver o complemento

Se quiser ajudar a traduzir ou desenvolver o complemento, acesse o [repositório do projeto](${addon_url}) e busque pelo arquivo contributing.md no diretório de documentação equivalente ao seu idioma ou no diretório do idioma Inglês.

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
