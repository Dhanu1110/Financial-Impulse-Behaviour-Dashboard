
np.random.seed(42)

num_users = 500
num_transactions = 20000

categories = ["Food", "Fashion", "Electronics",
              "Travel", "Grocery", "Entertainment", "Bills"]

start_date = datetime(2024, 1, 1)
data = []

user_avg_spend = {u: np.random.uniform(2000, 10000) for u in range(1, num_users+1)}

for i in range(num_transactions):
    user = np.random.randint(1, num_users+1)
    days_offset = np.random.randint(0, 180)
    transaction_time = start_date + timedelta(days=int(days_offset),
                                              hours=np.random.randint(0, 24),
                                              minutes=np.random.randint(0, 60))

    category = random.choice(categories)
    base_amount = np.random.normal(user_avg_spend[user]/30, 500)
    amount = abs(round(base_amount, 2))

    hour = transaction_time.hour
    weekend = 1 if transaction_time.weekday() >= 5 else 0
    night_transaction = 1 if hour >= 20 or hour <= 2 else 0
    discretionary = 1 if category in ["Fashion", "Entertainment", "Electronics"] else 0
    spending_spike = 1 if amount > user_avg_spend[user]/15 else 0
    short_time_gap = np.random.choice([0,1], p=[0.8,0.2])
    end_month_flag = 1 if transaction_time.day >= 25 else 0

    impulse_score = spending_spike + night_transaction + discretionary + short_time_gap + end_month_flag
    impulse_label = 1 if impulse_score >= 3 else 0

    data.append([user, transaction_time, amount, category,
                 hour, weekend, night_transaction,
                 discretionary, spending_spike,
                 short_time_gap, end_month_flag,
                 impulse_label])

df = pd.DataFrame(data, columns=[
    "user_id", "transaction_time", "amount",
    "merchant_category", "hour_of_day",
    "weekend_flag", "night_transaction",
    "discretionary_category",
    "spending_spike", "short_time_gap",
    "end_month_flag", "impulse_label"
])

df.head()
