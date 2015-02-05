from setuptools import setup, find_packages

version = __import__('puppet_run_predictor').__version__

setup(
        name="puppet_run_predictor",
        description="A tool to receive a list of files and predict which Puppet nodes would be affected by these files changing.",
        author="Eric Zounes",
        author_email="eric.zounes@puppetlabs.com",
        url="http://github.com/Ziaunys/puppet_run_predictor",
        keywords=["puppetdb", "infrastructure", "orchestration"],
        install_requires= [
            'flask',
        ],
        packages=find_packages(),
        entry_points="""
        [console_scripts]
        puppet_run_predictor=puppet_run_predictor.predictor:main
        """
)
