# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GeomCalculator
                                 A QGIS plugin
 This plugin calcs geometric indicators
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-05-21
        copyright            : (C) 2021 by Roman
        email                : philw7321980@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load GeomCalculator class from file GeomCalculator.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .geom_calc import GeomCalculator
    return GeomCalculator(iface)
