# This code is part of Qiskit.
#
# (C) Copyright IBM 2022.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""
=====================================
Primitives (:mod:`qiskit.primitives`)
=====================================

.. currentmodule:: qiskit.primitives

.. automodule:: qiskit.primitives.base_estimator
.. automodule:: qiskit.primitives.base_sampler

.. currentmodule:: qiskit.primitives

Estimator
=========

.. autosummary::
   :toctree: ../stubs/

   BaseEstimator
   Estimator
   BackendEstimator

Sampler
=======

.. autosummary::
   :toctree: ../stubs/

   BaseSampler
   Sampler
   BackendSampler

Results
=======

.. autosummary::
   :toctree: ../stubs/

   BasePrimitiveResult
   EstimatorResult
   SamplerResult
"""

from .base_estimator import BaseEstimator
from .base_result import BasePrimitiveResult
from .base_sampler import BaseSampler
from .backend_estimator import BackendEstimator
from .estimator import Estimator
from .estimator_result import EstimatorResult
from .backend_sampler import BackendSampler
from .sampler import Sampler
from .sampler_result import SamplerResult
