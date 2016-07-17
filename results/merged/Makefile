all: results_shapiro.pdf results_pearson.pdf results_None.pdf

results_shapiro.md: ../../analysis/sb_analyze.py experiment_results.csv task_questionnaire_results.csv final_questionnaire_results.csv demographic_data_fixed.csv
	python3 ../../analysis/sb_analyze.py experiment_results.csv -q task_questionnaire_results.csv -Q final_questionnaire_results.csv -D demographic_data_fixed.csv -en shapiro > results_shapiro.md

results_shapiro.pdf: results_shapiro.md
	pandoc -f markdown -t latex -o results_shapiro.pdf results_shapiro.md


results_pearson.md: ../../analysis/sb_analyze.py experiment_results.csv task_questionnaire_results.csv final_questionnaire_results.csv demographic_data_fixed.csv
	python3 ../../analysis/sb_analyze.py experiment_results.csv -q task_questionnaire_results.csv -Q final_questionnaire_results.csv -D demographic_data_fixed.csv -en pearson > results_pearson.md

results_pearson.pdf: results_pearson.md
	pandoc -f markdown -t latex -o results_pearson.pdf results_pearson.md


results_None.md: ../../analysis/sb_analyze.py experiment_results.csv task_questionnaire_results.csv final_questionnaire_results.csv demographic_data_fixed.csv
	python3 ../../analysis/sb_analyze.py experiment_results.csv -q task_questionnaire_results.csv -Q final_questionnaire_results.csv -D demographic_data_fixed.csv -en None > results_None.md

results_None.pdf: results_None.md
	pandoc -f markdown -t latex -o results_None.pdf results_None.md

