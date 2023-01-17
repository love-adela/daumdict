from setuptools import setup, find_packages

setup(name="daumdict",
      version="0.2",
      description="find a word from daum dict.",
      url="https://github.com/love-adela/daumdict",
      author="love-adela",
      author_email="love.adelar@gmail.com",
      license="MIT",
      packages=find_packages(),
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
      ],
      install_requires=["requests", "BeautifulSoup4"],
      python_requires=">=3.8",
)
