import ROOT
from plotting.plotBinByBinFR import plotBinByBinFR




#lows={'be2016': ['0.81', '0.802', '0.718', '0.766', '0.606', '0.574', '0.44599998', '0', '0'], 'be2017': ['0.87799996', '0.786', '0.806', '0.83', '0.654', '0.75', '0.40199998', '0.134', '0'], 'be2018': ['0.886', '0.886', '0.834', '0.838', '0.67399997', '0.61399996', '0.606', '0.118', '0'], 'allYearCombine': ['0.95', '0.93799996', '0.902', '0.898', '0.782', '0.81799996', '0.70199996', '0.29', '0.394'], 'allYearCombinebb': ['0.99799997', '0.978', '0.918', '0.894', '0.802', '0.81', '0.61399996', '0', '0.466'], 'bb2018': ['0.99399996', '0.958', '0.902', '0.834', '0.72999996', '0.726', '0.482', '0.122', '0.334'], 'allYearCombinebe': ['0.89', '0.84999996', '0.838', '0.862', '0.71', '0.73399997', '0.658', '0.198', '0'], 'bb2017': ['0.96199995', '0.978', '0.83', '0.84999996', '0.77', '0.75', '0.53', '0.24599999', '0.214'], 'bb2016': ['0.93', '0.858', '0.87399995', '0.838', '0.682', '0.64599997', '0.43', '0', '0']}

#meds={'be2016': ['0.93399996', '0.942', '0.87', '0.9400502', '0.81799996', '0.84999996', '1.05', '0.326', '0.61'], 'be2017': ['0.946', '0.87', '0.91116494', '0.94902194', '0.80716765', '1.0677013', '0.802', '0.82199997', '1.286'], 'be2018': ['0.958', '0.982', '0.9371231', '0.93799996', '0.802', '0.81', '1.09', '0.40152916', '0.366'], 'allYearCombine': ['1.0139999', '1.0059999', '0.9682709', '0.9591473', '0.8562081', '0.9286358', '0.9010206', '0.494', '0.84999996'], 'allYearCombinebb': ['1.0699999', '1.054', '0.99799997', '0.974', '0.90999997', '0.9631077', '0.854', '0.502', '1.27'], 'bb2018': ['1.0979999', '1.0720444', '1.0198097', '0.9572008', '0.898', '0.942', '0.8078129', '0.354', '1.2739999'], 'allYearCombinebe': ['0.95', '0.922', '0.918', '0.94269544', '0.806', '0.886', '0.97114277', '0.486', '0.518'], 'bb2017': ['1.066', '1.0991389', '0.954', '0.98077494', '0.95722795', '1.026', '0.9569413', '0.742', '1.2739999'], 'bb2016': ['1.038', '0.974', '1.0166997', '0.986', '0.871211', '0.922', '0.81', '0.522', '0.102']}

#highs={'be2016': ['1.086', '1.1259999', '1.062', '1.162', '1.118', '1.262', '2.534', '2.766', '0'], 'be2017': ['1.026', '0.96999997', '1.0339999', '1.094', '1.002', '1.5339999', '1.53', '3.6859999', '0'], 'be2018': ['1.05', '1.102', '1.066', '1.062', '0.954', '1.066', '1.9779999', '1.17', '1.638'], 'allYearCombine': ['1.094', '1.09', '1.046', '1.026', '0.93799996', '1.058', '1.158', '0.81799996', '1.806'], 'allYearCombinebb': ['1.15', '1.142', '1.086', '1.062', '1.0339999', '1.146', '1.186', '0', '3.514'], 'bb2018': ['1.226', '1.2179999', '1.158', '1.102', '1.094', '1.226', '1.354', '0.95', '0'], 'allYearCombinebe': ['1.026', '1.0139999', '1.0139999', '1.038', '0.914', '1.074', '1.426', '1.0059999', '1.566'], 'bb2017': ['1.1899999', '1.23', '1.102', '1.13', '1.202', '1.398', '1.726', '2.234', '0'], 'bb2016': ['1.158', '1.114', '1.194', '1.162', '1.122', '1.318', '1.526', '2.494', '0']}

