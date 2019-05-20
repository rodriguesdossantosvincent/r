# Accès

Démarrage de l'environnement :
https://mybinder.org/v2/gh/rodriguesdossantosvincent/r/master


Démarrage de l'environnement en pointant directement sur RStudio : 
https://mybinder.org/v2/gh/rodriguesdossantosvincent/r/master?urlpath=rstudio

Démarrage de l'environnement en pointant directement sur RStudio : 
https://mybinder.org/v2/gh/rodriguesdossantosvincent/r/master?urlpath=shiny/bus-dashboard/

Démarrage de l'environnement en pointant directement sur Dash : 
https://mybinder.org/v2/gh/rodriguesdossantosvincent/r/master?urlpath=proxy/8050


| **Url**  | **Nom**  |
| -------- | -------- |
| /tree    | Notebook |
| /rstudio | RStudio  |
| /rshiny/bus-dashboard  | RShiny   |
| /tree    | Notebook |

# Test d'utilisation

## Installation d'un nouveau dash RShiny avec installation de nouveaux paquets R

Cela est simple.

Depuis **Notebook - /tree**, créer un nouveau dossier, par exemple **crandash** et déposez-y les fichiers R de votre dashboard RShiny.

Connectez-vous sur **RStudio - /rstudio** et lancez les installations des paquets directement dans la console, par exemple :
```bash
install.packages(c("dplyr", "htmlwidgets", "digest", "bit"))
devtools::install_github("jcheng5/bubbles")
devtools::install_github("hadley/shinySignals")
```

Connectez-vous enfin sur votre Dash directement via l'url **/shiny/crandash**.

Un fichier log est créé afin de vous aider en cas d'erreur, accessible depuis **Notebook - /tree/logs**.

## Installation d'un nouveau dash Dash en plus de celui existant 




# Divers

jupyter serverextension list
jupyter serverextension disable --sys-prefix dashserverextension
jupyter serverextension enable --sys-prefix dashserverextension