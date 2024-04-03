# Minuterie et chronomètre simples pour NVDA ${addon_version}

Fournit des fonctionnalités de minuterie et de chronomètre directement  pour NVDA

## Télécharger

Télécharger l'extension [Minuterie et chronomètre simples pour NVDA ${addon_version}](${addon_url}/releases/download/${addon_version}/${addon_name}-${addon_version}.nvda-addon)

## Minuterie et chronomètre

Une minuterie commence un compte à rebours à partir d'un temps spécifié jusqu'à 0. Lorsqu'il atteint 0, il est terminé et une alarme est émise.

Un chronomètre commence un compte a partir de 0 et continue jusqu'à ce qu'il soit indiqué qu'il s'arrête. Lorsque cela se produit, le temps écoulé est affiché.

## Caractéristiques

### Dialogue de paramètres simples

Une minuterie ou un chronomètre peut être configuré à partir d'un  dialogue de paramètres simples.

Les différentes indications de surveillance de progrès peuvent également être configurés à partir de la même boîte de dialogue.

#### Comment ça marche?

Utiliser le sous-menu "Paramètres de la minuterie pour NVDA" ou appuyer sur NVDA + Shift + t pour ouvrir le dialogue de paramètres de l'extension.
Le sous-menu peut être trouvé dans le menu "Outils" de NVDA.

* S'il y a une minuterie ou un chronomètre en cours d'exécution, vous pouvez:
    * Surveiller le progrès en lisant la barre d'état du dialogue de paramètres.
    * Mettre en pause, reprendre ou arrêter la minuterie  ou le chronomètre.
* Si la minuterie ou le chronomètre sont arrêtés, vous pouvez:
    * Configurer le mode d'exécution (minuterie ou chronomètre )
    * Configurer l'unité de temps utilisée pour le temps initial pour la minuterie et aussi pour l'indication (secondes, minutes ou heures)
    * Démarrer la minuterie ou le chronomètre.
* À tout moment, vous pouvez:
    * Choisir si le progrès est indiqué avec la voix, bips, les deux ou aucun.

### Exécuter à partir de commandes NVDA

À tout moment, il est possible de démarrer, d'arrêter, de mettre en pause, de reprendre et d'obtenir les indications de progrès à partir d'une minuterie ou d'un chronomètre sans ouvrir le dialogue de paramètres.

#### Comment ça marche?

* Appuyer sur ctrl + shift + NVDA + s pour démarrer ou arrêter la minuterie ou le chronomètre.
    * S'il n'y a pas de minuterie ou de chronomètre en cours d'exécution, l'un d'entre eux  démarrera, selon le mode de configuration actuel.
    * Si l'un d'entre eux est en cours d'exécution, il s'arrêtera. Le temps écoulé sera annoncé si une minuterie a été arrêtée.
    * Si une minuterie tente d'être démarrée et qu'il n'y a pas de valeur initiale de temps configurée, un avertissement est émis.
* Appuyer sur ctrl + shift + NVDA + p pour mettre en pause ou reprendre une minuterie ou un chronomètre.
* Appuyer sur ctrl + shift + NVDA + r pour vérifier le progrès d'une minuterie ou un chronomètre. Ceci est particulièrement utile si toutes les indications de progrès sont désactivés et il est nécessaire de consulter le progrès à la demande.

### Écrivant le temps

Dans le dialogue de paramètres, le temps initial pour la minuterie est entrée au format HH:MM:SS, où  HH ça veut dire heures, MM minutes et SS secondes.

Il n'est pas nécessaire d'écrire le format complet, le système le déduira:

* Si un numéro simple est écrit, l'unité de temps configurée sera utilisée.
* Si les sous unités sont spécifiées, ils seront pris en compte. Par exemple, 01:05 devient une minute et cinq secondes, si l'unité de temps sélectionnée est "minutes".
Si l'unité de temps sélectionnée est "heures", 01:05 devient une heure, cinq minutes et zéro secondes.
* Les sous unités inférieures aux "secondes" sont invalides. Si l'unité de temps est "minutes", ", la valeur 01:05:02 ne sera pas acceptée.

### Exécutant minuteries et chronomètres

Un seul minuteur ou chronomètre peut être démarré à la fois.

Le progrès peut  être surveillé en activant aucune, une ou plusieurs des indications, en lisant la barre d'état du dialogue de paramètres ou en appuyant sur la commande NVDA pour l'indication de progrès, ctrl+shift+NVDA+r.

Ainsi, il est parfaitement possible d'activer une minuterie ou un chronomètre en maintenant toutes les indications désactivés et surveillez le progrès en lisant la barre d'état lorsque le dialogue de paramètres est ouvert.

Les commandes pour démarrer, arrêter, pause, reprendre et obtenir une indication de progrès à la demande peuvent être utilisées même si le dialogue de paramètres est actif.

