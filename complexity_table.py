from flask import Flask
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/complexity")


worst_syn = ['bigo', 'big o', 'big oh', 'worst', 'worst case']
average_syn = ['theta', 'big theta', 'average', 'average case']
best_syn = ['omega', 'big omega', 'best', 'best case']
ops_type = ['access', 'search', 'insertion', 'deletion']
special_algos = ['Dijkstra\'s algorithm', 'prims algorithm', 'bellman ford algorithm', 'floyd warshall algorithm', 'topological sort', 'sleep sort']


algorithms = {
    'quick sort': {
        'Time Complexity': {
            'best': 'Omega of n log n',
            'average': 'Theta of n log n',
            'worst': 'Order of n squared'
        },
        'Space Complexity': 'Order of log n'
    },
    'merge sort': {
        'Time Complexity': {
            'best': 'Omega of n log n',
            'average': 'Theta of n log n',
            'worst': 'Order of n log n'
        },
        'Space Complexity': 'Order of n'
    },
    'tim sort': {
        'Time Complexity': {
            'best': 'Omega of n',
            'average': 'Theta of n log n',
            'worst': 'Order of n squared'
        },
        'Space Complexity': 'Order of n'
    },
    'heap sort': {
        'Time Complexity': {
            'best': 'Omega of n log n',
            'average': 'Theta of n log n',
            'worst': 'Order of n log n'
        },
        'Space Complexity': 'Order of 1'
    },
    'bubble sort': {
        'Time Complexity': {
            'best': 'Omega of n',
            'average': 'Theta of n squared',
            'worst': 'Order of n squared'
        },
        'Space Complexity': 'Order of 1'
    },
    'insertion sort': {
        'Time Complexity': {
            'best': 'Omega of n',
            'average': 'Theta of n squared',
            'worst': 'Order of n squared'
        },
        'Space Complexity': 'Order of 1'
    },
    'selection sort': {
        'Time Complexity': {
            'best': 'Omega of n squared',
            'average': 'Theta of n squared',
            'worst': 'Order of n squared'
        },
        'Space Complexity': 'Order of 1'
    },
    'tree sort': {
        'Time Complexity': {
            'best': 'Omega of n log n',
            'average': 'Theta of n log n',
            'worst': 'Order of n squared'
        },
        'Space Complexity': 'Order of n'
    },
    'shell sort': {
        'Time Complexity': {
            'best': 'Omega of n log n',
            'average': 'Theta of n log n squared',
            'worst': 'Order of n log n squared'
        },
        'Space Complexity': 'Order of 1'
    },
    'bucket sort': {
        'Time Complexity': {
            'best': 'Omega of n+k',
            'average': 'Theta of n+k',
            'worst': 'Order of n squared'
        },
        'Space Complexity': 'Order of n'
    },
    'radix sort': {
        'Time Complexity': {
            'best': 'Omega of n times k',
            'average': 'Theta of n times k',
            'worst': 'Order of n time k'
        },
        'Space Complexity': 'Order of n+k'
    },
    'counting sort': {
        'Time Complexity': {
            'best': 'Omega of n+k',
            'average': 'Theta of n+k',
            'worst': 'Order of n+k'
        },
        'Space Complexity': 'Order of k'
    },
    'cube sort': {
        'Time Complexity': {
            'best': 'Omega of n',
            'average': 'Theta of n log n',
            'worst': 'Order of n log n'
        },
        'Space Complexity': 'Order of n'
    },
    'Dijkstra\'s algorithm': {
        'Time Complexity': {
            'average': 'Theta of E log V ',
            'worst': 'Order of V squared '
        },
        'Space Complexity': 'Order of V+E'
    },
    'prims algorithm': {
        'Time Complexity': {
            'average': 'Theta of E log V ',
            'worst': 'Order of V squared '
        },
        'Space Complexity': 'Order of V+E'
    },
    'bellman ford algorithm': {
        'Time Complexity': {
            'average': 'Theta of E times V ',
            'worst': 'Order of E times V '
        },
        'Space Complexity': 'Order of V'
    },
    'floyd warshall algorithm': {
        'Time Complexity': {
            'average': 'Theta of V cubed',
            'worst': 'Order of V cubed'
        },
        'Space Complexity': 'Order of n'
    },
    'topological sort': {
        'Time Complexity': {
            'average': 'Theta of V+E ',
            'worst': 'Order of V+E '
        },
        'Space Complexity': 'Order of V+E'
    },
    'sleep sort': {
        'Time Complexity': {
            'average': 'Theta of n + highest value element',
            'worst': 'Order of n squared + highest value element'
        },
        'Space Complexity': 'Order of 1'
    }
}


