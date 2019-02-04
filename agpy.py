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

import arcpy

def export_map_to_tiff(filename, width, height):
    '''Export the current project's active map to TIFF'''
    arcpy.mp.ArcGISProject('CURRENT').activeMap.defaultView.exportToTIFF(filename, width, height, geoTIFF_tags=True)

def convert_array_to_raster(array, ref_raster):
    '''Convert a numpy array to a raster'''
    raster = arcpy.NumPyArrayToRaster(array, ref_raster.extent.lowerLeft, ref_raster.meanCellWidth, ref_raster.meanCellHeight)
    return raster

def convert_raster_to_array(raster):
    '''Convert a raster to a numpy array'''
    array = arcpy.RasterToNumPyArray(raster)
    return array

def convert_array_to_grayscale(array):
    '''Convert a numpy array to grayscale'''
    # TODO: this line returns a true integer array, but symbology needs to be handled
    #gray_array = (array[0] * 0.299 + array[1] * 0.587 + array[2] * 0.114).astype(int)
    gray_array = array[0] * 0.299 + array[1] * 0.587 + array[2] * 0.114
    for i in range(0, gray_array.shape[0]):
        for j in range(0, gray_array.shape[1]):
            gray_array[i][j] = int(gray_array[i][j])
    return gray_array

def convert_array_to_grayscale_raster(array, ref_raster):
    '''Convert a numpy array to a grayscale raster'''
    gray_array = convert_array_to_grayscale(array)
    gray_raster = convert_array_to_raster(gray_array, ref_raster)
    return gray_array

def convert_raster_to_grayscale(raster):
    '''Convert a raster to grayscale'''
    gray_array = convert_raster_to_grayscale_array(raster)
    gray_raster = convert_array_to_raster(gray_array, raster)
    return gray_raster

def convert_raster_to_grayscale_array(raster):
    '''Convert a raster to a grayscale array'''
    array = arcpy.RasterToNumPyArray(raster)
    gray_array = convert_array_to_grayscale(array)
    return gray_array
