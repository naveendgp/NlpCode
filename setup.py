from setuptools import setup, find_packages

setup(
    name="your_package_name",
    version="0.1",
    author="Your Name",
    author_email="your.email@example.com",
    description="A short description of the package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",  # Specify markdown format
    url="https://github.com/yourusername/yourproject",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        # e.g., 'requests', 'numpy', etc.
    ],
)
