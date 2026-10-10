import streamlit as st
import pandas as pd

# Why: Set the title and layout of our dashboard
st.set_page_config(
    page_title="Customer Personality Analyzer",
    layout="wide"
)

# Why: Show the main heading of the dashboard
st.title("🛍️ Customer Personality & Shopping Behavior Analyzer")

# Why: Load our final customer segmentation data
df = pd.read_csv("rfm_customer_segments.csv")

# Why: Calculate important business KPIs for the dashboard
total_customers = df["CustomerID"].nunique()
total_revenue = df["Monetary"].sum()
avg_frequency = df["Frequency"].mean()
avg_Monetary = df["Monetary"].mean()

# Why: Create 4 columns so each KPI appears as a separate card
col1, col2, col3, col4 = st.columns(4)

# Why: Display the total number of unique customers
col1.metric("👥 Total Customers", total_customers)

# Why: Display total customer spending
col2.metric("💰 Total Revenue", f"₹{total_revenue:,.2f}")

# Why: Display average number of transactions per customer
col3.metric("🔄 Avg Frequency", f"{avg_frequency:.2f}")

# Why: Display average spending per customer
col4.metric("💵 Avg Monetary", f"₹{avg_Monetary:,.2f}")


import matplotlib.pyplot as plt
import seaborn as sns

# Why: Count how many customers belong to each segment
segment_counts = df["Segment"].value_counts()

# Why: Create a chart area for the segment distribution
st.subheader("Customer Segment Distribution")

fig, ax = plt.subplots()

# Why: Visualize the number of customers in each segment
sns.barplot(
    x=segment_counts.index,
    y=segment_counts.values,
    ax=ax
)

# Why: Make the chart easier to read
ax.set_xlabel("Customer Segment")
ax.set_ylabel("Number of Customers")
ax.tick_params(axis="x", rotation=20)

# Why: Display the chart in Streamlit
st.pyplot(fig)


# Why: Show the distribution of the three main RFM features
st.subheader("RFM Analysis")

# Why: Create three separate chart areas
col1, col2, col3 = st.columns(3)

# ---------------- Recency ----------------
with col1:
    fig1, ax1 = plt.subplots()

    # Why: Show how many customers have different Recency values
    sns.histplot(
        df["Recency"],
        bins=20,
        kde=True,
        ax=ax1
    )

    ax1.set_title("Recency Distribution")
    ax1.set_xlabel("Recency (Days)")
    ax1.set_ylabel("Customers")

    st.pyplot(fig1)

# ---------------- Frequency ----------------
with col2:
    fig2, ax2 = plt.subplots()

    # Why: Show the distribution of customer purchase frequency
    sns.histplot(
        df["Frequency"],
        bins=15,
        kde=True,
        ax=ax2
    )

    ax2.set_title("Frequency Distribution")
    ax2.set_xlabel("Number of Transactions")
    ax2.set_ylabel("Customers")

    st.pyplot(fig2)

# ---------------- Monetary ----------------
with col3:
    fig3, ax3 = plt.subplots()

    # Why: Show how customer spending is distributed
    sns.histplot(
        df["Monetary"],
        bins=20,
        kde=True,
        ax=ax3
    )

    ax3.set_title("Monetary Distribution")
    ax3.set_xlabel("Customer Spending")
    ax3.set_ylabel("Customers")

    st.pyplot(fig3)


# Why: Calculate average RFM values for each customer segment
segment_profile = df.groupby("Segment")[
    ["Recency", "Frequency", "Monetary"]
].mean()

# Why: Create a section for comparing customer segments
st.subheader("Segment RFM Comparison")

# Why: Create three chart areas
col1, col2, col3 = st.columns(3)

# ---------------- Recency Comparison ----------------
with col1:
    fig1, ax1 = plt.subplots()

    # Why: Compare average Recency across segments
    segment_profile["Recency"].plot(
        kind="bar",
        ax=ax1
    )

    ax1.set_title("Average Recency")
    ax1.set_xlabel("Segment")
    ax1.set_ylabel("Days")
    ax1.tick_params(axis="x", rotation=90)

    st.pyplot(fig1)

# ---------------- Frequency Comparison ----------------
with col2:
    fig2, ax2 = plt.subplots()

    # Why: Compare average purchase frequency across segments
    segment_profile["Frequency"].plot(
        kind="bar",
        ax=ax2
    )

    ax2.set_title("Average Frequency")
    ax2.set_xlabel("Segment")
    ax2.set_ylabel("Transactions")
    ax2.tick_params(axis="x", rotation=90)

    st.pyplot(fig2)

# ---------------- Monetary Comparison ----------------
with col3:
    fig3, ax3 = plt.subplots()

    # Why: Compare average customer spending across segments
    segment_profile["Monetary"].plot(
        kind="bar",
        ax=ax3
    )

    ax3.set_title("Average Monetary")
    ax3.set_xlabel("Segment")
    ax3.set_ylabel("Spending")
    ax3.tick_params(axis="x", rotation=90)

    st.pyplot(fig3)


# Why: Create a separate section for the selected customer's profile
st.subheader("🔎 Selected Customer Profile")

# Why: Let the user choose one customer from the dropdown
selected_customer = st.selectbox(
    "Select a Customer ID:",
    df["CustomerID"].unique()
)

customer_data = df[df["CustomerID"] == selected_customer].iloc[0]

# Why: Create columns to display the customer's RFM information
col1, col2, col3 = st.columns(3)

col1.metric(
    "Recency",
    f"{customer_data['Recency']} days"
)

col2.metric(
    "Frequency",
    f"{customer_data['Frequency']}"
)

col3.metric(
    "Monetary",
    f"₹{customer_data['Monetary']:,.2f}"
)

# Why: Display the customer's cluster and business segment
st.write("**Cluster:**", customer_data["Cluster"])
st.write("**Customer Segment:**", customer_data["Segment"])

# Why: Display the marketing recommendation for the selected customer
st.success(
    f"💡 Marketing Recommendation: "
    f"{customer_data['Recommendation']}"
)



# Why: Select only the important customer information for the dashboard
display_columns = [
    "CustomerID",
    "Recency",
    "Frequency",
    "Monetary",
    "Cluster",
    "Segment",
    "Recommendation"
]

# Why: Show a clean and interactive customer table
st.subheader("Customer Segmentation Data")

st.dataframe(
    df[display_columns],
    use_container_width=True,
    hide_index=True
)

