# File Name : Spearow_Assignment08
# Student Name: Richie James, Josh Slocumb, Caitlin Hutchins
# email: james2c4@mail.uc.edu slocumjt@mail.uc.edu hutchicu@mail.uc.edu08
# Due Date:  3/27/25
# Course #/Section:  IS 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Group assignment showing a team logo and bar chart
 
# Brief Description of what this module does: This module shows our team logo 
# Citations: ChatGPT
 
# Anything else that's relevant:n/a
 

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import urllib.request
from io import BytesIO
def team_image_display(image_url):
    """
   Display the team image from a URL using Matplotlib.

    @param image_url: str
        A direct link to an image file (e.g., .jpg, .png). The URL must be publicly accessible.
        Example: 'https://archives.bulbagarden.net/media/upload/2/2d/0021Spearow.png'

    @raises Exception:
        Raises an exception if the image cannot be loaded or displayed due to an invalid URL,
        network issues, or unsupported image format.

    @return: None
        Displays the image in a Matplotlib figure and prints a success message.
        If an error occurs, prints an error message instead.
    """
    try:
        #Open and read image from provided URL
        with urllib.request.urlopen(image_url) as url:
            img_data = BytesIO(url.read())
            img = plt.imread(img_data, format='jpg') #IMPORTANT: Assumes PNG format from the URL, ADJUST IF NEEDED!

        # Create figure with specific dimensions for 200x200 pixel display
        plt.figure(figsize=(2, 2))

        # Display the image
        plt.imshow(img)
        plt.axis('off')  # Hide axes for a clean display
        plt.title("Team Logo")
        plt.tight_layout()
        plt.show()  # Show but don't block execution

        print(f"Successfully displayed team image from URL: {image_url}")

    except Exception as e:
        print(f"Error displaying team image: {e}")
        print("Please ensure the image URL is correct, publicly accessible, and a valid image format.")
