from setuptools import setup, find_packages

setup(
    name='your_project_name',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'dotenv',
        'qiskit',
        'qiskit-ibm-runtime',
        'qiskit-aqua',
        'tensorflow',
        'numpy',
        'matplotlib',
        'pandas',
        'scipy',
        'qiskit_ionq',
        'cirq',
        'cuda',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            # Define command-line scripts here.
            # For example:
            # 'your_command=your_module:main_function',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A brief description of your project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/yourproject',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)