data_structures = {
    'array': {
        'Time Complexity': {
            'access': {'average': 'Theta of 1', 'worst': 'Order of 1'},
            'search': {'average': 'Theta of n', 'worst': 'Order of n'},
            'insertion': {'average': 'Theta of n', 'worst': 'Order of n'},
            'deletion': {'average': 'Theta of n', 'worst': 'Order of n'}
        },
        'Space Complexity': 'Order of n'
    },
    'stack': {
        'Time Complexity': {
            'access': {'average': 'Theta of n', 'worst': 'Order of n'},
            'search': {'average': 'Theta of n', 'worst': 'Order of n'},
            'insertion': {'average': 'Theta of 1', 'worst': 'Order of 1'},
            'deletion': {'average': 'Theta of 1', 'worst': 'Order of 1'}
        },
        'Space Complexity': 'Order of n'
    },
    'queue': {
        'Time Complexity': {
            'access': {'average': 'Theta of n', 'worst': 'Order of n'},
            'search': {'average': 'Theta of n', 'worst': 'Order of n'},
            'insertion': {'average': 'Theta of 1', 'worst': 'Order of 1'},
            'deletion': {'average': 'Theta of 1', 'worst': 'Order of 1'}
        },
        'Space Complexity': 'Order of n'
    },
    'singly linked list': {
        'Time Complexity': {
            'access': {'average': 'Theta of n', 'worst': 'Order of n'},
            'search': {'average': 'Theta of n', 'worst': 'Order of n'},
            'insertion': {'average': 'Theta of 1', 'worst': 'Order of 1'},
            'deletion': {'average': 'Theta of 1', 'worst': 'Order of 1'}
        },
        'Space Complexity': 'Order of n'
    },
    'doubly linked list': {
        'Time Complexity': {
            'access': {'average': 'Theta of n', 'worst': 'Order of n'},
            'search': {'average': 'Theta of n', 'worst': 'Order of n'},
            'insertion': {'average': 'Theta of 1', 'worst': 'Order of 1'},
            'deletion': {'average': 'Theta of 1', 'worst': 'Order of 1'}
        },
        'Space Complexity': 'Order of n'
    },
    'skip list': {
        'Time Complexity': {
            'access': {'average': 'Theta of log n', 'worst': 'Order of n'},
            'search': {'average': 'Theta of log n', 'worst': 'Order of n'},
            'insertion': {'average': 'Theta of log n', 'worst': 'Order of n'},
            'deletion': {'average': 'Theta of log n', 'worst': 'Order of n'}
        },
        'Space Complexity': 'Order of n log n'
    },

    'hash table': {
        'Time Complexity': {
            'access': {'average': 'Theta of 1', 'worst': 'Order of n'},
            'search': {'average': 'Theta of 1', 'worst': 'Order of n'},
            'insertion': {'average': 'Theta of 1', 'worst': 'Order of n'},
            'deletion': {'average': 'Theta of 1', 'worst': 'Order of n'}
        },
        'Space Complexity': 'Order of n'
    },
    'binary search tree': {
        'Time Complexity': {
            'access': {'average': 'Theta of log n', 'worst': 'Order of n'},
            'search': {'average': 'Theta of log n', 'worst': 'Order of n'},
            'insertion': {'average': 'Theta of log n', 'worst': 'Order of n'},
            'deletion': {'average': 'Theta of log n', 'worst': 'Order of n'}
        },
        'Space Complexity': 'Order of n'
    },
    'cartesian tree': {
        'Time Complexity': {
            'access': {'average': 'not applicable', 'worst': 'not applicable'},
            'search': {'average': 'Theta of log n', 'worst': 'Order of n'},
            'insertion': {'average': 'Theta of log n', 'worst': 'Order of n'},
            'deletion': {'average': 'Theta of log n', 'worst': 'Order of n'}
        },
        'Space Complexity': 'Order of n'
    },
    'b tree': {
        'Time Complexity': {
            'access': {'average': 'Theta of log n', 'worst': 'Order of log n'},
            'search': {'average': 'Theta of log n', 'worst': 'Order of log n'},
            'insertion': {'average': 'Theta of log n', 'worst': 'Order of log n'},
            'deletion': {'average': 'Theta of log n', 'worst': 'Order of log n'}
        },
        'Space Complexity': 'Order of n'
    },
    'red black tree': {
        'Time Complexity': {
            'access': {'average': 'Theta of log n', 'worst': 'Order of log n'},
            'search': {'average': 'Theta of log n', 'worst': 'Order of log n'},
            'insertion': {'average': 'Theta of log n', 'worst': 'Order of log n'},
            'deletion': {'average': 'Theta of log n', 'worst': 'Order of log n'}
        },
        'Space Complexity': 'Order of n'
    },
    'splay tree': {
        'Time Complexity': {
            'access': {'average': 'not applicable', 'worst': 'not applicable'},
            'search': {'average': 'Theta of log n', 'worst': 'Order of log n'},
            'insertion': {'average': 'Theta of log n', 'worst': 'Order of log n'},
            'deletion': {'average': 'Theta of log n', 'worst': 'Order of log n'}
        },
        'Space Complexity': 'Order of n'
    },
    'avl tree': {
        'Time Complexity': {
            'access': {'average': 'Theta of log n', 'worst': 'Order of log n'},
            'search': {'average': 'Theta of log n', 'worst': 'Order of log n'},
            'insertion': {'average': 'Theta of log n', 'worst': 'Order of log n'},
            'deletion': {'average': 'Theta of log n', 'worst': 'Order of log n'}
        },
        'Space Complexity': 'Order of n'
    },
    'kd tree': {
        'Time Complexity': {
            'access': {'average': 'Theta of log n', 'worst': 'Order of n'},
            'search': {'average': 'Theta of log n', 'worst': 'Order of n'},
            'insertion': {'average': 'Theta of log n', 'worst': 'Order of n'},
            'deletion': {'average': 'Theta of log n', 'worst': 'Order of n'}
        },
        'Space Complexity': 'Order of n'
    }
}


