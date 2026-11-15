import pytest
from homework import stack, zadacha


@pytest.fixture
def create_not_empty_stack():
    st = stack()
    for i in range(10):
        st.body.append(i)
    yield st

@pytest.fixture
def create_empty_stack():
    st = stack()
    yield st


def test_is_empty_empty(create_empty_stack):
    assert create_empty_stack.is_empty() == True

def test_is_empty_full(create_not_empty_stack):
    assert create_not_empty_stack.is_empty() == False

def test_push(create_not_empty_stack):
    create_not_empty_stack.push("TEST")
    assert create_not_empty_stack.body[0] == "TEST"

def test_pop(create_not_empty_stack):
    first_item = create_not_empty_stack.body[0]
    ln = len(create_not_empty_stack.body)
    assert create_not_empty_stack.pop() == first_item and len(create_not_empty_stack.body) == ln - 1

def test_peek(create_not_empty_stack):
    assert create_not_empty_stack.peek() == create_not_empty_stack.body[0]

def test_size(create_not_empty_stack):
    assert create_not_empty_stack.size() == len(create_not_empty_stack.body)

@pytest.mark.parametrize("item", [
    "(((([{}]))))",
    "[([])((([[[]]])))]{()}",
    "{{[()]}}",
    "}{}",
    "{{[(])]}}",
    "[[{())}]"
])

def test_skobs(create_empty_stack, item):
    for i in reversed(item):
        create_empty_stack.push(i)
    assert zadacha(create_empty_stack.body) == "Верно"