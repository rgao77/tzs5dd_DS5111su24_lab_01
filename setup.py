from setuptools import setup, find_packages

setup(
    name='pkg_dpy8wq',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pytest',
        # Add other dependencies here
    ],
    entry_points={
        'console_scripts': [
            # Define any command line scripts here
        ],
    },
)

