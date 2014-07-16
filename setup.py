from setuptools import setup

setup(
    name="ik.recipe.vimconf",
    version="0.1",
    author="Ivo Kubjas",
    author_email="ivokub@ut.ee",
    description="Buildout recipe for generating vim configuration",
    license="BSD",
    entry_points={
        'zc.buildout': ['default = ik.recipe.vimconf:VimConf'],
    },
    install_requires=[
        'zc.buildout',
        'zc.recipe.egg',
    ]
)
