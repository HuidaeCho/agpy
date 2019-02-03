#!/usr/bin/env python3
################################################################################
# Name:    AgPy: An ArcGIS Pro Python module
# Purpose: This module provides convenient functions for ArcGIS Pro Python
#          scripting.
# Author:  Huidae Cho
# Since:   February 2, 2018
#
# Copyright (C) 2019, Huidae Cho <https://idea.isnew.info>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
################################################################################

def export_map_to_tiff(filename, width, height):
    '''Export the current project's first map to TIFF'''
    arcpy.mp.ArcGISProject('CURRENT').listMaps('Map')[0].defaultView.exportToTIFF(filename, width, height, geoTIFF_tags=True)

def convert_array_to_grayscale(array):
    '''Convert a numpy array to grayscale'''
    gray_array = array[0] * 0.299 + array[1] * 0.587 + array[2] * 0.114
    return gray_array

def convert_raster_to_grayscale(raster):
    '''Convert a raster to grayscale'''
    array = arcpy.RasterToNumPyArray(raster)
    gray_array = convertNumPyArrayToGrayscale(array)
    gray_raster = arcpy.NumPyArrayToRaster(gray_array, raster.extent.lowerLeft, raster.meanCellWidth, raster.meanCellHeight)
    return gray_raster
