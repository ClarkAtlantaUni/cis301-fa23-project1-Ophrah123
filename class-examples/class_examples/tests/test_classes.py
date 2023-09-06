from cis301.classes.human import Human


def test_human_name():
    # Arrange
    human = Human("John")
    # Act
    name = human.name
    # Assert
    assert name == 'John'

def test_human_says():
    human = Human("John")
    assert "Hello" == human.says()