@app.route('/', methods=['GET'])
def homepage():
    return "server test"


def algo_complexity(algo, an_type, complexity_type):
    best_case_time = ''
    base_statement = 'For ' + algo + ', '

    if algo not in special_algos:
        best_case_time = 'Best case time complexity is, ' + algorithms[algo]['Time Complexity']['best'] + '. '
        if an_type in best_syn:
            return best_case_time
    avg_case_time = 'Average case time complexity is, ' + algorithms[algo]['Time Complexity']['average'] + '. '
    if an_type in average_syn:
        return 'For ' + algo + ', ' + avg_case_time
    worst_case_time = 'Worst case time complexity is, ' + algorithms[algo]['Time Complexity']['worst'] + '. '
    if an_type in worst_syn:
        return 'For ' + algo + ', ' + worst_case_time

    space_complexity = 'Space complexity is ' + \
        algorithms[algo]['Space Complexity'] + '. '
    if complexity_type == 'space' or complexity_type == 'space complexity':
        return base_statement + space_complexity
    elif complexity_type == 'time' or complexity_type == 'run time' or complexity_type == 'runtime':
        return base_statement + best_case_time + avg_case_time + ' and, ' + worst_case_time

    message = base_statement + best_case_time + avg_case_time + worst_case_time + ' and,  ' + space_complexity
    return message


def get_valid_ops_type(operation_type):
    valid_operation = None
    if operation_type == 'delete':
        valid_operation = 'deletion'
    elif operation_type == 'insert':
        valid_operation = 'insertion'
    elif operation_type == 'searching':
        valid_operation = 'search'
    return valid_operation


def get_dstruct_time_complexity(dstruct, an_type, operation_type):
    complexity_list = []
    if operation_type:
        complexity = data_structures[dstruct]['Time Complexity'][operation_type][an_type]
        return an_type + ' case time complexity for ' + operation_type + ' operation in ' + dstruct + ' is ' + complexity + '. '

    for op_type in ops_type:
        result = op_type + ' operation is, ' + data_structures[dstruct]['Time Complexity'][op_type][an_type]
        complexity_list.append(result)

    complexity = an_type + ' case time complexity of ' + dstruct + ' is as follows: ' + \
        complexity_list[0] + '. ' + complexity_list[1] + '. ' + \
        complexity_list[2] + '. ' + 'and ' + complexity_list[3] + '. '
    return complexity


