from setuptools import setup

setup(
    name='to31',
    version='1.0.0',
    description='Fetal brain MRI alignment',
    author='FNNDSC',
    author_email='dev@babyMRI.org',
    url='https://github.com/FNNDSC/pl-to31',
    py_modules=['align_to31'],
    install_requires=['chris_plugin'],
    license='MIT',
    python_requires='>=3.8.2',
    entry_points={
        'console_scripts': [
            'align_to31 = align_to31:main'
        ]
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.'
    ]
)
