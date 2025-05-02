import streamlit as st
from textblob import TextBlob
from googletrans import Translator

translator = Translator()
st.set_page_config(page_title="Análisis de Sentimientos 💖", page_icon="🌸")

st.markdown(
    """
    <style>
        html, body, .stApp {
            background-color: #FFE4F2;
        }
        h1, h2, h3, h4, p {
            text-align: center;
            color: #C2185B;
            font-family: 'Comic Sans MS', cursive;
        }
        .stButton>button {
            background-color: #F06292;
            color: white;
            border-radius: 10px;
            font-weight: bold;
            display: block;
            margin: auto;
        }
        .stTextArea, .stTextInput, .stSelectbox, .stCheckbox, .stRadio {
            display: flex;
            justify-content: center;
            margin: auto;
        }
        .stExpander, .stSidebar {
            font-family: 'Arial Rounded MT Bold', sans-serif;
        }
        .stMarkdown {
            text-align: center !important;
        }
        .block-container {
            padding-left: 10%;
            padding-right: 10%;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title('✨ Análisis de Sentimientos con TextBlob 💬')
st.markdown("<h3>Explora lo que siente tu texto... con estilo 💕</h3>", unsafe_allow_html=True)

st.subheader("✏️ Escribe tu frase para analizar:")

with st.sidebar:
    st.subheader("💡 ¿Qué significa cada cosa?")
    st.markdown("""
    **🔸 Polaridad:**  
    Mide si el sentimiento es positivo (+1), negativo (-1) o neutral (0).

    **🔸 Subjetividad:**  
    ¿El texto es más una opinión (1) o un hecho (0)?

    🌈 Una animación/emoción aparece según el resultado:
    - 😊 Positivo  
    - 😐 Neutral  
    - 😔 Negativo  

    ¡Explora la vibra de tus palabras! 🌟
    """)

with st.expander('📊 Analizar Polaridad y Subjetividad'):
    text1 = st.text_area('💬 Escribe tu frase:', key='1')
    if text1:
        translation = translator.translate(text1, src="es", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)
        
        st.markdown(f"<h4>🔍 Polaridad: {round(blob.sentiment.polarity, 2)}</h4>", unsafe_allow_html=True)
        st.markdown(f"<h4>📈 Subjetividad: {round(blob.sentiment.subjectivity, 2)}</h4>", unsafe_allow_html=True)

        x = round(blob.sentiment.polarity, 2)
        if x >= 0.5:
            st.markdown("<h4 style='color:#388E3C;'>🌟 ¡Sentimiento Positivo! 😊</h4>", unsafe_allow_html=True)
        elif x <= -0.5:
            st.markdown("<h4 style='color:#D32F2F;'>💔 Sentimiento Negativo 😔</h4>", unsafe_allow_html=True)
        else:
            st.markdown("<h4 style='color:#616161;'>😐 Sentimiento Neutral</h4>", unsafe_allow_html=True)

with st.expander('🛠️ Corrección ortográfica en inglés'):
    text2 = st.text_area('✍️ Escribe en inglés:', key='2')
    if text2:
        blob2 = TextBlob(text2)
        corrected = str(blob2.correct())
        st.markdown(f"<h4>✅ Corrección sugerida:</h4>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align:center; color:#6A1B9A;'>{corrected}</p>", unsafe_allow_html=True)
