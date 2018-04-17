user = "casader"
password = "Eri809@03"
hours = {
    "AWS": {'monday': 5, 'tuesday': 5, 'wednesday': 5, 'thursday': 5, 'friday': 5},
    "Virtual": {'monday': 2, 'tuesday': 2, 'wednesday': 2, 'thursday': 2, 'friday': 2},
    "Global": {'monday': 1, 'tuesday': 1, 'wednesday': 1, 'thursday': 1, 'friday': 1}
}
weekday = {'monday': '2', 'tuesday': '3',
           'wednesday': '4', 'thursday': '5', 'friday': '6'}


def get_day_cell_id(day, row):
    return "t_z17102516194911574423935_b_%s_r%s" % (weekday[day], row)
