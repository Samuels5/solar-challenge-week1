import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page config
title = "Solar Data Cross-Country Dashboard"
st.set_page_config(page_title=title, layout="wide")
st.title(title)

# Sidebar - Country selection
country_options = ["Benin", "Sierra Leone", "Togo"]
selected_countries = st.sidebar.multiselect(
    "Select countries to compare:", country_options, default=country_options
)

# Load data
def load_data():
    df_benin = pd.read_csv("data/benin_clean.csv")
    df_benin["Country"] = "Benin"
    df_sl = pd.read_csv("data/sierraleone_clean.csv")
    df_sl["Country"] = "Sierra Leone"
    df_togo = pd.read_csv("data/togo_clean.csv")
    df_togo["Country"] = "Togo"
    return pd.concat([df_benin, df_sl, df_togo], ignore_index=True)

df = load_data()

# Filter by selected countries
df = df[df["Country"].isin(selected_countries)]

# Main metrics selection
metric = st.sidebar.selectbox(
    "Select metric to visualize:", ["GHI", "DNI", "DHI"]
)

# Boxplot
st.subheader(f"{metric} Distribution by Country")
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x="Country", y=metric, data=df, ax=ax)
ax.set_ylabel(f"{metric} (W/m²)")
st.pyplot(fig)

# Summary table
st.subheader(f"Summary Statistics for {metric}")
st.dataframe(df.groupby("Country")[metric].agg(["mean", "median", "std"]))

# Time series plot (optional)
if st.checkbox("Show time series plot (first 1000 rows)"):
    st.subheader(f"Time Series of {metric}")
    fig2, ax2 = plt.subplots(figsize=(10, 4))
    for country in selected_countries:
        subset = df[df["Country"] == country].head(1000)
        ax2.plot(subset["Timestamp"], subset[metric], label=country)
    ax2.set_xlabel("Timestamp")
    ax2.set_ylabel(f"{metric} (W/m²)")
    ax2.legend()
    st.pyplot(fig2)

# Top regions table (if region column exists)
if "Region" in df.columns:
    st.subheader("Top Regions by Average GHI")
    top_regions = df.groupby(["Country", "Region"])['GHI'].mean().reset_index()
    st.dataframe(top_regions.sort_values("GHI", ascending=False).head(10))

st.markdown("---")
st.markdown("Developed for the Solar Data Discovery Challenge – Week 1")
