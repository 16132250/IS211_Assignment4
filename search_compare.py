import time
import random


def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list

def sequential_search(a_list, item):
    pos = 0
    found = False
    start_time = time.time()

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            # time.sleep(.00025)
            pos = pos + 1

    end_time = time.time()
    run_time = end_time - start_time
    # print(start_time,end_time)
    # print(run_time)
    return found, run_time


def ordered_sequential_search(a_list, item):
    pos = 0
    found = False
    stop = False
    start_time = time.time()

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1

    end_time = time.time()
    run_time = end_time - start_time
    # print(run_time)
    return found, run_time

def binary_search_iterative(a_list,item):
    first = 0
    last = len(a_list) - 1
    found = False
    start_time = time.time()
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    end_time = time.time()
    run_time = end_time - start_time
    # print(run_time)
    return found, run_time
    
def binary_search_recursive(a_list,item):
    if len(a_list) == 0:
        return False
    else:
        start_time = time.time()
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            end_time = time.time()
            run_time = end_time - start_time
            # print(start_time, end_time)
            # print(run_time)
            return True, run_time
        else:
            if item < a_list[midpoint]:
                end_time = time.time()
                run_time = end_time - start_time
                # print(start_time, end_time)
                # print(run_time)
                return binary_search_recursive(a_list[:midpoint], item), run_time
            else:
                end_time = time.time()
                run_time = end_time - start_time
                # print(start_time, end_time)
                # print(run_time)
                return binary_search_recursive(a_list[midpoint + 1:], item), run_time

if __name__ == "__main__":
    """Main entry point"""

    sizes = [500, 1000, 10000]
    search_item = -1
    # Test sequential search
    for the_size in sizes:
        total_time = 0

        for i in range(100):
            mylist = get_me_random_list(the_size)
            # print(mylist)
            sequential_search_result = sequential_search(mylist, search_item)
            total_time += sequential_search_result[1]

        average_time = total_time / 100
        print(f"Sequential Search took {average_time:10.7f} seconds to run, on average for list size {the_size}")

    #Test ordered sequential search
    for the_size in sizes:
        total_time = 0

        for i in range(100):
            mylist = get_me_random_list(the_size)
            mylist = sorted(mylist)
            # print(mylist)
            ordered_search_result = ordered_sequential_search(mylist, search_item)
            # print(ordered_search_result)
            total_time += ordered_search_result[1]

        average_time = total_time / 100
        print(f"Ordered Sequential Search took {average_time:10.7f} seconds to run, "
              f"on average for list size {the_size}")

    #Test binary_search_iterative
    for the_size in sizes:
        total_time = 0

        for i in range(100):
            mylist = get_me_random_list(the_size)
            mylist = sorted(mylist)

            binary_search_result = binary_search_iterative(mylist, search_item)

            total_time += binary_search_result[1]

        average_time = total_time / 100
        print(f"Binary Search took {average_time:10.7f} seconds to run, "
              f"on average for list size {the_size}")

    #Test binary_search_recursive
    for the_size in sizes:
        total_time = 0

        for i in range(100):
            mylist = get_me_random_list(the_size)
            mylist = sorted(mylist)

            binary_search_recursive_result = binary_search_recursive(mylist, search_item)

            total_time += binary_search_recursive_result[1]

        average_time = total_time / 100
        print(f"Binary Search Recursive took {average_time:10.7f} seconds to run, "
              f"on average for list size {the_size}")



    """
    # Original 
    the_size = 500

    total_time = 0
    for i in range(100):
        mylist = get_me_random_list(the_size)
        # sorting is not needed for sequential search.
        mylist = sorted(mylist)

        start = time.time()
        check = binary_search_iterative(mylist, -1)
        time_spent = time.time() - start
        total_time += time_spent

    avg_time = total_time / 100
    print(f"Binary Search Iterative took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")
    """