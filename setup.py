from setuptools import setup, find_packages

setup(
    name="security_package",  # The name of your new merged package
    version="0.1",           # Version number
    author="Udit Raj Singh",
    author_email="uditrajsingh815@example.com",
    description="A merged package combining gitleaks and zap",
    packages=find_packages(),  # Automatically find all packages
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': [
            'install-gitleaks=gitleaks.gitleaks_installer.installer:install_gitleaks',
            'add-gitleaks-path=gitleaks.gitleaks_installer.installer:add_gitleaks_to_path',
            'install-zap=zap.zap_installer.zap:main',
        ],
    },
    
    python_requires='>=3.6',  # Specify the minimum Python version required
    install_requires=[
        "requests>=2.25.1",  # Requests package to handle the download

    ],
    include_package_data=True,
    zip_safe=False,
)


