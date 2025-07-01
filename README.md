# Análisis de Regresión Lineal - Resistencia del Hormigón

Este proyecto analiza la resistencia de probetas de hormigón utilizando técnicas de regresión lineal univariante y multivariante.

## 📊 Contenido del Proyecto

- **`01 Regresión (Uni y Multivariante) (Hormigón).ipynb`**: Notebook principal con el análisis completo
- **`hormigon.csv`**: Dataset con datos de resistencia de probetas de hormigón

## 🔬 Análisis Realizado

### Regresión Lineal Univariante

- Análisis de correlación entre variables
- Modelo usando únicamente la variable "cement"
- Métricas de evaluación (R², MSE, MAE)

### Regresión Lineal Multivariante

- Modelo usando todas las variables disponibles
- Análisis de normalización de datos
- Evaluación de multicolinealidad (VIF)
- Comparación de resultados

## 📈 Resultados Principales

- **Regresión Univariante**: R² = 0.2426
- **Regresión Multivariante**: R² = 0.5935 (mejora significativa)

## 🛠️ Tecnologías Utilizadas

- Python 3.12
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- statsmodels

## 📋 Requisitos

```bash
pip install pandas numpy matplotlib seaborn scikit-learn statsmodels
```

## 🚀 Cómo ejecutar

1. Clona este repositorio
2. Instala las dependencias
3. Abre el notebook en Jupyter o VS Code
4. Ejecuta las celdas secuencialmente

## 📊 Variables del Dataset

- `cement`: Cantidad de cemento
- `slag`: Cantidad de escorias
- `ash`: Cantidad de cenizas
- `water`: Cantidad de agua
- `superplastic`: Cantidad de superplastificante
- `coarseagg`: Agregado grueso
- `fineagg`: Agregado fino
- `age`: Edad del hormigón
- `strength`: Resistencia del hormigón (variable objetivo)

## 📝 Notas

- Los datos están normalizados para el análisis multivariante
- Se incluye análisis de multicolinealidad usando VIF
- Las métricas se expresan en las mismas unidades que la variable objetivo
