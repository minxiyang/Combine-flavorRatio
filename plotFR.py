import ROOT
from plotting.plotBinByBinFR import plotBinByBinFR





lows={'2017be': ['0.885', '0.805', '0.845', '0.885', '0.715', '0.845', '0.515', '0.235', '0.255'], '2017bb': ['0.975', '1.005', '0.855', '0.895', '0.835', '0.835', '0.635', '0.275', '0.395'], 'allYearCombine': ['0.965', '0.955', '0.935', '0.935', '0.805', '0.855', '0.785', '0.255', '0.495'], '2018be': ['0.895', '0.915', '0.895', '0.895', '0.725', '0.655', '0.795', '0.085', '0.175'], 'allYearCombine_bb': ['1.015', '1.005', '0.955', '0.945', '0.855', '0.905', '0.735', '0.225', '0.625'], 'allYearCombine_be': ['0.905', '0.895', '0.885', '0.915', '0.765', '0.785', '0.795', '0.195', '0.305'], '2018bb': ['0.995', '0.985', '0.925', '0.875', '0.765', '0.805', '0.565', '0.035', '0.635'], '2016bb': ['0.935', '0.865', '0.905', '0.885', '0.705', '0.705', '0.555', '0', '0'], '2016be': ['0.755', '0.825', '0.735', '0.785', '0.625', '0.655', '0.545', '0', '0.245']}
meds={'2017be': ['0.934192', '0.87118334', '0.93460333', '0.9798138', '0.8396457', '1.1340656', '0.82580465', '0.8094654', '1.435'], '2017bb': ['1.0648406', '1.1114113', '0.975', '1.0018592', '1.022383', '1.0677936', '1.0116656', '0.745', '1.355'], 'allYearCombine': ['0.9943789', '0.9927474', '0.96540093', '0.97045535', '0.8664046', '0.9377068', '0.94127727', '0.425', '0.7695147'], '2018be': ['0.95198286', '0.9921407', '0.975', '0.975', '0.835', '0.825', '1.245', '0.33421105', '0.405'], 'allYearCombine_bb': ['1.0759553', '1.0819608', '1.035', '1.0174724', '0.9433272', '1.025', '0.935', '0.45966282', '1.185'], 'allYearCombine_be': ['0.9359068', '0.9374171', '0.9384503', '0.97191936', '0.8389106', '0.91082495', '1.055', '0.445', '0.56060696'], '2018bb': ['1.0809847', '1.089469', '1.025', '0.9825128', '0.9112556', '0.99203545', '0.8607076', '0.2726178', '1.425'], '2016bb': ['1.0223514', '0.9776801', '1.0324553', '1.0200527', '0.875', '0.945', '0.885', '0.375', '1.3537738e-09'], '2016be': ['0.913345', '0.9451692', '0.8817684', '0.9442465', '0.83789766', '0.875', '1.1308103', '0.0003191087', '0.7076508']}
highs={'2017be': ['0.985', '0.945', '1.025', '1.095', '0.995', '1.565', '1.355', '0', '0'], '2017bb': ['1.255', '1.225', '1.105', '1.135', '1.235', '1.375', '1.595', '1.745', '0'], 'allYearCombine': ['1.025', '1.035', '1.005', '1.015', '0.935', '1.035', '1.145', '0.675', '1.225'], '2018be': ['1.015', '1.075', '1.075', '1.065', '0.955', '1.035', '2.055', '0.895', '0.965'], 'allYearCombine_bb': ['1.135', '1.145', '1.105', '1.085', '1.035', '1.165', '1.195', '0.825', '2.295'], 'allYearCombine_be': ['0.975', '0.985', '0.995', '1.035', '0.925', '1.055', '1.425', '0.915', '1.065'], '2018bb': ['1.315', '1.225', '1.145', '1.105', '1.085', '1.215', '1.315', '0.695', '0'], '2016bb': ['1.195', '1.105', '1.205', '1.165', '1.085', '1.265', '1.395', '2.145', '0.855'], '2016be': ['1.045', '1.105', '1.055', '1.145', '1.105', '1.195', '2.455', '2.045', '2.345']}



bng=[200, 300, 400,500,690,900,1250,1610, 2000, 3500]

for year in ['2016', '2017', '2018']:
    for cg in ['bb', 'be']:
        key=year+cg
        lowStr=lows[key]
        medStr=meds[key]
        highStr=highs[key]
        low=[float(x) for x in lowStr]
        med=[float(x) for x in medStr]
        high=[float(x) for x in highStr]
        plotBinByBinFR(year, cg, bng, med, low, high) 
   
         

              
