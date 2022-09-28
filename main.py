import logging
# logging.basicConfig(filename="bigdara.log", level=logging.DEBUG)



from Question_1 import question_1 as question_1
from Question_2 import question_2_1 as question_2_1
from Question_2 import question_2_2 as question_2_2
from Question_2 import question_2_3 as question_2_3
from Question_4 import question_4 as question_4
from Question_6 import question_6 as question_6
from Question_7 import question_7 as question_7
from Question_8 import question_8 as question_8
from Question_9 import question_9 as question_9
from Question_10 import question_10 as question_10
from Question_11 import question_11 as question_11
from Question_12 import question_12 as question_12
from Question_13 import question_13 as question_13
from Question_14 import question_14 as question_14
from Question_15 import question_15 as question_15

from Pearson import pearson as pearson

if __name__ == '__main__':
    # columns_filtered = filter_NaN_values_by_threshold(dataset = dataset, threshold = 10)
    # stats = get_stats_of_each_column(dataset)
    # distribution_of_values_in_column(dataset,"TARGET")
    # pretty_print_of_dict(stats, file_name="initial_stats")
    # question_1.evaluate()
    # question_2_1.evaluate()
    # question_2_2.evaluate()
    # question_2_3.evaluate()
    # question_4.evaluate()
    # question_6.evaluate()
    # question_7.evaluate()
    # question_8.evaluate()
    # question_9.evaluate()
    # question_10.evaluate()
    # question_11.evaluate()
    question_12.evaluate()
    question_13.evaluate()
    question_14.evaluate()
    question_15.evaluate()
    pearson.evaluate()
