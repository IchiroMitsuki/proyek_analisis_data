import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

def load_data():
    # Load datasets
    
    
    df_final = pd.read_csv(r"C:\Latihan Python\proyek_analisis_data\Dataframe_proyek_analisis_data.csv")
    
    return df_final

def plot_payment_distribution(df):
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x="payment_type", palette="coolwarm", order=df["payment_type"].value_counts().index)
    plt.title("Distribusi Metode Pembayaran")
    plt.xlabel("Metode Pembayaran")
    plt.ylabel("Jumlah Transaksi")
    plt.xticks(rotation=45)
    st.pyplot(plt)
    
    
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
    
    
def plot_payment_distribution_boxplot(df):
    plt.figure(figsize=(10, 5))
    sns.boxplot(data=df, x="payment_type", y="payment_value", hue="payment_type", palette="coolwarm", legend=False)
    plt.yscale("log")  # Gunakan log scale agar lebih terbaca jika ada outlier besar
    plt.title("Distribusi Jumlah Pembayaran Berdasarkan Metode")
    plt.xlabel("Metode Pembayaran")
    plt.ylabel("Jumlah Pembayaran")
    plt.show()
    st.pyplot(plt)    


def plot_top_categories(df):
    top_categories = df["product_category_name_english"].value_counts().nlargest(5).index
    df_top = df[df["product_category_name_english"].isin(top_categories)]
    
    plt.figure(figsize=(10, 5))
    sns.countplot(data=df_top, x="product_category_name_english", palette="viridis", hue="payment_type", order=top_categories)
    plt.title("5 Kategori Produk dengan Transaksi Terbanyak")
    plt.xlabel("Kategori Produk")
    plt.ylabel("Jumlah Transaksi")
    plt.legend(title="Tipe Pembayaran")
    plt.xticks(rotation=45)
    st.pyplot(plt)

def plot_top_one_categories(df):
    top_categories = df["product_category_name_english"].value_counts().nlargest(5).index
    df_top = df[df["product_category_name_english"].isin(top_categories)]
    warna = ['royalblue'] + ['lightgrey'] * (len(top_categories) - 1)

    plt.figure(figsize=(10, 5))
    sns.countplot(data=df_top, x="product_category_name_english", palette=warna, hue=None, legend=False, order=top_categories)
    plt.title("Kategori Produk dengan Jumlah Total Transaksi Terbanyak")
    plt.xlabel("Kategori Produk")
    plt.ylabel("Jumlah Transaksi")
    plt.xticks(rotation=45)
    st.pyplot(plt)
    

def main():
    st.title("Analisis Metode Pembayaran E-Commerce")
    st.write("Aplikasi ini menampilkan analisis dari dataset pembayaran e-commerce.")
    
    df = load_data()
    st.write("### Data Overview")
    st.write(df.head())
    
    st.write("### Statistik Deskriptif")
    st.write(df.describe())
    
    st.write("### Distribusi Metode Pembayaran")
    plot_payment_distribution(df)
    
    st.write("### Distribusi Metode Pembayaran pada setiap Kategori Produk")
    plot_payment_distribution_depend_method(df)
    
    st.write("### Distribusi Jumlah Pembayaran Berdasarkan Metode yang digunakan menggunakan boxplot")
    plot_payment_distribution_boxplot(df)
    
    st.write("### Distribusi 5 Kategori Produk dengan Transaksi Terbanyak berdasarkan Metode Pembayaran")
    plot_top_categories(df)
    
    st.write("### Kategori Produk dengan Transaksi Terbanyak")
    plot_top_one_categories(df)
    

if __name__ == "__main__":
    main()
