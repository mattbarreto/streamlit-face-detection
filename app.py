"""
Versión simplificada de la aplicación de detección facial.
Interfaz directa y fácil de usar sin complicaciones.
"""

import streamlit as st
import cv2
import mediapipe as mp
import numpy as np
from PIL import Image
import io
import base64

# Configuración básica de la página
st.set_page_config(
    page_title="😊 Detector de Landmarks Faciales", page_icon="😊", layout="wide"
)

# Título principal
st.title("😊 Detector de Landmarks Faciales")
st.markdown("---")

# Información en el sidebar
st.sidebar.title("ℹ️ Información")
st.sidebar.info(
    """
    **Aplicación simplificada para detectar landmarks faciales**

    **Pasos:**
    1. Sube una imagen con un rostro
    2. Haz clic en "Detectar Landmarks"
    3. ¡Ve los resultados!

    **Características:**
    - Detección automática de hasta 478 puntos faciales
    - Procesamiento rápido y preciso
    - Visualización clara con puntos verdes
    """
)


def detectar_landmarks_faciales(imagen):
    """
    Detecta landmarks faciales en una imagen usando MediaPipe
    """
    # Inicializar MediaPipe Face Mesh
    mp_face_mesh = mp.solutions.face_mesh.FaceMesh(
        static_image_mode=True,
        max_num_faces=1,
        refine_landmarks=True,
        min_detection_confidence=0.5,
    )

    try:
        # Convertir imagen para procesamiento
        imagen_bgr = cv2.cvtColor(np.array(imagen), cv2.COLOR_RGB2BGR)
        imagen_rgb = cv2.cvtColor(imagen_bgr, cv2.COLOR_BGR2RGB)

        # Procesar imagen
        resultados = mp_face_mesh.process(imagen_rgb)

        # Crear copia para dibujar
        imagen_con_puntos = imagen_bgr.copy()
        alto, ancho, _ = imagen_con_puntos.shape

        landmarks_detectados = 0

        # Verificar si se detectaron rostros
        if resultados.multi_face_landmarks:
            rostro = resultados.multi_face_landmarks[0]

            # Dibujar cada landmark
            for punto in rostro.landmark:
                coord_x_pixel = int(punto.x * ancho)
                coord_y_pixel = int(punto.y * alto)

                cv2.circle(
                    imagen_con_puntos,
                    (coord_x_pixel, coord_y_pixel),
                    2,
                    (0, 255, 0),  # Verde
                    -1,
                )

            landmarks_detectados = len(rostro.landmark)

        # Cerrar detector
        mp_face_mesh.close()

        return imagen_con_puntos, landmarks_detectados

    except Exception as e:
        # Crear mensaje de error amigable
        error_msg = str(e).lower()

        if "out of memory" in error_msg or "memory" in error_msg:
            st.error("❌ **Imagen demasiado grande para procesar**")
            st.warning("""
            **Problema:** La imagen es muy grande y no se puede procesar.

            **Soluciones sugeridas:**
            - Usa una imagen más pequeña (menos de 5MB)
            - Reduce las dimensiones de la imagen
            - Comprime la imagen antes de subirla
            """)
        elif "face" in error_msg or "detection" in error_msg:
            st.error("❌ **No se pudo procesar el rostro**")
            st.warning("""
            **Problema:** Error interno al procesar la imagen.

            **Soluciones sugeridas:**
            - Intenta con otra imagen diferente
            - Asegúrate de que la imagen tenga buena calidad
            - Si el problema persiste, contacta al administrador
            """)
        else:
            st.error("❌ **Error interno al procesar la imagen**")
            st.warning("""
            **Problema:** Ocurrió un error técnico durante el procesamiento.

            **Soluciones sugeridas:**
            - Intenta procesar la imagen nuevamente
            - Usa una imagen diferente si el problema continúa
            - Contacta al administrador si el error persiste
            """)

        # Log del error técnico para debugging (sin mostrar al usuario)
        import logging

        logging.error(f"Error técnico en procesamiento: {e}")

        mp_face_mesh.close()
        return None, 0


def imagen_a_base64(imagen_cv2):
    """Convierte imagen OpenCV a base64"""
    imagen_rgb = cv2.cvtColor(imagen_cv2, cv2.COLOR_BGR2RGB)
    imagen_pil = Image.fromarray(imagen_rgb)

    buffer = io.BytesIO()
    imagen_pil.save(buffer, format="PNG")
    imagen_bytes = buffer.getvalue()

    return base64.b64encode(imagen_bytes).decode()


