from cleaner import clean_price, clean_rating, clean_stock


def test_clean_price_normal():
    assert clean_price("£51.77") == 51.77


def test_clean_price_empty():
    assert clean_price("") is None


def test_clean_rating():
    assert clean_rating("Three") == 3
    assert clean_rating("Banana") is None


def test_clean_stock():
    assert clean_stock("In stock (22 available)") == 22
    assert clean_stock("Out of stock") == 0