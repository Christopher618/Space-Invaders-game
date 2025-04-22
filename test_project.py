from project import isCollision, enemy, fire_bullet

def test_isCollision():
    assert isCollision(10, 20, 50, 100) == None

def test_enemy():
    assert enemy(10, 20, 4) == None

def test_fire_bullet():
    assert fire_bullet(10, 20) == None

