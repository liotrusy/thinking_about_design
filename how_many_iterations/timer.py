import subject_1, subject_2
import timeit

with open('subject_1.py') as first_file, open('subject_2.py') as second_file:
    first_file_code = first_file.read()
    second_file_code = second_file.read()

number_of_executions =  50

subject_1_execution_time = timeit.timeit(first_file_code, number= number_of_executions)
subject_2_execution_time = timeit.timeit(second_file_code, number= number_of_executions)

result_message = "Here is the final verdict:\n"
result_message += f">> Subject_1 time: {subject_1_execution_time:.4f}s. \n"
result_message += f">> Subject_2 time: {subject_2_execution_time:.4f}s. \n"

print(result_message)
with open("test_result.txt", mode='w', encoding="utf8") as output_file:
    output_file.write(result_message)

