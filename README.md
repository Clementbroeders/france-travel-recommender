# France Travel Recommander

<img src="img/image.jpg" alt="Image" width="50%" height="50%">


## Introduction

Après avoir effectué des recherches auprès des utilisateurs, l'équipe marketing de France Travel Recommender a découvert que **70 % de leurs utilisateurs planifiant un voyage souhaiteraient obtenir plus d'informations sur leur destination.**

De plus, la recherche utilisateur montre que **les gens ont tendance à être méfiants à l'égard des informations qu'ils lisent s'ils ne connaissent pas la marque** qui a produit le contenu.

Par conséquent, France Travel Recommender vous aidera à savoir où les gens devraient planifier leurs prochaines vacances. L'application est basée sur des données réelles concernant :

* La météo
* Les hôtels dans la région

Le notebook recommande les meilleures destinations et hôtels en fonction des variables ci-dessus à tout moment.


## Clone du repo

Pour cloner le repo, utilisez la commande suivante :

```
git clone https://github.com/Clementbroeders/france-travel-recommender.git
```


## Comment ça marche ?

France Travel Recommender récupère les données à partir de 3 sources :

1) API - Nominatim.org

    Récupération des coordonnées de longitude et de latitude pour chaque ville.

2) API - openweathermap.org

    Récupération des prévisions météorologiques pour chaque ville pour les 5 prochains jours.

3) Scraping - booking.com

    Récupération des données d'hôtel pour chaque ville.

Toutes les données sont compilées dans ce notebook, et le résultat est une carte interactive des 20 meilleurs hôtels dans les 5 villes sélectionnées.

Vous pouvez voir l'exemple en lançant le fichier html suivant : `plotly/example.html`


## Etapes

1) Tout d'abord, vous devez ouvrir src/list_cities.csv et y inscrire la liste des villes que vous souhaitez vérifier, une ville par ligne.

2) Assurez-vous que toutes les bibliothèques nécessaires sont installées dans votre environnement en exécutant la commande suivante depuis le terminal ou l'invite de commandes :

    `pip install -r requirements.txt`

3) Lancez le notebook et exécutez toutes les cellules jusqu'à la fin. La partie scraping peut rencontrer des échecs en raison des changements fréquents sur le site web de booking.com. N'hésitez pas à mettre à jour les scripts Scrapy en conséquence.


### OPTIONNEL

4) Si vous souhaitez vous connecter à votre AWS S3, configurez boto3 en conséquence.

5) Si vous souhaitez vous connecter à votre AWS RDS, assurez-vous que les variables d'environnement sont définies ou modifiez les variables directement dans le carnet de notes.