import streamlit as st
import openai

# API KEY
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="IntellimaKG PRO", page_icon="🚀")

# PASSWORD
password = st.text_input("Enter Password", type="password")
if password != "admin123":
    st.stop()

st.title("🚀 IntellimaKG PRO")
st.subheader("AI Marketing Engine")

# MODE
mode = st.selectbox("Select Mode", ["Basic", "SEO", "Sales"])

# INPUT
product = st.text_area("Enter product or multiple products (one per line)")

generate = st.button("Generate")

if generate and product:

    products = product.split("\n")

    results = ""

    for p in products:

        if mode == "Basic":
            prompt = f"""
            Δημιούργησε:
            - Περιγραφή προϊόντος
            - Instagram post
            για το προϊόν: {p}
            """

        elif mode == "SEO":
            prompt = f"""
            Δημιούργησε:
            - SEO Title
            - Meta Description
            - Keywords
            για το προϊόν: {p}
            """

        elif mode == "Sales":
            prompt = f"""
            Δημιούργησε:
            - Facebook Ad
            - Google Ad
            - Πωλησιακή περιγραφή
            για το προϊόν: {p}
            """

        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        result = response["choices"][0]["message"]["content"]

        results += f"\n\n---\n\n🔹 {p}\n{result}"

    st.text_area("Results", results, height=500)