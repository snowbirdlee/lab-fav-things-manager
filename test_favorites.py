from fav_things_functions_stretch import lookup_favorite, add_favorite, update_favorite, del_favorite

def test_lookup_favorite():
    data = {"book": "hunger games"}
    lookup_favorite(data, "book")
    
def test_add_favorite():
    data = {}
    result = add_favorite(data, "book", "hunger games")
    print("RESULT:", result)
    assert result == {"book": "hunger games"}
    
def test_update_favorite():
    data = add_favorite({}, "book", "harry potter")
    result = update_favorite(data, "book", "hunger games")
    assert result == {"book": "hunger games"}

def test_del_favorite():
    data = add_favorite({}, "book", "hunger games")  # Start with one item
    result = del_favorite(data, "book")              # Delete it
    assert result == {}                              # Should be empty now
    

test_lookup_favorite()
test_add_favorite()
test_update_favorite()
test_del_favorite()
