combine -M MultiDimFit card_histPdf.txt --algo grid --rMin 0.5 --rMax 1.5 --points 100 --X-rtd MINIMIZER_analytic
mv higgsCombineTest.MultiDimFit.mH120.root histpdf_result.root 
combine -M MultiDimFit card_TH1.txt --algo grid --rMin 0.5 --rMax 1.5 --points 100 --X-rtd MINIMIZER_analytic
mv higgsCombineTest.MultiDimFit.mH120.root TH1_result.root
