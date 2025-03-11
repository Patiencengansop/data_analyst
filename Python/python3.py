class DataAnalyst:
    def __init__(self, name, experience):
        self.name = name
        self.experience = experience

    def analyze_data(self, data):
        # Placeholder for data analysis logic
        print(f"{self.name} is analyzing data with {self.experience} years of experience.")

    def generate_report(self):
        # Placeholder for report generation logic
        print(f"{self.name} is generating a report.")
        
        
        df = fact_orders_grubhub_python .mer(dim_delivery_person_grubhub_python, on='Delivery_person_ID')
df = df.groupby('city_type'):agg({delivery_person_age: 'mean},{delivery_person_rating: 'mean'}).reset_index()