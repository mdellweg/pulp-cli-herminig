from setuptools import find_namespace_packages, setup

packages = find_namespace_packages(include=["pulpcore.cli.*"])


setup(
    name="pulp-cli-herminig",
    description="Command line interface to talk to pulpcore's REST API. (Herminig plugin commands)",
    version="0.0.0a1.dev",
    packages=packages,
    package_data={package: ["py.typed"] for package in packages},
    python_requires=">=3.6",
    install_requires=[
        "click",
        "pulp-cli",
    ],
    entry_points={
        "pulp_cli.plugins": [
            "herminig=pulpcore.cli.herminig",
        ],
    },
    license="GPLv2+",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: System :: Software Distribution",
        "Typing :: Typed",
    ],
)
