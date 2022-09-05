import logging
logging.basicConfig(filename="bigdara.log", level=logging.DEBUG)



from Question_1 import question_1 as question_1 
if __name__ == '__main__':
    # columns_filtered = filter_NaN_values_by_threshold(dataset = dataset, threshold = 10)
    # stats = get_stats_of_each_column(dataset)
    # distribution_of_values_in_column(dataset,"TARGET")
    # pretty_print_of_dict(stats, file_name="initial_stats")

    question_1.evaluate()
