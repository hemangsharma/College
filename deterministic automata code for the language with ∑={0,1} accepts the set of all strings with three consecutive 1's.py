#Q. Write a deterministic automata code for the language with ∑={0,1} accepts the set of all strings with three consecutive 1's.
#!pip install automata-lib


from automata.fa.dfa import DFA 

dfa = DFA( states={'q0', 'q1', 'q2','q3'}, input_symbols={'0', '1'}, transitions={ 'q0': {'1': 'q1','0':'q0'},
'q1': {'0': 'q2', '1': 'q1'}, 'q2': {'0': 'q2', '1': 'q3'},
'q3': {'0': 'q3', '1': 'q3'},
},initial_state='q0', final_states={'q3 '} )

dfa.read_input('111')

if dfa.accepts_input('111'): 
    print('accepted' ) 

else: 
    print('rejected')
