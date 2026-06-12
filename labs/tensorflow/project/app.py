import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from streamlit_drawable_canvas import st_canvas
import pandas as pd

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="MNIST Digit Classifier",
    page_icon="🔢",
    layout="centered"
)

# -----------------------------
# Load Model
# -----------------------------


@st.cache_resource
def load_model():
    return tf.keras.models.load_model("mnist_model.h5")


@st.cache_resource
def load_model_one():
    return tf.keras.models.load_model("mnist_model_one.h5")


model = load_model()

# -----------------------------
# Title
# -----------------------------
st.title("🔢 MNIST Digit Classifier")
st.write(
    "Draw a handwritten digit (0-9) in the canvas below and click **Predict**."
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.header("Canvas Settings")

stroke_width = st.sidebar.slider(
    "Stroke Width",
    min_value=5,
    max_value=30,
    value=15
)

# -----------------------------
# Drawing Canvas
# -----------------------------
canvas_result = st_canvas(
    fill_color="black",
    stroke_width=stroke_width,
    stroke_color="white",
    background_color="black",
    width=280,
    height=280,
    drawing_mode="freedraw",
    key="canvas",
)

# -----------------------------
# Prediction Function
# -----------------------------


def preprocess_image(image_data):
    img = Image.fromarray(image_data.astype("uint8"))

    # Convert to grayscale
    img = img.convert("L")

    # Resize to MNIST format
    img = img.resize((28, 28))

    img_array = np.array(img)

    # Normalize
    img_array = img_array.astype("float32") / 255.0

    # Shape for model
    img_array = img_array.reshape(1, 28, 28)

    return img_array


# -----------------------------
# Predict Button
# -----------------------------
if st.button("Predict Digit"):

    if canvas_result.image_data is not None:

        image_data = canvas_result.image_data[:, :, :3]

        processed_img = preprocess_image(image_data)

        prediction = model.predict(processed_img, verbose=0)

        predicted_digit = np.argmax(prediction)
        confidence = np.max(prediction)

        st.success(
            f"Predicted Digit: {predicted_digit}"
        )

        st.info(
            f"Confidence: {confidence:.2%}"
        )

        # Show processed image
        st.subheader("Processed 28×28 Image")

        display_img = processed_img.reshape(28, 28)

        st.image(
            display_img,
            width=200,
            clamp=True
        )

        # Probability Table
        st.subheader("Prediction Probabilities")

        probs = prediction[0]

        prob_df = pd.DataFrame({
            "Digit": list(range(10)),
            "Probability": probs
        })

        st.bar_chart(
            prob_df.set_index("Digit")
        )

    else:
        st.warning("Please draw a digit first.")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption(
    "TensorFlow + Streamlit MNIST Handwritten Digit Recognition"
)
