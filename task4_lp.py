# task4_lp.py
# IDLE-ready script for Task-4 (PuLP)
# pip install pulp
#
# Problem:
#   maximize  25*Chairs + 45*Tables
#   s.t.     3*Chairs + 5*Tables <= 240   (wood units)
#            2*Chairs + 4*Tables <= 160   (machine hours)
#            Tables <= 40                 (market demand)
#            Chairs,Tables >= 0  (integers)

try:
    import pulp as lp
except ImportError:
    raise SystemExit("PuLP is not installed. Run: pip install pulp")

def build_and_solve():
    # 1) Define problem
    prob = lp.LpProblem("Production_Planning", lp.LpMaximize)

    # 2) Decision variables (integers)
    Chairs = lp.LpVariable("Chairs", lowBound=0, cat="Integer")
    Tables = lp.LpVariable("Tables", lowBound=0, cat="Integer")

    # 3) Objective
    prob += 25 * Chairs + 45 * Tables, "Total_Profit"

    # 4) Constraints
    prob += 3 * Chairs + 5 * Tables <= 240, "Wood"
    prob += 2 * Chairs + 4 * Tables <= 160, "Machine_Hours"
    prob += Tables <= 40, "Market_Demand"

    # 5) Solve (CBC solver used by default)
    solver = lp.PULP_CBC_CMD(msg=0)  # set msg=1 to see solver output
    result_status = prob.solve(solver)

    # 6) Output results
    print("Solver status:", lp.LpStatus[result_status])
    for v in prob.variables():
        print(f"{v.name:10s} = {v.varValue}")

    print("Objective (Total profit) = ", lp.value(prob.objective))

    # 7) Compute slacks (RHS - LHS) for each named constraint
    # Note: We compute with final var values manually.
    chairs_val = Chairs.varValue
    tables_val  = Tables.varValue
    wood_slack = 240 - (3 * chairs_val + 5 * tables_val)
    machine_slack = 160 - (2 * chairs_val + 4 * tables_val)
    demand_slack = 40 - tables_val

    print("\nSlacks (RHS - LHS):")
    print(f"  Wood slack         = {wood_slack}")
    print(f"  Machine hours slack= {machine_slack}")
    print(f"  Market demand slack= {demand_slack}")

if __name__ == "__main__":
    build_and_solve()
