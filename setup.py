from setuptools import setup

setup(
    name='IntersectPeaks',
    version='1.0',
    install_requires=[
        'pathlib',
        'pysam',
        'numpy',
    ],
    packages=['IntersectPeaksLibs'],
    package_dir={'IntersectPeaksLibs': 'IntersectPeaksLibs'},
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts': [
            'intersectPeaks=IntersectPeaksLibs.__main__:main',
        ]
    }
)
