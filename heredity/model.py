import pandas as pd
from probability import calculate_probabilities


class GeneticTraitPredictorModel:
    def __init__(self):
        pass

    def predict(self, csv_file):
        data = pd.read_csv(csv_file)
        results = calculate_probabilities(data)
        report = ""
        for name, probabilities in results.items():
            report += f"{name}:\n"
            report += "  Gene:\n"
            for gene, prob in probabilities['gene'].items():
                report += f"    {gene}: {prob:.4f}\n"
            report += "  Trait:\n"
            for trait, prob in probabilities['trait'].items():
                report += f"    {trait}: {prob:.4f}\n"
            report += "\n"
        return report
