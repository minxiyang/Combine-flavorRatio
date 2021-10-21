combine -M MultiDimFit datacards/2018_bb.txt --algo grid --rMin 0.8 --rMax 1.2 --points 1000
mv higgsCombineTest.MultiDimFit.mH120.root outputs/2018_bb.root
python plotNll.py --input=outputs/2018_bb.root --year=2018 --category=bb --output=plots/LLN/2018_bb_fr.pdf

combine -M MultiDimFit datacards/2018_be.txt --algo grid --rMin 0.8 --rMax 1.2 --points 1000
mv higgsCombineTest.MultiDimFit.mH120.root outputs/2018_be.root
python plotNll.py --input=outputs/2018_be.root --year=2018 --category=be --output=plots/LLN/2018_be_fr.pdf

combine -M MultiDimFit datacards/2017_bb.txt --algo grid --rMin 0.8 --rMax 1.2 --points 1000
mv higgsCombineTest.MultiDimFit.mH120.root outputs/2017_bb.root
python plotNll.py --input=outputs/2017_bb.root --year=2017 --category=bb --output=plots/LLN/2017_bb_fr.pdf

combine -M MultiDimFit datacards/2017_be.txt --algo grid --rMin 0.8 --rMax 1.2 --points 1000
mv higgsCombineTest.MultiDimFit.mH120.root outputs/2017_be.root
python plotNll.py --input=outputs/2017_be.root --year=2017 --category=be --output=plots/LLN/2017_be_fr.pdf

combine -M MultiDimFit datacards/2016_bb.txt --algo grid --rMin 0.8 --rMax 1.2 --points 1000
mv higgsCombineTest.MultiDimFit.mH120.root outputs/2016_bb.root
python plotNll.py --input=outputs/2016_bb.root --year=2016 --category=bb --output=plots/LLN/2016_bb_fr.pdf

combine -M MultiDimFit datacards/2016_be.txt --algo grid --rMin 0.8 --rMax 1.2 --points 1000
mv higgsCombineTest.MultiDimFit.mH120.root outputs/2016_be.root
python plotNll.py --input=outputs/2016_be.root --year=2016 --category=be --output=plots/LLN/2016_be_fr.pdf








