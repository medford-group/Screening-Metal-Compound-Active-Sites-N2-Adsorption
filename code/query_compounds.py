"""
@author: Benjamin Comer
"""
from pymatgen.ext.matproj import MPRester
import itertools
import json
import yaml

#This initializes the REST adaptor. Put your own API key in.
MPR = MPRester("your_MP_API")

#query = {'elements':{'$all':['O']},'spacegroup.symbol':'P2_1/c'}#,'oxide_type':{}} #get all M1 oxides
#query = {'elements':{'$all':['V','Mo','O']},'nelements':3}#,'oxide_type':{}} #get all MoVOx oxides

band_gap_min = 0.1
band_gap_max = 5.0

all_results = {}
band_gaps = {}


for metal in ['Sc', 'Ru', 'V', 'Sn', 'Nb', 'Zr', 'Mo', 'Ti']:
    includes = ['O','B','P',metal]
    #includes = ['B','P',metal]
    #query = {'elements':{'$in':includes,'$all':[metal,'O']},'nelements':3}#,'band_gap':{'$gte':band_gap_min, '$lte':band_gap_max}}#, 'spacegroup.symbol':'Pmmn'} #get all oxides that include V or Mo or Nb or Te
    #query = {'elements':{'$in':includes,'$all':[metal]},'nelements':{'$lte':3}}#,'band_gap':{'$gte':band_gap_min, '$lte':band_gap_max}}#, 'spacegroup.symbol':'Pmmn'} #get all oxides that include V or Mo or Nb or Te

    #query = {'elements':{'$all':['Mo','O']},'nelements':2}

    #results = MPR.query(criteria = query, properties = ['formula', 'formation_energy_per_atom','spacegroup','material_id','oxide_type','unit_cell_formula','elements','final_structure','band_gap'])
    properties = ['formula', 'formation_energy_per_atom','material_id','unit_cell_formula','elements','final_structure','band_gap','spacegroup']
	

    elements = includes
    results = []
    for i in range(len(elements)):
        for combo in itertools.combinations(elements, i + 1):
            combo = list(set(list(combo) + [metal, 'O']))
            try:
                results.extend(MPR.query({"elements": {"$all": combo}, "nelements": i+1}, properties=properties))
            except:
                pass

    print('Query finished')
    structures = {}
    band_gaps[metal] = []

    i = 0
    element_results = {}
    screened_results = []
    for r in results:
        bg = r['band_gap']
        #if bg >= band_gap_min and bg <= band_gap_max:
        #    include = True
        #else:
        #    include = False
        elem = r['elements']
        for ei in elem: #exclude materials that have elements other than the "included" elements
            if includes and ei not in includes+['O']:
                include = False
                break
            else:
                if ei in element_results:
                    element_results[ei] += 1
                else:
                    element_results[ei] = 1
        if include == True:
            i+=1
            form_string = ''
            for elem, num in sorted(r['formula'].items()):
                form_string += str(elem)+str(int(num))
            name = form_string+'_'+str(int(r['spacegroup']['number']))
            E = r['formation_energy_per_atom']
            name += '_' + str(bg)
            structures[name] = r['final_structure']
            band_gaps[metal].append(r['band_gap'])

    all_results[metal] = structures
    for name, structure in structures.items():
        structure.to('cif','structures/' + name + '.cif')
    print(metal)
    print(len(all_results[metal]))


with open('BoroNitrides.yaml', 'w') as f:
    yaml.dump(structures, f)

with open('bandgap.json','w') as outfile:
    json.dump(band_gaps, outfile)

