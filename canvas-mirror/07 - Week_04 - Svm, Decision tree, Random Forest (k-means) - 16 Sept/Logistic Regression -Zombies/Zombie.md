# Zombie.zip

Source: `Zombie.zip` - 4 files in `Zombie/` (extracted to scratchpad, not run). Logistic regression exercise "Zombie problems" by Sila, January 10th 2026 (ITA ML, 6th semester).

## Files
- `Zombie.py` - Flask web game: trains LogisticRegression models (train_test_split, 20% test, random_state 42, accuracy_score) on the two CSVs; robot features battery_pct, sensor_confidence_pct, task_risk_level, safety_check_passed; target allowed_to_work_alone.
- `humanoid_robot.csv` - 120 rows, `;` delimiter, BOM. Columns: robot_case (string, e.g. HR-001), previous_errors_30d (int), battery_pct (int), sensor_confidence_pct (int), task_risk_level (int), safety_check_passed (0/1), allowed_to_work_alone (0/1, target: 36 ones, 84 zeros).
- `zombie_apocalypse.csv` - 120 rows, `;` delimiter, decimal comma, BOM. Columns: person_id (int), fitness_score (int), gaming_hours_week (int), run_speed_kmh (float, e.g. 14,6), food_cans (int), distance_to_zombie_m (float, e.g. 23,9), survived (0/1, target: 61 ones, 59 zeros).
- `ZombieProblems.pdf` - the task text (below).

## ZombieProblems.pdf (condensed)
Story: year 2032, humanoid robots everywhere; the company's robot "robo-7" claims to make the best coffee in Aarhus. Question: can robo-7 safely work without human supervision? Build a Logistic Regression predicting 1 = may work alone, 0 = requires supervision, from 120 earlier robot tests (previous errors, battery level, sensor confidence, task risk, safety checks). Twist: robo-7 will carry a container labelled "BIOHAZARD - ZOMBIE VIRUS - DO NOT DROP"; if the model wrongly says it may work alone, it may drop it and the zombie apocalypse begins. The exercise then switches to a second dataset of 120 people: predict 1 = survives, 0 = becomes a zombie. "So choose/use your model carefully."

Tasks:
- a) Run the program and see what it does.
- b) Train two Logistic Regression models, one per CSV; tune them (possibly run separately); use the hyperparameters in the Flask game; run again and check the models improved.
- c) Run the whole program in a Docker container.
