# OPTIMIZATION-MODEL

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: CHITTAMSETTY NAGA VIJAY SAI

*INTERN ID*: CT08DZ1376

*DOMAIN*: DATA SCIENCE

*DURATION*: 8 WEEKS

*MENTOR*:  NEELA SANTHOSH KUMAR 


*DESCRIPTION*:

🔹 Project Overview

This project demonstrates solving an optimization problem using Linear Programming (LP) in Python.
We use the PuLP library to maximize profit given production constraints (resources and demand).

🔹 Problem Statement

A company produces two products: Chairs and Tables.

Profit per Chair = 25

Profit per Table = 45

Constraints:

Wood: 3×Chairs + 5×Tables ≤ 240

Machine Hours: 2×Chairs + 4×Tables ≤ 160

Market Demand: Tables ≤ 40

Non-negativity: Chairs, Tables ≥ 0

Objective Function:

Maximize Profit = 25×Chairs + 45×Tables

🔹 Solution Approach

Formulated the LP model (decision variables, objective function, constraints).

Implemented using Python + PuLP.

Solved with the CBC solver (default in PuLP).

Extracted results, objective value, and resource slacks.

🔹 Results

Optimal Solution:

Chairs = 80

Tables = 0

Maximum Profit: 2000

Slack Analysis:

Wood Slack = 0 (fully used)

Machine Hours Slack = 0 (fully used)

Market Demand Slack = 40 (not binding)

📊 Interpretation: The company should produce only chairs to maximize profit with the given resources.

🔹 Technologies Used

Python 3

PuLP
 (Linear Programming library)

🔹 How to Run

Install PuLP:

pip install pulp

*OUTPUT*:

<img width="428" height="222" alt="Screenshot 2025-09-19 203314" src="https://github.com/user-attachments/assets/fd5e4824-5832-49b4-9001-e41d7dd66463" />



Run the script in IDLE or any Python IDE:

python task4_lp.py