#lows={'2017be': ['0.95525', '0.93535', '0.91545', '0.89555', '0.83585', '0.77615', '0.57715', '0.29855', '0'], '2017bb': ['0.91545', '0.89555', '0.87565', '0.89555', '0.83585', '0.79605', '0.61695', '0.39805', '0'], 'allYearCombine': ['0.99505', '0.97515', '0.97515', '0.97515', '0.93535', '0.91545', '0.83585', '0.67665', '0'], '2018be': ['0.95525', '0.93535', '0.91545', '0.91545', '0.85575', '0.81595', '0.63685', '0.37815', '0'], 'allYearCombine_bb': ['0.97515', '0.97515', '0.95525', '0.95525', '0.91545', '0.89555', '0.77615', '0.61695', '0'], 'allYearCombine_be': ['0.97515', '0.97515', '0.95525', '0.95525', '0.91545', '0.87565', '0.73635', '0.51745', '0'], '2018bb': ['0.93535', '0.91545', '0.89555', '0.89555', '0.83585', '0.81595', '0.67665', '0.45775', '0'], '2016bb': ['0.91545', '0.89555', '0.87565', '0.87565', '0.81595', '0.77615', '0.59705', '0.35825', '0'], '2016be': ['0.83585', '0.87565', '0.83585', '0.83585', '0.77615', '0.71645', '0.51745', '0.03985', '0']}
#meds={'2017be': ['1.0000778', '1.0000962', '1.0001353', '1.00023', '1.0002636', '1.0001925', '0.99505', '1.03485', '1.33335'], '2017bb': ['1.000042', '1.0000324', '1.0000494', '1.0000454', '0.9999054', '1.000192', '1.0000844', '1.0080343', '0.73635'], 'allYearCombine': ['1.0000921', '1.000225', '1.0002042', '1.0000963', '0.99991304', '1.0002421', '1.0002673', '0.99505', '0.99505'], '2018be': ['1.000066', '1.0000731', '1.0001105', '1.0001318', '1.0001743', '1.0000981', '0.999106', '0.99505', '0.89555'], 'allYearCombine_bb': ['1.0000124', '1.0000091', '1.0000128', '1.0000092', '1.0000091', '1.0000281', '1.0002823', '1.0043777', '0.99505'], 'allYearCombine_be': ['0.99998724', '1.000285', '1.000374', '1.0003793', '1.0003244', '1.0005481', '0.99505', '0.99505', '0.99505'], '2018bb': ['1.0000203', '1.0000244', '1.0000315', '1.0000377', '1.0000491', '1.0001482', '1.0001463', '1.0062943', '0.93535'], '2016bb': ['1.0000216', '1.0000206', '1.0000353', '1.0000337', '1.000058', '1.0001981', '0.9998318', '1.0102516', '0.71645'], '2016be': ['1.0000441', '1.0000033', '1.0000658', '1.0001222', '1.0002084', '1.00002', '0.99505', '1.03485', '1.67165']}
#highs={'2017be': ['1.05475', '1.07465', '1.09455', '1.11445', '1.21395', '1.31345', '1.87065', '0', '0'], '2017bb': ['1.15425', '1.09455', '1.13435', '1.11445', '1.21395', '1.27365', '1.61195', '0', '0'], 'allYearCombine': ['1.01495', '1.01495', '1.03485', '1.03485', '1.05475', '1.09455', '1.21395', '1.49255', '0'], '2018be': ['1.07465', '1.07465', '1.09455', '1.09455', '1.17415', '1.25375', '1.65175', '0', '0'], 'allYearCombine_bb': ['1.01495', '1.03485', '1.03485', '1.05475', '1.09455', '1.11445', '1.27365', '1.61195', '0'], 'allYearCombine_be': ['1.01495', '1.03485', '1.03485', '1.05475', '1.09455', '1.15425', '1.37315', '0', '0'], '2018bb': ['1.19405', '1.11445', '1.11445', '1.13435', '1.17415', '1.23385', '1.49255', '0', '0'], '2016bb': ['1.15425', '1.13435', '1.15425', '1.15425', '1.23385', '1.31345', '1.67165', '0', '0'], '2016be': ['1.13435', '1.15425', '1.19405', '1.19405', '1.29355', '1.41295', '0', '0', '0']}
lows={'2017be': ['0.89', '0.81', '0.85', '0.89', '0.71', '0.85', '0.53', '0.23', '0.27'], '2017bb': ['0.97', '1.01', '0.87', '0.89', '0.85', '0.85', '0.65', '0.27', '0.41'], 'allYearCombine': ['0.97', '0.97', '0.93', '0.93', '0.81', '0.85', '0.79', '0.27', '0.49'], '2018be': ['0.91', '0.91', '0.89', '0.89', '0.73', '0.67', '0.81', '0.09', '0.17'], 'allYearCombine_bb': ['1.01', '1.01', '0.97', '0.95', '0.87', '0.91', '0.73', '0.23', '0.63'], 'allYearCombine_be': ['0.91', '0.89', '0.89', '0.93', '0.77', '0.79', '0.79', '0.21', '0.31'], '2018bb': ['0.99', '0.99', '0.93', '0.87', '0.77', '0.81', '0.57', '0.03', '0.65'], '2016bb': ['0.93', '0.87', '0.91', '0.89', '0.71', '0.71', '0.55', '0', '0'], '2016be': ['0.75', '0.83', '0.75', '0.79', '0.63', '0.65', '0.55', '0', '0.25']}
meds={'2017be': ['0.93417007', '0.87125033', '0.93461394', '0.97980434', '0.83967304', '1.1343008', '0.8256603', '0.81', '1.43'], '2017bb': ['1.065189', '1.1119045', '0.975452', '1.0025047', '1.0203837', '1.0682281', '1.012134', '0.7439497', '1.3554904'], 'allYearCombine': ['0.99432087', '0.99276584', '0.96527386', '0.9703901', '0.86637837', '0.93768317', '0.9414619', '0.42562607', '0.77'], '2018be': ['0.949929', '0.98990315', '0.9787844', '0.9729102', '0.83444875', '0.8205354', '1.2445806', '0.33420876', '0.40658745'], 'allYearCombine_bb': ['1.0758493', '1.0821562', '1.0347856', '1.0175694', '0.9430252', '1.0248234', '0.9356231', '0.4598937', '1.19'], 'allYearCombine_be': ['0.9362486', '0.9377704', '0.9386289', '0.9721652', '0.8388757', '0.9109973', '1.0543387', '0.44366267', '0.5610807'], '2018bb': ['1.0807219', '1.09', '1.0246738', '0.98209757', '0.91148543', '0.9913709', '0.8610026', '0.2725451', '1.43'], '2016bb': ['1.0224003', '0.9779557', '1.0326223', '1.0199927', '0.87464786', '0.94596094', '0.88403666', '0.37505016', '8.878825e-08'], '2016be': ['0.9126461', '0.9454044', '0.88158494', '0.9433273', '0.83694375', '0.87471664', '1.130889', '1.7396334e-06', '0.7091575']}
highs={'2017be': ['0.99', '0.93', '1.03', '1.09', '0.99', '1.55', '1.35', '3.39', '0'], '2017bb': ['1.25', '1.23', '1.11', '1.13', '1.23', '1.37', '1.59', '1.75', '0'], 'allYearCombine': ['1.03', '1.03', '1.01', '1.01', '0.93', '1.03', '1.13', '0.67', '1.21'], '2018be': ['1.01', '1.07', '1.07', '1.05', '0.95', '1.03', '2.05', '0.89', '0.95'], 'allYearCombine_bb': ['1.13', '1.13', '1.09', '1.07', '1.03', '1.17', '1.19', '0.81', '2.29'], 'allYearCombine_be': ['0.97', '0.99', '0.99', '1.03', '0.91', '1.05', '1.43', '0.91', '1.05'], '2018bb': ['1.31', '1.23', '1.13', '1.11', '1.07', '1.21', '1.31', '0.69', '3.43'], '2016bb': ['1.19', '1.09', '1.19', '1.17', '1.09', '1.27', '1.39', '2.11', '0.85'], '2016be': ['1.03', '1.11', '1.05', '1.15', '1.11', '1.19', '2.45', '2.03', '2.33']}
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
   
         

              