Il ne peut y avoir qu'un dialogue de paramètres ouverts. S'il y a une minuterie ou un chronomètre en cours d'exécution lorsque le dialogue est fermé, l'exécution se poursuivra normalement.

Si le dialogue de paramètres est ouvert lorsqu'une minuterie ou un chronomètre est en cours d'exécution, les informations mises à jour seront affichées en conséquence.

### Précision du temps

Cette extension n'est pas capable de compter le temps de manière extrêmement précise.

Cela se produit parce que Python, le langage de programmation dans lequel NVDA est écrit, n'est pas capable d'exécuter plus d'une instruction en même temps, même lorsqu'il y a plus d'un processeur ou d'un noyau de processeur disponible sur l'ordinateur.

Donc, chaque fois que NVDA verbalise, calcule ou traite quelque chose, un petit retard est inséré dans le décompte du temps.

La précision devrait toutefois être suffisamment acceptable pour la grande majorité des situations, sauf si la précision au niveau des millisecondes est requise ou si une imprécision entraîne un impact grave sur un processus.

Pour de meilleurs résultats, les indications de progrès doivent être conservées désactivés et un progrès doit être sollicités à la demande à l'aide de la commande NVDA pour l'indication de progrès, ctrl+shift+NVDA+r, ou en lisant la barre d'état du dialogue de paramètres.

### Indications de progrès

#### Indication par son

Lorsqu'il est actif, cette indication émet un bip à chaque fois que le comptage  du temps de la minuterie ou du chronomètre atteint une valeur ronde, en fonction de l'unité de temps configurée dans le dialogue de paramètres.

Si, par exemple, vous avez configuré une minuterie pour démarrer dans 02:30 minutes, un bip sera émis lorsque le comptage  est sur 02:00 minutes et un autre lorsque le comptage   est sur 01:00 minute.

Vous pouvez consulter le comptage exacte du temps à tout moment en lisant la barre d'état du dialogue de paramètres ou en utilisant la commande NVDA pour l'indication de progrès, ctrl+shift+NVDA+r.

#### Indication par parole

Lorsqu'il est actif, cette indication verbalise le temps  actuel à chaque fois que le comptage  du temps atteint une valeur ronde, en fonction de l'unité de temps configurée dans le dialogue de paramètres.

Si, par exemple, vous avez configuré une minuterie pour démarrer dans 02:30 minutes, "2" sera verbalisé lorsque le comptage  est sur 02:00 minutes et "1" sera verbalisé lorsque le comptage   est sur 01:00 minute.

Vous pouvez consulter le comptage exacte du temps à tout moment en lisant la barre d'état du dialogue de paramètres ou en utilisant la commande NVDA pour l'indication de progrès, ctrl+shift+NVDA+r.

### Indication d'achèvement de la minuterie

Lorsque le comptage du temps pour une minuterie atteint 0,  la minuterie est terminée. Cet événement est signalé, quelle que soit  le dialogue  de paramètres actif, avec un son d'alarme d'horloge discret. Ce son ne dépend de aucune indication de progrès active.

### Indication d'achèvement du chronomètre

Lorsque le chronomètre est arrêté, le temps écoulé est annoncé de manière indépendante du dialogue  de paramètres actif.

Le temps écoulé de la dernière exécution du chronomètre peut être consultée à tout moment en examinant la barre d'état du dialogue de paramètres ou en appuyant sur NVDA+ctrl+shift+r. Ces informations sont réinitialisées lorsqu'une nouvelle minuterie ou un nouveau chronomètre est démarré.

### Modifier les gestes de commandes

Dans le menu NVDA / Préférences / Gestes de commandes / Minuterie pour NVDA nous pouvons modifier  un geste de commande c'est-à-dire des combinaisons de touches aux commandes existantes assignées par défaut.

Rappelez-vous que la combinaison de touches ne soit pas assignée  à une autre fonction ou ne se chevauchent pas avec l'une des applications que nous utilisons.

# aidant à traduire ou à développer l'extension

Si vous voulez aider à traduire ou à développer l'extension, s'il vous plaît accéder au [dépôt du projet](${addon_url}) et recherchez le fichier contributing.md dans le répertoire de documentation équivalent à votre langue.

## Contributeurs

Remerciement spécial à

*  Marlon Brandão de Sousa - Traduction Portugais Brésil
* Ângelo Miguel Abrantes - Traduction Portugais Portugal
* Tarik Hadžirović - Traduction Croate
* Rémy Ruiz - Traduction Français
* Rémy Ruiz - Traduction Espagnol
* Umut KORKMAZ - Traduction turc
* Danil Kostenkov - Traduction Russe
* Heorhii - Traduction ukrainienne
* Brian Missao da Vera - Compatibilité NVDA 2022.1
* Edilberto Fonseca - Compatibilité NVDA 2022.1
