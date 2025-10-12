import os

def add_spoons_carpet(interactive=True):
    if interactive:
        
        folder_path = "./assets/spoons-carpet/"
        image_path = input(f"Enter the path to the image (e.g., yourimage.jpg)\n Current folder is {folder_path} \n")
        while not os.path.isfile(folder_path + image_path):
            print("Error: File does not exist. Please try again.")
            image_path = input(f"Enter the path to the image (e.g., yourimage.jpg)\n Current folder is {folder_path} \n")
        print(f"Image found: {folder_path + image_path}")


        title = input("Enter the title of the review (e.g., 'Hemel Hempstead'): ")
        rating = input("Enter the rating (1-5): ")
        description = input("Enter the description of the review: ")

        md_folder = "_spoons-carpet"
        md_filename = f"{md_folder}/{title.replace(' ', '-').lower()}.md"

        with open(md_filename, "w", encoding="utf-8") as f:
            f.write("---\n")
            f.write(f"title: {title}\n")
            f.write(f"image: '{folder_path + image_path}'\n")
            f.write(f"rating: {rating}\n")
            f.write("---\n\n")
            f.write(f"{description}\n")
        print(f"Markdown file created: {md_filename}")
        

