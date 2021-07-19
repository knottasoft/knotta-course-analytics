"""
Setup script for the Open edX package.
"""
import os
import re
import sys

from setuptools import setup

def get_version(*file_paths):
    """
    Extract the version string from the file at the given relative path fragments.
    """
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

VERSION = get_version("course_analytics", "__init__.py")


setup(
    name="course_analytics",
    version=VERSION,
    install_requires=["setuptools"],
    requires=[],
    packages=["course_analytics"],
    include_package_data=True,
    author="Knotta",
    author_email="info@knotta.ru",
    zip_safe=False,
    entry_points={
        "openedx.course_tab": [
            "course_analytics = course_analytics.tab:CourseAnalyticsTab"
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
)
