file_names = [
"dynamic_memory_allocation",
"malloc_and_calloc_functions",
"deallocate_memory",
"strings",
"null_terminated_string",
"recursion",
"pointer_to_a_function",
"file_handling",
"open_and_close_file",
"file_modes",
"read_and_write_file",
"binary_file_IO",
"command_line_arguments",
"multi_dimensional_arrays",
"error_handling",
"macros",
"typedef_keyword",
"enums",
"bitwise_operations",
"bitwise_shift_operator",
"adv_and_disadv_of_recursion",
"reverse_a_string",
"i_plus_plus_and_plus_plus_i",
"find_length_of_string",
"strcpy_and_strncpy",
"concatenate_two_strings",
"diffe_value_and_reference",
"swap__temporary_variable",
"break_and_continue",
"largest_and_smallest_elements",
"static_and_dynamic",
"function_pointers",
"implement_stack_using_arrays",
"structure",
"implement_linked_list",
"recursion_to_cal_factorial",
"pointers_to_pointers",
"header_files",
"function_overloading",
"operator_overloading",
"union",
"static_variables",
"exception_handling",
"purpose_of_volatile_keyword",
"local_and_global_variables",
"queue_using_linked_lists",
"doubly_linked_list",
"priority_queue"
]


# Generating HTML files
for index, name in enumerate(file_names, start=31):
    file_name = f"{index}_c_{name}.html"
    with open(file_name, "w") as file:
        file.write(f"<!DOCTYPE html>\n<html>\n<head>\n<title>{file_name}</title>\n</head>\n<body>\n<h1>{file_name}</h1>\n</body>\n</html>")
        print(f"Created file: {file_name}")
