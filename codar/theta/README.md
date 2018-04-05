# Savanna Theta Install Notes

Before installing anything from scratch, check for an up to date install
in `/projects/CSC249ADCD01/`. To update or create a new configuration, use
the following as a starting point:

1. Install EVPath and related libraries using
 [Korvo Bootstrap](https://gtkorvo.github.io/). Consider using a shared
 location in `/projects/CSC249ADCD01/`.

2. Install [spack](http://spack.readthedocs.io/en/latest/getting_started.html)
 from the `CODARcode` fork and `codar-theta` branch:

    git clone --branch codar-theta git@github.com:CODARcode/spack.git

 Note: use the codar branch once these changes have been merged.

3. Copy `codar/theta/packages.yaml` to `~/.spack/packages.yaml`. Edit korvo
 paths to point at location of installed GTkorvo libraries.

4. Install adios and dependencies using spack:

    spack install adios
