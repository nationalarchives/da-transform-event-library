import setuptools

setuptools.setup(
    name='trelib',
    version="0.0.4",
    description='TRE Events Library',
    packages=['tre_event_lib.tre_schemas', 'tre_lib'],
    package_data={'tre_event_lib.tre_schemas': ['*.json']},
    python_requires='>=3.8'
)
