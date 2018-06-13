user = ""
password = ""
hours = {
    "AWS": {'monday': 2, 'tuesday': 2, 'wednesday': 2, 'thursday': 2, 'friday': 2},
    "Customer": {'monday': 3, 'tuesday': 3, 'wednesday': 3, 'thursday': 3, 'friday': 3},
    "Global": {'monday': 3, 'tuesday': 3, 'wednesday': 3, 'thursday': 3, 'friday': 3}
}
weekday = {'monday': '2', 'tuesday': '3',
           'wednesday': '4', 'thursday': '5', 'friday': '6'}


def get_day_cell_id(day, row):
    return "t_z17102516194911574423935_b_%s_r%s" % (weekday[day], row)
