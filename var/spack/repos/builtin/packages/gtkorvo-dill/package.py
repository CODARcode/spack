##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the LICENSE file for our notice and the LGPL.
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
from spack import *


class GtkorvoDill(CMakePackage):
    """DILL provides instruction-level code generation,
    register allocation and simple optimizations for generating
    executable code directly into memory regions for immediate use.
    """

    homepage = "https://github.com/GTkorvo/dill"
    url = "https://github.com/GTkorvo/dill/archive/v2.2.tar.gz"

    version('develop', git='https://github.com/GTkorvo/dill.git',
            branch='master')
    version('2.2', 'e81b77a4ab0142566157e0314be328f7')
    version('2.1', '14c835e79b66c9acd2beee01d56e6200')

    def cmake_args(self):
        args = ["-DENABLE_TESTING=0", "-DBUILD_SHARED_STATIC=STATIC"]
        return args
