import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)

# Layout aplikasi
st.set_page_config(page_title="Visualisasi Penjualan Sepeda Motor",
                   page_icon="📊")

# Tampilan judul
st.title("Visualisasi Penjualan Sepeda Motor")

# Upload file dataset
uploaded_file = st.file_uploader("Upload file CSV", type=["csv"])

if uploaded_file is not None:
    # Membaca data dari file yang diunggah
    dataset = pd.read_csv(uploaded_file)

    # Menggabungkan kolom 'MERK' dan 'f_cluster' menjadi 'MERK_CLUSTER'
    dataset['MERK_CLUSTER'] = dataset['MERK'] + ' - ' + dataset['f_cluster'].astype(str)

    # Layout aplikasi untuk visualisasi jumlah masing-masing MERK dalam setiap f_cluster
    st.subheader("Visualisasi Jumlah Masing-Masing MERK dalam Setiap f_cluster")
    
    # Pilihan f_cluster
    selected_cluster = st.selectbox("Pilih f_cluster", dataset['f_cluster'].unique())

    # Mengelompokkan berdasarkan 'f_cluster' dan menghitung jumlah masing-masing 'MERK'
    merk_group_by_cluster = dataset.groupby('f_cluster')['MERK'].value_counts()

    # Membuat palet warna yang berbeda untuk setiap 'MERK'
    merk_palette = sns.color_palette("husl", n_colors=len(dataset['MERK'].unique()))

    # Menampilkan visualisasi jumlah masing-masing MERK dalam f_cluster yang dipilih
    fig, ax = plt.subplots(figsize=(10, 6))
    merk_group_by_cluster.unstack().loc[selected_cluster].plot(kind='bar', ax=ax, color=merk_palette)
    ax.set_xlabel('f_cluster')
    ax.set_ylabel('Jumlah')
    ax.set_title(f'Jumlah Masing-Masing MERK dalam f_cluster {selected_cluster}')
    ax.legend(title='MERK', bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.tick_params(axis='x', rotation=90)

    # Menambahkan value label pada grafik
    for p in ax.patches:
        ax.annotate(format(p.get_height(), '.0f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom', xytext=(0, 5), textcoords='offset points')

    st.pyplot(fig)
    
    # Menggabungkan kolom 'JENIS' dan 'KELURAHAN' menjadi satu kolom baru
    dataset['JENIS_KELURAHAN'] = dataset['JENIS'] + ' - ' + dataset['KELURAHAN']

    # Memfilter data hanya untuk yang memiliki 100 baris atau lebih
    if len(dataset) >= 100:
        # Membuat plot bar untuk Cluster 1
        st.subheader('Top 10 Penjualan Sepeda Motor Per Kelurahan (Cluster 0)')
        cluster_1_data = dataset[dataset['f_cluster'] == 0]
        jenis_kabupaten_counts_cluster_1 = cluster_1_data['JENIS_KELURAHAN'].value_counts().head(10)
        total_penjualan_cluster_1 = jenis_kabupaten_counts_cluster_1.sum()
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x=jenis_kabupaten_counts_cluster_1.index, y=jenis_kabupaten_counts_cluster_1.values, palette='viridis', ax=ax)
        ax.set_xlabel('JENIS_KELURAHAN')
        ax.set_ylabel('Frekuensi')
        ax.set_title(f'Top 10 Penjualan Sepeda Motor Per Kelurahan (Cluster 0)\nTotal Penjualan: {total_penjualan_cluster_1}')
        plt.xticks(rotation=90)
        for p in ax.patches:
            ax.annotate(format(p.get_height(), '.0f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom', xytext=(0, 5), textcoords='offset points')
        st.pyplot(fig)

        # Membuat plot bar untuk Cluster 2
        st.subheader('Top 10 Penjualan Sepeda Motor Per Kelurahan (Cluster 1)')
        cluster_2_data = dataset[dataset['f_cluster'] == 1]
        jenis_kabupaten_counts_cluster_2 = cluster_2_data['JENIS_KELURAHAN'].value_counts().head(10)
        total_penjualan_cluster_2 = jenis_kabupaten_counts_cluster_2.sum()
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x=jenis_kabupaten_counts_cluster_2.index, y=jenis_kabupaten_counts_cluster_2.values, palette='viridis', ax=ax)
        ax.set_xlabel('JENIS_KELURAHAN')
        ax.set_ylabel('Frekuensi')
        ax.set_title(f'Top 10 Penjualan Sepeda Motor Per Kelurahan (Cluster 1)\nTotal Penjualan: {total_penjualan_cluster_2}')
        plt.xticks(rotation=90)
        for p in ax.patches:
            ax.annotate(format(p.get_height(), '.0f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom', xytext=(0, 5), textcoords='offset points')
        st.pyplot(fig)
    else:
        st.write("Data tidak mencukupi untuk menampilkan plot bar.")
        # Menggabungkan kolom 'JENIS' dan 'KELURAHAN' menjadi satu kolom baru


    dataset['JENIS_KECAMATAN'] = dataset['JENIS'] + ' - ' + dataset['KECAMATAN']

    # Memfilter data hanya untuk yang memiliki 100 baris atau lebih
    if len(dataset) >= 100:
        # Membuat plot bar untuk Cluster 1
        st.subheader('Top 10 Penjualan Sepeda Motor Per Kecamatan (Cluster 0)')
        cluster_1_data = dataset[dataset['f_cluster'] == 0]
        jenis_kabupaten_counts_cluster_1 = cluster_1_data['JENIS_KECAMATAN'].value_counts().head(10)
        total_penjualan_cluster_1 = jenis_kabupaten_counts_cluster_1.sum()
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x=jenis_kabupaten_counts_cluster_1.index, y=jenis_kabupaten_counts_cluster_1.values, palette='viridis', ax=ax)
        ax.set_xlabel('JENIS_KECAMATAN')
        ax.set_ylabel('Frekuensi')
        ax.set_title(f'Top 10 Penjualan Sepeda Motor Per Kecamatan (Cluster 0)\nTotal Penjualan: {total_penjualan_cluster_1}')
        plt.xticks(rotation=90)
        for p in ax.patches:
            ax.annotate(format(p.get_height(), '.0f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom', xytext=(0, 5), textcoords='offset points')
        st.pyplot(fig)

        # Membuat plot bar untuk Cluster 2
        st.subheader('Top 10 Penjualan Sepeda Motor Per Kecamatan (Cluster 1)')
        cluster_2_data = dataset[dataset['f_cluster'] == 1]
        jenis_kabupaten_counts_cluster_2 = cluster_2_data['JENIS_KECAMATAN'].value_counts().head(10)
        total_penjualan_cluster_2 = jenis_kabupaten_counts_cluster_2.sum()
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x=jenis_kabupaten_counts_cluster_2.index, y=jenis_kabupaten_counts_cluster_2.values, palette='viridis', ax=ax)
        ax.set_xlabel('JENIS_KECAMATAN')
        ax.set_ylabel('Frekuensi')
        ax.set_title(f'Top 10 Penjualan Sepeda Motor Per Kecamatan (Cluster 1)\nTotal Penjualan: {total_penjualan_cluster_2}')
        plt.xticks(rotation=90)
        for p in ax.patches:
            ax.annotate(format(p.get_height(), '.0f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom', xytext=(0, 5), textcoords='offset points')
        st.pyplot(fig)
    else:
        st.write("Data tidak mencukupi untuk menampilkan plot bar.")

        
    dataset['JENIS_KABUPATEN'] = dataset['JENIS'] + ' - ' + dataset['KABUPATEN']

    # Memfilter data hanya untuk yang memiliki 100 baris atau lebih
    if len(dataset) >= 100:
        # Membuat plot bar untuk Cluster 1
        st.subheader('Top 10 Penjualan Sepeda Motor Per Kabupaten (Cluster 0)')
        cluster_1_data = dataset[dataset['f_cluster'] == 0]
        jenis_kabupaten_counts_cluster_1 = cluster_1_data['JENIS_KABUPATEN'].value_counts().head(10)
        total_penjualan_cluster_1 = jenis_kabupaten_counts_cluster_1.sum()
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x=jenis_kabupaten_counts_cluster_1.index, y=jenis_kabupaten_counts_cluster_1.values, palette='viridis', ax=ax)
        ax.set_xlabel('JENIS_KABUPATEN')
        ax.set_ylabel('Frekuensi')
        ax.set_title(f'Top 10 Penjualan Sepeda Motor Per Kabupaten (Cluster 0)\nTotal Penjualan: {total_penjualan_cluster_1}')
        plt.xticks(rotation=90)
        for p in ax.patches:
            ax.annotate(format(p.get_height(), '.0f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom', xytext=(0, 5), textcoords='offset points')
        st.pyplot(fig)

        # Membuat plot bar untuk Cluster 2
        st.subheader('Top 10 Penjualan Sepeda Motor Per Kabupaten (Cluster 1)')
        cluster_2_data = dataset[dataset['f_cluster'] == 1]
        jenis_kabupaten_counts_cluster_2 = cluster_2_data['JENIS_KABUPATEN'].value_counts().head(10)
        total_penjualan_cluster_2 = jenis_kabupaten_counts_cluster_2.sum()
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x=jenis_kabupaten_counts_cluster_2.index, y=jenis_kabupaten_counts_cluster_2.values, palette='viridis', ax=ax)
        ax.set_xlabel('JENIS_KABUPATEN')
        ax.set_ylabel('Frekuensi')
        ax.set_title(f'Top 10 Penjualan Sepeda Motor Per Kelurahan (Cluster 1)\nTotal Penjualan: {total_penjualan_cluster_2}')
        plt.xticks(rotation=90)
        for p in ax.patches:
            ax.annotate(format(p.get_height(), '.0f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom', xytext=(0, 5), textcoords='offset points')
        st.pyplot(fig)
    else:
        st.write("Data tidak mencukupi untuk menampilkan plot bar.")
    

    
    dataset['DP NET_KELURAHAN'] = dataset['DP NET'].astype(str) + ' - ' + dataset['KELURAHAN']

    # Memfilter data hanya untuk yang memiliki 100 baris atau lebih
    if len(dataset) >= 100:
        # Membuat plot bar untuk Cluster 1
        st.subheader('Top 10 Penjualan Sepeda Motor Per Kelurahan (Cluster 0)')
        cluster_1_data = dataset[dataset['f_cluster'] == 0]
        DP_NET_KELURAHAAN_counts_cluster_1 = cluster_1_data['DP NET_KELURAHAN'].value_counts().head(10)
        total_penjualan_cluster_1 = DP_NET_KELURAHAAN_counts_cluster_1.sum()
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x=DP_NET_KELURAHAAN_counts_cluster_1.index, y=DP_NET_KELURAHAAN_counts_cluster_1.values, palette='viridis', ax=ax)
        ax.set_xlabel('DP NET_KELURAHAN')
        ax.set_ylabel('Frekuensi')
        ax.set_title(f'Top 10 Penjualan Sepeda Motor Per Kelurahan (Cluster 0)\nTotal Penjualan: {total_penjualan_cluster_1}')
        plt.xticks(rotation=90)
        for p in ax.patches:
            ax.annotate(format(p.get_height(), '.0f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom', xytext=(0, 5), textcoords='offset points')
        st.pyplot(fig)

        # Membuat plot bar untuk Cluster 2
        st.subheader('Top 10 Penjualan Sepeda Motor Per Kelurahan (Cluster 1)')
        cluster_2_data = dataset[dataset['f_cluster'] == 1]
        DP_NET_KELURAHAAN_counts_cluster_2 = cluster_2_data['DP NET_KELURAHAN'].value_counts().head(10)
        total_penjualan_cluster_2 = DP_NET_KELURAHAAN_counts_cluster_2.sum()
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x=DP_NET_KELURAHAAN_counts_cluster_2.index, y=DP_NET_KELURAHAAN_counts_cluster_2.values, palette='viridis', ax=ax)
        ax.set_xlabel('DP NET_KELURAHAAN')
        ax.set_ylabel('Frekuensi')
        ax.set_title(f'Top 10 Penjualan Sepeda Motor Per Kelurahan (Cluster 1)\nTotal Penjualan: {total_penjualan_cluster_2}')
        plt.xticks(rotation=90)
        for p in ax.patches:
            ax.annotate(format(p.get_height(), '.0f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom', xytext=(0, 5), textcoords='offset points')
        st.pyplot(fig)
    else:
        st.write("Data tidak mencukupi untuk menampilkan plot bar.")
    
    dataset['DP NET_KECAMATAN'] = dataset['DP NET'].astype(str) + ' - ' + dataset['KECAMATAN']

    # Memfilter data hanya untuk yang memiliki 100 baris atau lebih
    if len(dataset) >= 100:
        # Membuat plot bar untuk Cluster 1
        st.subheader('Top 10 Penjualan Sepeda Motor Per Kecamatan (Cluster 0)')
        cluster_1_data = dataset[dataset['f_cluster'] == 0]
        DP_NET_KECAMATAN_counts_cluster_1 = cluster_1_data['DP NET_KECAMATAN'].value_counts().head(10)
        total_penjualan_cluster_1 = DP_NET_KECAMATAN_counts_cluster_1.sum()
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x=DP_NET_KECAMATAN_counts_cluster_1.index, y=DP_NET_KECAMATAN_counts_cluster_1.values, palette='viridis', ax=ax)
        ax.set_xlabel('DP NET_KECAMATAN')
        ax.set_ylabel('Frekuensi')
        ax.set_title(f'Top 10 Penjualan Sepeda Motor Per Kecamatan (Cluster 0)\nTotal Penjualan: {total_penjualan_cluster_1}')
        plt.xticks(rotation=90)
        for p in ax.patches:
            ax.annotate(format(p.get_height(), '.0f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom', xytext=(0, 5), textcoords='offset points')
        st.pyplot(fig)

        # Membuat plot bar untuk Cluster 2
        st.subheader('Top 10 Penjualan Sepeda Motor Per Kecamatan (Cluster 1)')
        cluster_2_data = dataset[dataset['f_cluster'] == 1]
        DP_NET_KECAMATAN_counts_cluster_2 = cluster_2_data['DP NET_KECAMATAN'].value_counts().head(10)
        total_penjualan_cluster_2 = DP_NET_KECAMATAN_counts_cluster_2.sum()
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x=DP_NET_KECAMATAN_counts_cluster_2.index, y=DP_NET_KECAMATAN_counts_cluster_2.values, palette='viridis', ax=ax)
        ax.set_xlabel('DP NET_KECAMATAN')
        ax.set_ylabel('Frekuensi')
        ax.set_title(f'Top 10 Penjualan Sepeda Motor Per Kecamatan (Cluster 1)\nTotal Penjualan: {total_penjualan_cluster_2}')
        plt.xticks(rotation=90)
        for p in ax.patches:
            ax.annotate(format(p.get_height(), '.0f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom', xytext=(0, 5), textcoords='offset points')
        st.pyplot(fig)
    else:
        st.write("Data tidak mencukupi untuk menampilkan plot bar.")

    dataset['DP NET_KECAMATAN'] = dataset['DP NET'].astype(str) + ' - ' + dataset['KECAMATAN']

    # Memfilter data hanya untuk yang memiliki 100 baris atau lebih
    if len(dataset) >= 100:
        # Membuat plot bar untuk Cluster 1
        st.subheader('Top 10 Penjualan Sepeda Motor Per Kecamatan (Cluster 0)')
        cluster_1_data = dataset[dataset['f_cluster'] == 0]
        DP_NET_KECAMATAN_counts_cluster_1 = cluster_1_data['DP NET_KECAMATAN'].value_counts().head(10)
        total_penjualan_cluster_1 = DP_NET_KECAMATAN_counts_cluster_1.sum()
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x=DP_NET_KECAMATAN_counts_cluster_1.index, y=DP_NET_KECAMATAN_counts_cluster_1.values, palette='viridis', ax=ax)
        ax.set_xlabel('DP NET_KECAMATAN')
        ax.set_ylabel('Frekuensi')
        ax.set_title(f'Top 10 Penjualan Sepeda Motor Per Kecamatan (Cluster 0)\nTotal Penjualan: {total_penjualan_cluster_1}')
        plt.xticks(rotation=90)
        for p in ax.patches:
            ax.annotate(format(p.get_height(), '.0f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom', xytext=(0, 5), textcoords='offset points')
        st.pyplot(fig)

        # Membuat plot bar untuk Cluster 2
        st.subheader('Top 10 Penjualan Sepeda Motor Per Kecamatan (Cluster 1)')
        cluster_2_data = dataset[dataset['f_cluster'] == 1]
        DP_NET_KECAMATAN_counts_cluster_2 = cluster_2_data['DP NET_KECAMATAN'].value_counts().head(10)
        total_penjualan_cluster_2 = DP_NET_KECAMATAN_counts_cluster_2.sum()
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x=DP_NET_KECAMATAN_counts_cluster_2.index, y=DP_NET_KECAMATAN_counts_cluster_2.values, palette='viridis', ax=ax)
        ax.set_xlabel('DP NET_KECAMATAN')
        ax.set_ylabel('Frekuensi')
        ax.set_title(f'Top 10 Penjualan Sepeda Motor Per Kecamatan (Cluster 1)\nTotal Penjualan: {total_penjualan_cluster_2}')
        plt.xticks(rotation=90)
        for p in ax.patches:
            ax.annotate(format(p.get_height(), '.0f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom', xytext=(0, 5), textcoords='offset points')
        st.pyplot(fig)
    else:
        st.write("Data tidak mencukupi untuk menampilkan plot bar.")
    

    dataset['DP NET_KABUPATEN'] = dataset['DP NET'].astype(str) + ' - ' + dataset['KABUPATEN']

    # Memfilter data hanya untuk yang memiliki 100 baris atau lebih
    if len(dataset) >= 100:
        # Membuat plot bar untuk Cluster 1
        st.subheader('Top 10 Penjualan Sepeda Motor Per Kabupaten(Cluster 0)')
        cluster_1_data = dataset[dataset['f_cluster'] == 0]
        DP_NET_KECAMATAN_counts_cluster_1 = cluster_1_data['DP NET_KABUPATEN'].value_counts().head(10)
        total_penjualan_cluster_1 = DP_NET_KECAMATAN_counts_cluster_1.sum()
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x=DP_NET_KECAMATAN_counts_cluster_1.index, y=DP_NET_KECAMATAN_counts_cluster_1.values, palette='viridis', ax=ax)
        ax.set_xlabel('DP NET_KABUPATEN')
        ax.set_ylabel('Frekuensi')
        ax.set_title(f'Top 10 Penjualan Sepeda Motor Per Kabupaten (Cluster 0)\nTotal Penjualan: {total_penjualan_cluster_1}')
        plt.xticks(rotation=90)
        for p in ax.patches:
            ax.annotate(format(p.get_height(), '.0f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom', xytext=(0, 5), textcoords='offset points')
        st.pyplot(fig)

        # Membuat plot bar untuk Cluster 2
        st.subheader('Top 10 Penjualan Sepeda Motor Per Kabupaten (Cluster 1)')
        cluster_2_data = dataset[dataset['f_cluster'] == 1]
        DP_NET_KECAMATAN_counts_cluster_2 = cluster_2_data['DP NET_KABUPATEN'].value_counts().head(10)
        total_penjualan_cluster_2 = DP_NET_KECAMATAN_counts_cluster_2.sum()
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x=DP_NET_KECAMATAN_counts_cluster_2.index, y=DP_NET_KECAMATAN_counts_cluster_2.values, palette='viridis', ax=ax)
        ax.set_xlabel('DP NET_KABUPATEN')
        ax.set_ylabel('Frekuensi')
        ax.set_title(f'Top 10 Penjualan Sepeda Motor Per Kabupaten (Cluster 1)\nTotal Penjualan: {total_penjualan_cluster_2}')
        plt.xticks(rotation=90)
        for p in ax.patches:
            ax.annotate(format(p.get_height(), '.0f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom', xytext=(0, 5), textcoords='offset points')
        st.pyplot(fig)
    else:
        st.write("Data tidak mencukupi untuk menampilkan plot bar.")
    
    dataset['TENOR_KELURAHAN'] = dataset['TENOR'].astype(str) + ' - ' + dataset['KELURAHAN']

    # Memfilter data hanya untuk yang memiliki 100 baris atau lebih
    if len(dataset) >= 100:
        # Membuat plot bar untuk Cluster 1
        st.subheader('Top 10 Penjualan Sepeda Motor Per Kelurahan (Cluster 0)')
        cluster_1_data = dataset[dataset['f_cluster'] == 0]
        DP_NET_KECAMATAN_counts_cluster_1 = cluster_1_data['TENOR_KELURAHAN'].value_counts().head(10)
        total_penjualan_cluster_1 = DP_NET_KECAMATAN_counts_cluster_1.sum()
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x=DP_NET_KECAMATAN_counts_cluster_1.index, y=DP_NET_KECAMATAN_counts_cluster_1.values, palette='viridis', ax=ax)
        ax.set_xlabel('TENOR_KELURAHAN')
        ax.set_ylabel('Frekuensi')
        ax.set_title(f'Top 10 Penjualan Sepeda Motor Per Kelurahan (Cluster 0)\nTotal Penjualan: {total_penjualan_cluster_1}')
        plt.xticks(rotation=90)
        for p in ax.patches:
            ax.annotate(format(p.get_height(), '.0f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom', xytext=(0, 5), textcoords='offset points')
        st.pyplot(fig)

        # Membuat plot bar untuk Cluster 2
        st.subheader('Top 10 Penjualan Sepeda Motor Per Kelurahaan (Cluster 1)')
        cluster_2_data = dataset[dataset['f_cluster'] == 1]
        DP_NET_KECAMATAN_counts_cluster_2 = cluster_2_data['TENOR_KELURAHAN'].value_counts().head(10)
        total_penjualan_cluster_2 = DP_NET_KECAMATAN_counts_cluster_2.sum()
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x=DP_NET_KECAMATAN_counts_cluster_2.index, y=DP_NET_KECAMATAN_counts_cluster_2.values, palette='viridis', ax=ax)
        ax.set_xlabel('TENOR_KELURAHAAN')
        ax.set_ylabel('Frekuensi')
        ax.set_title(f'Top 10 Penjualan Sepeda Motor Per Kelurahaan (Cluster 1)\nTotal Penjualan: {total_penjualan_cluster_2}')
        plt.xticks(rotation=90)
        for p in ax.patches:
            ax.annotate(format(p.get_height(), '.0f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom', xytext=(0, 5), textcoords='offset points')
        st.pyplot(fig)
    else:
        st.write("Data tidak mencukupi untuk menampilkan plot bar.")
    
    
    dataset['TENOR_KECAMATAN'] = dataset['TENOR'].astype(str) + ' - ' + dataset['KECAMATAN']

    # Memfilter data hanya untuk yang memiliki 100 baris atau lebih
    if len(dataset) >= 100:
        # Membuat plot bar untuk Cluster 1
        st.subheader('Top 10 Penjualan Sepeda Motor Per Kecamatan (Cluster 0)')
        cluster_1_data = dataset[dataset['f_cluster'] == 0]
        DP_NET_KECAMATAN_counts_cluster_1 = cluster_1_data['TENOR_KECAMATAN'].value_counts().head(10)
        total_penjualan_cluster_1 = DP_NET_KECAMATAN_counts_cluster_1.sum()
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x=DP_NET_KECAMATAN_counts_cluster_1.index, y=DP_NET_KECAMATAN_counts_cluster_1.values, palette='viridis', ax=ax)
        ax.set_xlabel('TENOR_KECAMATAN')
        ax.set_ylabel('Frekuensi')
        ax.set_title(f'Top 10 Penjualan Sepeda Motor Per Kecamatan (Cluster 0)\nTotal Penjualan: {total_penjualan_cluster_1}')
        plt.xticks(rotation=90)
        for p in ax.patches:
            ax.annotate(format(p.get_height(), '.0f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom', xytext=(0, 5), textcoords='offset points')
        st.pyplot(fig)

        # Membuat plot bar untuk Cluster 2
        st.subheader('Top 10 Penjualan Sepeda Motor Per Kecamatan (Cluster 1)')
        cluster_2_data = dataset[dataset['f_cluster'] == 1]
        DP_NET_KECAMATAN_counts_cluster_2 = cluster_2_data['TENOR_KECAMATAN'].value_counts().head(10)
        total_penjualan_cluster_2 = DP_NET_KECAMATAN_counts_cluster_2.sum()
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x=DP_NET_KECAMATAN_counts_cluster_2.index, y=DP_NET_KECAMATAN_counts_cluster_2.values, palette='viridis', ax=ax)
        ax.set_xlabel('TENOR_KECAMATAN')
        ax.set_ylabel('Frekuensi')
        ax.set_title(f'Top 10 Penjualan Sepeda Motor Per Kecamatan (Cluster 1)\nTotal Penjualan: {total_penjualan_cluster_2}')
        plt.xticks(rotation=90)
        for p in ax.patches:
            ax.annotate(format(p.get_height(), '.0f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom', xytext=(0, 5), textcoords='offset points')
        st.pyplot(fig)
    else:
        st.write("Data tidak mencukupi untuk menampilkan plot bar.")
    
    dataset['TENOR_KABUPATEN'] = dataset['DP NET'].astype(str) + ' - ' + dataset['KABUPATEN']

    # Memfilter data hanya untuk yang memiliki 100 baris atau lebih
    if len(dataset) >= 100:
        # Membuat plot bar untuk Cluster 1
        st.subheader('Top 10 Penjualan Sepeda Motor Per Kabupaten (Cluster 0)')
        cluster_1_data = dataset[dataset['f_cluster'] == 0]
        DP_NET_KECAMATAN_counts_cluster_1 = cluster_1_data['TENOR_KABUPATEN'].value_counts().head(10)
        total_penjualan_cluster_1 = DP_NET_KECAMATAN_counts_cluster_1.sum()
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x=DP_NET_KECAMATAN_counts_cluster_1.index, y=DP_NET_KECAMATAN_counts_cluster_1.values, palette='viridis', ax=ax)
        ax.set_xlabel('KABUPATEN')
        ax.set_ylabel('Frekuensi')
        ax.set_title(f'Top 10 Penjualan Sepeda Motor Per Kabupaten (Cluster 0)\nTotal Penjualan: {total_penjualan_cluster_1}')
        plt.xticks(rotation=90)
        for p in ax.patches:
            ax.annotate(format(p.get_height(), '.0f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom', xytext=(0, 5), textcoords='offset points')
        st.pyplot(fig)

        # Membuat plot bar untuk Cluster 2
        st.subheader('Top 10 Penjualan Sepeda Motor Per Kabupaten (Cluster 1)')
        cluster_2_data = dataset[dataset['f_cluster'] == 1]
        DP_NET_KECAMATAN_counts_cluster_2 = cluster_2_data['TENOR_KABUPATEN'].value_counts().head(10)
        total_penjualan_cluster_2 = DP_NET_KECAMATAN_counts_cluster_2.sum()
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x=DP_NET_KECAMATAN_counts_cluster_2.index, y=DP_NET_KECAMATAN_counts_cluster_2.values, palette='viridis', ax=ax)
        ax.set_xlabel('TENOR_KABUPATEN')
        ax.set_ylabel('Frekuensi')
        ax.set_title(f'Top 10 Penjualan Sepeda Motor Per Kabupaten (Cluster 1)\nTotal Penjualan: {total_penjualan_cluster_2}')
        plt.xticks(rotation=90)
        for p in ax.patches:
            ax.annotate(format(p.get_height(), '.0f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom', xytext=(0, 5), textcoords='offset points')
        st.pyplot(fig)
    else:
        st.write("Data tidak mencukupi untuk menampilkan plot bar.")
    
    
    





else:
    st.write("Silakan upload file dataset terlebih dahulu.")
