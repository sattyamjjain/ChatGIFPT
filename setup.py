import setuptools

with open('requirements.txt') as f:
     reqs = f.read().split('\n')

setuptools.setup(
    name='ChatGIFPT',
    version='0.0.1',
    scripts=[],
    author="Sattyam Jain",
    author_email="sattyamjain96@gmail.com",
    description="Library for GIF generator",
    url="https://github.com/sattyamjjain/ChatGIFPT.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=reqs
)