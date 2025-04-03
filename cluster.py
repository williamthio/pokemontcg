import pandas as pd
import matplotlib.pyplot as plt
from scipy.sparse import hstack
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import silhouette_score

# Load the CSV File
file_path = "tournament_decks.csv"
data = pd.read_csv(file_path)

# Parse the "cards" column to extract card links, counts, and types as features
def parse_cards_with_types(cards):
    card_list = cards.split('|')
    card_features = {"p": {}, "t": {}, "e": {}}
    for card in card_list:
        parts = card.split('#')
        if len(parts) >= 3:
            card_type = parts[0].lower() # Extract card type (e.g., "pokemon", "trainer", "energy")
            card_link = parts[3]         # Use the card link as the feature
            card_count = int(parts[2])   # Use the card count as the value
            if card_type in card_features:
                card_features[card_type][card_link] = card_count
    return card_features

card_features_with_types = data['cards'].apply(parse_cards_with_types)

# Separate features by card type
pokemon_features = card_features_with_types.apply(lambda x: x['p'])
trainer_features = card_features_with_types.apply(lambda x: x['t'])
energy_features = card_features_with_types.apply(lambda x: x['e'])

# Convert each card type into a feature matrix
vectorizer = DictVectorizer(sparse=True)
pokemon_matrix = vectorizer.fit_transform(pokemon_features)
trainer_matrix = vectorizer.fit_transform(trainer_features)
energy_matrix = vectorizer.fit_transform(energy_features)

# Weight the features by card type (adjust weights as needed)
pokemon_weight = 1.0
trainer_weight = 0.3
energy_weight = 0.1

# Combine the weighted feature matrices
X_combined = hstack([
    pokemon_matrix * pokemon_weight,
    trainer_matrix * trainer_weight,
    energy_matrix * energy_weight
])

# Normalize the combined feature matrix
scaler = StandardScaler(with_mean=False)
X_scaled = scaler.fit_transform(X_combined)

# Find the optimal number of clusters
start_clusters = 300
end_clusters = 600
silhouette_scores = []
wcss = []
cluster_range = range(start_clusters, end_clusters + 1)
for n_clusters in cluster_range:
    print(f"Processing {n_clusters} clusters...")
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    cluster_labels = kmeans.fit_predict(X_scaled)
    silhouette_scores.append(silhouette_score(X_scaled, cluster_labels))
    wcss.append(kmeans.inertia_)

# Plot silhouette scores and WCSS and save the figure with HQ
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(cluster_range, silhouette_scores, marker='o')
plt.title('Silhouette Scores')
plt.xlabel('Number of Clusters')
plt.ylabel('Silhouette Score')
plt.grid()
plt.subplot(1, 2, 2)
plt.plot(cluster_range, wcss, marker='o')
plt.title('WCSS (Within-Cluster Sum of Squares)')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.grid()
plt.tight_layout()
plt.savefig('silhouette_wcss.png')

# Determine the optimal number of clusters based on silhouette scores
num_clusters = silhouette_scores.index(max(silhouette_scores)) + start_clusters
print(f"Optimal number of clusters: {num_clusters}")

# Perform KMeans clustering with the optimal number of clusters
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
data['cluster'] = kmeans.fit_predict(X_scaled)

# Save the clustered data to a new CSV file
output_file_path = "clustered_tournament_decks.csv"
data.to_csv(output_file_path, index=False)
print(f"Clustered data saved to {output_file_path}")
