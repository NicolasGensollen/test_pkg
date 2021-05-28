.. _user_guide:

User guide: table of contents
==============================

This is the user guide of toy_pkg.

Scientific computing with Python
--------------------------------

Basic numerics
..............

:Numerical arrays:

    The numerical data are stored in numpy arrays:

    ::

        >>> import numpy as np
        >>> t = np.linspace(1, 10, 2000)  # 2000 points between 1 and 10
        >>> t
        array([  1.        ,   1.00450225,   1.0090045 , ...,   9.9909955 ,
                 9.99549775,  10.        ])
        >>> t / 2
        array([0.5       , 0.50225113, 0.50450225, ..., 4.99549775, 4.99774887,
           5.        ])

:Plotting and figures:

    ::

        >>> import matplotlib.pyplot as plt
        >>> plt.plot(t, np.cos(t))      # doctest: +ELLIPSIS
        [<matplotlib.lines.Line2D object at ...>]

That's all.
