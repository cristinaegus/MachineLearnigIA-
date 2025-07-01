Para obtener el score del conjunto de entrenamiento (train), necesito agregar esa evaluación al código. Actualmente solo tienes las métricas para el conjunto de prueba (test). Te voy a añadir el cálculo del score para el train: 
```


Se realizaron cambios.


```
Ahora también necesito actualizar la parte de visualización para usar las variables renombradas: 
```


Se realizaron cambios.


```
Ahora ejecuto la celda principal para que veas los scores tanto del train como del test: ¡Perfecto! Aquí tienes los **scores de tu modelo** tanto para entrenamiento como para prueba:

## **📊 MÉTRICAS DEL MODELO DE REGRESIÓN LINEAL**

### **🎯 Conjunto de Entrenamiento (TRAIN):**
- **R² Train: 0.8294** (82.94%)
- **MAE Train: 1,866.71 €** 
- **MSE Train: 6,035,715.60**

### **🎯 Conjunto de Prueba (TEST):**
- **R² Test: 0.8329** (83.29%)
- **MAE Test: 1,766.60 €**
- **MSE Test: 5,816,672.27**

## **📈 ANÁLISIS DEL RENDIMIENTO:**

### **✅ Excelente rendimiento:**
1. **R² > 0.83**: El modelo explica más del 83% de la variabilidad en los precios
2. **Diferencia Train-Test: -0.0035**: Prácticamente no hay sobreajuste
3. **Generalización**: El modelo funciona igual de bien con datos nuevos

### **🎯 Interpretación:**
- **MAE ~1,800€**: En promedio, las predicciones se desvían ±1,800€ del precio real
- **Buen balance**: El modelo no está sobreajustado (overfitting)
- **Confiabilidad**: Los gráficos muestran una buena alineación entre valores reales y predichos

### **📊 Correlaciones clave:**
- **Año vs Precio**: 0.81 (correlación fuerte positiva)
- **Kilometraje vs Precio**: -0.68 (correlación negativa - más km, menor precio)
- **Potencia vs Precio**: 0.37 (correlación moderada positiva)

**En resumen**: Tu modelo tiene un rendimiento excelente con un R² de **82.94% en train** y **83.29% en test**, lo que indica un modelo bien ajustado y confiable para predecir precios de coches Renault.