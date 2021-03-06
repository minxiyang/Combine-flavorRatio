
zScale = {
        "electrons":(0.895176,0.902374,0.874569),
        "muons":1.0282
}
zScale2018 = {
        "electrons":(0.946127,0.949371,0.938017),
        "muons":1.0062
}
zScale2016 = {
        "electrons":(0.951472,0.950691,0.953648),
        "muons":0.9727
        # ~ "muons":1.0
}

def_bng=(200,300,400,500,690,900,1250,1610,2000,3500)

Run3_scale=(1.04263e+00, 5.85277e-05, -3.94195e-09, 1.95841e-12)# 13.6/13 TeV scale
phase2_scale_el={"bb":(1.03395e+00, 1.07103e-04, -1.23108e-08, 4.84213e-12), "be":(2.08466e+00,  - 5.98116e-04, 1.89076e-07, - 2.84911e-12)}
phase2_scale_mu={"bb":(1.03560e+00, 9.69473e-05, -1.00991e-08, 4.68645e-12), "be":(1.42173e+00, -8.11513e-05, 4.03991e-08, 7.83587e-13)}
lumi_el = {"2016":35.9*1000, "2017":41.529*1000, "2018":59.97*1000}
lumi_mu = {"2016":36.3*1000, "2017":42.135*1000, "2018":61.608*1000}


sys_uncers={"el":('MassScaleUp', 'MassScaleDown' ,'PrefireUp', 'PrefireDown', 'PUScaleUp', 'PUScaleDown'), "mu":('Smear', 'MassScaleUp', 'MassScaleDown', 'MuonID')}
shape_corr=("2016bb_MuonID","2016be_MuonID","2017be_MuonID","2018be_MuonID","2016bb_Smear","2016be_Smear", "2017be_Smear", "2018be_Smear", "2016bbbe_muMassScale", "2016bb_elMassScale", "2016be_elMassScale", "2017bb_elMassScale", "2017be_elMassScale", "2018bb_elMassScale", "2018be_elMassScale", "Run3bb_muMassScale", "Run3bb_elMassScale", "Run3bb_Smear", "Run3bb_MuonID", "Run3bb_Prefire", "Run3bb_PUScale", "Run3be_muMassScale", "Run3be_elMassScale", "Run3be_Smear", "Run3be_MuonID", "Run3be_Prefire", "Run3be_PUScale")
eff_corr={"effbb":"1.06","effbe":"1.08","trig2016bb":"1.003","trig2016be":"1.007","trig2017bb":"1.01","trig2017be":"1.01","trig2018bb":"1.01","trig2018be":"1.01", "effRun3bb":"1.06", "effRun3be":"1.08", "trigRun3bb":"1.01", "trigRun3be":"1.01"}
data_files=("dimuon_Mordion2017_BB.txt",  "eventList_ele_2016_BB.txt",  "eventList_ele_2017_BB.txt",  "eventList_ele_2018_BB.txt", "event_list_2017_bb_clean_sort.txt",    "event_list_2018_bb_clean_sort.txt",  "dimuon_Mordion2017_BE.txt",  "eventList_ele_2016_BE.txt",  "eventList_ele_2017_BE.txt",  "eventList_ele_2018_BE.txt",  "event_list_2017_beee_clean_sort.txt",  "event_list_2018_beee_clean_sort.txt")

post_fit_nev={
              '2016be':(11300., 2900., 950., 560., 143., 68., 10.9, 2.1, 3.5),
              '2017be':(12800., 3300., 1090., 670., 210., 62., 17., 4.8, 1.8),
              '2018be':(18600., 5000., 1630., 1040., 340., 106., 22., 8., 6.)
             }
heur_FR={"bb":(0.997211515903, 1.02444338799, 0.964806497097, 0.958923399448, 0.909400641918, 0.968627750874, 0.881528973579, 0.404131144285, 1.14586627483),
         "be":(0.98937523365, 1.02850532532, 1.03766715527, 1.05181705952, 0.906596004963, 0.982578933239, 1.17025470734, 0.370507836342, 0.652740955353),
         "all":(0.981883347034, 1.05922007561, 1.05031919479, 1.03738903999, 0.962003231049, 0.949558615685, 0.963932454586, 0.36852106452, 0.908277630806)
        }
heur_err={"bb":(0.0612235776022, 0.0665341488089, 0.0655901234431, 0.0668230679758, 0.0796996623739, 0.102534452141, 0.162534509603, 0.19672309684, 0.505412258053),
          "be":(0.0806358574423, 0.0864146835932, 0.0906448432772, 0.0928929220624, 0.0929292304645, 0.12748276894, 0.260892216239, 0.251768770314, 0.281863408362),
          "all":(0.0611765463777, 0.0693621275802, 0.0692931592061, 0.0686772279782, 0.0702782069186, 0.0816357707416, 0.134434867108, 0.153042021589, 0.278643358961)
         }


