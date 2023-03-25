import pytest
from game import Game
from enemy import Enemy
from menu import Menu


@pytest.fixture()
def game():
    return Game()


@pytest.fixture()
def enemy(game):
    return Enemy(game)


@pytest.fixture()
def menu():
    return Menu()


def test_game(game):
    result = game.score
    assert result == 0


@pytest.mark.parametrize("a, b, expected_result", [(10, 10, 20),
                                                   (1, 2, 3),
                                                   (3, 4, 7)])
def test_enemy_change_position(enemy, a, b, expected_result):
    result = enemy.change_position(a, b)
    assert result == expected_result


@pytest.mark.parametrize("a, expected_result", [(1, 0),
                                                (10, 9),
                                                (11, 10)])
def test_enemy_reduce_points(enemy, a, expected_result):
    result = enemy.reduce_points(a)
    assert result == expected_result
