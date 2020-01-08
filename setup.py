from setuptools import setup, find_packages

from src.fog.buildtools import __version__


setup(
    name="fog.buildtools",
    version=__version__,
    license="MIT",
    description="Build tools used by FriendsOfGalaxy plugins",
    author='FriendsOfGalaxy',
    author_email='FriendsOfGalaxy@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
)
