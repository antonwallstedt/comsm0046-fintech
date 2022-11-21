import BSE
import numpy as np
import csv
import math
import random
from BSE import market_session

# 900 / 15 = 60 trading days
start_time = 0
end_time   = 600 
interval   = 15

# Market configuration
sup_range = (10, 190)
dem_range = (10, 190)
sup_schedule = [{
    'from': start_time, 'to': end_time,
    'ranges': [sup_range],
    'stepmode': 'fixed'
}]
dem_schedule = sup_schedule

order_schedule = {
    'sup': sup_schedule, 'dem': dem_schedule,
    'interval': interval,
    'timemode': 'periodic'
}

# (k, F) values to test
k_vals = [4, 6, 7, 8, 9, 10]
F_vals = [0.25, 0.5, 0.75, 1, 1.25, 1.5]

trial_dump = open('bigtestdata.csv', 'w')
for k_val in k_vals:
    for F_val in F_vals:
        print(f'k: {k_val}, F: {F_val}')
        buyers_spec = [
            ('ZIC', 10), ('ZIP', 10),
            ('PRDE', 10, {'k': k_val, 's_min': -1, 's_max': +1, 'F': F_val})
        ]
        sellers_spec = buyers_spec
        traders_spec = {'sellers': sellers_spec, 'buyers': buyers_spec}
        trial = 0
        while (trial < 50):
            trial_id = f"trial{trial}_{k_val}_{F_val}"
            market_session(
                trial_id,
                start_time, end_time,
                traders_spec,
                order_schedule,
                trial_dump,
                False,
                False
            )
            trial += 1
trial_dump.close()