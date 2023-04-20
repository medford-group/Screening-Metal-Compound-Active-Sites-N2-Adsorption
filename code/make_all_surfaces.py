"""
@author: Benjamin Comer
"""

import os
from pymatgen.core.surface import generate_all_slabs
from pymatgen.core.structure import Structure
from pymatgen.io.ase import AseAtomsAdaptor as trans
from pymatgen.analysis.adsorption import AdsorbateSiteFinder

from pymatgen import Molecule
import numpy as np
from ase.build import molecule
from ase.constraints import FixAtoms
from ase.visualize import view

nh3 = Molecule('NHHH',-1*molecule('NH3').positions)
n2  = Molecule("NN",-1*molecule('N2').positions)

#mlecule("H",molecule('H').positions)
nh2 = Molecule("NHH",-1*molecule('NH2').positions)
o2 = Molecule("OO", molecule('O2').positions)
nh = Molecule("NH",-1*molecule('NH').positions)
N = Molecule("N",molecule('N').positions)
H =  Molecule("H",molecule('H').positions)
no2 = Molecule("NOO",-1*molecule('NO2').positions)
no = Molecule("NO",-1*molecule('NO').positions)


def filter_surface(atoms):
    d = []
    indices = []
    for atom in atoms:
        if atom.symbol == 'N':
            o_inds = [a.index for a in atoms if a.symbol != 'N']
            dists = atoms.get_distances(atom.index, o_inds)
            d.append(dists)
            indices.append(atom.index)
    mean_dists = [np.mean(a) for a in d]
    closest_index = mean_dists.index(min(mean_dists))
    dists = d[closest_index]
    if not min(dists) < 2:
        return False
    elif min(dists) < 0.9:
        return False
    syms = []
    d=[]
    for i, dist in enumerate(dists):
        if dist <= 2:
            syms.append(atoms[o_inds[i]].symbol)
            d.append(dist)
    if len(syms) == 1 and syms[0] == 'O':
        return False
    if syms[d.index(min(d))] == 'O':
        return False
    return True


n = 0

if not os.path.isdir('surfaces'):
    os.mkdir('surfaces')

for struct_file in os.listdir('../query/structures'):
    struct = Structure.from_file(os.path.join('../query/structures', struct_file))
    surfs = generate_all_slabs(struct, 1,  8, 10, repair=True)
    for surf in surfs:
        #s = surf.get_orthogonal_c_slab()
        if len(surf) > 50:
            continue
        n += 1
        print(n)
        for site_type, height in zip(['ontop', 'bridge','hollow'], [1.9, 1.7,1.7]):
            as_finder = AdsorbateSiteFinder(surf)
            a_structs = as_finder.generate_adsorption_structures(n2, find_args= {'distance':height,
                                                                             'positions':[site_type],
                                                                             })

            for i, a_struct in enumerate(a_structs):
                if len(a_struct) > 50:
                    continue
                #a = a_struct.get_orthogonal_c_slab()
                atoms = trans.get_atoms(a_struct)
                #print(filter_surface(atoms))
                if not filter_surface(atoms):
                    continue
                c = FixAtoms(mask=[a.symbol != 'N' for a in atoms])
                atoms.set_constraint(c)
                millers = ''.join([str(a) for a in surf.miller_index])
                fname = 'surfaces/' + struct_file.split('.')[0] + '_'\
                            +  millers + 'wN2_{}_{}.traj'.format(site_type, i)
                atoms.write(fname)
                for atom in atoms:
                    if atom.symbol == 'N':
                        atom.symbol = 'O'
                fname = 'surfaces/' + struct_file.split('.')[0] + '_'\
                            +  millers + 'wO2_{}_{}.traj'.format(f, i)
                atoms.write(fname)

        """
        a_structs = as_finder.generate_adsorption_structures(o2, find_args= {'distance':2})
        for i, a_struct in enumerate(a_structs):
            if len(a_struct) > 50:
                continue
            #a = a_struct.get_orthogonal_c_slab()
            atoms = trans.get_atoms(a_struct)
            millers = ''.join([str(a) for a in surf.miller_index])
            atoms.write('surfaces/' + struct_file.split('.')[0] + '_' +  millers + 'O2_{}.cif'.format(i))
        """

        atoms = trans.get_atoms(surf)
        atoms.center()
        millers = ''.join([str(a) for a in surf.miller_index])
        atoms.write('surfaces/' + struct_file.split('.')[0] + '_' +  millers + '.traj')


