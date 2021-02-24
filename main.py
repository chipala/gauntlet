import Character as m_character
import Capacity as m_capacity

if __name__ == "__main__":    
    print("!! Gauntlet !!")

    # Test
    ## Character
    c = m_character.Character("character")
    z = m_character.Wizard("wizard")
    w = m_character.Warrior("warrior")
    e = m_character.Elf("elf")

    l = [c, z, w, e]

    for character in l:
        print(character)

    ## Capacity
    c.addCapacity(m_capacity.Capacity("c_jump"))
    c.addCapacity(m_capacity.Capacity("c_run"))
    z.addCapacity(m_capacity.Capacity("z_speak"))
    w.addCapacity(m_capacity.Capacity("w_fight"))
    e.addCapacity(m_capacity.Capacity("e_fast"))

    for character in l:
        print(f"{character}")
        character.listCapacity()
