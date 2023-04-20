# Metal Oxides Screening for Photocatalytic Nitrogen Fixation
This is a material screening project specifically focusing on finding promising metal oxide catalysts for the photo-fixation of nitrogen under ambient conditions.
## Table of Contents
- [Introduction](#introduction)
- [Usage](#Usage)
- [Data](#Data)
- [Final_Candidate_Visualization](#Final_Candidate_Visualization)


## Introduction
In this repository, we provide a material screening scheme that compares material's selectivity toward nitrogen and oxygen with low- and high-fidelity density functional theory  (DFT) calculations.

## Usage
1. The code to query bulk strucutres from Materials Project can be found [here](https://github.com/nianhant/metal_oxides_screening_for_photocatalytic_nitrogen_fixation/blob/main/code/query_compounds.py). 
2. The code to generate surfaces and add adsorbates to target bulk structures can be found [here](https://github.com/nianhant/metal_oxides_screening_for_photocatalytic_nitrogen_fixation/blob/main/code/make_all_surfaces.py).
3. We used [CatMAP](https://catmap.readthedocs.io/en/latest/) package to compute free energies of adsorbed structures from electronic energy and vibrational energy data. The code to generate the input to CatMAP and to create free energy diagrams can be found [here](https://github.com/nianhant/metal_oxides_screening_for_photocatalytic_nitrogen_fixation/blob/main/code/paper_make_catmap_input.ipynb) and [here](https://github.com/nianhant/metal_oxides_screening_for_photocatalytic_nitrogen_fixation/blob/main/code/paper_generate_FED.ipynb).

## Data
1. All relaxed structures (i.e. bare and adsorbed slabs) from the initial/low-fidelity screening can be found [here](https://github.com/nianhant/metal_oxides_screening_for_photocatalytic_nitrogen_fixation/blob/main/low_fidelity_screening.zip).

2. All relaxed structures (i.e. bare and adsorbed slabs) from the second round/high-fidelity DFT screening can be found[here](https://github.com/nianhant/metal_oxides_screening_for_photocatalytic_nitrogen_fixation/tree/main/high_fidelity_screening_data).

3. Images of relaxed structures from the high-fidelity DFT screening can be found [here](https://github.com/nianhant/metal_oxides_screening_for_photocatalytic_nitrogen_fixation/tree/main/converged_high_fidelity_screening_surface_image).

4. Animation of promising candidates from the high-fidelity DFT screening can be found [here](https://github.com/nianhant/metal_oxides_screening_for_photocatalytic_nitrogen_fixation/tree/main/qualified_high_fidelity_gifs).


## Final_Candidate_Visualization
Final Candidates that Remained Promising after High Fidelity Screening
| Candidate  | E<sub>N2</sub> (eV) | E<sub>O2</sub>(eV) | N<sub>2</sub> strucutre | O<sub>2</sub> strucutre |
| ------------- | ------------- | ------------- | -------------| -------------|
|O2Ti1_152_3_0_001_ontop|   -0.6669|   -0.4500|![](https://github.com/nianhant/metal_oxides_screening_for_photocatalytic_nitrogen_fixation/blob/main/qualified_high_fidelity_gifs/O2Ti1_152_3_0_001/O2Ti1_152_3_0_001_N2_ontop.gif)|![](https://github.com/nianhant/metal_oxides_screening_for_photocatalytic_nitrogen_fixation/blob/main/qualified_high_fidelity_gifs/O2Ti1_152_3_0_001/O2Ti1_152_3_0_001_O2_ontop.gif)| 
|O2Ti1_12_2_0_111_ontop|   -0.4444|   -0.3292|![](https://github.com/nianhant/metal_oxides_screening_for_photocatalytic_nitrogen_fixation/blob/main/qualified_high_fidelity_gifs/O2Ti1_12_2_0_111/O2Ti1_12_2_0_111_N2_ontop.gif)|![](https://github.com/nianhant/metal_oxides_screening_for_photocatalytic_nitrogen_fixation/blob/main/qualified_high_fidelity_gifs/O2Ti1_12_2_0_111/O2Ti1_12_2_0_111_O2_ontop.gif)| 
|O2Ti1_225_1_0_10-1_ontop|   -0.3464|    0.1633|![](https://github.com/nianhant/metal_oxides_screening_for_photocatalytic_nitrogen_fixation/blob/main/qualified_high_fidelity_gifs/O2Ti1_225_1_0_10-1/O2Ti1_225_1_0_10-1_N2_ontop.gif)|![](https://github.com/nianhant/metal_oxides_screening_for_photocatalytic_nitrogen_fixation/blob/main/qualified_high_fidelity_gifs/O2Ti1_225_1_0_10-1/O2Ti1_225_1_0_10-1_O2_ontop.gif)| 
|B1O3Sc1_167_4_0_100_ontop|   -0.2770|   -0.1589|![](https://github.com/nianhant/metal_oxides_screening_for_photocatalytic_nitrogen_fixation/blob/main/qualified_high_fidelity_gifs/B1O3Sc1_167_4_0_100/B1O3Sc1_167_4_0_100_N2_ontop.gif)|![](https://github.com/nianhant/metal_oxides_screening_for_photocatalytic_nitrogen_fixation/blob/main/qualified_high_fidelity_gifs/B1O3Sc1_167_4_0_100/B1O3Sc1_167_4_0_100_O2_ontop.gif)| 
|Mo1O5_6_0_2_110_bridge|   -0.2613|    3.2670|![](https://github.com/nianhant/metal_oxides_screening_for_photocatalytic_nitrogen_fixation/blob/main/qualified_high_fidelity_gifs/Mo1O5_6_0_2_110/Mo1O5_6_0_2_110_N2_bridge.gif)|![](https://github.com/nianhant/metal_oxides_screening_for_photocatalytic_nitrogen_fixation/blob/main/qualified_high_fidelity_gifs/Mo1O5_6_0_2_110/Mo1O5_6_0_2_110_O2_bridge.gif)| 
|O2Zr1_61_3_13_110_bridge|   -0.2476|   -0.0663|![](https://github.com/nianhant/metal_oxides_screening_for_photocatalytic_nitrogen_fixation/blob/main/qualified_high_fidelity_gifs/O2Zr1_61_3_13_110/O2Zr1_61_3_13_110_N2_bridge.gif)|![](https://github.com/nianhant/metal_oxides_screening_for_photocatalytic_nitrogen_fixation/blob/main/qualified_high_fidelity_gifs/O2Zr1_61_3_13_110/O2Zr1_61_3_13_110_O2_bridge.gif)| 
|O2Ti1_225_1_0_111_ontop|   -0.2289|    0.9842|![](https://github.com/nianhant/metal_oxides_screening_for_photocatalytic_nitrogen_fixation/blob/main/qualified_high_fidelity_gifs/O2Ti1_225_1_0_111/O2Ti1_225_1_0_111_N2_ontop.gif)|![](https://github.com/nianhant/metal_oxides_screening_for_photocatalytic_nitrogen_fixation/blob/main/qualified_high_fidelity_gifs/O2Ti1_225_1_0_111/O2Ti1_225_1_0_111_O2_ontop.gif)| 
|O2Zr1_136_3_0_111_ontop|   -0.2166|    0.8677|![](https://github.com/nianhant/metal_oxides_screening_for_photocatalytic_nitrogen_fixation/blob/main/qualified_high_fidelity_gifs/O2Zr1_136_3_0_111/O2Zr1_136_3_0_111_N2_ontop.gif)|![](https://github.com/nianhant/metal_oxides_screening_for_photocatalytic_nitrogen_fixation/blob/main/qualified_high_fidelity_gifs/O2Zr1_136_3_0_111/O2Zr1_136_3_0_111_O2_ontop.gif)| 