def dstruct_complexity(dstruct, an_type, complexity_type, operation_type):
    avg_case = get_dstruct_time_complexity(dstruct, 'average', operation_type)
    if an_type in average_syn:
        return avg_case

    worst_case = get_dstruct_time_complexity(dstruct, 'worst', operation_type)
    if an_type in worst_syn:
        return worst_case

    space_complexity = 'Space complexity is ' + data_structures[dstruct]['Space Complexity'] + '. '
    if complexity_type == 'space' or complexity_type == 'space complexity':
        return 'For ' + dstruct + ', ' + space_complexity
    elif complexity_type == 'time' or complexity_type == 'run time' or complexity_type == 'runtime' or operation_type:
        return avg_case + worst_case

    message = avg_case + worst_case + " and finally,  " + space_complexity
    return message


@ask.launch
def start_skill():
    welcome_message = "Hi there, tell me the name of the data structure or the algorithm that you would like to know the time and space complexity for?"
    return question(welcome_message)


@ask.intent("GetComplexity",
    mapping={'dstruct_algo': 'Algo_DS', 'an_type': 'Asymptotic_Notation_Type', 'complexity_type': 'Complexity_Type', 'operation_type': 'Operation_Type'})
def complexity(dstruct_algo, an_type, complexity_type, operation_type):
    try:
        #to check if data structure name or algorithm name is provided
        if not dstruct_algo:
            complexity_msg = "I think I can help you but please provide me the data structure or algorithm name that you would like to know the time And/or space complexity for?"
            return question(complexity_msg)

        #alexa might send some params in uppercase convert everything to lower case to find correct result
        if dstruct_algo is not 'Dijkstra\'s algorithm':
            dstruct_algo = dstruct_algo.lower()
        if an_type:
            an_type.lower()
        if complexity_type:
            complexity_type.lower()
        if operation_type:
            operation_type.lower()

        #to handle the case if user gives an invalid operation type
        if(operation_type and operation_type not in ops_type):
            operation_type = get_valid_ops_type(operation_type) #incase user says delete instead of deletion
            if(not operation_type):
                return statement("Sorry I only know complexities for, Access, Search, Insertion and Deletion operations in a data structure.")

        #base message
        complexity_msg = "Sorry! I don't know the time and space complexity for the given data structure or algorithm at the moment."

        # to handle the case if quicksort is one word, we still want to treat this as quick sort
        if 'sort' in dstruct_algo and len(dstruct_algo.split(' ')) == 1:
            dstruct_algo = ''.join(dstruct_algo.split('sort')) + ' ' + 'sort'


        #check if its an algorithm or data structure and proceed accordingly
        if dstruct_algo in algorithms:
            complexity_msg = algo_complexity(
                dstruct_algo, an_type, complexity_type)
        elif dstruct_algo in data_structures:
            complexity_msg = dstruct_complexity(
                dstruct_algo, an_type, complexity_type, operation_type)

        return statement(complexity_msg)

    except:
        complexity_msg = "Sorry I did not understand your request, please try again or you can say help to know more about the skill!"
        return question(complexity_msg)


@ask.intent('AMAZON.HelpIntent')
def help():
    help_msg = """Algorithm and data structure complexities, is an alexa skill
           that lets you find the worst, average and best case time complexities
           and space complexity of various data structures and algorithms in
           computer science. In order to ask this skill the complexity of a data
           structure or an algorithm you can say the name of the data
           structure or algorithm. Or you can also say something more specific
           like, What is the time complexity for insertion operation in a hash table?
           .. Now tell me for which data structure or algorithm would you like to know
           time and space complexity for?"""
    return question(help_msg).reprompt(help_msg)


@ask.intent('AMAZON.StopIntent')
@ask.intent('AMAZON.CancelIntent')
@ask.intent("AMAZON.NoIntent")
def stop():
    end_msg = "Thanks for using Algorithm and data structure Complexities skill, Goodbye!"
    return statement(end_msg)


@ask.session_ended
def session_ended():
    return "", 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)