crossSections = {
"dyInclusive50":5765.4,
"dy50to120":2112.90,
"dy120to200":20.56,
"dy200to400":2.89,
"dy400to800": 0.252,
"dy800to1400":1.71E-2,
"dy1400to2300":1.37E-3,
"dy2300to3500":8.178E-5,
"dy3500to4500":3.191E-6,
"dy4500to6000":2.787E-7,
"dy6000toInf":9.56E-9,

# ~ "tW":35.6,
# ~ "Wantitop":35.6,
"tW":19.47,
"Wantitop":19.47,
"Wjets":61526.7,
"WW200to600":1.385,
"WW600to1200":0.0566,
"WW1200to2500":0.003557,
"WW2500": 0.00005395,
"WWinclusive":12.178,
# ~ "WWinclusive":118.7,
"WZ":47.13,
"WZ_ext":47.13,
"ZZ_ext":16.523,
"ZZ":16.523,
'WZ3LNu':4.42965,
'WZ2L2Q': 6.331,
'ZZ4L': 1.212,
'ZZ2L2Nu': 0.564,
'ZZ2L2Q': 1.999,
"ttbar_lep":87.31,
"ttbar_lep50to500":87.31,
"ttbar_lep_500to800":0.32611,
"ttbar_lep_500to800_ext":0.32611,
"ttbar_lep_800to1200":0.03265,
"ttbar_lep_1200to1800":0.00305,
"ttbar_lep_1800toInf":0.00017,
"dyInclusive50_2018":5765.4,
"dy50to120_2018":2112.90,
"dy120to200_2018":20.56,
"dy200to400_2018":2.89,
"dy400to800_2018": 0.252,
"dy800to1400_2018":1.71E-2,
"dy1400to2300_2018":1.37E-3,
"dy2300to3500_2018":8.178E-5,
"dy3500to4500_2018":3.191E-6,
"dy4500to6000_2018":2.787E-7,
"dy6000toInf_2018":9.56E-9,
# ~ "tW_2018":35.6,
# ~ "Wantitop_2018":35.6,
"tW_2018":19.47,
"Wantitop_2018":19.47,
"Wjets_2018":61526.7,
"WW200to600_2018":1.385,
"WW600to1200_2018":0.0566,
"WW1200to2500_2018":0.003557,
"WW2500_2018": 0.00005395,
"WWinclusive_2018":12.178,
# ~ "WWinclusive":118.7,
"WZ_2018":47.13,
"WZ_ext_2018":47.13,
"ZZ_ext_2018":16.523,
"ZZ_2018":16.523,
'WZ3LNu_2018':4.42965,
'WZ2L2Q_2018': 6.331,
'ZZ4L_2018': 1.212,
'ZZ4L_ext_2018': 1.212,
'ZZ2L2Nu_2018': 0.564,
'ZZ2L2Nu_ext_2018': 0.564,
'ZZ2L2Q_2018': 1.999,
"ttbar_lep_2018":87.31,
"ttbar_lep50to500_2018":87.31,
"ttbar_lep_500to800_2018":0.32611,
"ttbar_lep_800to1200_2018":0.03265,
"ttbar_lep_1200to1800_2018":0.00305,
"ttbar_lep_1800toInf_2018":0.00017,
"dyInclusive50_2016":5765.4,
"dy50to120_2016":1975,
"dy120to200_2016":19.32,
"dy200to400_2016":2.731,
"dy400to800_2016": 0.241,
"dy800to1400_2016":0.01678,
"dy1400to2300_2016":0.00139,
"dy2300to3500_2016":0.00008948,
"dy3500to4500_2016":0.0000041,
"dy4500to6000_2016":4.56E-7,
"dy6000toInf_2016":2.06E-8,
"tW_2016":19.47,
"Wantitop_2016":19.47,
"Wjets_2016":61526.7,
"WW200to600_2016":1.385,
"WW600to1200_2016":0.0566,
"WW1200to2500_2016":0.003557,
"WW2500_2016": 0.00005395,
"WWinclusive_2016":12.178,
"WZ_2016":47.13,
"WZ_ext_2016":47.13,
"ZZ_ext_2016":16.523,
"ZZ_2016":16.523,
'WZ3LNu_2016':4.42965,
'WZ3LNu_ext_2016': 4.42965,
'WZ2L2Q_2016': 6.331,
'ZZ4L_2016': 1.212,
'ZZ4L_ext_2016': 1.212,
'ZZ2L2Nu_2016': 0.564,
'ZZ2L2Nu_ext_2016': 0.564,
'ZZ2L2Q_2016': 1.999,
"ttbar_lep_2016":87.31,
"ttbar_lep50to500_2016":87.31,
"ttbar_lep_500to800_2016":0.32611,
"ttbar_lep_800to1200_2016":0.03265,
"ttbar_lep_1200to1800_2016":0.00305,
"ttbar_lep_1800toInf_2016":0.00017,
}
