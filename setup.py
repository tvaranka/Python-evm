from setuptools import setup, find_packages

setup(
    name='py_evm',
    version='0.1.0',
    packages=find_packages(include=['py_evm', 'py_evm.*']),
    install_requires=[
        "numpy",
        "torch",
        "opencv-python",
        "scikit-image",
        "matplotlib"
    ]
)
