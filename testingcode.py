import elections
college = {'Virginia': 13,
 'Ohio': 18,
 'Minnesota': 10,
 'Alabama': 9,
 'Maine': 4
}
print(elections.winner({}))
elections.add_state('Virginia', {
 'Turing': 15,
 'Lovelace': 20,
 'Dijkstra': 10
})
elections.add_state('Ohio', {
 'Turing': 1,
 'Dijkstra': 15
})
elections.add_state('Alabama', {
 'Turing': 10,
 'Lovelace': 20,
 'Dijkstra': 8
})
print(elections.winner(college))
elections.add_state('Minnesota', {
 'Lovelace': 10,
 'Dijkstra': 30,
})
elections.add_state('Florida', {
 'Turing': 10,
 'Lovelace': 30,
 'Dijkstra': 15
})
print(elections.winner(college))
elections.clear()
elections.add_state('Maine', {
 'Turing': 2,
 'Dijkstra': 1,
 'Lovelace': 5
})
print(elections.winner(college))