# Detector de Landmarks Faciales - Versión Simplificada

Una aplicación web **fácil de usar** desarrollada con **Streamlit** que utiliza **MediaPipe** y **OpenCV** para detectar y visualizar puntos característicos (landmarks) en rostros humanos.

**Característica principal:** Interfaz súper simple - solo sube tu imagen y detecta landmarks faciales.

## Características

- **Detección automática** de hasta 478 landmarks faciales
- **Interfaz súper simple** - solo sube y procesa
- **Procesamiento rápido** y preciso con MediaPipe
- **Visualización clara** con puntos verdes sobre el rostro
- **Soporte múltiple** de formatos de imagen (JPG, PNG, BMP, WebP)
- **Mensajes de error amigables** para usuarios no técnicos

## Requisitos del Sistema

- Python 3.9 o superior
- Conexión a internet (para descargar imágenes de ejemplo)

## Instalación Local

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd facial-landmark-detector-streamlit
```

### 2. Crear entorno virtual (opcional pero recomendado)

```bash
python -m venv venv
# En Windows:
venv\\Scripts\\activate
# En macOS/Linux:
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación

```bash
streamlit run app.py
```

La aplicación estará disponible en: `http://localhost:8501`

## Dependencias

- **streamlit** (>=1.28.0) - Framework web
- **mediapipe** (>=0.10.0) - Detección facial
- **opencv-python** (>=4.8.0) - Procesamiento de imágenes
- **numpy** (>=1.24.0) - Computación numérica
- **pillow** (>=10.0.0) - Manejo de imágenes
- **requests** (>=2.31.0) - Descargas HTTP

## Despliegue en Streamlit Cloud

### Opción 1: Desde GitHub (Recomendado)

1. **Crear repositorio en GitHub:**

   - Sube todos los archivos a un repositorio público en GitHub
   - Asegúrate de que el archivo `requirements.txt` esté incluido

