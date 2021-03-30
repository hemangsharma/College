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


#Q. Write a deterministic automata code for the language with ∑={0,1} accepts even Number of 0's and even number of 1's.
#pip install automata-lib

from automata.fa.dfa import DFA 

dfa = DFA(
states={'q0', 'q1', 'q2','q3'},
input_symbols={'0', '1'}, transitions={ 'q0': {'1': 'q1','0':'q0'}, 'q1': {'0': 'q2', '1': 'q1'},
'q2': {'0': 'q2', '1': 'q3'},
'q3': {'0': 'q3', '1': 'q3'},
 },
initial_state='q0', final_states={'q3 '}
)
dfa.read_input('1010 ') 

if input = ‘1’:
	even1=even1 +1 

if input = ‘0’:
	even0=even0 +1
if even1 % 2 == 0 and even0 % 2 == 0: 
	print('accepted' ) 

else: 
	print('rejected')



#Q. Write a deterministic automata code for the language with ∑ = {0, 1}
#accepts the only input 101.
#pip install automata-lib

from automata.fa.dfa import DFA 

dfa = DFA( states={'q0', 'q1', 'q2','q3'}, input_symbols={'0', '1'},
transitions={
'q0': {'1': 'q1','0':'q0'}, 'q1': {'0': 'q2', '1': 'q1'}, 'q2': {'0': 'q2', '1': 'q3'}, 'q3': {'0': 'q3', '1': 'q3'},
},
initial_state='q0', final_states={'q3 '} )
dfa.read_input('101') #answer is q3 

if dfa.accepts_input('101'): 
	print('accepted' ) 

else: 
	print('rejected')


#Q. Write a deterministic automata code for the language with ∑ = {0,1} accepts those string which starts with 1 and ends with 0.

from automata.fa.dfa import DFA 

dfa=DFA(
states={'q0','q1','q2'},
input_symbols={'0','1' }, transitions={ 'q0':{'0':'q1','1':'q0'}, 'q1':{'1':'q1','0':'q2'}, 'q2':{'0':'q2','1':'q2'}
},
initial_state='q0', final_states={'q0','q1 '}
)
string="00"

if dfa.accepts_input(string):
	print("String is Accepted") 

else:
    print("string is Rejected")



#Q. Give a non-deterministic automata code for (a|b)*aab.

from automata.fa.nfa import NFA 

nfa=NFA( states={'q0','q1','q2','q3','q4','q5'} , input_symbols={'a','b'}, transitions={ 'q0':{'':{'q1'},'':{'q2'}},
'q1':{'a':{'q3'},'1':{'q1'}}, 'q2':{'b':{'q4'},'0':{'q2'}}, 'q3':{'a':{'q3'},'1':{'q1'}}, 'q4':{'a':{'q4'},'1':{'q5'}}, 'q5':{'b':{'q5'},'1':{'q2'}} },
initial_state='q0', final_states={'q1', 'q2','q3','q4','q5'} ) 

string="a|b*aab"

if nfa.accepts_input(string):
	print("String is Accepted") 

else:
	print("string is Rejected")


#Q Give a non-deterministic automata code for the set of all binary strings that have either the number of 0’s odd, or the number of 1’s not a multiple of 3, or both

from automata.fa.nfa import NFA 

nfa=NFA( states={'q0','q1','q2','q3','q4','q5'} , input_symbols={'0','1'}, transitions={
'q0':{'':{'q1'},'':{'q2'}}, 'q1':{'0':{'q3'},'1':{'q1'}}, 'q2':{'1':{'q4'},'0':{'q2'}}, 'q3':{'1':{'q3'},'1':{'q1'}}, 'q4':{'0':{'q4'},'1':{'q5'}}, 'q5':{'0':{'q5'},'1':{'q2'}}
},
initial_state='q0', final_states={'q3','q4','q5 '} )

string="011"
if nfa.accepts_input(string): 
	print("String is Accepted") 

else: 
	print("string is Rejected")


#Q. Give a non-deterministic automata code for the language L=(ab)*(ba)*U aa*

from automata.fa.nfa import NFA 

nfa=NFA( states={'q0','q1','q2','q3','q4','q5'} , input_symbols={'a','b'}, transitions={ 'q0':{'':{'q1'},'':{'q2'}},
'q1':{'a':{'q3'},'1':{'q1'}}, 'q2':{'b':{'q4'},'0':{'q2'}}, 'q3':{'a':{'q3'},'1':{'q1'}}, 'q4':{'a':{'q4'},'1':{'q5'}}, 'q5':{'b':{'q5'},'1':{'q2'}} },
initial_state='q0', final_states={'q1', 'q2','q3','q4','q5'} )

string="ab*ba* U aa"

if nfa.accepts_input(string):
	print("String is Accepted") 

else: 
	print("string is Rejected")


#Q. Give a non-deterministic automata code for the language L that have at least two consecutive 0’s or 1’s

from automata.fa.nfa import NFA 

nfa=NFA( states={'q0','q1','q2','q3'}, input_symbols={'0','1'}, transitions={ 'q0':{'0':{'q0','q1'},'1':{'q0','q2'}}, 'q1':{'0':{'q3'},'':{'q1'}},
'q2':{'1':{'q3'},'':{'q2'}}, 'q3':{'0':{'q3'},'1':{'q3'}}
},
initial_state='q0', final_states={'q3 '} )

string="010100"
if nfa.accepts_input(string): 
	print("String is Accepted") 

else: 
	print("string is Rejected")


#Q. Give a non-deterministic automata code for the the language L =(01 U 010).

from automata.fa.nfa import NFA 

nfa=NFA( states={'q0','q1','q2','q3'}, input_symbols={'0','1'}, transitions={ 'q0':{'0':{'q0','q1'},'1':{'q0','q2'}},
'q1':{'0':{'q3'},'':{'q1'}}, 'q2':{'1':{'q3'},'':{'q2'}}, 'q3':{'0':{'q3'},'1':{'q3'}} },
initial_state='q0', final_states={'q3 '} ) 

string="01U010"
if nfa.accepts_input(string): 
	print("String is Accepted") 

else: 
	print("string is Rejected")




