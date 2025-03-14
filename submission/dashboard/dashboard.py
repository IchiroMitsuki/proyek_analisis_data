import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')


def load_data():
    # Load datasets
    
    df_final = pd.read_csv("submission/dashboard/Dataframe_proyek_analisis_data.csv")
    
    return df_final


def plot_payment_distribution_depend_method(df):
    hitung_carabayar_perkategori = df.groupby(["product_category_name_english", "payment_type"]).size().reset_index(name="count")

    plt.figure(figsize=(12, 6))
    sns.barplot(data=hitung_carabayar_perkategori, x="product_category_name_english", y="count", hue="payment_type")
    plt.xticks(rotation=90)
    plt.xlabel("Kategori Produk")
    plt.ylabel("Jumlah Pembayaran")
    plt.title("Distribusi Metode Pembayaran berdasarkan Kategori Produk")
    plt.legend(title="Tipe Pembayaran")
    plt.show()
    st.pyplot(plt)


def plot_payment_distribution(df):
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x="payment_type", palette="coolwarm", order=df["payment_type"].value_counts().index)
    plt.title("Distribusi Metode Pembayaran")
    plt.xlabel("Metode Pembayaran")
    plt.ylabel("Jumlah Transaksi")
    plt.xticks(rotation=45)
    st.pyplot(plt)


def plot_top_categories(df):
    top_categories = df["product_category_name_english"].value_counts().nlargest(5).index
    df_top_categories = df[df["product_category_name_english"].isin(top_categories)]

    plt.figure(figsize=(10, 5))
    sns.countplot(data=df_top_categories, x="product_category_name_english", palette="viridis", hue="payment_type", order=top_categories)
    plt.title("5 Kategori Produk dengan Jumlah Transaksi Terbanyak Berdasarkan Metode Pembayaran")
    plt.xlabel("Kategori Produk")
    plt.ylabel("Jumlah Transaksi")
    plt.legend(title="Tipe Pembayaran")
    plt.xticks(rotation=45)
    plt.show()
    st.pyplot(plt)


def plot_top_one_categories(df):
    top_categories = df["product_category_name_english"].value_counts().nlargest(5).index
    df_top_categories = df[df["product_category_name_english"].isin(top_categories)]
    warna = ['royalblue'] + ['lightgrey'] * (len(top_categories) - 1)

    plt.figure(figsize=(10, 5))
    sns.countplot(data=df_top_categories, x="product_category_name_english", palette=warna, hue=None, legend=False, order=top_categories)
    plt.title("Kategori Produk dengan Jumlah Total Transaksi Terbanyak")
    plt.xlabel("Kategori Produk")
    plt.ylabel("Jumlah Transaksi")
    plt.xticks(rotation=45)
    plt.show()
    st.pyplot(plt)
    
    
def plot_top_one_categories_depend_transaction_piechart(df):
    kategori_teratas = df["product_category_name_english"].value_counts().idxmax()

    #Filter untuk kategori
    df_kategori_teratas = df[df["product_category_name_english"] == kategori_teratas]

    #Hitung distribusi metode pembayaran
    metode_pembayaran_kategori = df_kategori_teratas["payment_type"].value_counts()

    #Visualisasi dengan Pie Chart
    plt.figure(figsize=(8, 8))
    metode_pembayaran_kategori.plot(kind="pie", autopct="%1.1f%%", cmap="coolwarm", startangle=90, wedgeprops={'edgecolor': 'black'})
    plt.title(f"Distribusi Metode Pembayaran pada Kategori '{kategori_teratas}'")
    plt.ylabel("")
    plt.show()
    st.pyplot(plt)


def plot_top_one_categories_depend_transaction_barchart(df):
    top_categories = df["product_category_name_english"].value_counts().nlargest(5).index
    warna = ['royalblue'] + ['lightgrey'] * (len(top_categories) - 1)
    
    kategori_teratas = df["product_category_name_english"].value_counts().idxmax()

    #Filter untuk kategori
    df_kategori_teratas = df[df["product_category_name_english"] == kategori_teratas]

    #Hitung distribusi metode pembayaran
    metode_pembayaran_kategori = df_kategori_teratas["payment_type"].value_counts()
    
    plt.figure(figsize=(10, 5))
    sns.barplot(x=metode_pembayaran_kategori.values, y=metode_pembayaran_kategori.index, palette=warna, hue=metode_pembayaran_kategori.index, legend=False)
    plt.xlabel("Jumlah Transaksi")
    plt.ylabel("Metode Pembayaran")
    plt.title(f"Distribusi Metode Pembayaran pada Kategori '{kategori_teratas}'")
    plt.show()
    st.pyplot(plt)

    df_filtered = df[
    (df["product_category_name_english"] == selected_category) &
    (df["payment_type"] == selected_payment)
]

def main():
    st.title("Analisis Metode Pembayaran E-Commerce")
    st.write("Aplikasi ini menampilkan analisis dari dataset pembayaran e-commerce.")
    st.sidebar.header("Filter Data")

    
    df = load_data()
    st.write("### Data Overview")
    st.write(df.head())
    
    st.write("### Statistik Deskriptif")
    st.write(df.describe())
    
    st.write("### Distribusi Metode Pembayaran pada setiap Kategori Produk")
    plot_payment_distribution_depend_method(df)
    
    st.write("### Distribusi Metode Pembayaran")
    plot_payment_distribution(df)
    
    st.write("### Distribusi 5 Kategori Produk dengan Transaksi Terbanyak berdasarkan Metode Pembayaran")
    plot_top_categories(df)
    
    st.write("### Kategori Produk dengan Transaksi Terbanyak dari 5 Terbesar")
    plot_top_one_categories(df)
    
    st.write("### Distribusi Metode Pembayaram dari Kategori Produk dengan Transaksi Terbanyak dengan Pie Chart")
    plot_top_one_categories_depend_transaction_piechart(df)
    
    st.write("### Distribusi Metode Pembayaram dari Kategori Produk dengan Transaksi Terbanyak dengan Bar Chart")
    plot_top_one_categories_depend_transaction_barchart(df)

    selected_category = st.sidebar.selectbox("Pilih Kategori Produk", df["product_category_name_english"].unique())

    selected_payment = st.sidebar.selectbox("Pilih Metode Pembayaran", df["payment_type"].unique())
    
    st.write("### Hasil Filtering")
    st.write(df_filtered)
    

if __name__ == "__main__":
    main()
