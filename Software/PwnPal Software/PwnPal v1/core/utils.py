def format_scan_results(results):
    formatted = ""
    counter = 0
    for item in results:
        if formatted.__contains__(item):
            continue
        counter += 1
        formatted += f"{counter}. " + item + "\n"
    return formatted
    # return results
