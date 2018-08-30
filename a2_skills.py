"""
The Skill classes for A2.

See a2_characters.py for how these are used.
For any skills you make, you're responsible for making sure their style adheres
to PythonTA and that you include all documentation for it.
"""

from typing import Any

class Skill:
    """
    An abstract superclass for all Skills.
    """

    def __init__(self, cost: int, damage: int) -> None:
        """
        Initialize this Skill such that it costs cost SP and deals damage
        damage.
        """
        self._cost = cost
        self._damage = damage

    def get_sp_cost(self) -> int:
        """
        Return the SP cost of this Skill.
        """
        return self._cost

    def use(self, caster: 'Character', target: 'Character') -> None:
        """
        Makes caster use this Skill on target.
        """
        raise NotImplementedError

    def _deal_damage(self, caster: 'Character', target: 'Character') -> None:
        """
        Reduces the SP of caster and inflicts damage on target.
        """
        caster.reduce_sp(self._cost)
        target.apply_damage(self._damage)

class NormalAttack(Skill):
    """
    A class representing a NormalAttack.
    Not to be instantiated.
    """

    def use(self, caster: 'Character', target: 'Character') -> None:
        """
        Makes caster use this Skill on target.
        """
        self._deal_damage(caster, target)
        caster.battle_queue.add(caster)

class MageAttack(NormalAttack):
    """
    A class representing a Mage's Attack.
    """

    def __init__(self) -> None:
        """
        Initialize this MageAttack.

        >>> m = MageAttack()
        >>> m.get_sp_cost()
        5
        """
        super().__init__(5, 20)

class MageSpecial(Skill):
    """
    A class representing a Mage's Special Attack.
    """

    def __init__(self) -> None:
        """
        Initialize this MageAttack.

        >>> m = MageSpecial()
        >>> m.get_sp_cost()
        30
        """
        super().__init__(30, 40)

    def use(self, caster: 'Character', target: 'Character') -> None:
        """
        Makes caster use a Mage's SpecialAttack on target.

        >>> from a2_playstyle import ManualPlaystyle
        >>> from a2_battle_queue import BattleQueue
        >>> from a2_characters import Rogue, Mage
        >>> bq = BattleQueue()
        >>> r = Rogue("r", bq, ManualPlaystyle(bq))
        >>> m = Mage("m", bq, ManualPlaystyle(bq))
        >>> r.enemy = m
        >>> m.enemy = r
        >>> m.special_attack()
        >>> m.get_sp()
        70
        >>> r.get_hp()
        70
        """

        self._deal_damage(caster, target)
        caster.battle_queue.add(target)
        caster.battle_queue.add(caster)

class RogueAttack(NormalAttack):
    """
    A class representing a Rogue's Attack.
    """

    def __init__(self) -> None:
        """
        Initialize this RogueAttack.

        >>> r = RogueAttack()
        >>> r.get_sp_cost()
        3
        """
        super().__init__(3, 15)


class RogueSpecial(Skill):
    """
    A class representing a Rogue's Special Attack.
    """

    def __init__(self) -> None:
        """
        Initialize this RogueSpecial.

        >>> r = RogueSpecial()
        >>> r.get_sp_cost()
        10
        """
        super().__init__(10, 20)

    def use(self, caster: 'Character', target: 'Character') -> None:
        """
        Makes caster use a Rogue's SpecialAttack on target.

        >>> from a2_playstyle import ManualPlaystyle
        >>> from a2_battle_queue import BattleQueue
        >>> from a2_characters import Rogue, Mage
        >>> bq = BattleQueue()
        >>> r = Rogue("r", bq, ManualPlaystyle(bq))
        >>> m = Mage("m", bq, ManualPlaystyle(bq))
        >>> r.enemy = m
        >>> m.enemy = r
        >>> r.special_attack()
        >>> r.get_sp()
        90
        >>> m.get_hp()
        88
        """
        self._deal_damage(caster, target)
        caster.battle_queue.add(caster)
        caster.battle_queue.add(caster)

class SorcererAttack(NormalAttack):
    """
    A class representing a Sorcerer's Attack.
    """

    def __init__(self, real: Any) -> None:
        """
        Initialize this RogueSpecial.

        >>> r = RogueSpecial()
        """
        self.real = real
        self.real.__init__()

    def use(self, caster: 'Character', target: 'Character') -> None:
        """
        Makes caster use this Skill on target.

        """
        self.real.use(caster, target)

    def get_sp_cost(self) -> int:
        """
        Return the SP cost of this Skill.
        """
        return 15


class SorcererSpecial(Skill):
    """
    A class representing a Sorcerer's Special Attack.

    """

    def __init__(self)-> None:
        """
        Initialize this Sorccerer Special.

        >>> r = SorcererSpecial()
        >>> r.get_sp_cost()
        20
        """

        super().__init__(20, 25)

    def use(self, caster: 'Character', target: 'Character') -> None:
        """
        Makes caster use a Sorcerer's SpecialAttack on target.

        >>> from a2_playstyle import ManualPlaystyle
        >>> from a2_battle_queue import BattleQueue
        >>> from a2_characters import Sorcerer
        >>> bq = BattleQueue()
        >>> r = Sorcerer("r", bq, ManualPlaystyle(bq))
        >>> m = Sorcerer("m", bq, ManualPlaystyle(bq))
        >>> r.enemy = m
        >>> m.enemy = r
        >>> r.special_attack()
        >>> r.get_sp()
        80
        >>> m.get_hp()
        85
        """

        self._deal_damage(caster, target)
        while not caster.battle_queue.is_empty():
            caster.battle_queue.remove()

        caster.battle_queue.add(caster)
        caster.battle_queue.add(target)
        caster.battle_queue.add(caster)


class VampireAttack(NormalAttack):

    """
    A class representing a Vampire's Attack.
    """

    def __init__(self) -> None:
        """
        Initialize this Vampire Attack.

        >>> r = VampireAttack()
        >>> r.get_sp_cost()
        15
        """
        super().__init__(15, 20)


class VampireSpecial(Skill):
    """
    A class representing a Vampire's Special Attack.

    """

    def __init__(self) -> None:
        """
        Initialize this Vampire Special Attack.

        >>> r = VampireSpecial()
        >>> r.get_sp_cost()
        20
        """
        super().__init__(20, 30)

    def use(self, caster: 'Character', target: 'Character') -> None:
        """
        Makes caster use a Sorcerer's SpecialAttack on target.

        >>> from a2_playstyle import ManualPlaystyle
        >>> from a2_battle_queue import BattleQueue
        >>> from a2_characters import Vampire
        >>> bq = BattleQueue()
        >>> r = Vampire("r", bq, ManualPlaystyle(bq))
        >>> m = Vampire("m", bq, ManualPlaystyle(bq))
        >>> r.enemy = m
        >>> m.enemy = r
        >>> r.special_attack()
        >>> r.get_sp()
        80
        >>> m.get_hp()
        73
        """

        self._deal_damage(caster, target)
        caster.battle_queue.add(caster)
        caster.battle_queue.add(caster)
        caster.battle_queue.add(target)



if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config='a2_pyta.txt')


    #import doctest
    #doctest.testmod()
