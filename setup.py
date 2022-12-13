import setuptools

setuptools.setup(
    name='tre-event-lib',
    use_scm_version={
        'version_scheme': 'release-branch-semver',
    },
    setup_requires=['setuptools_scm'],
    description='TRE Events Library',
    packages=['tre_event_lib.tre_schemas', 'tre_event_lib'],
    package_data={'tre_event_lib.tre_schemas': ['*.json']},
    python_requires='>=3.8'
)
