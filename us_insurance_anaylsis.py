import csv

# 1. DATA LOADING SECTION
# Initializing empty lists to store raw data from insurance.csv
ages, smoker_statuses, insurance_charges, regions, bmis = [], [], [], [], []

with open('insurance.csv') as csv_info:
    csv_dict = csv.DictReader(csv_info)
    for row in csv_dict:
        ages.append(row['age'])
        smoker_statuses.append(row['smoker'])
        insurance_charges.append(row['charges'])
        regions.append(row['region'])
        bmis.append(row['bmi'])

# 2. ANALYSIS CLASS DEFINITION
class PatientAnalysis:
    """
    A class to perform structured analysis on U.S. Medical Insurance data.
    Demonstrates data segmentation, categorical bucketing, and financial auditing.
    """
    def __init__(self, ages, charges, smokers, regions, bmis):
        self.smokers_records = []
        self.nonsmokers_records = []
        
        # Zip and bundle data into dictionaries for easier iteration
        for i in range(len(smokers)):
            record = {
                "age": int(ages[i]), 
                "charge": float(charges[i]),
                "bmi": float(bmis[i]),
                "region": regions[i]
            }
            if smokers[i] == 'yes':
                self.smokers_records.append(record)
            else:
                self.nonsmokers_records.append(record)

    def analyze_smoking_by_age(self):
        """Calculates the 'Smoking Premium' (cost difference) across different age decades."""
        print("--- Question 1: Smoking Premium by Age Group ---")
        smoker_ages = {"20s": [], "30s": [], "40s": [], "50s": [], "60s": []}
        nonsmoker_ages = {"20s": [], "30s": [], "40s": [], "50s": [], "60s": []}

        for record in self.smokers_records:
            age = record["age"]
            if age < 30: smoker_ages["20s"].append(record["charge"])
            elif age < 40: smoker_ages["30s"].append(record["charge"])
            elif age < 50: smoker_ages["40s"].append(record["charge"])
            elif age < 60: smoker_ages["50s"].append(record["charge"])
            else: smoker_ages["60s"].append(record["charge"])

        for record in self.nonsmokers_records:
            age = record["age"]
            if age < 30: nonsmoker_ages["20s"].append(record["charge"])
            elif age < 40: nonsmoker_ages["30s"].append(record["charge"])
            elif age < 50: nonsmoker_ages["40s"].append(record["charge"])
            elif age < 60: nonsmoker_ages["50s"].append(record["charge"])
            else: nonsmoker_ages["60s"].append(record["charge"])

        for decade in smoker_ages:
            if len(smoker_ages[decade]) > 0 and len(nonsmoker_ages[decade]) > 0:
                premium = (sum(smoker_ages[decade])/len(smoker_ages[decade])) - (sum(nonsmoker_ages[decade])/len(nonsmoker_ages[decade]))
                print(f"{decade}: Smokers pay ${premium:,.2f} more than non-smokers.")

    def find_bmi_tipping_point(self):
        """Identifies the BMI range where insurance charges spike, segmented by smoker status."""
        print("\n--- Question 2: BMI Tipping Point Analysis ---")
        smoker_bmi_costs = {"Healthy": [], "Overweight": [], "Obese": [], "Extreme": []}
        non_smoker_bmi_costs = {"Healthy": [], "Overweight": [], "Obese": [], "Extreme": []}

        for record in self.smokers_records:
            bmi = record["bmi"]
            if bmi < 25: smoker_bmi_costs["Healthy"].append(record["charge"])
            elif bmi < 30: smoker_bmi_costs["Overweight"].append(record["charge"])
            elif bmi < 35: smoker_bmi_costs["Obese"].append(record["charge"])
            else: smoker_bmi_costs["Extreme"].append(record["charge"])

        for record in self.nonsmokers_records:
            bmi = record["bmi"]
            if bmi < 25: non_smoker_bmi_costs["Healthy"].append(record["charge"])
            elif bmi < 30: non_smoker_bmi_costs["Overweight"].append(record["charge"])
            elif bmi < 35: non_smoker_bmi_costs["Obese"].append(record["charge"])
            else: non_smoker_bmi_costs["Extreme"].append(record["charge"])

        for cat in ["Healthy", "Overweight", "Obese", "Extreme"]:
            if len(smoker_bmi_costs[cat]) > 0 and len(non_smoker_bmi_costs[cat]) > 0:
                s_avg = sum(smoker_bmi_costs[cat]) / len(smoker_bmi_costs[cat])
                ns_avg = sum(non_smoker_bmi_costs[cat]) / len(non_smoker_bmi_costs[cat])
                print(f"{cat} BMI: Smokers Avg ${s_avg:,.2f} | Non-Smokers Avg ${ns_avg:,.2f}")

    def regional_cost_variance(self):
        """Analyzes geographic data to find the average cost per US region."""
        print("\n--- Question 3: Regional Cost Variance ---")
        regional_costs = {"southwest": [], "southeast": [], "northwest": [], "northeast": []}
        combined = self.smokers_records + self.nonsmokers_records
        
        for record in combined:
            region = record["region"]
            if region in regional_costs:
                regional_costs[region].append(record["charge"])

        for region, costs in regional_costs.items():
            if len(costs) > 0:
                avg = sum(costs) / len(costs)
                print(f"Average cost in the {region.title()}: ${avg:,.2f}")

# 3. EXECUTION BLOCK
analysis = PatientAnalysis(ages, insurance_charges, smoker_statuses, regions, bmis)

# Triggering all analysis methods
analysis.analyze_smoking_by_age()
analysis.find_bmi_tipping_point()
analysis.regional_cost_variance()