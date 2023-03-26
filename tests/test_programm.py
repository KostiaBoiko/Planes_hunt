import pytest
from pygame import mixer
from enemy import Enemy
from menu import Menu
from game import Game


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


@pytest.mark.enemy
@pytest.mark.parametrize("a, b, expected_result", [(10, 10, 20),
                                                   (1, 2, 3),
                                                   (3, 4, 7)])
def test_enemy_change_position(enemy, a, b, expected_result):
    result = enemy.change_position(a, b)
    assert result == expected_result


@pytest.mark.enemy
@pytest.mark.parametrize("a, expected_result", [(1, 0),
                                                (10, 9),
                                                (11, 10)])
def test_enemy_reduce_points(enemy, a, expected_result):
    result = enemy.reduce_points(a)
    assert result == expected_result


mixer.init()
em = mixer.Sound('assets/sounds/Hatsune Miku - Ievan Polkka (mp3store.cc).mp3')
nm = mixer.Sound('assets/sounds/undertale_050. Metal Crusher.mp3')
hm = mixer.Sound('assets/sounds/Daniel_Tidwell_-_At_Dooms_Gate_DOOM_E1M1_(musmore.com).mp3')


@pytest.mark.menu
@pytest.mark.parametrize("expected_music", [em, nm, hm])
def test_music(menu, expected_music):
    result = menu.change_music(expected_music)
    assert result == expected_music


@pytest.mark.enemy
@pytest.mark.parametrize("a, expected_result", [(0, 1),
                                                (9, 10),
                                                (10, 11)])
def test_enemy_append_points(enemy, a, expected_result):
    result = enemy.append_points(a)
    assert result == expected_result


@pytest.mark.enemy
def test_enemy_type(enemy):
    plane_types = [0, 1, 2]
    result = enemy.plane_type
    assert result in plane_types

