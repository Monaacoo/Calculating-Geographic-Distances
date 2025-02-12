# 🌍 Cálculo de Distâncias Geográficas com Python

Este projeto demonstra como calcular a **distância entre pontos geográficos** usando a **fórmula de Haversine** em Python. O código utiliza bibliotecas populares como `pandas`, `numpy` e `plotly` para manipulação de dados e visualização gráfica.

## 🚀 Funcionalidades

- Cálculo de distâncias entre coordenadas geográficas (latitude e longitude).
- Visualização interativa das distâncias com **gráficos de barras** usando Plotly.
- Manipulação de dados com `pandas` para facilitar o processamento.

## 📦 Tecnologias Utilizadas

- **Python 3.x**
- `pandas` para manipulação de dados.
- `numpy` para cálculos matemáticos.
- `plotly.express` para visualização interativa.

## 📊 Exemplo de Dados

O código trabalha com um conjunto de dados simulados, representando pares de localizações:

| Latitude  | Longitude  | Location Latitude | Location Longitude |
|-----------|------------|-------------------|--------------------|
| -23.5505  | -46.6333   | -22.9068          | -43.1729           |
| 48.8566   | 2.3522     | 51.5074           | -0.1278            |
| 34.0522   | -118.2437  | 40.7128           | -74.0060           |

O cálculo resultará na distância entre essas coordenadas.

## 📐 Fórmula de Haversine

A fórmula utilizada para calcular a distância considera o formato esférico da Terra:


  d = 2 \cdot R \cdot \arcsin \left( \sqrt{\sin^2\left(\frac{\Delta \varphi}{2}\right) + \cos(\varphi_1) \cdot \cos(\varphi_2) \cdot \sin^2\left(\frac{\Delta \lambda}{2}\right)} \right)


Onde:
- **R** = 6.371 km (raio da Terra)
- **\(\Delta \varphi\)** = diferença de latitude em radianos
- **\(\Delta \lambda\)** = diferença de longitude em radianos


## 📈 Exemplo de Gráfico

O código gera um gráfico de barras mostrando a distância calculada entre os pares de coordenadas.
**Visualize o gráfico:**
   O gráfico interativo abrirá automaticamente em uma nova aba do navegador.

![Exemplo de Gráfico](https://via.placeholder.com/600x300)

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir *issues* ou enviar *pull requests*.

1. Fork o projeto
2. Crie uma branch: `git checkout -b feature/MinhaNovaFeature`
3. Faça suas alterações e *commit*: `git commit -m 'Adiciona nova feature'`
4. Envie para a branch: `git push origin feature/MinhaNovaFeature`
5. Abra um Pull Request

