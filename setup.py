import setuptools


setuptools.setup(
    name="hotpp-benchmark",
    version="0.0.1",
    description="Evaluate generative event sequence models on the long horizon prediction task.",
    packages=setuptools.find_packages(include=["hotpp", "hotpp.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=[
        "datasets",
        "hydra-core>=1.1.2",
        "lightgbm",
        "numpy>=1.23",
        "ptls-validation @ git+https://git@github.com/dllllb/ptls-validation.git#egg=ptls-validation",
        "pyarrow>=14.0.0",
        "pyspark>=3",
        "pytorch-lifestream>=0.6.0",
        "pytorch-lightning",
        "scikit-learn>=1.3.2",
        "scipy>=1.11",
        "torch-linear-assignment", # Anonymized, install from current folder.
        "tqdm",
    ],
)
