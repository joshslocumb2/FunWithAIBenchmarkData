# File Name : Spearow_Assignment08
# Student Name: Richie James, Josh Slocumb, Caitlin Hutchins
# email: james2c4@mail.uc.edu slocumjt@mail.uc.edu hutchicu@mail.uc.edu08
# Due Date:  3/27/25
# Course #/Section:  IS 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Group assignment showing a team logo and bar chart
 
# Brief Description of what this module does: This module shows our team logo and data visualization by calling them from our packages
# Citations: ChatGPT, Perplexity AI
 
# Anything else that's relevant:

from teamPackage.team_image_display import team_image_display

team_image_display("https://www.postavy.cz/foto/spearow-foto.jpg")
 #SPECIFIC URL INSERTED
 
import pandas as pd
import matplotlib.pyplot as plt
 
def count_letters_in_column(file_path, column_index=5, letters=["a", "b", "c", "d"]):
    try:
        df = pd.read_csv(file_path)
        if column_index >= len(df.columns):
            raise IndexError(f"Column index {column_index} is out of range for this dataset.")
        column_data = df.iloc[:, column_index].astype(str)
        letter_counts = {letter: 0 for letter in letters}
        for entry in column_data:
            for letter in letters:
                letter_counts[letter] += entry.lower().count(letter)
        return letter_counts
    except Exception as e:
        print(f"Error processing file: {e}")
        return {}
 
def plot_letter_counts(letter_counts):
    try:
        letters = list(letter_counts.keys())
        counts = list(letter_counts.values())
        plt.figure(figsize=(8, 5))
        plt.bar(letters, counts, color=['red', 'blue', 'green', 'purple'])
        plt.xlabel("Letters")
        plt.ylabel("Frequency")
        plt.title("Count of Answers")
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()
    except Exception as e:
        print(f"Error generating plot: {e}")
 
def main():
    file_path = "dataPackage/MMLU/data/nutrition_test.csv"
    letter_counts = count_letters_in_column(file_path)
    if letter_counts:
        print("Letter Counts:", letter_counts)
        plot_letter_counts(letter_counts)
 
if __name__ == "__main__":
    main()

