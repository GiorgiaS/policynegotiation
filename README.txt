https://pymoo.org/getting_started/part_2.html

In pymoo, each objective function is supposed to be minimized, and each constraint needs to be provided in the form of ≤0.

I encountered issues because my variable (the new set) is a set. However, I need to set a upperbound and lowerbound as integer and this is not compatible with my variable.


Results into dictionary:
result = {
    round(g+f,4): "{prp1, ...}"
}

so, to get the key, I need to sum g+f, approximate to 4 decimal numbers


NSGA-III
- populazion size: see paper: https://www.researchgate.net/publication/308114941_Effect_of_selection_operator_on_NSGA-III_in_single_multi_and_many-objective_optimization
