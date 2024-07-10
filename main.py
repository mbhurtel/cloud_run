from .tools.set import Set

def main(task, setA, setB):
    setObj = Set(setA, setB)

    if task == "intersection":
        setObj.perform_interection()
        return setObj.intersection_set
    
    elif task == "union":
        setObj.perform_union()
        return setObj.union_set
    
    elif task == "difference":
        setObj.perform_difference()
        return setObj.diff_set
