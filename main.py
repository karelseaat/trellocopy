url_member = "https://trello.com/akarelse/boards"
querystring = {"key":"3cd117a524913b8e457893f9fff7b327","token":"4fa723f0134f1e2970eae1db9aa1c6b9764c0ccab5a9992906cfa2d64d791da2"}


from trello import TrelloClient, Card

client = TrelloClient(
    api_key='3cd117a524913b8e457893f9fff7b327',
    api_secret='4fa723f0134f1e2970eae1db9aa1c6b9764c0ccab5a9992906cfa2d64d791da2',
)

copyboard = client.get_board('62c57908ee94d77ab6f39383')

aatlist = copyboard.get_list('62c579171436d928d98792ea')

print(aatlist)

print(dir(aatlist))

print(dir(aatlist.list_cards()[0]))
aatlist.add_card(name = "CARD SAMPLE", desc = "Description Sample")