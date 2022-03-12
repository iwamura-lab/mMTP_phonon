#!/usr/bin/env python

import argparse
import numpy as np

from pymatgen.core.structure import Lattice, Structure
from phonopy.interface.calculator import read_crystal_structure
from phonopy.structure.atoms import PhonopyAtoms

if __name__ == '__main__' :
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', dest='lattice_constant', type=float, default=2.9, help='lattice constant. default value is 2.9(ang).')
    parser.add_argument('--supercell', nargs='*', type=int, default=[1]*3, help='expansion size of each axis')
    args = parser.parse_args()

    unitcell = PhonopyAtoms(symbols=['Fe']*2,
                            cell=np.eye(3) * args.lattice_constant,
                            scaled_positions=[[0, 0, 0],
                                              np.eye(3) * args.lattice_constant,
                                              [0, 0, 0],
                                              [0.5, 0.5, 0.5]])
    #a
