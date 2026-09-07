tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
} 

types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
} 



def delete_duplicates(tickets_dict):
  seen = set()
  no_duplicate_tickets = {}
  for level in tickets_dict.keys():
    cleaned = []
    for ticket in tickets_dict[level]:
        if ticket not in seen:
            cleaned.append(ticket)
            # print('This is cleaned', cleaned)
            seen.add(ticket)
            # print('This is seen', seen)
    no_duplicate_tickets[level] = cleaned
  return no_duplicate_tickets
    
def assign_tickets_to_types(tickets_dict, types_dict):
  tickets_by_type = {}
  for key in tickets_dict.keys():
    tickets_by_type[types_dict[key]] = tickets_dict[key]
  return tickets_by_type

new_dict = delete_duplicates(tickets)
assign_tickets_to_types(new_dict, types)
