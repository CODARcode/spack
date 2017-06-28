#!/usr/bin/python

import subprocess
from os.path import expanduser


def search_binary (binary_name):
    """Search if binary exists in PATH. If it does,
     get the version number and parent directory name,
     and write it to ~/.spack/packages.yaml
    """

    # Check if binary exists
    binary_found = subprocess.call( [ 'which', binary_name ] )

    # Get version number and parent directory if binary exists
    if binary_found == 0:

        # Get ther version of the binary package
        version_str = '--version'
        version_tokens= subprocess.check_output(binary_name + " " + version_str, stderr=subprocess.STDOUT, shell=True)\
            .splitlines()[0].split()
        for token in version_tokens:
            if token.replace(".","").isdigit():
                version = token

        # Get the parent dir of the binary
        binary_path = subprocess.check_output(['dirname',subprocess.check_output(['which', binary_name]) ])
        root_dir = subprocess.check_output(['dirname',binary_path])

        # Write everything to the spack packages.yaml file
        fd.write("    %s:\n        paths:\n            %s@%s: %s"
              % (binary_name,binary_name,version,root_dir))


# General information
print("""
This utility will create the packages.yaml file required by spack.
It has been tested on a local machine running Debian, do not use it on a Cray machine.
If this utility fails for you for some reason, manually create the
    packages.yaml file at ~/.spack/packages.yaml .
When the utility exits, please verify the contents of the packages.yaml file.
""")


# Open packages.yaml
home = expanduser("~")
fd = open ("%s/.spack/packages.yaml" % (home), 'w')
fd.write("packages:\n")


# List of binaries commonly found on a typical Linux system
for binary_name in ['cmake','autoconf','m4','flex','python','automake','pkg-config','gettext','tar','bison','zsh']:
    search_binary(binary_name)

print("---Done---")
