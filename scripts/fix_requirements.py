def fix_requirements():
    """
    When we run pipreqs it adds 'skimage==0.0' to requirments.txt
    This create issue. This script automatically replace 'skimage==0.0'
    with scikit-image==0.22.0
    """
    try:
        with open("requirements.txt", "r") as file:
            requirements = file.read()

        updated_requirements = requirements.replace("skimage==0.0", "scikit-image==0.22.0")
        updated_requirements = updated_requirements.replace("numpy==", "numpy==1.16")

        with open("requirements.txt", "w") as file:
            file.write(updated_requirements)

        print("Successfully updated requirements.txt")

    except FileNotFoundError:
        print("Error: requirements.txt not found")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    fix_requirements()
