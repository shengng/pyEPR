import pyEPR as epr
import matplotlib.pylab as plt
import numpy as np
import pyEPR.calcs
from pyEPR.calcs import Convert
import pandas as pd
from scipy.interpolate import InterpolatedUnivariateSpline, UnivariateSpline

class Toolbox_pyEPR():
    def __int__(self, path, project_name, design_name):
        self.EPRInfo = epr.ProjectInfo(project_path = path,
                                   project_name = project_name,
                                   design_name = design_name)
        self.EPR_Object = None
        self.EPR_parameters = []

    def get_all_object_names(self):
        return self.EPRInfo.get_all_object_names()

    def get_all_variables_names(self):
        return self.EPRInfo.get_all_variables_names()

    def epr_HFSS_Analysis(self):
        return self.epr.DistributedAnalysis(self.EPRInfo)

    def junction(self, junction_name, Lj_name, rect_name, line_name, length= epr.parse_units('10um')):
        self.EPRInfo.junctions[junction_name] = { 'Lj_variable' : Lj_name,
                                                  'rect'        : rect_name,
                                                  'line'        : line_name,
                                                  'length'      : length}

    def Validate_junction(self):
        self.EPRInfo.validate_junction_info()

    def setup_analyze(self):
        self.EPRInfo.setup_analyze()

    def optimetrics(self, setup_num=0):
        self.EPRInfo.design.optimetrics.solve_setup(self.EPRInfo.design.optimetrics.get_setup_names()[setup_num])

    def get_EPR_object(self):
        self.EPR_Object = epr.DistributedAnalysis(self.EPRInfo)
        return self.EPR_Object

    def list_parameters(self):
        if self.EPR_Object == None:
            try:
                self.get_EPR_object()
            except:
                raise ValueError("Something went wrong in dealing with EPR objects.")
        self.EPR_parameters = self.EPR_Object.get_ansys_variables().transpose()
        return self.EPR_parameters


class Arr():
    def __int__(self, xarr, yarr):
        self.xarr = xarr
        self.yarr = yarr
        self.spl = None

    def Sorting(self):
        ind = np.lexsort((self.yarr, self.xarr))
        self.xarr = self.xarr[ind]
        self.yarr = self.yarr[ind]

    def InterpolatedUnivariateSpline(self, xarr=None, yarr=None, Plot=False):
        if xarr != None and yarr != None:
            self.spl = InterpolatedUnivariateSpline(xarr, yarr)
        else:
            xarr, yarr = self.xarr, self.yarr
            self.spl = self.InterpolatedUnivariateSpline(xarr, yarr, Plot)
        return self.spl

    def UnivariateSpline(self, xarr=None, yarr=None, Plot=False):
        if xarr != None and yarr != None:
            self.spl = UnivariateSpline(xarr, yarr)
        else:
            xarr, yarr = self.xarr, self.yarr
            self.spl = self.UnivariateSpline(xarr, yarr, Plot)
        return self.spl

    def SplineTarget(self, target, Plot=False, method = "Uni"):
        spl2 = self.UnivariateSpline(self.x, self.y - target, s=0)
        xbest = spl2.roots()[-1]

class PlotModule():
    def __int__(self, xarr:np.ndarray, yarr:np.ndarray, labels):
        self.xarr, self.yarr = xarr, yarr
        self.labels = labels

    def Visualize(self, fig=None, ax=None, figsize=(8, 6),
                  colorbar=True, cmap=None,
                  show_xlabel=True, show_ylabel=True):
        if len(self.xarr.shape) == 1:

    def Plot1D(self, fig=None, ax=None, figsize=(8, 6),
               colorbar=True, cmap=None,
               show_xlabel=True, show_ylabel=True):
        

