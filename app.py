import streamlit as st
import pandas as pd
import io

def clean_data(df):
    """Cleans the uploaded dataset."""
    df.dropna(inplace=True)  # Remove missing values
    df.drop_duplicates(inplace=True)  # Remove duplicate rows
    return df

def convert_df(df, file_format):
    """Converts dataframe into selected file format and returns downloadable file."""
    if file_format == "CSV":
        return df.to_csv(index=False).encode('utf-8')
    elif file_format == "Excel":
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name='Cleaned Data')
        processed_data = output.getvalue()
        return processed_data
    elif file_format == "JSON":
        return df.to_json(indent=4).encode('utf-8')
    elif file_format == "TXT":
        return df.to_csv(index=False, sep='\t').encode('utf-8')








# Streamlit UI
st.title("🚀 Data Sweeper & Converter - Growth Mindset Challenge")
st.markdown("### Upload your CSV file to clean and convert it")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("📌 Original Data Preview")
    st.write(df.head())
    
    # Clean Data
    df_cleaned = clean_data(df)
    st.subheader("✅ Cleaned Data Preview")
    st.write(df_cleaned.head())
    
    # File format selection
    file_format = st.selectbox("Choose file format to convert:", ["CSV", "Excel", "JSON", "TXT"])
    
    # Convert & Download
    converted_file = convert_df(df_cleaned, file_format)
    st.download_button(
        label=f"Download Cleaned Data as {file_format}",
        data=converted_file,
        file_name=f"cleaned_data.{file_format.lower()}",
        mime="text/csv" if file_format == "CSV" else "application/json" if file_format == "JSON" else "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" if file_format == "Excel" else "text/plain"
    )

# Growth Mindset Message
st.markdown("---")
st.markdown(
    "**🌱 Growth Mindset Tip:** Mistakes and challenges are part of learning. Keep improving and keep growing! 🚀"
)


# made with codecraftali