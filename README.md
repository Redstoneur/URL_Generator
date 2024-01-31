# URL Generator

URL Generator est un petit programme Python 3.8 qui permet de convertir une URL en sa version encodée en pourcentage et de la copier dans le presse-papiers. Le programme offre deux modes d'utilisation : une interface graphique utilisateur (GUI) basée sur Tkinter et une interface en ligne de commande (CLI) utilisant argparse.

## Prérequis

- Python 3.8 ou version ultérieure
- Les modules Python standard : `argparse`, `tkinter`, `urllib`, `pyperclip`

## Utilisation

### Interface Graphique Utilisateur (GUI)

Pour lancer l'application en mode GUI, exécutez simplement le script sans aucun argument :

```bash
python main.py
```

Cela ouvrira une fenêtre où vous pourrez saisir l'URL à convertir.

### Interface en Ligne de Commande (CLI)

Pour utiliser l'application en mode CLI, vous pouvez spécifier l'option `-c` ou `--cli` pour activer le mode CLI. Vous pouvez également spécifier l'option `-u` ou `--url` pour fournir l'URL à convertir. Si aucune URL n'est spécifiée, le programme demandera à l'utilisateur de saisir l'URL à convertir :

```bash
python main.py -c
```

ou

```bash
python main.py -c -u "votre_url_ici"
```

Ceci convertira l'URL spécifiée en sa version encodée en pourcentage et la copiera dans le presse-papiers.

### Aide

Pour obtenir de l'aide sur les options de ligne de commande, vous pouvez utiliser l'option `-h` ou `--help` :

```bash
python main.py --help
```

Cela affichera une aide détaillée sur les options disponibles pour l'interface en ligne de commande.