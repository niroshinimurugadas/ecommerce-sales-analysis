import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Set page config
st.set_page_config(page_title="Ecommerce Sales Analysis", layout="wide")
# Title
st.title("📊 Ecommerce Sales Analysis Dashboard")

# Load the dataset
sales = pd.read_csv(r"C:/Users/fastt/Desktop/salesanalysis/ecommerce_sales_analysis.csv")

# Transform data
sales_long = sales.melt(
    id_vars=['category', 'price'],
    value_vars=[col for col in sales.columns if col.startswith('sales_month_')],
    var_name='month',
    value_name='monthly_sales'
)
sales_long['revenue'] = sales_long['price'] * sales_long['monthly_sales']
total_sales = sales_long['revenue'].sum(skipna=True)

# Most popular category
most_popular_product = (
    sales_long.groupby('category')
    .size()
    .reset_index(name='count_category')
    .sort_values(by='count_category', ascending=False)
    .head(1)
)

# Revenue per category
revenue_per_product = (
    sales_long.groupby('category')['revenue']
    .sum()
    .reset_index()
    .sort_values(by='revenue', ascending=False)
)

# Show total sales
st.metric("💰 Total Sales Revenue", f"${total_sales:,.2f}")

# Show most popular product category
st.subheader("🔥 Most Popular Product Category")
st.dataframe(most_popular_product)

# Revenue by product category chart
st.subheader("📈 Revenue by Product Category")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=revenue_per_product, x='category', y='revenue', palette='Set2', ax=ax)
ax.set_title("Revenue by Product Category")
ax.set_xlabel("Category")
ax.set_ylabel("Revenue")
plt.xticks(rotation=90)
st.pyplot(fig)

# Show revenue per product category table
st.subheader("📋 Revenue Table")
st.dataframe(revenue_per_product)