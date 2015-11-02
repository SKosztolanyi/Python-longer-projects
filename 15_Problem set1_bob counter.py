## This is a problem set 1 b) assignment,
# where I have to count times of occurrence of "bob" string in long strings

# The "s" is full string which is defined in the test grader

def bobcounter(full_string, substring):
    results = []
    sub_len = len(substring)
    for i in range(len(full_string)):
        if full_string[i:i+sub_len] == substring:
            results.append(i)
    return results

full_string = s
substring = "bob"
occurrence_array = bobcounter(full_string, substring)
times_of_occurrence = len(occurrence_array)

print ("Number of times bob occurs is: %s" %times_of_occurrence)