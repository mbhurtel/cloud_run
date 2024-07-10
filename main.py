from tools.set import Set

def main(operation, setA, setB):
    setObj = Set(setA, setB)

    if operation == "intersection":
        setObj.perform_interection()
        print("in main:", setObj.intersection_set)
        return setObj.intersection_set
    
    elif operation == "union":
        setObj.perform_union()
        return setObj.union_set
    
    elif operation == "difference":
        setObj.perform_difference()
        return setObj.diff_set
