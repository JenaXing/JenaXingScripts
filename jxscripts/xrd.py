from jxhfet.extraction.xrd import fitter
from jxhfet.extraction.xrd import GaN, AlN, InN, AlGaN, InGaN
from jxhfet.readers.Panalytical_XRDML import read
from pandas import DataFrame

from matplotlib.pyplot import *
rcParams['font.size'] = 18

def load_xrdml(filename, mtype):
	return DataFrame(data={
		'sample': [''],
		'data': [read(filename)],
		'mtype': [mtype]}).iloc[0]

