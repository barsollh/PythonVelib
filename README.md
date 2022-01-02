Notre Dashboard a pour objectif de montrer le recouvrement des vélibs dans la ville de Paris et ses alentours. Notre map nous montre toutes les stations vélibs d’ile de France, chaque point représente une station et nous pouvons voir le nom de la station en survolant avec votre souris. Les couleurs vont de vert à rouge, vert étant là où il y a le moins de vélo disponible et rouge là où il y en a le plus. Plus un cercle est gros, plus la station a la capacité d’accueillir des vélos. Grâce à cette map nous pouvons voir que les stations vélibs sont plus remplies aux alentours de la Seine et au milieu de grandes villes de banlieue.

Le premier histogramme montre les nombres de vélos disponibles dans les stations. L'axe y représente le nombre de stations et l'axe x le nombre de vélos disponibles. On remarque que la majorité des stations n'ont que un ou aucun vélo disponible.  

Le second histogramme représente le nombre de station de vélos en fonction de leur capacité. On remarque que la capacité la plus fréquente est une capacité de 24 ou 25 vélos avec 133 stations. La moins fréquente capacité observée quant à elle est 74-75 vélos, en effet une seule station propose cette capacité.  

User Guide : Pour que le Dashboard fonctionne il faut avoir installé python et les scripts dash, pandas, folium, branca, plotly.express.
Avec la commande : pip install *elt*  
Exemple : pip install dash  
Il suffit d’ouvrir votre invité de commandes, vous mettre dans le répertoire ou le fichier python “main.py” est localisé. Lorsque vous etes dans le répertoire, tapez : python main.py  
Une phrase va être affichée, il suffit de cliquer sur l’URL pour être transféré sur la Dashboard.  
Dash is running on http://127.0.0.1:8050/

Developer Guide : Nous importons au début tous les packages utilisés puis nous ouvrons notre dossier CV grâce à pandas. Ensuite nous déclarons des listes qui vont être utiles à la création de notre map et de nos histogrammes dans le main. 
