import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import io

# Streamlit app
def main():
    st.title("KMeans Clustering Analysis")

    # Upload dataset
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file is not None:
        # Load dataset
        dataset = pd.read_csv(uploaded_file)
        
        # Drop unnecessary columns
        dataset = dataset.drop(['KECAMATAN', 'KABUPATEN', 'NO'], axis=1)

        # Display the first few rows of the dataset
        st.write("Dataset:")
        st.dataframe(dataset.head())

        # Data preprocessing
        X = dataset.iloc[:, 0:7].values
        scaler = StandardScaler()
        X = scaler.fit_transform(X)

        # Elbow Method for determining the number of clusters
        wcss = []
        for i in range(1, 11):
            kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
            kmeans.fit(X)
            wcss.append(kmeans.inertia_)
        plt.plot(range(1, 11), wcss)
        plt.title('Elbow Method')
        plt.xlabel('Cluster Number')
        plt.ylabel('WCSS')
        st.pyplot()

        # Slider to choose the number of clusters
        n_clusters = st.slider("Choose the number of clusters:", 2, 10, 3)
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        cluster_labels = kmeans.fit_predict(X)
        dataset['f_cluster'] = cluster_labels  

        # Display the processed dataset
        st.write("Processed Dataset:")
        st.dataframe(dataset)

        # 3D Scatter plot
        fig = plt.figure(figsize=(7, 7))
        ax = fig.add_subplot(111, projection='3d')
        for cluster_number in range(n_clusters):
            ax.scatter(X[cluster_labels == cluster_number, 0], X[cluster_labels == cluster_number, 1], X[cluster_labels == cluster_number, 2],
                       s=40, label=f"cluster {cluster_number + 1}")
        ax.set_xlabel('kelurahan')
        ax.set_ylabel('Jenis Kendaraan')
        ax.set_zlabel('jenis Merk')
        ax.legend()
        ax.set_title('3D Scatter Plot with Clusters')
        st.pyplot(fig)

        # Export the processed dataset
        csv_export = dataset.to_csv(index=False)
        st.download_button(label="Export Processed Dataset", data=io.BytesIO(csv_export.encode()), file_name="processed_dataset.csv")

if __name__ == "__main__":
    main()
