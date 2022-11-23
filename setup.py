import setuptools

setuptools.setup(
    name='trelib',
    version="0.0.3",
    description='TRE Events Library',
    packages=['tre_lib'],
    package_data={'tre_lib': ['schema*.json']},
    python_requires='>=3.8'
)
