combineTool.py -M Impacts -d $1/combined_datacard$1.root -m 800 --doInitialFit -t -1 --toysFrequentist --expectSignal 1 --X-rtd MINIMIZER_analytic

combineTool.py -M Impacts -d $1/combined_datacard$1.root -m 800 --doFits -t -1 --toysFrequentist --expectSignal 1 --X-rtd MINIMIZER_analytic

combineTool.py -M Impacts -d $1/combined_datacard$1.root -m 800 --autoBoundsPOIs r -t -1 --toysFrequentist --expectSignal 1 --X-rtd MINIMIZER_analytic -o impacts$1.json

plotImpacts.py -i impacts$1.json -o impacts_$1
