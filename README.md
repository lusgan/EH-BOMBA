TF de CAL - implementar um algoritimo heuristico para fazer a separação de produtos explosivos que nao podem estar em contato um com o outro

Ideia: usar algoritimo guloso de coloração de grafos.

Os vértices serão os produtos, e uma aresta deve conectar produtos que não podem ficar juntos.
Ao colorir com cores diferentes, conseguimos separar os objetos pelas cores. Os que possuírem a mesma cor podem ficar juntos na mesma estante.
Enquanto os que possuem cores diferentes devem ficar separados.
