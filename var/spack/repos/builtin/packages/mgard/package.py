##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install mgard
#
# You can edit this file again by typing:
#
#     spack edit mgard
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class Mgard(Package):
    """A Multilevel Technique for Compression of Floating-Point Data."""

    # Note: no homepage yet?! Use placeholders.
    homepage = "https://github.com/CODARcode/cheetah"
    url      = "https://github.com/CODARcode/cheetah/archive/v0.1.tar.gz"

    version('develop', '2cc795b5da26036097b8bcda748649e4')

    def build(self, spec, prefix):
        make()

    def install(self, spec, prefix):
        # Note: mgard package does not provide an install target
        mkdirp(prefix.lib)
        mkdirp(prefix.include)
        install('lib/libmgard.a', prefix.lib)
        install('include/mgard.h', prefix.include)
        install('include/mgard_capi.h', prefix.include)
        install('include/mgard_nuni.h', prefix.include)
