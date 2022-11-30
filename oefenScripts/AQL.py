def scoreAQL(batch): # batch name = date of batch creation + batch number (starts at 1 every new day)

    aql_classes = [[0],[5],[10],[11]]
    batch_size = len(batch)

    # Apple count for apples other than normal, to determine AQL
    sick_in_batch_size = 0

    for apple in batch:

        if apple != 'h':
            sick_in_batch_size += 1

            
    for aqlClass in aql_classes:
        # initialize AQL as class 4, true unless 1, 2 or 3 is true in which case lowest classe (1 being lowest) becomes true
        batch_aql_class = 'AQL class : 4 (rejected)'
        aql_index = 0
        if sick_in_batch_size <= aqlClass[aql_index]:
            # checks wether batch meets critreria for classes 1, 2 and 3, otherwise breaks and prints class 4
            batch_aql_class = (f'AQL class : {aql_classes.index(aqlClass)+1}')
            aql_index += 1
            break
            
    aql_label = f'Lot AQL class {aql_classes.index(aqlClass)+1} : sample of {batch_size} apples contained {batch_size -sick_in_batch_size} healthy apples and {sick_in_batch_size} sick apples'
    return aql_label