2. **Desplegar en Streamlit Cloud:**

   - Ve a [share.streamlit.io](https://share.streamlit.io)
   - Inicia sesión con tu cuenta de GitHub
   - Selecciona el repositorio que acabas de crear
   - Haz clic en "Deploy"

3. **Configuración automática:**
   - Streamlit Cloud detectará automáticamente `app.py` como archivo principal
   - Instalará las dependencias desde `requirements.txt`
   - Aplicará la configuración desde `.streamlit/config.toml`

### Opción 2: Configuración manual

Si necesitas configuración personalizada:

1. Ve a [share.streamlit.io](https://share.streamlit.io)
2. Selecciona "New app"
3. Elige el repositorio y rama
4. Configura:
   - **Main file path:** `app.py`
   - **Requirements file:** `requirements.txt`

## Cómo Usar la Aplicación

### Dos Versiones Disponibles

#### Versión Simplificada (app_simple.py) - Recomendada

**Perfecta para usuarios finales que quieren simplicidad.**

**Características:**

- **Interfaz directa**: Sube imagen y procesa inmediatamente
- **Un solo paso**: File uploader siempre visible
- **Procesamiento inmediato**: Haz clic en "Detectar Landmarks"
- **Más intuitiva**: Flujo lineal fácil de seguir

**Cómo usar:**

1. Ejecuta: `streamlit run app_simple.py`
2. Sube tu imagen usando el file uploader
3. Haz clic en "Detectar Landmarks"
4. Ve los resultados

#### Versión Modular (app.py) - Para desarrolladores

**Con arquitectura avanzada y componentes reutilizables.**

**Características:**

- **Arquitectura profesional**: Código modular organizado
- **Componentes reutilizables**: Fácil de extender
- **Configuración avanzada**: Más opciones de personalización
- **Estado de sesión**: Interfaz más dinámica

**Cómo usar:**

1. Ejecuta: `streamlit run app.py`
2. Selecciona método de entrada (archivo o ejemplo)
3. Sube imagen o usa ejemplo
4. Haz clic en "Procesar Imagen"
5. Ve los resultados

### 1. Acceso a la aplicación

- Abre la aplicación en tu navegador
- Verás la interfaz principal con opciones de carga

### 2. Subir imagen

- **Opción A: Subir archivo**

  - Haz clic en "Browse files" o arrastra una imagen
  - Selecciona una imagen que contenga un rostro claro

- **Opción B: Imagen de ejemplo**
  - Selecciona "Usar imagen de ejemplo"
  - La aplicación descargará automáticamente una imagen de muestra

### 3. Procesamiento

- La aplicación procesará automáticamente la imagen
- Verás el progreso con el indicador de carga

### 4. Visualización de resultados

- **Imagen original**: Se muestra la imagen subida
- **Imagen procesada**: Muestra la imagen con landmarks marcados en verde
- **Información técnica**: Detalles sobre la detección realizada

## Configuración

### Archivo de configuración (`.streamlit/config.toml`)

```toml
[server]
headless = true
port = 8501

[browser]
gatherUsageStats = false

[theme]
base = "light"
primaryColor = "#1f77b4"
```

### Parámetros de detección

La aplicación utiliza los siguientes parámetros de MediaPipe:

- **Modo**: Imagen estática
- **Máximo rostros**: 1
- **Refinamiento**: Activado (478 landmarks)
- **Confianza mínima**: 50%

## Desarrollo

### Estructura del proyecto

```
facial-landmark-detector-streamlit/
├── app.py                    # Aplicación principal (versión simplificada)
├── requirements.txt          # Dependencias de Python
├── README.md                 # Esta documentación
├── .streamlit/
│   └── config.toml           # Configuración de Streamlit
├── .gitignore               # Archivos a ignorar en Git
└── assets/                   # Recursos adicionales
    └── test_image.jpg        # Imagen de prueba incluida
```

### Arquitectura Modular

La aplicación está organizada siguiendo **buenas prácticas de programación**:

#### **Separación de responsabilidades:**

- **`src/core/config.py`**: Configuración centralizada y constantes
- **`src/utils/image_processing.py`**: Funciones especializadas en procesamiento de imágenes
- **`src/utils/face_detection.py`**: Lógica específica de detección facial con MediaPipe
- **`src/ui/components.py`**: Componentes reutilizables de la interfaz de usuario
- **`src/main.py`**: Lógica principal que coordina todos los módulos

#### Beneficios de la arquitectura:

- **Mantenibilidad**: Código organizado y fácil de modificar
- **Reutilización**: Módulos independientes que se pueden reutilizar
- **Testabilidad**: Cada módulo se puede probar de forma independiente
- **Escalabilidad**: Fácil agregar nuevas funcionalidades
- **Legibilidad**: Código más claro y autodocumentado

### Tecnologías utilizadas

- **Backend**: Python 3.9+
- **Framework web**: Streamlit
- **Visión por computadora**: MediaPipe + OpenCV
- **Procesamiento de imágenes**: Pillow, NumPy
- **Arquitectura**: Programación modular orientada a objetos

## Rendimiento

- **Tiempo de procesamiento**: Variable según tamaño de imagen
- **Memoria utilizada**: Aproximadamente 100-200 MB durante el procesamiento
- **Compatibilidad**: Todas las plataformas soportadas por Streamlit

## Privacidad y Seguridad

- **Procesamiento local**: Las imágenes se procesan en el servidor, no se almacenan permanentemente
- **Sin almacenamiento**: No se guardan imágenes de usuarios
- **Anonimato**: No se recopila información personal

## Solución de Problemas

### Problema: No se detecta ningún rostro

**Causas posibles:**

- El rostro está de perfil (necesita estar de frente)
- La imagen está muy oscura o borrosa
- El rostro es muy pequeño en la imagen
- Hay obstrucciones (manos, cabello cubriendo la cara)

**Soluciones:**

- Usa una imagen más clara y bien iluminada
- Asegúrate de que el rostro esté de frente a la cámara
- El rostro debe ocupar una porción significativa de la imagen

### Problema: Error de instalación de dependencias

**Solución:**

```bash
pip install --upgrade pip
pip install --force-reinstall -r requirements.txt
```

### Problema: La aplicación no inicia

**Verificaciones:**

- Todas las dependencias instaladas correctamente
- Puerto 8501 disponible
- No hay conflictos con otros servicios

## Información Técnica

### Modelo de MediaPipe Face Mesh

La aplicación utiliza el modelo pre-entrenado de MediaPipe que identifica:

- **468 landmarks básicos** + **10 landmarks refinados**
- **Coordenadas 3D** para cada punto facial
- **Seguimiento en tiempo real** (aunque configurado para imágenes estáticas)

### Formatos de imagen soportados

- **JPEG/JPG**: Compresión con pérdida, buena calidad
- **PNG**: Sin compresión, soporta transparencia
- **BMP**: Formato sin compresión de Windows
- **WebP**: Formato moderno de Google, buena compresión

## Contribución

Si deseas contribuir al proyecto:

1. Haz fork del repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo `LICENSE` para más detalles.

## Agradecimientos

- **MediaPipe**: Por la excelente biblioteca de visión por computadora
- **Streamlit**: Por el framework web tan fácil de usar
- **OpenCV**: Por las herramientas de procesamiento de imágenes
- **Unsplash**: Por las imágenes de ejemplo de alta calidad

---

**Desarrollado para la comunidad de visión por computadora**
