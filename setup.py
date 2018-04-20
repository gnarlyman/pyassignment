from setuptools import setup, find_packages
try:
    from pip.req import parse_requirements
    from pip.download import PipSession
except ImportError:
    from pip._internal.req import parse_requirements
    from pip._internal.download import PipSession


install_reqs = parse_requirements('requirements.txt', session=PipSession())
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='crudapi',
    packages=find_packages(),
    install_requires=reqs,
    version='0.0.1'
)
