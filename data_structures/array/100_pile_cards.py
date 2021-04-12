def get_card(Round,pile_arr,nth_card):
    card=[i for i in range(1,101)]
    for i in range(Round):
        temp_matrix=[[] for _ in range(pile_arr[i])]
        j=0
        for val in card:
            temp_matrix[j].append(val)
            j+=1
            if j==pile_arr[i]:
                j=0
        card=[]
        for val in temp_matrix:
            card.extend(val)
    print(card)

get_card(2,[2,2],4)