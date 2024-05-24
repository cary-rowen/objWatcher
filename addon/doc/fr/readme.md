# obj Watcher #

**Cette extension pour NVDA surveille les modifications apportées aux attributs des objets de navigation.**

* Auteur :: Cary-rowen <manchen_0528@outlook.com>, hwf1324
  <1398969445@qq.com>
* Compatibilité : NVDA-2023.1 ou version ultérieure

## Cas d'utilisation possibles

1. Affichez les sous-titres ou les paroles des chansons sur certains
   lecteurs et activez l'annonce automatique lors de leur mise à jour.
2. Affichez les éléments d'intérêt dans la liste d'une discussion de groupe
   Unigram ou dans la liste des conversations sur WeChat. Les nouveaux
   messages seront annoncés automatiquement et l'annonce en arrière-plan est
   prise en charge.
3. Juste à des fins de test, consultez également la barre d'état du
   Bloc-notes pour annoncer les lignes et les colonnes lors de l'insertion
   et de la suppression de contenu.

## Gestes

``Contrôle+NVDA+W`` : Appuyez une fois pour surveiller l'objet sous le
navigateur d'objets. Si l'objet actuel dans le navigateur d'objets est déjà
sous surveillance, l'attribut surveillé sera annoncé. Appuyez deux fois pour
arrêter la surveillance.

**Vous pouvez modifier ce geste à partir du dialogue Gestes de commandes.**

## Contributeurs

* Cary-rowen
* ibrahim hamadeh
* hwf1324

## Contribution

1. L'extension accueille les Pull Requests (PR) pour les nouvelles
   fonctionnalités et les traductions localisées sur [GitHub][GitHub].
2. Pour tout commentaire, veuillez le soumettre via un [GitHub
   Issue][GitHubIssue].

## Notes de version
### Version 0.4.4
* Mode de parole à la demande pris en charge sur NVDA2024.1.

### Version 0.4.3
* Compatible avec NVDA2024.1

### Version 0.4.2
* Ajout de la traduction ukrainienne par VovaMobile.

### Version 0.4.1
* Ajout de la traduction arabe par Ibrahim Hamadeh.

### Version 0.4.0
* L'intervalle de surveillance peut être défini dans le panneau des
  paramètres, la valeur par défaut est 100.

### Version 0.3.4
* Documentation améliorée.
* En appuyant deux fois rapidement sur le geste ne donne plus
  systématiquement la priorité à l'exécution de la première fonction lors
  d'un appui.

[[!tag dev stable]]

[GitHub]: https://github.com/cary-rowen/objWatcher [GitHubIssue]:
https://github.com/cary-rowen/objWatcher/issues

