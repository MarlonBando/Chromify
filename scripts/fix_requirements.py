import re

def fix_requirements():
    """
    When we run pipreqs it adds 'skimage==0.0' to requirments.txt
    This create issue. This script automatically replace 'skimage==0.0'
    with scikit-image==0.22.0
    """
    try:
        with open("requirements.txt", "r") as file:
            requirements = file.readlines()

        for i, requirement in enumerate(requirements):
            requirement = requirement.strip()
            if re.search(r'^numpy==', requirement):
                requirements[i] = "numpy==1.26.4\n"
            if requirement == "skimage==0.0":
                requirements[i] = "scikit-image==0.22.0\n"
        
        with open("requirements.txt", "w") as file:
            file.writelines(requirements)

        print("Successfully updated requirements.txt")

    except FileNotFoundError:
        print("Error: requirements.txt not found")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    fix_requirements()
