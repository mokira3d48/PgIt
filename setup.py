import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "pgit",
    version = "0.1.0",
    author = "Arnold Mokira",
    author_email = "dr.mokira@gmail.com",
    description = (
        "Progress iterator for feed back program execution."
    ),
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/mokira3d48/pgit",
    project_urls = {
        "Bug Tracker": "package issues URL",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.7"
)
