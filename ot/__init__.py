"""

This is the main module of the POT toolbox. It provides easy access to 
a number of functions described below.

.. warning::
    The list of automatically imported sub-modules is as follows: 
    :py:mod:`ot.lp`, :py:mod:`ot.bregman`, :py:mod:`ot.optim`
    :py:mod:`ot.utils`, :py:mod:`ot.datasets`,
    :py:mod:`ot.gromov`, :py:mod:`ot.smooth`
    :py:mod:`ot.stochastic`    

    The other sub-modules are not imported due to additional dependencies.

"""

# Author: Remi Flamary <remi.flamary@unice.fr>
#         Nicolas Courty <ncourty@irisa.fr>
#
# License: MIT License


# All submodules and packages
from . import lp
from . import bregman
from . import optim
from . import utils
from . import datasets
from . import da
from . import gromov
from . import smooth
from . import stochastic
from . import unbalanced

# OT functions
from .lp import emd, emd2
from .bregman import sinkhorn, sinkhorn2, barycenter
from .unbalanced import sinkhorn_unbalanced, barycenter_unbalanced
from .da import sinkhorn_lpl1_mm

# utils functions
from .utils import dist, unif, tic, toc, toq

__version__ = "0.5.1"

__all__ = ["emd", "emd2", "sinkhorn", "sinkhorn2", "utils", 'datasets',
           'bregman', 'lp', 'tic', 'toc', 'toq', 'gromov',
           'dist', 'unif', 'barycenter', 'sinkhorn_lpl1_mm', 'da', 'optim',
           'sinkhorn_unbalanced', "barycenter_unbalanced"]
