# List of file names
file_names = [
    "dynamic",
    "malloc",
    "deallocate",
    "strings",
    "nullstring",
    "recursion",
    "pointerf",
    "handling",
    "openclose_file",
    "modes",
    "rwfile",
    "binary",
    "clargument",
    "mul_d_array",
    "error",
    "macros",
    "typedef",
    "enums",
    "bitwise",
    "bitwiseshift",
    "adrecursion",
    "reverse_str",
    "iplus",
    "find_lenstr",
    "strcpy",
    "concatenate_str",
    "pvpr",
    "swap_without_temp",
    "break_conti",
    "lar_small_elem"
]

# Generating HTML files
for index, name in enumerate(file_names, start=31):
    file_name = f"{index}_c_{name}.html"
    with open(file_name, "w") as file:
        file.write(f"<!DOCTYPE html>\n<html>\n<head>\n<title>{file_name}</title>\n</head>\n<body>\n<h1>{file_name}</h1>\n</body>\n</html>")
        print(f"Created file: {file_name}")
