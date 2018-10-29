from setuptools import setup, find_packages

package_name = "Pyrate"
package_version = "1.0.0"

setup(
    name=package_name,
    version=package_version,
    author="some author",
    install_requires=["requests", "numpy", "Django==1.9.6"],
    entry_points={
        'console_scripts': [
            'Pyrate=Main:main'
        ]
    }
)
