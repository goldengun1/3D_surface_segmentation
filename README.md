# Segmentacija 3D površi

Projekat je rađen kao tema za seminarski rad za kurs "Računarska topologija" na četvrtoj godini Matematičkog fakulteta. Tema je Segmentacija 3D površi koja je definisana kao funckija visine nad 2D mrežom.

Podaci i funkcije površi su neke od prepoznatljivih površi u matematici i sve su naznačene i objašnjene u samom projektu.

## Korišćene biblioteke

1. [Python](https://www.python.org/)
2. [Numpy](https://numpy.org/)
3. [Matplotlib](https://matplotlib.org/)
4. [GUDHI](https://gudhi.inria.fr/)
5. [NetworkX](https://networkx.org/)

## Metodologije

U sklopu ovog projekta su demonstrirane neke od metodologija kao i struktura podataka za segmentaciju 3D površi.

1. Konturna stabla ([Reeb Graph](https://en.wikipedia.org/wiki/Reeb_graph))
2. Simpleksna stabla ([Simplex Trees](https://en.wikipedia.org/wiki/Simplex_tree))
3. Perzistencija i perzistentna homologija simplicijalnih kompleksa ([Persistent Homology](https://en.wikipedia.org/wiki/Persistent_homology))

## Testiranje i razvoj

U koliko biste želeli da pokrenete i testirate kodove iz ovog projekta to možete uraditi na neki od sledećih načina

### Pokretanje iz Google Collab okruženja

1. Potrebno je da sve `.py` fajlove iskopirate u lokalno okruženje Google Collab-a.
2. Nakon toga je neophodno da instalirate biblioteke koje se koriste a nisu podrazumevano dostupne na Google Collab-u. Ovo možete uraditi tako što na samom vrhu ubacite novu ćeliju i u njoj pokrenete sledeći kod.

```bash
# Ako je requrements.txt fajl iskopiran zajedno sa kodovima
pip install -r requirements.txt
```

ili

```bash
# samo preko komande
pip install gudhi networkx
```

3. Nakon ovoga možete pokretati kodove iz projekta i testirate postojeće ili vaše nove funkcije.

### Pokretanje lokalno na vašoj mašini

1. Ako na računaru nemate instaliran jupyter kernel potrebno je da se on instalira. Ovo se može automatski uraditi preko VSCode razvojnog okruženje (VSCode će sam predložiti instalaciju kernela čim se otvori `.ipynb` fajl u editoru). Ukoliko koristite neki drugi editor ili želite samostalno to da urdite možete pokrenuti sledeću komandu u terminalu.

```
pip install ipython ipykernel jupyter_client jupyter_core
```

##### NAPOMENA: Preporučujemo da sve instalacije vršite u virtualnom python okruženju (venv).

2. Nakon instalacije jupyter-a potrebno je da se instaliraju neophodne biblioteke. Ovo se može uraditi sledećom komandom iz terminala.

```
pip install -r requirements.txt
```

3. Sada se mogu pokretati i testirati kodovi.
