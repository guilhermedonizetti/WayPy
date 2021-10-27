<h1 align="center">WayPy</h1>
<p align="center">
Python package to find a path between two distinct points in a graph.<br>
<i>Project Status: <b>Under development</b> :computer:</i><br>
  <a href="https://pypi.org/project/WayPy/"><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen" /></a>
</p>

<b>Usage:</b> To find a path between two different points in a graph, you must inform in list format which are the nodes and edges, after that you can choose a search method and inform the points where you want to find a path, then the package generates that result. Whereas, each search method can yield different results.

<p align="center">
<img src="https://www.researchgate.net/profile/Helenice-Florentino/publication/276508266/figure/fig3/AS:391774762749955@1470417790101/Figura-3-Ilustracao-de-um-grafo-GV-A-que-o-algoritmo-de-Dijkstra-modificado-pode-ser.png" width="350" height="250">
</p>

<b>Instructions for use: </b><br>
Initially, it is necessary to install the package. No dependencies are required:
```python
pip install WayPy
```
After installation, you must perform the import inside the Python file:
```python
from waypy.agent import Agente
```
To assign the values of the graph and perform the searches, it is necessary to instantiate the Agente class and inform the values.
```python
agent = Agente()

agent.starting_points = start
agent.arrival_points = arriv
agent.nodes = nodes
agent.graphs = edges
```
Start, arrive, nodes and edge are considered to be variables that contain the values. See more enlightening examples in the <a href="https://github.com/guilhermedonizetti/WayPy/tree/examples">examples branch</a>.

<br>

<p align="center"><b>Devs: </b></p>
<table align="center">
  <tr>
    <td align="center"><a href="https://br.linkedin.com/in/guilhermedonizetti-ads"><img src="https://avatars.githubusercontent.com/u/47000945?v=4" width="100px;" alt=""/><br /><sub><b>Guilherme Donizetti</b></sub></a><br /><a href="https://github.com/guilhermedonizetti/WayPy/commits?author=guilhermedonizetti" title="Desenvolvedor">💻</a></td>
    <td align="center"><a href="https://github.com/SACRIER"><img src="https://avatars.githubusercontent.com/u/61637378?v=4" width="100px;" alt=""/><br /><sub><b>Luiz Fernando Rodrigues</b></sub></a><br /><a href="https://github.com/guilhermedonizetti/WayPy/commits?author=SACRIER" title="Desenvolvedor">💻</a></td>
  </tr>
</table>
</center>

<br>

<p align="center">
<b>WayPy</b><br>
Python, Artificial Intelligence.
</p>
