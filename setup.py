from setuptools import setup, find_packages

setup(
    name="hand",  # Replace with your package name
    version="0.1.0",    # Initial version
    author="W.Achila Apollon",
    author_email="dev@achila",
    description="foundational deep learning model is designed to serve as a starting point for training various 3D heustric behaviors and capabilities",
    long_description=open("README.md").read().splitlines()[5],
    long_description_content_type="text/markdown",
    url="https://github.com/alapollon/hand.git",  # Repository URL
    packages=find_packages(

            

        ),  # Automatically find sub-packages
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
