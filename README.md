# Tarea 2: Algoritmos de Reducción de Dimensionalidad

## Algoritmos Implementados

### 1. SVD (Singular Value Decomposition)
- **Dataset**: MovieLens 100K
- **Aplicación**: Sistema de recomendación por filtrado colaborativo
- **Resultados**: Compresión 12.1x con RMSE=1.75 (k=50)

### 2. t-SNE (t-Distributed Stochastic Neighbor Embedding)
- **Dataset**: Breast Cancer Wisconsin
- **Aplicación**: Visualización de datos médicos
- **Resultados**: KL Divergence=0.94, clara separación de clusters

### 3. UMAP (Uniform Manifold Approximation and Projection)
- **Dataset**: Breast Cancer Wisconsin
- **Aplicación**: Visualización preservando estructura local-global
- **Resultados**: Mejor ratio de separación (2.90)

### 4. ICA (Independent Component Analysis)
- **Dataset**: EEG durante tareas aritméticas
- **Aplicación**: Separación de fuentes y eliminación de artefactos
- **Resultados**: Identificación efectiva de componentes independientes

## Instalación y Requisitos

### Dependencias Principales
```bash
pip install numpy pandas matplotlib seaborn scikit-learn scipy
```

### Dependencias Opcionales (auto-instaladas)
```bash
pip install umap-learn pyedflib
```

### Versions Recomendadas
- Python 3.8+
- numpy >= 1.21.0
- scikit-learn >= 1.0.0
- matplotlib >= 3.5.0

## Uso del Notebook

1. **Abrir el notebook**:
   ```bash
   jupyter notebook tarea2.ipynb
   ```

2. **Ejecutar celdas secuencialmente** - Cada sección es independiente

3. **Datasets requeridos**:
   - MovieLens 100K (incluido)
   - Breast Cancer Wisconsin (incluido)
   - EEG datos (incluido)

## Características Destacadas

### Análisis Exploratorio
- Visualizaciones comprehensivas para cada dataset
- Estadísticas descriptivas detalladas
- Análisis de distribución de datos

### Evaluación Cuantitativa
- **SVD**: RMSE, varianza explicada, ratio de compresión
- **t-SNE/UMAP**: Métricas de separación de clusters
- **ICA**: Análisis espectral y potencia por bandas


## Aplicaciones Prácticas

### SVD es ideal para:
- Sistemas de recomendación
- Compresión de datos
- Análisis de componentes principales

### t-SNE/UMAP para:
- Exploración visual de datos complejos
- Identificación de clusters
- Análisis de alta dimensionalidad

### ICA para:
- Separación de señales (EEG, audio)
- Eliminación de artefactos
- Análisis de fuentes independientes