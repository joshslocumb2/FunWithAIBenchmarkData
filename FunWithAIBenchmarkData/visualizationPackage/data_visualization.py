# File Name : Spearow_Assignment08
# Student Name: Richie James, Josh Slocumb, Caitlin Hutchins
# email: james2c4@mail.uc.edu slocumjt@mail.uc.edu hutchicu@mail.uc.edu08
# Due Date:  3/27/25
# Course #/Section:  IS 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Group assignment showing a team logo and bar chart
 
# Brief Description of what this module does: This module creates a bar chart reflecting the nutrition data file
# Citations: ChatGPT, Perplexity AI
 
# Anything else that's relevant:n/a
 
import matplotlib.pyplot as plt

def count_letters_in_column(file_path, column_index=5, letters=["a", "b", "c", "d"]):
    """
    Reads a CSV file, extracts the specified column, and counts occurrences of given letters.

    @param file_path str: The path to the CSV file.
    @param column_index int: The column index to analyze (default is 5, which is the 6th column).
    @param letters list: List of letters to count.
    @return dict: Dictionary with letter counts.
    """
    try:
        # Read CSV file
        df = pd.read_csv(file_path)

        # Ensure column exists
        if column_index >= len(df.columns):
            raise IndexError(f"Column index {column_index} is out of range for this dataset.")

        # Extract the target column
        column_data = df.iloc[:, column_index].astype(str)  # Convert to string to avoid NaN issues

        # Initialize count dictionary
        letter_counts = {letter: 0 for letter in letters}

        # Count occurrences of each letter
        for entry in column_data:
            for letter in letters:
                letter_counts[letter] += entry.lower().count(letter)

        return letter_counts

    except Exception as e:
        print(f"Error processing file: {e}")
        return {}

def plot_letter_counts(letter_counts):
    """
    Plots a bar graph of letter counts.

    @param letter_counts dict: Dictionary of letter counts.
    """
    try:
        # Extract data
        letters = list(letter_counts.keys())
        counts = list(letter_counts.values())

        # Create bar graph
        plt.figure(figsize=(8, 5))
        plt.bar(letters, counts, color=['red', 'blue', 'green', 'purple'])

        # Add labels and title
        plt.xlabel("Letters")
        plt.ylabel("Frequency")
        plt.title("Nutrition Letter Frequency")
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        # Display the plot
        plt.show()

    except Exception as e:
        print(f"Error generating plot: {e}")

# Example Usage (replace 'your_file.csv' with an actual CSV file path)
file_path = "your_file.csv"  # Update this path
letter_counts = count_letters_in_column(file_path)

# Check results before plotting
if letter_counts:
    print("Letter Counts:", letter_counts)
    plot_letter_counts(letter_counts)