def main():
    """Función principal simplificada"""
    st.header("📸 Subir Imagen")

    # File uploader - siempre visible
    archivo_subido = st.file_uploader(
        "Elige una imagen con un rostro humano:",
        type=["jpg", "jpeg", "png", "bmp", "webp"],
        help="Sube una imagen clara con un rostro visible",
    )

    if archivo_subido is not None:
        try:
            # Cargar imagen
            imagen = Image.open(archivo_subido)

            # Mostrar imagen original
            st.subheader("🖼️ Imagen Original")
            st.image(
                imagen,
                caption=f"Imagen: {archivo_subido.name}",
                width="stretch",
            )

            # Botón para procesar
            if st.button("🔍 Detectar Landmarks", type="primary"):
                with st.spinner("🔄 Procesando imagen..."):
                    # Procesar imagen
                    imagen_procesada, num_landmarks = detectar_landmarks_faciales(
                        imagen
                    )

                if imagen_procesada is not None:
                    # Mostrar resultados
                    st.markdown("---")
                    st.subheader("🎯 Resultados")

                    if num_landmarks > 0:
                        # Información de éxito
                        col1, col2 = st.columns([1, 1])

                        with col1:
                            st.success(f"✅ ¡Rostro detectado exitosamente!")
                            st.metric("Landmarks detectados", num_landmarks)

                        with col2:
                            st.info("📊 Información técnica")
                            st.write("- Modelo: MediaPipe Face Mesh")
                            st.write(f"- Puntos de precisión: {num_landmarks}")
                            st.write("- Confianza mínima: 50%")

                        # Mostrar imagen procesada
                        st.subheader("🔍 Imagen con Landmarks")
                        imagen_base64 = imagen_a_base64(imagen_procesada)
                        st.markdown(
                            f'<img src="data:image/png;base64,{imagen_base64}" width="100%">',
                            unsafe_allow_html=True,
                        )

                        # Información adicional
                        st.markdown("---")
                        st.subheader("📝 ¿Qué son los landmarks?")

                        st.markdown("""
                        Los **landmarks faciales** son puntos característicos que identifican:
                        - 👀 **Ojos**: Párpados, cejas, pupilas
                        - 👃 **Nariz**: Puente, fosas nasales, punta
                        - 👄 **Boca**: Labios, comisuras, contorno
                        - 😊 **Contorno facial**: Mandíbula, mejillas, frente

                        **Aplicaciones comunes:**
                        - Análisis de expresiones faciales
                        - Realidad aumentada
                        - Reconocimiento biométrico
                        - Investigación médica
                        """)

                    else:
                        st.error("❌ No se detectó ningún rostro en la imagen")
                        st.warning("""
                        **¿Por qué no se detectó el rostro?**

                        - El rostro podría estar de perfil (necesita estar de frente)
                        - La imagen podría estar muy oscura o borrosa
                        - El rostro podría ser muy pequeño en la imagen
                        - Podría haber obstrucciones (manos, cabello, etc.)

                        **Solución:** Intenta con otra imagen más clara donde el rostro esté bien iluminado y ocupe una porción significativa de la imagen.
                        """)

        except Exception as e:
            # Crear mensaje de error amigable basado en el tipo de error
            error_msg = str(e).lower()

            if "cannot identify image file" in error_msg:
                st.error("❌ **Error al cargar la imagen**")
                st.warning("""
                **Problema:** La imagen subida no parece ser un archivo de imagen válido.

                **Soluciones sugeridas:**
                - Verifica que el archivo sea una imagen (JPG, PNG, BMP, WebP)
                - Intenta comprimir la imagen si es muy grande
                - Usa una imagen diferente si el archivo está dañado
                """)
            elif "cannot read" in error_msg or "corrupt" in error_msg:
                st.error("❌ **Imagen corrupta o ilegible**")
                st.warning("""
                **Problema:** La imagen está dañada o no se puede leer.

                **Soluciones sugeridas:**
                - Usa una imagen diferente
                - Intenta abrir la imagen en otro programa para verificar si funciona
                - Si puedes, exporta nuevamente la imagen desde su origen
                """)
            elif "out of memory" in error_msg or "memory" in error_msg:
                st.error("❌ **Imagen demasiado grande**")
                st.warning("""
                **Problema:** La imagen es muy grande para procesar.

                **Soluciones sugeridas:**
                - Usa una imagen más pequeña (menos de 5MB)
                - Reduce las dimensiones de la imagen antes de subirla
                - Comprime la imagen usando herramientas en línea
                """)
            else:
                st.error("❌ **Error inesperado al cargar la imagen**")
                st.warning("""
                **Problema:** Ocurrió un error inesperado.

                **Soluciones sugeridas:**
                - Intenta con otra imagen diferente
                - Refresca la página e intenta nuevamente
                - Si el problema persiste, contacta al administrador
                """)

            # Log del error técnico para debugging (sin mostrar al usuario)
            import logging

            logging.error(f"Error técnico al cargar imagen: {e}")

    else:
        # Mensaje cuando no hay imagen subida
        st.info(
            "💡 **Consejo:** Sube una imagen con un rostro humano para comenzar. La imagen debe ser clara y el rostro debe estar de frente."
        )

    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: #666;'>
        <p>Desarrollado con ❤️ usando Streamlit, MediaPipe y OpenCV</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
