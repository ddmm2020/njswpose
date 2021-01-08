import setuptools

with open("README.md", 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="njswpose",
    version="0.1.5",
    author="ddmm",
    author_email="1126557295@qq.com",
    description="Detection human body keypoints",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ddmm2020/njswpose",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
