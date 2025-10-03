import pandas as pd
from preprocesing_data import prepare_data

data = pd.read_csv('books.csv')
df = prepare_data(data)

data = {
    'mean': df['ratings_count'].mean(),
    'median':df['ratings_count'].median(),
    'mode':df['ratings_count'].mode().tolist(),
    'sum':df['ratings_count'].sum(),
    'count':df['ratings_count'].count(),
    'min':df['ratings_count'].min(),
    'max':df['ratings_count'].max()
}

for key, value in data.items():
    print(f"{key}: {value}")

df = pd.read_csv('products_dataset.csv')

aggregated_data = {
    'Mean Price': df['price'].mean(),
    'Median Rating': df['rating'].median(),
    'Mode Ratings_Count': df['rating'].mode().tolist(),
    'Total Stock': df['stock'].sum(),
    'Total Products': df['product_id'].count(),
    'Min Price': df['price'].min(),
    'Max Price': df['price'].max()
}

for key, value in aggregated_data.items():
    print(f"{key}: {value}")
 

data = pd.read_csv('books.csv')
df = prepare_data(data)
grouped_data = df.groupby("genre")

# for genre, group in grouped_data:
#     print(f"Genre: {genre}")
#     print(group)
#     print("-" * 60)

grouped_data = df.groupby("section")

# for section, group in grouped_data:
#     print(f"Section: {section}")
#     print(group)
#     print("-" * 60)



avg_price_per_genre = df.groupby("genre")["price"].mean().sort_values(ascending=False)
print(avg_price_per_genre)


rentals_per_author = df.groupby("author")["times_borrowed"].sum().sort_values(ascending=False)

print(rentals_per_author)

price_stats = df.groupby('genre').agg({
    "price": ['mean', 'median']
}).sort_values(("price", "mean"),ascending=True)

print(price_stats)


author_stats = df.groupby("author").agg({
    "times_borrowed": ["sum", "mean", "max"],
    "rating": ["max"],
    "ratings_count": ["sum"],
    "price": ["mean"]
})

author_stats_sorted = author_stats.sort_values(("times_borrowed", "sum"), ascending=False)

print(author_stats_sorted)