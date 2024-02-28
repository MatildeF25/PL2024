import re
import os

class SummingAutomaton:
    def __init__(self, states, alphabet, transitions, initial_state, accepting_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.current_state = initial_state
        self.initial_state = initial_state
        self.accepting_states = accepting_states
        self.total = 0

    def process(self, text):
        words = re.split('\s+', text)
        for word in words:
            if re.match(self.alphabet['on'], word):
                self.current_state = 'ON'
            elif re.match(self.alphabet['off'], word):
                self.current_state = 'OFF'
            elif re.match(self.alphabet['='], word):
                print('total: ' + str(self.total))
            elif re.match(self.alphabet['\d+'], word) and self.current_state == 'ON':
                self.total += int(word)

states = {'ON', 'OFF'}
alphabet = {'\d+': re.compile(r'\d+'), 'off': re.compile("[Oo][Ff]{2}"), 'on': re.compile("[Oo][Nn]"), '=': re.compile("=")}
transitions = {
    'ON': {
        'off': ('OFF', None),
        'on': ('ON', None),
        '=': ('ON', 'output')
    },
    'OFF': {
        'off': ('OFF', None),
        'on': ('ON', None),
        '=': ('OFF', 'output')
    }
}

automaton = SummingAutomaton(states, alphabet, transitions, 'OFF', {})
f = open("texto.txt", "r")
text = f.read()
automaton.process(text)
